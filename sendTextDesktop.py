# @author: https://github.com/key6oardWarrior

import os
import sys
import datetime
from twilio.rest import Client

class SetUp:
	def addNums2File(self): # add each number to file
		numbers = 0

		try: # handle type mismatch
			numbers = int(input("Enter number: "))
		except:
			print("Please only enter numbers")
			return self.addNums2File()

		if len(str(numbers)) != 10:
			print("Your number must be 10 digits")
			return self.addNums2File()
		else:
			open("textToNumbers.txt", "a").write(str(numbers) + " ")

	def howManyNumbers(self): # ask user how many numbers do they want to add
		num = 0

		try: # handle type mismatch
			num = int(input("Enter how many numbers you want to text: "))
		except:
			print("Enter only numbers")
			return self.howManyNumbers()
	
		if num <= 0:
			print("Number must be greater than 0")
			return self.howManyNumbers()

		for i in range(0, num):
			self.addNums2File()

	def removeNums(self): # remove numbers from list of nums 2 be texted
		nums = open("textToNumbers.txt", "r").read().split()
		nums2Remove = input("What numbers do you want to remove? Seprate each phone number each by a whitespace. ").split()

		for i in nums2Remove:
			if i in nums:
				INDEX = nums.index(i)
				del nums[INDEX]

		for i in nums:
			open("textToNumbers.txt", "w").write(i + " ")

class MsgTimer:
	def timeChanger(self):
		open("textTime.txt", "w").write(input("What time do you want your message to be recived? Format MUST BE: hh:mm:ss "))

	def msgChanger(self):
		open("message.txt", "w").write(input("Enter new message: "))

	def sendMessage(self): # send a message to each number on file
		textFrom = open("textFrom.txt", "r").read().strip(" ")
		lstNums = open("textToNumbers.txt", "r").read().split()
		message = open("message.txt", "r").read()

		for i in lstNums: # send message
			message = Main.client.messages.create(
				body = message + "\nThis is an automated messaging system. Designed by https://github.com/key6oardWarrior via Twilio API",
				from_ = textFrom, 
				to = i
			)

			if message.sid == Main.sid: # print either error or success for each number
				print(message.sid, "sent the message!")
			else:
				print(message.sid, "error sending to", i)

	def getTime(self): # return what time it is
		return datetime.datetime.now().strftime("%X")

	def timer(self, msgTimer): # determin when to send the message
		while getTime() != msgTimer:
			pass
		sendMessage()

class Main:
	client = ""
	sid = ""

	def main(self): # handle user input
		setUp = SetUp()
		authToken = ""

		if not(os.path.exists("AUTH.txt")): # first time users setup
			authFile = open("AUTH.txt", "w")
			authFile.write(input("Enter Twilio SID: ") + ", ")
			authFile.write(input("Enter Twilio authentcation token: "))
			authFile.close()

		authFile = open("AUTH.txt", "r").read()

		try:
			sid = authFile[:34]
			authToken = authFile[36:]
		except:
			os.remove("AUTH.txt")
			print("SID must be 34 characters long and authentcation token must be at least 32 characters long. Please exit program and try again!")
			sys.exit()

		try:
			client = Client(sid, authToken)
		except:
			print("SID and Token must be authentic.")

		if os.path.exists("textToNumbers.txt"):
			isAddNums = input("Do you want to add numbers to be texted? Y/n ")
			if isAddNums.upper() == "Y":
				setUp.howManyNumbers()

			isRemoveNumbers = input("Do you want to remove any numbers? Y/n ")
			if isRemoveNumbers.upper() == "Y":
				setUp.removeNums()

			changeTime = input("Do you want to change the send time? Y/n ")
			if changeTime.upper() == "Y":
				setUp.timeChanger()

			changeMessage = input("Do you want to change the automated message? Y/n ")
			if changeMessage.upper() == "Y":
				setUp.msgChanger()

			print("Starting auto texting application")
			sendTime = open("textTime.txt", "r").read()
			sendMsg = MsgTimer()
			sendMsg.timer(sendTime)	
		else: # first time users setup
			numberFile = open("textToNumbers.txt", "w")
			numberFile.close()

			setUp.howManyNumbers()
			setUp.msgChanger()
			setUp.timeChanger()
			print("Starting auto texting application")
			sendTime = open("textTime.txt", "r").read()
			sendMsg = MsgTimer()
			sendMsg.timer(sendTime)	

app = Main()
app.main()
