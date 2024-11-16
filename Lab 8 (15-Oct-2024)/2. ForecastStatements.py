forecast = "It will be a sunny day today"

# (a) To variable count, the number of occurrences of string 'day' in string forecast.
count = forecast.count("day")

# (b) To variable weather, the index where substring 'sunny' starts.
weather = forecast.index('s')

# (c) To variable change, a copy of forecast in which every occurrence of substring 'sunny' is replaced by 'cloudy'.
change = forecast[:weather] + "cloudy" + forecast[weather + 5:]
