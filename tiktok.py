import requests
import json


url ='https://vm.tiktok.com/ZMFnohMVX/"'
def tik(url):
	url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

	querystring = {"url":url}

	headers = {
		"X-RapidAPI-Key": "3fd3438d2fmsh3b6d9366cc09585p10da90jsn9922848ab085",
		"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	result = response.text
	rest = json.loads(result)
	print(rest)
	return {'Video': rest['video'][0], "Music":rest['music'[0]]}


print(tik(url))