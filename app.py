import json

f = open('data.json')

data = json.load(f)

newData = {}

for i in data:
    actors = i['stars'].split(', ')
    for actor in actors:
        if not actor in newData:
            newData[actor] = {}
            newData[actor]['appearances'] = 1
            newData[actor]['ratings'] = []
            newData[actor]['ratings'].append(float(i['rating']))
        else:
            newData[actor]['appearances'] += 1
            newData[actor]['ratings'].append(float(i['rating']))
            
for key, value in newData.items():
    if value['appearances'] >= 2:
        rating = '{0:.2f}'.format(sum(value['ratings'])/len(value['ratings']))
        print("Star Name: " + key + " Movies: " + str(value['appearances']) + " AVG Rating: " + str(rating))