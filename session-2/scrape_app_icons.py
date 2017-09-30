import json,urllib,os

with open('/Users/jerrychi/Downloads/sensor_strategy.csv') as f:
    print(f.readline())


url = 'http://itunes.apple.com/lookup?id=529479190'
response = urllib.urlopen(url)
picurl = json.loads(response.read())['results'][0]['artworkUrl100']
urllib.urlretrieve(picurl,'/Users/jerrychi/Downloads/dlpix/' + picurl.split('/')[-1])

    
    
    