# @author: https://github.com/key6oardWarrior

import os
import sys
import datetime
from plyer import *

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
		j = 0

		for i in range(len(nums)): # remove numbers that are in both nums & nums2Remove
			if nums[i] in nums2Remove:
				del nums[i]
				i = 0

		isWrite = True
		for i in nums:
			if isWrite == False:
				open("textToNumbers.txt", "a").write(i + " ")
			else:
				open("textToNumbers.txt", "w").write(i + " ")
				isWrite = False

	def timeChanger(self):
		open("textTime.txt", "w").write(input("What time do you want your message to be recived? Format MUST BE: hh:mm:ss "))

	def msgChanger(self):
		open("message.txt", "w").write(input("Enter new message: "))

class MsgTimer:
	def sendMessage(self): # send a message to each number on file
		lstNums = open("textToNumbers.txt", "r").read().split()
		message = open("message.txt", "r").read()

		for i in lstNums:
			sms.send(i, message)

	def getTime(self): # return what time it is
		return datetime.datetime.now().strftime("%X") # test

	def timer(self, msgTimer): # determin when to send the message
		while True:
			while self.getTime() != msgTimer:
				pass
			self.sendMessage()

class Main:
	def main(self): # handle user input
		setUp = SetUp()

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

			sendTime = open("textTime.txt", "r").read()
		else: # first time users setup
			numberFile = open("textToNumbers.txt", "w")
			numberFile.close()

			setUp.howManyNumbers()
			setUp.msgChanger()
			setUp.timeChanger()

		print("Starting auto texting application")
		msgTimer = open("textTime.txt", "r").read()
		sendMsg = MsgTimer()
		sendMsg.timer(msgTimer)

app = Main()
app.main()
