#!/home/renat/envs/scraper/bin/python
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://gesundheit.jena.de/de/coronavirus"

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
    pattern_stand = re.compile(r".*(?P<timestamp>\d{2}\.\d{2}\.\d{4}, \d{2}:\d{2}).*")
    timestamp_str = pattern_stand.match(stand_str).group("timestamp")
    timestamp = datetime.strptime(timestamp_str, "%d.%m.%Y, %H:%M")
    date = timestamp.strftime("%Y-%m-%d")
    time = timestamp.strftime("%H:%M")

    # so far they had the number in bold, let's see if I can rely on it
    number_str = result.find("strong").text
    pattern = re.compile(r"(?P<cases>\d+) ?")
    match = pattern.match(number_str)
    number = int(match.group("cases"))

    new_entry = f"{date},{time},{number}"
    print(new_entry)
