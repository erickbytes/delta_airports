import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_Delta_Air_Lines_destinations"
tables = pd.read_html(url)
destinations = tables[0]
print(destinations.head())
