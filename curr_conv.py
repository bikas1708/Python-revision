import json
import requests


class EXCHG_RATE(object):

    def __init__(self, app_id, api_base="https://openexchangerates.org/api/"):
        self.api_base = api_base.rstrip("/")
        self.app_id = app_id
        self.session = requests.Session()

    def get_exchg(self):
        return self.__request("currenciecs.json")

    def __request(self, endpoint, payload=None):
        url = self.api_base + "/" + endpoint
        request = requests.Request("GET", url, params=payload)
        prepared = request.prepare()

        response = self.session.send(prepared)
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
            raise Exception(f"Request failed with status code {response.status_code}")
        json = response.json()
        if json is None:
            raise OXRDecodeError(request, response)
        return json


def load_rates(json_file: str) -> dict[str, dict]:

    with open(json_file, "r") as file:
        return json.load(file)


def ext_all(rates: dict[str, dict]) -> str:
    all: dict = [(key, value_dict["name"]) for key, value_dict in rates.items()]

    # return all
    for key, name in all:
        print(f"{key.strip()}: {name.strip()}")
    return print("eur: Euro")  # Need to return Euro too cuz not in file


def convert(amount: float, base: str, to: str, rates: dict[str, dict]) -> float:
    base: str = base.lower()
    to: str = to.lower()

    from_rates: dict | None = rates.get(base)
    to_rates: dict | None = rates.get(to)

    # Converting everything from euros so
    if from_rates is not None and to_rates is not None:
        if base == "eur":
            return amount * to_rates["rate"]

        else:
            return amount * (to_rates["rate"] / from_rates["rate"])
    elif from_rates is not None and to == "eur":
        return amount * from_rates["inverseRate"]

    else:
        print("Please enter a valid currency from below options!")
        # return [{key: value_dict["name"]} for key, value_dict in rates.items()]
        ext_all(rates)
        return 0


def main1() -> None:
    rates: dict[str, dict] = load_rates("rates.json")
    result: float = convert(amount=10, base="USD", to="eur", rates=rates)
    print(result)


def main() -> None:
    cli = EXCHG_RATE(app_id="8c435d81228a4735acd425e03a5a90ba")
    result = cli.get_exchg()
    print(result)


if __name__ == "__main__":
    main()


"""
Homework:
1. Right now it works fine if you insert a rate that exists, but make it so that if the user
enters a rate that doesn't exist, the program tells them that the currency is invalid, then
show them a list of all the valid currency options.
2. Edit the script so that the "to" currency can also be specified as euro. 
3. [Hard] Instead of loading the data from a local JSON file, try loading the data from an API. 
This task will require you to search online for a free API for currency exchange rates, and to make
a request to it so that you can load that data in this script. 

"""
