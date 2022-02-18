import requests
import jsonpath
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}
response = requests.get('https://www.lagou.com/lbs/getAllCitySearchLabels.json', headers=headers)
dict_data = json.loads(response.content)
print(jsonpath.jsonpath(dict_data, '$..name..A'))


