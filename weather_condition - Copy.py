import argparse, json, requests, pyperclip, pprint, pycountry
from Mclipboard import multi_clip
from weather_data import Weather
parser = argparse.ArgumentParser()
parser.add_argument('country_code')
parser.add_argument('city_name', nargs = '+')
arg = parser.parse_args()
multi_clip('get', 'APIID')
APIID = pyperclip.paste()
location = ' '.join(arg.city_name) + ', ' + arg.country_code
url = 'https://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s&units=metric' % (location, APIID)
download = requests.get(url)
download.raise_for_status()
json_text = download.text
file = f"{pycountry.countries.get(alpha_2 = arg.country_code).name} \
_{' '.join(arg.city_name)}_weather_condition.txt"
with open(file, 'w') as note:
    note.write(pprint.pformat(json.loads(json_text)))
Weather(file)
