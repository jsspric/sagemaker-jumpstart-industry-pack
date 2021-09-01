# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
"""The utils module."""
from __future__ import absolute_import

import re
from typing import Callable
import pandas as pd


def _get_freq_label_by_day(date_value: str) -> str:
    """Gets frequency label for the date value which is aggregated by day.

    Args:
        date_value (str): The date value.

    Returns:
        str: The date value aggregated by day.
    """
    if not bool(re.match(r"^\d{4}-\d{1,2}-\d{1,2}$", date_value)):
        raise ValueError("Date needs to be in yyyy-mm-dd format when freq is D")
    return date_value


def _get_freq_label_by_week(date_value: str) -> str:
    """Gets frequency label for the date value which is aggregated by week.

    Args:
        date_value (str): The date value.

    Returns:
        str: The date value aggregated by week.
    """
    if bool(re.match(r"^\d{4}W\d{1,2}$", date_value)):
        return date_value
    if not bool(re.match(r"^\d{4}-\d{1,2}-\d{1,2}$", date_value)):
        raise ValueError("Date needs to be in yyyy-mm-dd format when freq is W")
    ts = pd.Timestamp(date_value)
    return "{}W{}".format(ts.year, ts.week)


def _get_freq_label_by_month(date_value: str) -> str:
    """Gets frequency label for the date value which is aggregated by month.

    Args:
        date_value (str): The date value.

    Returns:
        str: The date value aggregated by month.
    """
    if bool(re.match(r"^\d{4}M\d{1,2}$", date_value)):
        return date_value
    if not bool(re.match(r"^\d{4}-\d{1,2}(-\d{1,2})?$", date_value)):
        raise ValueError("Date needs to be in yyyy-mm-dd or yyyy-mm format when freq is M")
    ts = pd.Timestamp(date_value)
    return "{}M{}".format(ts.year, ts.month)


def _get_freq_label_by_quarter(date_value: str) -> str:
    """Gets frequency label for the date value which is aggregated by quarter.

    Args:
        date_value (str): The date value.

    Returns:
        str: The date value aggregated by quarter.
    """
    if bool(re.match(r"^\d{4}Q\d{1,2}$", date_value)):
        return date_value
    if not bool(re.match(r"^\d{4}-\d{1,2}(-\d{1,2})?$", date_value)):
        raise ValueError("Date needs to be in yyyy-mm-dd or yyyy-mm format when freq is Q")
    ts = pd.Timestamp(date_value)
    return "{}Q{}".format(ts.year, ts.quarter)


def _get_freq_label_by_year(date_value: str) -> str:
    """Gets frequency label for the date value which is aggregated by year.

    Args:
        date_value (str): The date value.

    Returns:
        str: The date value aggregated by year.
    """
    if bool(re.match(r"^\d{4}$", date_value)):
        return date_value
    if not bool(re.match(r"^\d{4}(-\d{1,2}){0,2}$", date_value)):
        raise ValueError("Date needs to be in yyyy-mm-dd, yyyy-mm or yyyy format when freq is Y")
    ts = pd.Timestamp(date_value)
    return str(ts.year)


FREQ_LABEL_MAP = {
    "D": _get_freq_label_by_day,
    "W": _get_freq_label_by_week,
    "M": _get_freq_label_by_month,
    "Q": _get_freq_label_by_quarter,
    "Y": _get_freq_label_by_year,
}


def get_freq_label(date_value: str, freq: str) -> Callable:
    """Gets frequency label for the date value.

    Args:
        date_value (str): The date value.
        freq (str): The frequency value specifies how the date field should be aggregated,
            by year, quarter, month, week, day. Possible values:
            {'Y', 'Q', 'M', 'W', 'D'}, default ‘Q’.

    Returns:
        python function: The function call to get date aggregated by certain frequency.
    """
    freq = freq.upper()
    if freq not in FREQ_LABEL_MAP:
        raise ValueError("frequency {} not supported".format(freq))
    if not isinstance(date_value, str):
        raise Exception("The date column needs to be string")
    return FREQ_LABEL_MAP[freq](date_value.upper())