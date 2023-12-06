############################################### Author: MardOrange ###############################################
######################### Noten : This script is a work in progress and is not finished yet.######################

from tkinter import *
import csv

win = Tk()
win.iconbitmap("The Akatsuki Logo.ico")
win.configure(bg="#1A1B26")
win.title("Who you wanna kill first? (Akatsuki members only)!")
win.geometry("960x500")


# Functions
def submit():
	global Naruto, Sasuke, Kakashi, Jiraya, Tsunade, MightGuy, rav

	# Extract values from StringVar instances
	member_name = rav.get()
	data = [member_name, Naruto.get(), Sasuke.get(), Kakashi.get(), Jiraya.get(), Tsunade.get(), MightGuy.get()]

	try:
		with open("Killdata.csv", 'r') as csv_file:
			csv_reader = csv.reader(csv_file)
			rows = list(csv_reader)

		header_exists = 'Naruto' in rows[0] if rows else False

		with open("Killdata.csv", 'w', newline='') as csv_file:
			csv_writer = csv.writer(csv_file)

			# If the header row doesn't exist, add it
			if not header_exists:
				csv_writer.writerow(['Member', 'Naruto', 'Sasuke', 'Kakashi', 'Jiraya', 'Tsunade', 'MightGuy'])

			member_exists = False
			for i, row in enumerate(rows[1:], 1):  # Skip the header row
				if row and row[0] == member_name:  # Check if row has at least one element
					rows[i] = data
					member_exists = True
					break

			# If the member doesn't exist, add a new row
			if not member_exists:
				rows.append(data)

			# Write all rows to the CSV file
			csv_writer.writerows(rows)

	except FileNotFoundError:
		with open("Killdata.csv", 'w', newline='') as csv_file:
			csv_writer = csv.writer(csv_file)
			csv_writer.writerow(['Member', 'Naruto', 'Sasuke', 'Kakashi', 'Jiraya', 'Tsunade', 'MightGuy'])
			csv_writer.writerow(data)

	print(f'Data added to the CSV file "Killdata.csv" successfully.')


def ClearData():
	with open("Killdata.csv", 'w', newline='') as csv_file:
		csv_file.truncate()


def who():
	global rav


# Creating a variable to store the values of the radio buttons for members
rav = StringVar()
membwho = rav
# Creating a variable to store the values of the radio buttons for Enemies ratings
Naruto = IntVar()
Sasuke = IntVar()
Kakashi = IntVar()
Jiraya = IntVar()
Tsunade = IntVar()
MightGuy = IntVar()

# Creating and putting radio buttons and it's labels for the members
Radiobuttonp1 = Radiobutton(text="", font=("Arial", 13), bg="#1A1B26", fg="black", variable=rav, value="Tobi")
Radiobuttonp2 = Radiobutton(text="", font=("Arial", 13), bg="#1A1B26", fg="black", variable=rav, value="Deidara")
Radiobuttonp3 = Radiobutton(text="", font=("Arial", 13), bg="#1A1B26", fg="black", variable=rav, value="Kakazu")
Radiobuttonp4 = Radiobutton(text="", font=("Arial", 13), bg="#1A1B26", fg="black", variable=rav, value="Orochimaru")
Radiobuttonp5 = Radiobutton(text="", font=("Arial", 13), bg="#1A1B26", fg="black", variable=rav, value="Itachi")
Radiobuttonp6 = Radiobutton(text="", font=("Arial", 13), bg="#1A1B26", fg="black", variable=rav, value="Kisame")

Radiobuttonplabel1 = Label(text="       Tobi", font=("Arial", 13), bg="#1A1B26", fg="#917BD7")
Radiobuttonplabel2 = Label(text="Deidara", font=("Arial", 13), bg="#1A1B26", fg="#FFCB6B")
Radiobuttonplabel3 = Label(text="Kakazu", font=("Arial", 13), bg="#1A1B26", fg="white")
Radiobuttonplabel4 = Label(text="Orochimaru", font=("Arial", 13), bg="#1A1B26", fg="#71C764")
Radiobuttonplabel5 = Label(text="Itachi", font=("Arial", 13), bg="#1A1B26", fg="#FF5370")
Radiobuttonplabel6 = Label(text="Kisame", font=("Arial", 13), bg="#1A1B26", fg="#67A9FF")

Radiobuttonplabel1.grid(row=1, column=0)
Radiobuttonplabel2.grid(row=1, column=2)
Radiobuttonplabel3.grid(row=1, column=4)
Radiobuttonplabel4.grid(row=1, column=6)
Radiobuttonplabel5.grid(row=1, column=8)
Radiobuttonplabel6.grid(row=1, column=10)

