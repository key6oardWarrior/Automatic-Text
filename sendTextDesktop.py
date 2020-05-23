import os
import sys
import datetime
from twilio.rest import Client

# @author: https://github.com/key6oardWarrior

sid = ""
authToken = ""
callTimer = False

if not(os.path.exists("C:/Code/Python/AutoText/AUTH.txt")): # first time users setup
	authFile = open("C:/Code/Python/AutoText/AUTH.txt", "w")
	authFile.write(input("Enter Twilio SID: ") + ", ")
	authFile.write(input("Enter Twilio authentcation token: "))
	authFile.close()

authFile = open("C:/Code/Python/AutoText/AUTH.txt", "r").read()

try:
	sid = authFile[:34]
	authToken = authFile[36:]
except:
	os.remove("C:/Code/Python/AutoText/AUTH.txt")
	print("SID must be 34 characters long and authentcation token must be at least 32 characters long. Please exit program and try again!")
	sys.exit()

client = Client(sid, authToken)

def addNums2File(): # add each number to file
	numberFile = open("C:/Code/Python/AutoText/textToNumbers.txt", "a")
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

def removeNums(): # remove numbers from list of nums 2 be texted
	nums = [""]
	numbers = open("C:/Code/Python/AutoText/textToNumbers.txt", "r").read()
	nums2Remove = input("What numbers do you want to remove (seprate phone number each by a whitespace)? ")
	j = 0

	for i in range(len(numbers)): # add all nums to nums list
		if numbers[i] != " ":
			nums[j] += numbers[i]
		else:
			nums.append("")
			j += 1

	j = 0
	for i in nums: # remove all occurrences of nums2Remove
		try:
			if i == nums2Remove[j: j+10]:
				numbers = numbers.strip(i)
				j += 11
		except:
			break

	print("final print: " + numbers)
	fileWriter = open("C:/Code/Python/AutoText/textToNumbers.txt", "w").write(numbers)

def timeChanger():
	textTime = open("C:/Code/Python/AutoText/textTime.txt", "w").write(input("What time do you want your message to be recived? Format MUST BE: hh:mm:ss "))

def msgChanger():
	messageChanger = open("C:/Code/Python/AutoText/message.txt", "w").write(input("Enter new message: "))

def sendMessage(): # send a message to each number on file
	textFrom = open("C:/Code/Python/AutoText/textFrom.txt", "r").read()
	numberFile = open("C:/Code/Python/AutoText/textToNumbers.txt", "r").read()
	message = open("C:/Code/Python/AutoText/message.txt").read()
	lstNums = numberFile.split()

	for i in lstNums: # send message
		message = client.messages.create(
			body = message + "\nThis is an automated messaging system. Designed by https://github.com/key6oardWarrior",
			from_ = textFrom, 
			to = i
		)

		if message.sid == sid: # print either error or success for each number
			print(message.sid + " sent the message!")
		else:
			print(message.sid)

def getTime(): # return what time it is
	dateTime = datetime.datetime.now()
	return dateTime.strftime("%X")

def timer(msgTimer): # determin when to send the message
	while getTime() != msgTimer:
		pass
	sendMessage()

def main(): # handle user input
	if os.path.exists("C:/Code/Python/AutoText/textToNumbers.txt"):
		isAddNums = input("Do you want to add numbers to be texted? Y/n ")
		if isAddNums.upper() == "Y":
			howManyNumbers()

		isRemoveNumbers = input("Do you want to remove any numbers? Y/n ")
		if isRemoveNumbers.upper() == "Y":
			removeNums()

		changeTime = input("Do you want to change the send time? Y/n ")
		if changeTime.upper() == "Y":
			timeChanger()

		changeMessage = input("Do you want to change the automated message? Y/n ")
		if changeMessage.upper() == "Y":
			msgChanger()

		sendTime = open("C:/Code/Python/AutoText/textTime.txt", "r").read()
		timer(sendTime)	
	else: # first time users setup
		numberFile = open("C:/Code/Python/AutoText/textToNumbers.txt", "w")
		numberFile.close()

		howManyNumbers()
		msgChanger()
		timeChanger()

while __name__ == "__main__":
	if callTimer == False:
		callTimer = True
		main()
	else:
		msgTimer = open("C:/Code/Python/AutoText/textTime.txt", "r").read()
		timer(msgTimer)
