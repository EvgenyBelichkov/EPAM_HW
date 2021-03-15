class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [
            item
            for item in data
            if all([i(item) for i in self.functions]) and len(self.functions) > 0
        ]


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():

        def keyword_filter_func(item):
            return key in item and item[key] == value

        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


# positive_even = Filter([lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)])
# print(positive_even.apply(range(10)))

print(make_filter().apply(sample_data))
print(make_filter(name="Bill").apply(sample_data))
# print(make_filter(name="Bill", kind = 'parrot').apply(sample_data))
