#if we are looking for the highest temperature on 6 Jan...

temperature_data = []
with open("weather_data.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        temperature = float(tokens[1])
        temperature_data.append([day, temperature])

for element in temperature_data:
    if element[0] == "6-Jan":
        print(element[1])
        
    
