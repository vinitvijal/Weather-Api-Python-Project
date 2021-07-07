import requests
import json

# My Functions Are Down Here :
def weather(city):
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=0c42f7f6b53b244c78a418f4f181282a')
    return response
    print()
    # json_check = json.loads(response.text)
    # if json_check['message'] == "city not found":
    #     print()
    #     print("Spelling of City is Wrong")
    # else:
    #     return response
    #     print()
        

# Main Program

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


num = 0                     #at 0 it will directly run without asking do you want details....
work = 1                    #Here 1 means Yes and 0 means No
while work == 1:
    if num != 0:
        code = input("Try More Cities? (y/n) : ")
        if code== "y":
            print()
            print()
            print()
            city = input("Enter Your City Name : ")
            weather(city)
            data = weather(city)
            json_data = json.loads(data.text)
            print()
            # print(json_data)
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
            num += 1
        elif code =="n" :
            print()
            print()
            print()
            print("Thanks For Using 'VinuWeather PyApp' Byy....")
            break
        else:
            print("Wrong Input!!!!!")
    elif num == 0:
            city = input("Enter Your City Name : ")
            weather(city)
            data = weather(city)
            json_data = json.loads(data.text)
            print()
            # print(json_data)
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
            num += 1