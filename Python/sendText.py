import os
import datetime
from twilio.rest import Client

''' 
* @author https://github.com/key6oardWarrior
'''

authFile = open("C:/FBS/FBSTC/Text_TC/AUTH.txt", "r").read()
sid = authFile[:34]
authToken = authFile[36:]
client = Client(sid, authToken)

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

def sendMessage(msgTimer): # send a message to each number on file
	textFrom = open("C:/FBS/FBSTC/Text_TC/textFrom.txt", "r").read()
	numberFile = open("C:/FBS/FBSTC/Text_TC/textToNumbers.txt", "r").read()
	lstNums = [""]
	j = 0

	for i in range(0, len(numberFile)): # adds numbers to list
		try:
			if numberFile[i] != " ":
				lstNums[j] += numberFile[i]
			else:
				j += 1
		except:
			break

	for i in lstNums: # send message
		message = client.messages.create(
			body = "URGENT: Please Check the Tech Coach schedule to know if you are working today!\nPlease do not respond this is an automated messaging system.\nDesigned by https://github.com/key6oardWarrior",
			from_ = textFrom, 
			to = i
		)

		if message.sid == sid: # print either error or success for each number
			print(message.sid + " sent the message!")
		else:
			print(message.sid)
	timer(msgTimer)

def currentTime(): # return what time it is
	dateTime = datetime.datetime.now()
	return dateTime.strftime("%X")

def timer(msgTimer): # determin when to send the message
	while currentTime() != currentTime():
		pass
	sendMessage(msgTimer)

def mainCaller():
	main()

def main(): # determin if send text or add numbers to file
	if os.path.exists("C:/FBS/FBSTC/Text_TC/textToNumbers.txt"):
		isAddNums = input("Do you want to add numbers to the list of numbers? Y/n ")

		if isAddNums.upper() == "Y":
			howManyNumbers()
			isSendMessage = input("Do you want to text all numbers? Y/n ")

			if isSendMessage.upper() == "Y":
				sendTime = open("C:/FBS/FBSTC/Text_TC/textTime.txt", "r").read()
				timer(sendTime)
			else:
				print("Message not sent :(")
		else:
			changeTime = input("Do you want to change the send time? Y/n ")

			if changeTime.upper() == "Y":
				textTime = open("C:/FBS/FBSTC/Text_TC/textTime.txt", "w")
				temp = input("What time do you want to text your people/person? Format: hh:mm:ss ")
				textTime.write(temp)
				textTime.close()

				sendTime = open("C:/FBS/FBSTC/Text_TC/textTime.txt", "r").read()
				timer(sendTime)
			else:
				sendTime = open("C:/FBS/FBSTC/Text_TC/textTime.txt", "r").read()
				timer(sendTime)	
	else:
		numberFile = open("C:/FBS/FBSTC/Text_TC/textToNumbers.txt", "w")
		numberFile.close()
		textTime = open("C:/FBS/FBSTC/Text_TC/textTime.txt", "w")

		temp = input("What time do you want to text your people/person? Format: hh:mm:ss ")
		textTime.write(temp)
		textTime.close()
		howManyNumbers()
		mainCaller()

if __name__ == "__main__":
	main()
