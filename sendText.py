import os
import datetime
from twilio.rest import Client

# @author: https://github.com/key6oardWarrior

authFile = open("C:/FBS/FBSTC/Text_TC/AUTH.txt", "r").read()
sid = authFile[:34]
authToken = authFile[36:]
client = Client(sid, authToken)
callTimer = False

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

def removeNums():
	nums = [""]
	numbers = open("C:/FBS/FBSTC/Text_TC/textToNumbers.txt", "r").read()
	nums2Remove = input("What numbers do you want to remove (seprate each by whitespace)? ")
	j = 0

	for i in range(len(numbers)):
		if numbers[i] != " ":
			nums[j] += numbers[i]
		else:
			nums.append("")
			j += 1

	j = 0
	for i in nums:
		print(nums)
		if i == numbers[j: j+10]:
			numbers = numbers.strip(numbers[j: j+11])
			j += 11

	print("final print: " + numbers)
	fileWriter = open("C:/FBS/FBSTC/Text_TC/textToNumbers.txt", "w").write(numbers)

def timeChanger():
	textTime = open("C:/FBS/FBSTC/Text_TC/textTime.txt", "w").write(input("What time do you want your message to be recived? Format MUST BE: hh:mm:ss "))

def msgChanger():
	messageChanger = open("C:/FBS/FBSTC/Text_TC/message.txt", "w").write(input("Enter new message: "))

def sendMessage(): # send a message to each number on file
	textFrom = open("C:/FBS/FBSTC/Text_TC/textFrom.txt", "r").read()
	numberFile = open("C:/FBS/FBSTC/Text_TC/textToNumbers.txt", "r").read()
	message = open("C:/FBS/FBSTC/Text_TC/message.txt").read()
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
	if os.path.exists("C:/FBS/FBSTC/Text_TC/textToNumbers.txt"):
		isAddNums = input("Do you want to add numbers to the list of numbers? Y/n ")
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

		sendTime = open("C:/FBS/FBSTC/Text_TC/textTime.txt", "r").read()
		timer(sendTime)	
	else:
		numberFile = open("C:/FBS/FBSTC/Text_TC/textToNumbers.txt", "w")
		numberFile.close()

		howManyNumbers()
		msgChanger()
		timeChanger()

while __name__ == "__main__":
	if callTimer == False:
		callTimer = True
		main()
	else:
		msgTimer = open("C:/FBS/FBSTC/Text_TC/textTime.txt", "r").read()
		timer(msgTimer)