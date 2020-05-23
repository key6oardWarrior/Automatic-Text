# @author: https://github.com/key6oardWarrior

import os
import sys
import datetime
from plyer import *

class SetUp:
	def addNums2File(self): # add each number to file
		numberFile = open("C:/Code/Python/AutoText/textToNumbers.txt", "a")
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
			numberFile.write(str(numbers) + " ")
		numberFile.close()

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

	def timeChanger(self):
		textTime = open("C:/Code/Python/AutoText/textTime.txt", "w").write(input("What time do you want your message to be recived? Format MUST BE: hh:mm:ss "))

	def msgChanger(self):
		messageChanger = open("C:/Code/Python/AutoText/message.txt", "w").write(input("Enter new message: "))

class MsgTimer:
	def sendMessage(self): # send a message to each number on file
		numberFile = open("C:/Code/Python/AutoText/textToNumbers.txt", "r").read()
		message = open("C:/Code/Python/AutoText/message.txt").read()
		lstNums = [""]
		j = 0

		for i in range(len(numberFile)): # adds numbers to list
			try:
				if numberFile[i] != " ":
					lstNums[j] += numberFile[i]
				else:
					j += 1
			except:
				break

		for i in lstNums:
			i = i.strip(" ")
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

		if os.path.exists("C:/Code/Python/AutoText/textToNumbers.txt"):
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

			sendTime = open("C:/Code/Python/AutoText/textTime.txt", "r").read()
		else: # first time users setup
			numberFile = open("C:/Code/Python/AutoText/textToNumbers.txt", "w")
			numberFile.close()

			setUp.howManyNumbers()
			setUp.msgChanger()
			setUp.timeChanger()

		print("Starting auto texting application")
		msgTimer = open("C:/Code/Python/AutoText/textTime.txt", "r").read()
		sendMsg = MsgTimer()
		sendMsg.timer(msgTimer)

main = Main()
main.main()
