import time
#if we are looking for the temperature on 6 Jan...
temperature_data = []
temperature_dict = {}
with open("weather_data.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        temperature = float(tokens[1])
        temperature_data.append([day, temperature])
        temperature_dict[day] = temperature

#comparing the execution times

start_time = time.time()
for element in temperature_data:
    if element[0] == "6-Jan":
        print(element[1])
        
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(temperature_dict["6-Jan"])
print("--- %s seconds ---" % (time.time() - start_time))


    
