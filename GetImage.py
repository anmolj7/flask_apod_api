import requests 
from bs4 import BeautifulSoup
import datetime
from credentials import API_KEY

URL = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}'

class Image:
    def __init__(self, json_data):
        self.Dict = json_data 
        print(self.Dict)
        for key in self.Dict:
            setattr(self, key, self.Dict[key])

    def __getitem__(self, key):
        if key in self.Dict:
            return self.Dict[key]
        return False 

    def keys(self):
        return list(self.Dict.keys())

    def values(self):
        return list(self.Dict.values())


def get_json_data(str_date):
    #Date should be in the format YYYY-MM-DD
    date = datetime.datetime.strptime(str_date, '%m/%d/%Y')
    print(date)
    if date.date() > datetime.date.today() or date.date() < datetime.date(1995, 6, 16):
        return False #Since date can't be smaller than 16th june 1995, or more than today's date.
    curr_url = URL + f'&date={str(date.date())}'
    json = requests.get(curr_url).json()
    return json 


def main():
    str_date = str(datetime.date.today())
    data = get_json_data(str_date)
    Img = Image(data)
    print(Img['hdurl'])
    print(Img.keys())
    print(Img.hdurl)
    print(Img.url)


if __name__ == "__main__":
    main()