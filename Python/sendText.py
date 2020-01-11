import os
import datetime
from twilio.rest import Client

''' 
* Author https://github.com/key6oardWarrior
* Code Propety of Full Blast S.T.E.A.M
* Twilio API used https://twilio.com
'''

authFile = open("C:/Users/Lewjb/Documents/Code/FullBlast/FBSTC/Text_TC/AUTH.txt", "r").read()
sid = authFile[:34]
authToken = authFile[36:]
client = Client(sid, authToken)

def howManyNumbers(): # ask user how many numbers do they want to add
	num = 0

	try:
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
	numberFile = open("C:/Users/Lewjb/Documents/Code/FullBlast/FBSTC/Text_TC/textToNumbers.txt", "a")
	numbers = 0

	try:
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
	numberFile = open("C:/Users/Lewjb/Documents/Code/FullBlast/FBSTC/Text_TC/textToNumbers.txt", "r").read()
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

	for i in lstNums:
		message = client.messages.create(
			body = 'URGENT: Please Check the schedule to know if you are working today!',
			from_ = '+12512205235', 
			to = i
		)
		print(message.sid + ": Sent the message!")

dateTime = datetime.datetime.now()

def caller():
	i = 0
	if dateTime.strftime("%X") + dateTime.strftime("%p") == "5:00:00AM": # if fix is found: != not ==
		# caller() cause error so don't run until fix is found
	# else:
		sendMessage()

def main(): # determin if send text or add numbers to file
	if os.path.exists("C:/Users/Lewjb/Documents/Code/FullBlast/FBSTC/Text_TC/textToNumbers.txt"):
		isAddNums = input("Do you want to add numbers to the list of numbers? Y/n ")
		if isAddNums.upper() == "Y":
			howManyNumbers()
			isSendMessage = input("Do you want to text all numbers? Y/n ")
			if isSendMessage.upper() == "Y":
				caller()
			else:
				print("Message not sent :(")
		else:
			caller()
			
	else:
		numberFile = open("C:/Users/Lewjb/Documents/Code/FullBlast/FBSTC/Text_TC/textToNumbers.txt", "w")
		numberFile.close()
		howManyNumbers()
		main()

if __name__ == "__main__":
	main()
