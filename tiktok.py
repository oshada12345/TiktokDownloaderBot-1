import requests
import json


url ='https://vm.tiktok.com/ZMFnohMVX/"'
def tik(url):
	url = "https://tiktok-info.p.rapidapi.com.p.rapidapi.com/vid/index"

	querystring = {"url":url}

	headers = {
		"X-RapidAPI-Key": "3f7b85e600msh163785d28acda05p113d81jsncbb31efb5ffc",
		"X-RapidAPI-Host": "tiktok-info.p.rapidapi.com.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	result = response.text
	rest = json.loads(result)
	print(rest)
	return {'Video': rest['video'][0], "Music":rest['music'[0]]}


print(tik(url))
