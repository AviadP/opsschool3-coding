import json

j = "input.json"

with open ("input.json") as jfile:
    output = json.load(jfile)

#print(output)
ppl_ages = output['ppl_ages']
buckets = output['buckets']
print (ppl_ages, "\n", buckets)