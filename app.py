import requests
import json, sys

if not len(sys.argv) == 2:
    print("usage: python3 app.py arg(movie name)")
    sys.exit()

parameters = {}
parameters['t'] = sys.argv[1]
response = requests.get("http://www.omdbapi.com/?apikey=aa38cdb2&", params=parameters)
data2json = json.dumps(response.json(), sort_keys=True, indent=4)
data2dict = json.loads(data2json)
var = data2dict['Ratings']
for i in var:
    if i['Source'] == 'Rotten Tomatoes':
        print("Rotten Tomatoes rating :" + i['Value'])
        break
