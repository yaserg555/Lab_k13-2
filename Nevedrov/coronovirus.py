#!/usr/bin/env python3

"""
Provide the current worldwide COVID-19 statistics.
This data is being scrapped from 'https://www.worldometers.info/coronavirus/'.
"""

import requests
from bs4 import BeautifulSoup


def world_covid19_stats(url: str = "https://www.worldometers.info/coronavirus/country/netherlands/") -> dict:
    """
    Return a dict of current worldwide COVID-19 statistics
    """
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    keys = soup.findAll("h1")
    values = soup.findAll("div", {"class": "maincounter-number"})
    keys += soup.findAll("span", {"class": "panel-title"})
    values += soup.findAll("div", {"class": "number-table-main"})
    return {key.text.strip(): value.text.strip() for key, value in zip(keys, values)}
