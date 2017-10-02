import datetime
import praw
import pickle

Players = { 
	#"Player 1": "Full Name"
	"Bozak": "Tyler Bozak",
	"Brown": "Connor Brown",
	"Fehr": "Eric Fehr",
	"Greening": "Colin Greening",
	"Hyman": "Zach Hyman",
	"Kadri": "Nazem Kadri",
	"Komarov": "Leo Komarov",
	"Leivo": "Josh Leivo",
	"Lupul": "Joffrey Lupul",
	"Marleau": "Patrick Marleau",
	"Marner": "Mitchell Marner",
	"Martin": "Matt Martin",
	"Matthews": "Auston Matthews",
	"Moore": "Dominic Moore",
	"Mueller": "Chris Mueller",
	"Nylander": "William Nylander",
	"Smith": "Ben Smith",
	"Soshnikov": "Nikita Soshnikov",
	"van Riemsdyk": "James van Riemsdyk",
	"Borgman": "Andreas Borgman",
	"Carrick": "Connor Carrick",
	"Gardiner": "Jake Gardiner",
	"Hainsey": "Ron Hainsey",
	"Holl": "Justin Holl",
	"Liljegren": "Timothy Liljegren",
	"LoVerde": "Vincent LoVerde",
	"Marincin": "Martin Marincin",
	"Rielly": "Morgan Rielly",
	"Rosen": "Calle Rosen",
	"Zaitsev": "Nikita Zaitsev",
	"Andersen": "Frederik Andersen",
	"McElhinney": "Curtis McElhinney",
	"Sparks": "Garret Sparks"
}

file = open('Players.pkl', 'wb')
pickle.dump(Players, file, -1)
file.close()
	
