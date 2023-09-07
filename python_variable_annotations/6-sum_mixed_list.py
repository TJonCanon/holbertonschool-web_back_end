#!/usr/bin/env python3
""" returns sum of list of ints and floats as a float """


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ returns the sum of a list """
    return sum(mxd_list)
