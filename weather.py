import requests
import os
import sys

while True:
    example_cities = ["London", "Tokyo", "New York"]
    print("Enter a city to check its weather. 3-letter airport codes, ZIP codes and GPS cooridinates are accepted. Examples:")
    for i in example_cities:
        print(i, end=" ")
    print()
    city = str(input("City: "))
    city = city.strip().title().replace(" ", "")

    try:
        weather = requests.get("https://wttr.in/" + city).text
        print(weather)
    except requests.exceptions.RequestException:
        print("Not a valid city.")
        pass
    while True:
        end = input("Clear screen / exit: ").lower()
        if end == "clear screen":
            os.system("cls")
            break
        elif end == "exit":
            sys.exit()
        else:
            print("Invalid choice. ")
            pass