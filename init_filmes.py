## THIS FILE IS MADE TO INITIALISE A DATABASE CONTAINING INFORMATIONS ABOUT MOVIES ##

from pymongo import MongoClient

#connect to database
client = MongoClient()
db = client.seances

filmes = [
	{
		"Titre" : "Titanic",
		"Genre" : ["Romantique", "Drama"],
		"Realisateur" : "James Cameron",
		"Acteurs" : ["Leonardo DiCaprio","Kate Winslet","Victor Garber"],
		"Duree" : 194,
		"Comments" : [{
			"Timestamp" : 1684044915.3496928,
			"Content" : "A great drama classic !",
			"Rate" : 4,
			"User" : {
				"Nom" : "Doe",
				"Prenom" : "John",
				"Pseudo" : "qwerty"
			}
		}]
	},

	{
	    "Titre": "The Shawshank Redemption",
	    "Genre": ["Drama", "Crime"],
	    "Realisateur": "Frank Darabont",
	    "Acteurs": ["Tim Robbins", "Morgan Freeman"],
	    "Duree": 142,
	    "Comments": [{
	        "Timestamp": 1684044915.3496928,
	        "Content": "This movie is a masterpiece!",
	        "Rate": 5,
	        "User": {
	            "Nom": "Smith",
	            "Prenom": "Emily",
	            "Pseudo": "emilysmith"
	        }
	    }]
	},

	{
	    "Titre": "The Godfather",
	    "Genre": ["Crime", "Drama"],
	    "Realisateur": "Francis Ford Coppola",
	    "Acteurs": ["Marlon Brando", "Al Pacino", "James Caan"],
	    "Duree": 175,
	    "Comments": [{
	        "Timestamp": 1684054315.3496928,
	        "Content": "A masterpiece of cinema!",
	        "Rate": 5,
	        "User": {
	            "Nom": "Doe",
	            "Prenom": "Jane",
	            "Pseudo": "janedoe"
	        }
	    }]
	},
]

for film in filmes:

	db.filmes.insert_one(
		film
	)