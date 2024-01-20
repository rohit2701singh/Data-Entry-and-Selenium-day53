from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
content = response.text


class Rent:
    def __init__(self):
        self.__places = None

        soup = BeautifulSoup(content, "html.parser")

        all_places = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
        self.__place_detail(all_places)

    def __place_detail(self, places):

        self.__places = places
        self.__full_detail = []

        for place in self.__places:

            rent_tag = place.find(name="span", class_="PropertyCardWrapper__StyledPriceLine")
            rent = rent_tag.getText().strip()

            place_address_tag = place.select_one(selector="div a")

            place_link = place_address_tag.get("href").strip()
            place_address = place_address_tag.getText().strip()
            self.__full_detail.append({"place_rent": rent, "address": place_address, "address_link": place_link})

    def get_detail(self):
        return self.__full_detail