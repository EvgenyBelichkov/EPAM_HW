class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(i(item) for i in self.functions)]


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():

        def returning_function(key_, value_):
            def keyword_filter_func(data):
                return key_ in data and data[key_] == value_

            return keyword_filter_func

        filter_funcs.append(returning_function(key, value))
    return Filter(filter_funcs)
