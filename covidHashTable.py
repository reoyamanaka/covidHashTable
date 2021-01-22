import time, requests

fsasCases = {}

url = "https://ckan0.cf.opendata.inter.prod-toronto.ca/download_resource/e5bf35bc-e681-43da-b2ce-0242d00922ad?format=json"
resp = requests.get(url)
for obj in resp.json():
    if obj['Outcome'] == "ACTIVE":
        if not obj['FSA'] in fsasCases.keys():
            fsasCases[obj["FSA"]] = 0
        else:
            fsasCases[obj["FSA"]] += 1

start_time = time.time()
for fsa in fsasCases.keys():
    if fsa == "M5V":
        print(fsasCases[fsa])
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(fsasCases["M5V"])
print("--- %s seconds ---" % (time.time() - start_time))

    
