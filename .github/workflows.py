import requests
from typing import Optional


class Brewery:
    def __init__(
        self,
        brewery_id: str,
        name: str,
        brewery_type: str,
        city: str,
        street: Optional[str],
        country: str,
        latitude: Optional[str],
        longitude: Optional[str],
    ):
        self.brewery_id = brewery_id
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.street = street
        self.country = country
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self) -> str:
        return (
            "Brewery:\n"
            f"  Name: {self.name}\n"
            f"  Type: {self.brewery_type}\n"
            f"  City: {self.city}\n"
            f"  Street: {self.street}\n"
            f"  Country: {self.country}\n"
            f"  Coordinates: ({self.latitude}, {self.longitude})"
        )


def fetch_breweries():
    url = "https://api.openbrewerydb.org/breweries"
    params = {"per_page": 20}

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    return response.json()