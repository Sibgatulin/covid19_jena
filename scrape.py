#!/home/renat/envs/scraper/bin/python
import re
import requests
import dateutil.parser
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://gesundheit.jena.de/de/coronavirus"


def standardise_format(inp_str, fmt):
    """ Parses the input string with dateutil and converts to the specified format
    The rationale for the function is that I do not trust Jena Gesundheitsamt to be
    be consistent with how they timestamp the data. Yet I sort of rely on it in bigger
    way in how I scrape the data anyway...
    """
    timestamp = dateutil.parser.parse(inp_str)
    return timestamp.strftime(fmt)


if __name__ == "__main__":

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # I expect it to be a big tag with some text, the number and the time
    result = soup.find(
        name="div",
        class_="clearfix text-formatted field field--name-field-content field--type-text-with-summary field--label-hidden field__item",
    )

    # the second and the last ``span`` contains the timestamp
    stand_str = result.find_all("span")[-1].text
    pattern_stand = re.compile(
        r".*(?P<date>\d{2}\.\d{2}\.\d{4})(, (?P<time>\d{2}:\d{2}))?.*"
    )
    timestamp_match = pattern_stand.match(stand_str)
    date_str = timestamp_match.group("date")
    time_str = timestamp_match.group("time")
    date = standardise_format(date_str, "%Y-%m-%d") if date_str else date_str
    time = standardise_format(time_str, "%Y-%m-%d") if time_str else time_str

    # so far they had the number in bold, let's see if I can rely on it
    number_str = result.find("strong").text
    pattern = re.compile(r"(?P<cases>\d+) ?")
    match = pattern.match(number_str)
    number = int(match.group("cases"))

    new_entry = f"{date},{time},{number}"
    print(new_entry)
