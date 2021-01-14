travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


def add_new_country(country, visits, cities):
    newDict = {"country": country, "visits": visits,
               "cities": cities}  # created a new dictionary
    # for city in cities: # loop through the list and append
    #     newDict["cities"].append(city)
    travel_log.append(newDict)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg", ])

print(travel_log)
