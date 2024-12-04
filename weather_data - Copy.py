import ast, time, pycountry
def Weather(filename):
    with open(filename) as file:
        weather = ast.literal_eval(file.read())
        citydata = weather['city']
        weather_data = weather['list']
        coord, country, city = [citydata['coord'], citydata['country'], citydata['name']]
        with open(f"{filename.split('.txt')[0]}_data.txt", 'w') as news:
            news.write(f"Country: {pycountry.countries.get(alpha_2 = country).name}\n\n")
            news.write(f'City: {city}\n\n')
            news.write(f"Latitude: {coord['lat']}\t\t\tLongitude: {coord['lon']}\n\n")
            for i, day in enumerate(weather_data):
                news.write(time.ctime(weather_data[i]['dt']) + '\n\n')
                news.write(f"Temperature: {round(weather_data[i]['main']['temp'])} \
Degree Celcius" + '\n')
                news.write(f"Weather Description: {weather_data[i]['weather'][0]['description']}"
                .title() + '\n\n\n\n')
