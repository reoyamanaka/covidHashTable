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
fsaOfInterest = "M5V"
print("Retrieving the number of ACTIVE COVID-19 cases in the FSA '%s'..."%fsaOfInterest)
start_time = time.time()
for fsa in fsasCases.keys():
    if fsa == fsaOfInterest: 
        print("The number of ACTIVE cases in the FSA is %d."%fsasCases[fsa])
print("This process, which used a list, took --- %s seconds ---." %(time.time() - start_time))

start_time = time.time()
print("The number of ACTIVE cases in the FSA is %d."%fsasCases[fsaOfInterest])
print("This process, which used a hash table, took --- %s seconds ---." % (time.time() - start_time))

    
