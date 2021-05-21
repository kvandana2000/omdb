import requests
import json, sys

if not len(sys.argv) == 3:
    print("please pass movie title and api key as arguments. For ref check below example")
    print("**********Example********")
    print("docker run mycustomimage:tag python /app/app.py avengers  api_key")
    sys.exit()

parameters = {}
parameters['t'] = sys.argv[1]
api_key = sys.argv[2]
response = requests.get("http://www.omdbapi.com/?apikey=" + api_key + "&", params=parameters)
code = response.status_code
if code == 200:
    print("request success: " + str(code))
else:
    print("request failed: " + str(code))
    sys.exit()    
data2json = json.dumps(response.json(), sort_keys=True, indent=4)
data2dict = json.loads(data2json)
var = data2dict['Ratings']
for i in var:
    if i['Source'] == 'Rotten Tomatoes':
        print("Rotten Tomatoes rating :" + i['Value'])
        break
