from bs4 import BeautifulSoup
import requests
import json



url_date = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2_%D0%B8_%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D1%8B%D1%85_%D1%82%D0%B5%D1%80%D1%80%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B9_%D0%BF%D0%BE_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8E"

def get_country_population():
    raw_page = requests.get(url=url_date).text
    
    soup = BeautifulSoup(raw_page, "html.parser")
    countries_table = soup.find("table", class_="standard").find("tbody")
    countries_rows = countries_table.find_all("tr")

    result_data = {}
    for row in countries_rows[1:]:
        population = row.find_all("td")[2].text

        country_name = row.find_all("td")[1].find("a").text
        if country_name == "":
            country_name = row.find_all("td")[1].find_all("a")[1].text
        
        result_data[country_name] = int(population.replace(" ", "").replace(" ", ""))

    with open("countryData.json", "w", encoding="utf-8") as json_file:
        json.dump(result_data, json_file)

get_country_population()