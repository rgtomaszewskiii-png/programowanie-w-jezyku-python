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

    def __str__(self):
        return (
            f"Brewery:\n"
            f"  Name: {self.name}\n"
            f"  Type: {self.brewery_type}\n"
            f"  City: {self.city}\n"
            f"  Street: {self.street}\n"
            f"  Country: {self.country}\n"
            f"  Coordinates: ({self.latitude}, {self.longitude})"
        )

    import requests

    def fetch_breweries(city: str | None = None):
        url = "https://api.openbrewerydb.org/breweries"
        params = {"per_page": 20}

        if city:
            params["by_city"] = city

        response = requests.get(url, params=params)
        response.raise_for_status()

        return response.json()

    def create_brewery_objects(data):
        breweries = []

        for item in data:
            brewery = Brewery(
                brewery_id=item["id"],
                name=item["name"],
                brewery_type=item["brewery_type"],
                city=item["city"],
                street=item["street"],
                country=item["country"],
                latitude=item["latitude"],
                longitude=item["longitude"],
            )
            breweries.append(brewery)

        return breweries

    def display_breweries(breweries):
        for brewery in breweries:
            print(brewery)
            print("-" * 40)

            import argparse
def main():
    parser = argparse.ArgumentParser(description="Fetch breweries from OpenBreweryDB API")
    parser.add_argument(
        "--city",
        type=str,
        help="Filter breweries by city name",
        required=False
    )

    args = parser.parse_args()

    data = fetch_breweries(args.city)
    breweries = create_brewery_objects(data)
    display_breweries(breweries)


if __name__ == "__main__":
    main()