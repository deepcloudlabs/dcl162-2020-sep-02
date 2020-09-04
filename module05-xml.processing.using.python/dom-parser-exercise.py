from xml.dom import minidom
from world.domain import Country

dom_tree = minidom.parse("resources/countries.xml")
root_countries = dom_tree.documentElement

countries = root_countries.getElementsByTagName("country")
asian_countries = []

for country in countries:
    continent = country.getElementsByTagName("Continent")[0].childNodes[0].data
    if continent == "Asia":
        ctry = Country()
        ctry.continent = continent
        ctry.code = country.getElementsByTagName("Code")[0].childNodes[0].data
        ctry.name = country.getElementsByTagName("Name")[0].childNodes[0].data
        ctry.population = country.getElementsByTagName("Population")[0].childNodes[0].data
        ctry.surfaceArea = country.getElementsByTagName("SurfaceArea")[0].childNodes[0].data
        asian_countries.append(ctry)

for asian_country in asian_countries:
    print(asian_country)
