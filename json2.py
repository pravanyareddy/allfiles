import requests
import json
import time
 
responseReceived = requests.get("http://www.cykul.com/CYKULStations/Python/getCardValidationStatus.php")
 
parentRootJSONObject = responseReceived.json()
 
print(parentRootJSONObject)
 
print(parentRootJSONObject['validation_status'])
 
print(parentRootJSONObject['validation_status_message'])
#json_txt = requests.get('responseReceived = requests.get("http://www.cykul.com/CYKULStations/Python/getCardValidationStatus.php")

#parsed_json = json.loads(json_txt)

#print parsed_json['Valid']

#json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
#'["foo", {"bar": ["baz", null, 1.0, 2]}]'
#print json.dumps("\"foo\bar")
#"\"foo\bar"
#print json.dumps(u'\u1234')
#"\u1234"
#print json.dumps('\\')
#"\\"
#print json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
#{"a": 0, "b": 0, "c": 0}
#from StringGPIO import StringGPIO
#GPIO = StringGPIO()
#json.dump(['streaming API'],GPIO)