Radiobuttonp1.grid(row=1, column=1)
Radiobuttonp2.grid(row=1, column=3)
Radiobuttonp3.grid(row=1, column=5)
Radiobuttonp4.grid(row=1, column=7)
Radiobuttonp5.grid(row=1, column=9)
Radiobuttonp6.grid(row=1, column=11)

memblabel = Label(text="Members", font=("Arial", 15), bg="#1A1B26", fg="white")
memblabel.grid(row=0, column=0, columnspan=12)

# Labels of the enemies
enemieslabel1 = Label(text="Naruto    ", font=("Arial", 12), fg="#fe7f2d", bg="#1A1B26")
enemieslabel2 = Label(text="Sasuke   ", font=("Arial", 12), fg="#4895ef", bg="#1A1B26")
enemieslabel3 = Label(text="Kakashi  ", font=("Arial", 12), fg="#fcca46", bg="#1A1B26")
enemieslabel4 = Label(text="Jiraya      ", font=("Arial", 12), fg="#a1c181", bg="#1A1B26")
enemieslabel5 = Label(text="Tsunade  ", font=("Arial", 12), fg="#619b8a", bg="#1A1B26")
enemieslabel6 = Label(text="MightGuy", font=("Arial", 12), fg="#598392", bg="#1A1B26")

enemieslabel1.grid(row=5, column=0, columnspan=1)
enemieslabel2.grid(row=6, column=0)
enemieslabel3.grid(row=7, column=0)
enemieslabel4.grid(row=8, column=0)
enemieslabel5.grid(row=9, column=0)
enemieslabel6.grid(row=10, column=0)

# Creating invsible Labels for the enemies labels to stay on correct row
invislabel1 = Label(text="", font=("Arial", 15), bg="#1A1B26", fg="white")
invislabel1.grid(row=2, column=0, )


def killrating():
	global Naruto
	global Sasuke
	global Kakashi
	global Jiraya
	global Tsunade
	global MightGuy
	global rav

	data = [rav, Naruto, Sasuke, Kakashi, Jiraya, Tsunade, MightGuy]


# Creating rating Lables
enemieslabel1 = Label(
	text="Enemies                                                                                  ",
	font=("Arial", 15), bg="#1A1B26", fg="white")
enemieslabel1.grid(row=3, column=0, columnspan=11)
enemieslabel1 = Label(text="Ratings", font=("Arial", 15), bg="#1A1B26", fg="white")
enemieslabel1.grid(row=3, column=1, columnspan=6)
enemieslabel1 = Label(text="                                     1     2     3     4     5", font=("Arial", 10),
					  bg="#1A1B26", fg="white")
enemieslabel1.grid(row=4, column=0, columnspan=6)

# Creating radiobuttons for ratings each enemy
# Naruto
NarutoRating1 = Radiobutton(win, text="", bg="#1A1B26", variable=Naruto, value=1)
NarutoRating2 = Radiobutton(win, text="", bg="#1A1B26", variable=Naruto, value=2)
NarutoRating3 = Radiobutton(win, text="", bg="#1A1B26", variable=Naruto, value=3)
NarutoRating4 = Radiobutton(win, text="", bg="#1A1B26", variable=Naruto, value=4)
NarutoRating5 = Radiobutton(win, text="", bg="#1A1B26", variable=Naruto, value=5)

NarutoRating1.place(x=176, y=151, anchor=CENTER)
NarutoRating2.place(x=277 - 76, y=151, anchor=CENTER)
NarutoRating3.place(x=376 - 149, y=151, anchor=CENTER)
NarutoRating4.place(x=479 - 223, y=151, anchor=CENTER)
NarutoRating5.place(x=476 - 192, y=151, anchor=CENTER)

# Sasuke
SasukeRating1 = Radiobutton(text="", bg="#1A1B26", variable=Sasuke, value=1)
SasukeRating2 = Radiobutton(text="", bg="#1A1B26", variable=Sasuke, value=2)
SasukeRating3 = Radiobutton(text="", bg="#1A1B26", variable=Sasuke, value=3)
SasukeRating4 = Radiobutton(text="", bg="#1A1B26", variable=Sasuke, value=4)
SasukeRating5 = Radiobutton(text="", bg="#1A1B26", variable=Sasuke, value=5)

SasukeRating1.place(x=176, y=150 + 24, anchor=CENTER)
SasukeRating2.place(x=277 - 76, y=150 + 24, anchor=CENTER)
SasukeRating3.place(x=376 - 149, y=150 + 24, anchor=CENTER)
SasukeRating4.place(x=479 - 223, y=150 + 24, anchor=CENTER)
SasukeRating5.place(x=476 - 192, y=150 + 24, anchor=CENTER)

