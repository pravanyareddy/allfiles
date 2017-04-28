import urllib2
import urllib
GPIO.setwarnings(False)
url = 'http://www.cykul.com/cykulstations/python/getcardValidationstatus.php'
data = urllib2.urlopen('http://www.cykul.com/cykulstations/python/getcardValidationstatus.php')
GPIO.cleanup()

