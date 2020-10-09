import pandas as pd

world_cups_matches = pd.read_csv("WorldCupMatches.csv")
world_cups_matches = world_cups_matches.replace("Germany FR", "Germany")
world_cups_matches = world_cups_matches.replace("C�te d'Ivoire", "Côte d'Ivoire")
world_cups_matches = world_cups_matches.replace(
    'rn">Republic of Ireland', "Republic of Ireland"
)
world_cups_matches = world_cups_matches.replace(
    'rn">Bosnia and Herzegovina', "Bosnia and Herzegovina"
)
world_cups_matches = world_cups_matches.replace(
    'rn">Serbia and Montenegro', "Serbia and Montenegro"
)
world_cups_matches = world_cups_matches.replace(
    'rn">Trinidad and Tobago', "Trinidad and Tobago"
)
world_cups_matches = world_cups_matches.replace(
    'rn">United Arab Emirates', "United Arab Emirates"
)
world_cups_matches = world_cups_matches.replace("Soviet Union", "Russia")
world_cups_matches = world_cups_matches.drop_duplicates()