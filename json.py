import json
import RPi.GPIO as GPIO

json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
'["foo", {"bar": ["baz", null, 1.0, 2]}]'
print json.dumps("\"foo\bar")
"\"foo\bar"
print json.dumps(u'\u1234')
"\u1234"
print json.dumps('\\')
"\\"
print json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
{"a": 0, "b": 0, "c": 0}
from StringGPIO import StringGPIO
GPIO = StringGPIO()
json.dump(['streaming API'], GPIO)
GPIO.getvalue()