# Kakashi
KakashiRating1 = Radiobutton(text="", bg="#1A1B26", variable=Kakashi, value=1)
KakashiRating2 = Radiobutton(text="", bg="#1A1B26", variable=Kakashi, value=2)
KakashiRating3 = Radiobutton(text="", bg="#1A1B26", variable=Kakashi, value=3)
KakashiRating4 = Radiobutton(text="", bg="#1A1B26", variable=Kakashi, value=4)
KakashiRating5 = Radiobutton(text="", bg="#1A1B26", variable=Kakashi, value=5)

KakashiRating1.place(x=176, y=150 + 48, anchor=CENTER)
KakashiRating2.place(x=277 - 76, y=150 + 48, anchor=CENTER)
KakashiRating3.place(x=376 - 149, y=150 + 48, anchor=CENTER)
KakashiRating4.place(x=479 - 223, y=150 + 48, anchor=CENTER)
KakashiRating5.place(x=476 - 192, y=150 + 48, anchor=CENTER)

# Jiraya
JirayaRating1 = Radiobutton(text="", bg="#1A1B26", variable=Jiraya, value=1)
JirayaRating2 = Radiobutton(text="", bg="#1A1B26", variable=Jiraya, value=2)
JirayaRating3 = Radiobutton(text="", bg="#1A1B26", variable=Jiraya, value=3)
JirayaRating4 = Radiobutton(text="", bg="#1A1B26", variable=Jiraya, value=4)
JirayaRating5 = Radiobutton(text="", bg="#1A1B26", variable=Jiraya, value=5)

JirayaRating1.place(x=176, y=150 + 72, anchor=CENTER)
JirayaRating2.place(x=277 - 76, y=150 + 72, anchor=CENTER)
JirayaRating3.place(x=376 - 149, y=150 + 72, anchor=CENTER)
JirayaRating4.place(x=479 - 223, y=150 + 72, anchor=CENTER)
JirayaRating5.place(x=476 - 192, y=150 + 72, anchor=CENTER)

# Tsunade
TsunadeRating1 = Radiobutton(text="", bg="#1A1B26", variable=Tsunade, value=1)
TsunadeRating2 = Radiobutton(text="", bg="#1A1B26", variable=Tsunade, value=2)
TsunadeRating3 = Radiobutton(text="", bg="#1A1B26", variable=Tsunade, value=3)
TsunadeRating4 = Radiobutton(text="", bg="#1A1B26", variable=Tsunade, value=4)
TsunadeRating5 = Radiobutton(text="", bg="#1A1B26", variable=Tsunade, value=5)

TsunadeRating1.place(x=176, y=150 + 97, anchor=CENTER)
TsunadeRating2.place(x=277 - 76, y=150 + 97, anchor=CENTER)
TsunadeRating3.place(x=376 - 149, y=150 + 97, anchor=CENTER)
TsunadeRating4.place(x=479 - 223, y=150 + 97, anchor=CENTER)
TsunadeRating5.place(x=476 - 192, y=150 + 97, anchor=CENTER)

# MightGuy
MightGuyRating1 = Radiobutton(text="", bg="#1A1B26", variable=MightGuy, value=1)
MightGuyRating2 = Radiobutton(text="", bg="#1A1B26", variable=MightGuy, value=2)
MightGuyRating3 = Radiobutton(text="", bg="#1A1B26", variable=MightGuy, value=3)
MightGuyRating4 = Radiobutton(text="", bg="#1A1B26", variable=MightGuy, value=4)
MightGuyRating5 = Radiobutton(text="", bg="#1A1B26", variable=MightGuy, value=5)

MightGuyRating1.place(x=176, y=150 + 124, anchor=CENTER)
MightGuyRating2.place(x=277 - 76, y=150 + 124, anchor=CENTER)
MightGuyRating3.place(x=376 - 149, y=150 + 124, anchor=CENTER)
MightGuyRating4.place(x=479 - 223, y=150 + 124, anchor=CENTER)
MightGuyRating5.place(x=476 - 192, y=150 + 124, anchor=CENTER)

# Submitt button
SubmittButton = Label(text="", bg="#1A1B26", fg="white")
SubmittButton.grid(row=11, column=2)

SubmittButton = Button(text="Submit", bg="#161720", fg="white", command=submit)
SubmittButton.grid(row=12, column=2)

# Reports button
SubmittButton = Button(text="Details", bg="#161720", fg="white")
SubmittButton.grid(row=12, column=3)

