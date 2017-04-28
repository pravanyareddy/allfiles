import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode


while True:
  (error, tag_type) = GPIO.request()
  if not error:
    print("Tag detected")
    (error, uid) = GPIO.anticoll()
    if not error:
      print("UID: " + GPIO(uid))
      # Select Tag is required before Auth
      if not GPIO.select_tag(uid):
        # Auth for block 10 (block 2 of sector 2) using default shipping key A
        if not GPIO.card_auth(GPIO.auth_a, 10, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], uid):
          # This will print something like (False, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
          print("Reading block 10: " + GPIO(GPIO.read(10)))
          # Always stop crypto1 when done working
          GPIO.stop_crypto()

# Calls GPIO cleanup
GPIO.cleanup()
