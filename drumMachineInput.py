#WasteMyTime.wav 6.012 secs
#TooLate.wav 5.994 secs
#StayWokeClean.wav 6.021 secs
#CloseYourEyes.wav 5.986 secs
#BassAndSnare.wav 2.942 secs
#BassAndGuitar.wav 8.999 secs
#MainMelody.wav 12.071 secs
#TheyGoneFindYou.wav 5.994 secs
from music import *
from osc import *
import time

sample1 = AudioSample("redboneSamples\MainMelody.wav")
sample2 = AudioSample("redboneSamples\TheyGoneFindYou.wav")
sample3 = AudioSample("redboneSamples\CloseYourEyes.wav")
sample4 = AudioSample("redboneSamples\TooLate.wav")
sample5 = AudioSample("redboneSamples\BassAndGuitar.wav")
sample6 = AudioSample("redboneSamples\WasteMyTime.wav")

redboneSamples = [sample1,sample2,sample3,sample4,sample5,sample6]
def stopSamples(sampleArray):
   for i in sampleArray:
      i.stop()

def buttonInput(message):
   stopSamples(redboneSamples)
   print "in button input"
   OSCaddress = message.getAddress()
   print OSCaddress
   args = message.getArguments()
   if args[0]==0.0:
      if OSCaddress == "/1/push1" or OSCaddress=="/multi/0":
         sample1.play()
         print "Inside 1"
      elif OSCaddress == "/1/push2" or OSCaddress=="/multi/1":
         sample2.play()
         print "Inside 2"
      elif OSCaddress =="/1/push3" or OSCaddress=="/multi/2":
         sample3.play()
         print "Inside 3"
      elif OSCaddress =="/1/push4" or OSCaddress=="/multi/3":
         sample4.play()
         
      elif OSCaddress =="/1/push5" or OSCaddress=="/multi/4":
         sample5.play()
      elif OSCaddress="/1/stop8":
         stopSamples(redboneSamples)
        
      else:
         sample6.play()
            
oscIn= OscIn(8000) # sets up an connection to accept OSC messages through port 8000         
oscIn.onInput("/.*",buttonInput) #sends messages via all addresses to the function button input



"""
for i in range(3):
   sample1.play()
   time.sleep(12.071)
sample2.play()
time.sleep(5.994)
sample5.play()
time.sleep(8.999)
for i in range(2):
   sample4.play()
   time.sleep(5.994)
sample6.play()
""" 
