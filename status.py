import urllib2
import json
import os
import logging

claymoreExe = "C:\platform\claymore\ethdcrminer64.exe"
logFile = "c:\platform\status.log"
worker = "worker1"
wallet = "0xE18c5d3689476fBed966d36c9FEae502FC36d7f2"
email = "my@email.com"
secondsSinceSubmitLimit = 480

logging.basicConfig(filename=logFile,level=logging.DEBUG,format='%(asctime)s %(message)s')
logging.info("Checking status")

response = urllib2.urlopen("http://dwarfpool.com/eth/api?wallet="+wallet+"&email="+email)
string = response.read()
status = json.loads(string)
error = status["error"]
hashrate = status["workers"][worker]["hashrate"]
hashrateCalculated = status["workers"][worker]["hashrate_calculated"]
secondsSinceSubmit = status["workers"][worker]["second_since_submit"]

logging.info("since submit:"+ str(secondsSinceSubmit) + " error:" + str(error) +" HR:"+str(hashrate) +" HRC:"+str(hashrateCalculated))

if secondsSinceSubmit > secondsSinceSubmitLimit :
	logging.error("Restaring miner")
	os.system("taskkill /F /im ethdcrminer64.exe")
	os.startfile(claymoreExe)
