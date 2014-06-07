#!/usr/bin/python
""" unix_timestamp.py
Provides datetime function
"""
__author__ = 'olivier'

# import statements
from datetime import datetime
import time


def timestamp_to_date(timestamp, hours=False):
    """
    converts a UNIX time stamp to date

    Examples:
    >>> timestamp_to_date(1402139738)
    '2014-06-07'

    >>> timestamp_to_date(1402139738, True)
    '2014-06-07 13:20:10'
    """

    t=datetime.fromtimestamp(time.time())
    if hours:
        return t.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return t.strftime('%Y-%m-%d')


def main():
    """
    main function
    """
    # do nothing
    pass

if __name__ == "__main__":
    main()