# Clear Data Button
ClearButton = Label(text="", bg="#1A1B26", fg="white")
ClearButton.grid(row=13, column=4)

ClearButton = Button(text="Clear Data!", bg="#161720", fg="white", command=ClearData)
ClearButton.grid(row=14, column=0)

# Stars
# Naruto
StarNarutoLabel = Label(text="5⭐", bg="#1A1B26", fg="white", font=("Arial", 10))
StarNarutoLabel.place(x=476 - 160, y=150, anchor=CENTER)

# Sasuke
StarNarutoLabel = Label(text="5⭐", bg="#1A1B26", fg="white", font=("Arial", 10))
StarNarutoLabel.place(x=476 - 160, y=150 + 23, anchor=CENTER)

# Kakashi
StarNarutoLabel = Label(text="5⭐", bg="#1A1B26", fg="white", font=("Arial", 10))
StarNarutoLabel.place(x=476 - 160, y=150 + 47, anchor=CENTER)

# Jiraya
StarNarutoLabel = Label(text="5⭐", bg="#1A1B26", fg="white", font=("Arial", 10))
StarNarutoLabel.place(x=476 - 160, y=150 + 71, anchor=CENTER)

# Tsunade
StarNarutoLabel = Label(text="5⭐", bg="#1A1B26", fg="white", font=("Arial", 10))
StarNarutoLabel.place(x=476 - 160, y=150 + 96, anchor=CENTER)

# MightGuy
StarNarutoLabel = Label(text="5⭐", bg="#1A1B26", fg="white", font=("Arial", 10))
StarNarutoLabel.place(x=476 - 160, y=150 + 123, anchor=CENTER)

# Creating DataTables
# Tobi
OrochimaruDataLabel = Label(text="Tobi            ", font=("Arial", 12), bg="#1A1B26", fg="white")
OrochimaruDataLabel.place(x=176 + 300, y=151, anchor=CENTER)

# Deidara
OrochimaruDataLabel = Label(text="Deidara      ", font=("Arial", 12), bg="#1A1B26", fg="white")
OrochimaruDataLabel.place(x=176 + 300, y=150 + 24, anchor=CENTER)

# Kakazu
OrochimaruDataLabel = Label(text="Kakazu       ", font=("Arial", 12), bg="#1A1B26", fg="white")
OrochimaruDataLabel.place(x=176 + 300, y=150 + 48, anchor=CENTER)

# Orochimaru
OrochimaruDataLabel = Label(text="Orachimaru ", font=("Arial", 12), bg="#1A1B26", fg="white")
OrochimaruDataLabel.place(x=176 + 300, y=151 + 72, anchor=CENTER)

# Itachi
OrochimaruDataLabel = Label(text="Itachi           ", font=("Arial", 12), bg="#1A1B26", fg="white")
OrochimaruDataLabel.place(x=176 + 300, y=151 + 97, anchor=CENTER)

# "Kisame
OrochimaruDataLabel = Label(text="Kisame       ", font=("Arial", 12), bg="#1A1B26", fg="white")
OrochimaruDataLabel.place(x=176 + 300, y=151 + 124, anchor=CENTER)

# Creating DataTables2

# Naruto
NarutoDataLabel = Label(text="Naruto", font=("Arial", 12), fg="#fe7f2d", bg="#1A1B26")
NarutoDataLabel.place(x=176 + 300 + 100, y=130, anchor=CENTER)

# Sasuke
SasukeDataLabel = Label(text="Sasuke", font=("Arial", 12), fg="#4895ef", bg="#1A1B26")
SasukeDataLabel.place(x=176 + 300 + 200 - 35, y=130, anchor=CENTER)

# Kakashi
KakashiDataLabel = Label(text="Kakashi", font=("Arial", 12), fg="#fcca46", bg="#1A1B26")
KakashiDataLabel.place(x=176 + 300 + 300 - 63, y=130, anchor=CENTER)

# Tsunade
TsunadeDataLabel = Label(text="Tsunade ", font=("Arial", 12), fg="#619b8a", bg="#1A1B26")
TsunadeDataLabel.place(x=176 + 300 + 400 - 90, y=130, anchor=CENTER)

# Jiraya
JirayaDataLabel = Label(text="Jiraya", font=("Arial", 12), fg="#a1c181", bg="#1A1B26")
JirayaDataLabel.place(x=176 + 300 + 500 - 130, y=130, anchor=CENTER)

# MightGuy
MightGuyDataLabel = Label(text="MightGuy", font=("Arial", 12), fg="#598392", bg="#1A1B26")
MightGuyDataLabel.place(x=176 + 300 + 600 - 167, y=130, anchor=CENTER)

win.mainloop()
