"""
usernames = ["Ted","Chad","Jesus", "Adam"]
# sign in user
user = input("What is your username?")
if user in usernames:
	print("Hello, " + user)
else:
	usernames.append(user)
	print("Hello, " + user)

chosen = False
while not chosen:
	print("\nWhat would you like to do? \nSubmit (s), Review (r), Collect (c)")
	option = input().lower()
	if option == "s":
		chosen = True
	elif option == "r":
		print(NotImplemented)
		chosen = True
	elif option == "c":
		print(NotImplemented)
		chosen = True
	else:
		print("Stahp! You haven't selected an option!")
"""
subquestions = {"psychology": {0: "how much is too much",
							   1: "how much is a qbosir?"}}
subject = input("Which subject?\n").lower()
if subject not in subquestions:
	subquestions[subject] = {} 

print(subject.title() + " selected.")

qnams = subquestions[subject]

print(qnams)



def checkinput(): # check whether input is a number and whether it is in the list of options
	while True:
		try:
			qnam = int(input("Which question?\n"))
			if True:
				if qnam not in qnams:
					print("This question is not in the list.")
				else:
					print(qnams[int(qnam)]) 
					break
		except:
			print("This is not a number.")
			continue

checkinput()
