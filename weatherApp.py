

import requests
import json


print()
print()
print()
print('# ' + '=' * 78)
print('Author: ' + "Vinit Vijal")
print('Version: ' + "1.0.1")
print('Maintainer: ' + "Vinit Vijal")
print('Email: ' + "Vinudev.web@gmail.com")
print('Status: ' + "Development")
print('Date: ' + "7th July 2021")
print('Username: ' + "@vinuDev_")
print('Description: ' + "Its a Weather App Created by Vinit Vijal. ")
print('# ' + '=' * 78)
print()
print()
print()
print()
# print("/////////////////////////////////////////////////////////////////////////")
# print("//    $$      $$  $$$$$     $$    $$$$$$ $$$$   $$$$$  $$$$            //")
# print("//     $$ $$ $$   $$$      $$$$     $$   $$  $  $$$    $$  $           //")
# print("//      $$  $$    $$$$$$  $$  $$    $$   $$$$   $$$$$$ $$$$            //")
# print("//                                       $$  $         $$  $           //")
# print("/////////////////////////////////////////////////////////////////////////")
# print()
# print()
# print()
# print()
print(" 1. Delhi ")
print(" 2. Mumbai ")
print(" 3. Jaipur ")
print(" 4. Kolkata ")
print(" 5. Agra ")
print(" 6. Bangalore ")
print(" 7. Hyderabad ")
print(" 8. Ahmedabad ")
print(" 9. Chennai ")
print(" 10. Assam ")


print()
print()
print()
code = "y"
city = int(input("Enter Your City Code : "))
def weather(city, code):
    while code=="y":
        if city == 1:
            response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+'Delhi'+'&appid=0c42f7f6b53b244c78a418f4f181282a')
            return response
            print()
            break
        elif city == 2:
            response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+'Mumbai'+'&appid=0c42f7f6b53b244c78a418f4f181282a')
            print()
            return response
            break
        elif city == 3:
            response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+'Jaipur'+'&appid=0c42f7f6b53b244c78a418f4f181282a')
            print()
            return response
            break
        elif city == 4:
            response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+'Mumbai'+'&appid=0c42f7f6b53b244c78a418f4f181282a')
            print()
            return response
            break
        elif city == 5:
            response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+'Agra'+'&appid=0c42f7f6b53b244c78a418f4f181282a')
            print()
            return response
            break
        elif city == 6:
            response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+'Bangalore'+'&appid=0c42f7f6b53b244c78a418f4f181282a')
            print()
            return response
            break
        elif city == 7:
            response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+'Hyderabad'+'&appid=0c42f7f6b53b244c78a418f4f181282a')
            print()
            return response
            break
        elif city == 8:
            response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+'Ahmedabad'+'&appid=0c42f7f6b53b244c78a418f4f181282a')
            print()
            return response
            break
        elif city == 9:
            response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+'Chennai'+'&appid=0c42f7f6b53b244c78a418f4f181282a')
            print()
            return response
            break
        elif city == 10:
            response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+'Assam'+'&appid=0c42f7f6b53b244c78a418f4f181282a')
            print()
            return response
            break
        else:
            print("Wrong Input!!!!!!")
            break
data = weather(city, code)
json_data = json.loads(data.text)
print()
print(json_data)
print()
print()
print()
print("===========================================================")
print()
print("Name of City : " + json_data['name'])
print()
print("Current Temperature of Today is : " + str(str(round(float(json_data['main']['temp'])-273.16)))+ " C")
print()
print("Current Mood of weather : " + str(((json_data['weather'])[-1])['main']))
print()
print("===========================================================")
print()
print()
code = input("Do you want more weather details? (y/n) : ")
print()
print()

print("Thanks For Using 'VinuWeather PyApp' Byy....")
print()


