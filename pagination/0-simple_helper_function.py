#!/usr/bin/env python3
""" takes two ints and returns a tuple containing a start index
    and an end index corresponding to the range of indexes to return
    in a list for those particular pagination parameters """


def index_range(page, page_size):
    """ takes two ints """
    return (page_size * (page - 1), page_size * page)
