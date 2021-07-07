import requests
import json
print("/////////////////////////////////////////////////////////////////////////")
print("//    $$      $$  $$$$$     $$    $$$$$$ $$$$   $$$$$  $$$$            //")
print("//     $$ $$ $$   $$$      $$$$     $$   $$  $  $$$    $$  $           //")
print("//      $$  $$    $$$$$$  $$  $$    $$   $$$$   $$$$$$ $$$$            //")
print("//                                       $$  $         $$  $           //")
print("/////////////////////////////////////////////////////////////////////////")
print(" 1. Delhi ")
print(" 2. Mumbai ")
print(" 3. Jaipur ")
print(" 4. Kolkata ")
print()
print()
print()
city = int(input("Enter Your City Code : "))
if city == 1:
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+'Delhi'+'&appid=0c42f7f6b53b244c78a418f4f181282a')
    print()
elif city == 2:
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+'Mumbai'+'&appid=0c42f7f6b53b244c78a418f4f181282a')
    print()
elif city == 3:
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+'Jaipur'+'&appid=0c42f7f6b53b244c78a418f4f181282a')
    print()
elif city == 4:
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+'Kolkata'+'&appid=0c42f7f6b53b244c78a418f4f181282a')
    print()
else:
    print("Wrong Input!!!!!!")
    breakpoint
json_data = json.loads(response.text)
print()
# print(json_data)
print()
print()
print()
print("Name of City : " + json_data['name'])
print("Current Temperature of Today is : " + str(json_data['main']['temp'])+ " C")
print("Current Mood of weather : " + str(((json_data['weather'])[0])['main']))


