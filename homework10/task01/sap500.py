import asyncio
import json
import operator

import aiohttp
import requests
from bs4 import BeautifulSoup


async def fetch_response(url):
    """Assync function that return requested html code"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            assert response.status == 200
            return await response.text()


def content_from_table(html):
    """Collecting company_link and growth from common table"""
    soup = BeautifulSoup(html, "html.parser")
    table_elements = soup.find_all("tr")[2:]
    companys_information = []
    for row in table_elements:
        companys_information.append(
            {
                "company_link": "https://markets.businessinsider.com"
                + (row.find("a").get("href")),
                "growth": float(row.find_all("span")[9].get_text().rstrip("%")),
            }
        )
    return companys_information


def getting_exchange_rate():
    """Getting actual rate Russian ruble/dollar USD"""
    rates = requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text
    soup = BeautifulSoup(rates, "lxml")
    requested_rate = float(soup.find(text="Доллар США").next.text.replace(",", "."))
    return round(requested_rate, 1)


def content_from_company_page(html, current_rate):
    """Collecting company code, name, price, PE and potential_profit from company page"""
    detailed_company_information = []
    soup = BeautifulSoup(html, "html.parser")
    detailed_company_information.append(
        {
            "code": soup.find("span", class_="price-section__category")
            .find("span")
            .text.lstrip(", "),
            "name": soup.find("span", class_="price-section__label").text.strip(),
            "price": round(
                float(
                    soup.find(
                        "span", class_="price-section__current-value"
                    ).text.replace(",", "")
                )
                * current_rate,
                1,
            ),
            "PE": counting_price_earnings(soup),
            "growth": None,
            "potential_profit": counting_potential_profit(soup),
        }
    )

    return detailed_company_information


def counting_price_earnings(soup):
    """Searching p/e parameter. In case of Attribute error - returning parameter is 0"""
    try:
        pe = float(
            soup.find(text="P/E Ratio", class_="snapshot__header")
            .previous_sibling.strip()
            .replace(",", "")
        )
        return round(pe, 1)
    except AttributeError:
        return 0


def counting_potential_profit(soup):
    """Searching potential_profit. In case of Attribute error - returning parameter is 0"""
    try:
        high_profit = float(
            soup.find(text="52 Week High", class_="snapshot__header")
            .previous_sibling.strip()
            .replace(",", "")
        )
        low_profit = float(
            soup.find(text="52 Week Low", class_="snapshot__header")
            .previous_sibling.strip()
            .replace(",", "")
        )
        return round(high_profit - low_profit, 1)
    except AttributeError:
        return 0


def connect_common_and_detailed_information(
    common_company_information, detailed_company_information
):
    """Adding growth from common table to company dictionary"""
    iterable_list = iter(common_company_information)
    for el in detailed_company_information:
        el["growth"] = next(iterable_list)["growth"]
    return detailed_company_information


async def main(current_rate):
    """Async function that started getting HTML code from requested links"""
    common_company_information = []
    detailed_company_information = []
    tasks = [asyncio.create_task(fetch_response(url)) for url in urls]
    await asyncio.gather(*tasks)
    for task in tasks:
        for i in content_from_table(await task):
            common_company_information.append(i)

    tasks1 = [
        asyncio.create_task(fetch_response(url))
        for url in [i["company_link"] for i in common_company_information]
    ]
    await asyncio.gather(*tasks1)
    for task in tasks1:
        detailed_company_information.extend(
            content_from_company_page(await task, current_rate)
        )

    return connect_common_and_detailed_information(
        common_company_information, detailed_company_information
    )


def result_list_of_dicts(data, param):
    """Forming result dictionaries with top 10 companies"""
    if param == "PE":
        data.sort(key=operator.itemgetter(param))
    else:
        data.sort(key=operator.itemgetter(param), reverse=True)
    result_list = []
    requested_companies = data[:10]
    for company in requested_companies:
        result_list.append(
            {
                "code": company["code"],
                "name": company["name"],
                str(param): company[param],
            }
        )
    return result_list


if __name__ == "__main__":
    urls = [
        "https://markets.businessinsider.com/index/components/s&p_500?p=" + str(i)
        for i in range(1, 11)
    ]
    current_rate = getting_exchange_rate()
    data = asyncio.run(main(current_rate))
    for i in ["price", "PE", "growth", "potential_profit"]:
        with open("sorting_" + i + ".json", "w+") as file:
            json.dump(result_list_of_dicts(data, i), file)
