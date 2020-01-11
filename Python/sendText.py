import os
import datetime
from twilio.rest import Client

''' 
* Author https://github.com/key6oardWarrior
* Code Propety of Full Blast S.T.E.A.M
* Twilio API used https://twilio.com
'''

authFile = open("C:/FBS/FBSTC/Text_TC/AUTH.txt", "r").read()
sid = authFile[:34]
authToken = authFile[36:]
client = Client(sid, authToken)

def howManyNumbers(): # ask user how many numbers do they want to add
	num = 0

	try: # handle type mismatch
		num = int(input("Enter how many numbers you want to text: "))
	except:
		print("Enter only numbers")
		howManyNumbers()
	
	if num <= 0:
		print("Number must be greater than 0")
		howManyNumbers()

	for i in range(0, num):
		addNums2File()

def addNums2File(): # add each number to file
	numberFile = open("C:/FBS/FBSTC/Text_TC/textToNumbers.txt", "a")
	numbers = 0

	try: # handle type mismatch
		numbers = int(input("Enter number: "))
	except:
		print("Please only enter numbers")
		addNums2File()

	if len(str(numbers)) != 10:
		print("Your number must be 10 digits")
		addNums2File()
	else:
		numberFile.write(str(numbers) + " ")
	numberFile.close()

def sendMessage(): # send a message to each number on file
	textFrom = open("C:/FBS/FBSTC/Text_TC/textFrom.txt", "r").read()
	numberFile = open("C:/FBS/FBSTC/Text_TC/textToNumbers.txt", "r").read()
	cnt = 0

	for i in range(0, len(numberFile)): # count how many phone numbers
		if numberFile[i] == " ":
			cnt += 1

	lstNums = [""]*cnt
	j = 0

	for i in range(0, len(numberFile)): # adds numbers to list
		if numberFile[i] != " ":
			lstNums[j] += numberFile[i]
		else:
			j += 1

	for i in lstNums: # send message
		message = client.messages.create(
			body = "URGENT: Please Check the Tech Coach schedule to know if you are working today!\nPlease do not respond this is an automated messaging system.\nDesigned by https://github.com/key6oardWarrior",
			from_ = textFrom, 
			to = i
		)

		if message.sid == sid: # print either error or success for each number
			print(message.sid + " sent the message!")
			timer()
		else:
			print(message.sid)

def currentTime(): # return what time it is
	dateTime = datetime.datetime.now()
	return dateTime.strftime("%X")

def timer(): # determin when to send the message
	while currentTime() != "5:00:00":
		currentTime()
	sendMessage()

def main(): # determin if send text or add numbers to file
	if os.path.exists("C:/FBS/FBSTC/Text_TC/textToNumbers.txt"):
		isAddNums = input("Do you want to add numbers to the list of numbers? Y/n ")
		if isAddNums.upper() == "Y":
			howManyNumbers()
			isSendMessage = input("Do you want to text all numbers? Y/n ")
			if isSendMessage.upper() == "Y":
				timer()
			else:
				print("Message not sent :(")
		else:
			timer()	
	else:
		numberFile = open("C:/FBS/FBSTC/Text_TC/textToNumbers.txt", "w")
		numberFile.close()
		howManyNumbers()
		main()

if __name__ == "__main__":
	main()
