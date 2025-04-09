countries = [
    {"name": "India", "population": 1463865525},
    {"name": "USA", "population": 347275807},
    {"name": "China", "population": 1416096094},
    {"name": "France", "population":66650804}
]
for country in countries:
    print(f"{country['name']}  population  {country['population']:,}")

biggest = countries[0]
for country in countries:
    if country["population"] > biggest["population"]:
        biggest = country
print(f"The biggest country is {biggest["name"]} with a population of {biggest["population"]:,}")