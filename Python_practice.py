counties = ("Arapahoe", "Denver", "Jefferson")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys

for county, voters in counties_dict.items():
    print(county + "has " + str(voters) + " registered voters.")
