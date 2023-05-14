## THIS FILE IS MADE TO INITIALISE A COLLECTION CONTAINING INFORMATIONS ABOUT SEANCES ##

from pymongo import MongoClient

#connect to database
client = MongoClient()
db = client.seances

seances = [
	{
		"Entree" : 123,
		"Begin" : 1683839929.791858,
		"End" : 1683844915.3496928,
		"Film" : {
			"Titre" : "Titanic",
			"Genre" : ["Romantique", "Drama"],
			"Realisateur" : "James Cameron",
			"Acteurs" : ["Leonardo DiCaprio","Kate Winslet","Victor Garber"],
			"Duree" : 194
		},
		"Salle" : {
			"Id_salle" : 2,
			"Capacite" : 150,
			"Cinema" : {
				"Nom" : "Olympia",
				"Addresse" : "64 Rue somewhere City",
				"Gerant" : {
					"Nom" : "Daniels",
					"Prenom" : "Jack",
					"Pseudo" : "Single_Malt"
				}
			}
		}
	},

	{
	    "Entree": 150,
	    "Begin": 1683839929.791858,
	    "End": 1683844915.3496928,
	    "Film": {
	        "Titre": "The Shawshank Redemption",
	        "Genre": ["Drama", "Crime"],
	        "Realisateur": "Frank Darabont",
	        "Acteurs": ["Tim Robbins", "Morgan Freeman"],
	        "Duree": 142
	    },
	    "Salle": {
	        "Id_salle": 3,
	        "Capacite": 200,
	        "Cinema": {
	            "Nom": "Rex",
	            "Addresse": "26 Rue du Theatre, City",
	            "Gerant": {
	                "Nom": "Garcia",
	                "Prenom": "Juan",
	                "Pseudo": "juangarcia"
	            }
	        }
	    }
	},

	{
	    "Entree": 95,
	    "Begin": 1683849315.3496928,
	    "End": 1683854315.3496928,
	    "Film": {
	        "Titre": "The Godfather",
	        "Genre": ["Crime", "Drama"],
	        "Realisateur": "Francis Ford Coppola",
	        "Acteurs": ["Marlon Brando", "Al Pacino", "James Caan"],
	        "Duree": 175
	    },
	    "Salle": {
	        "Capacite": 200,
	        "Cinema": {
	            "Nom": "Palace",
	            "Addresse": "32 Avenue somewhere City",
	            "Gerant": {
	                "Nom": "Smith",
	                "Prenom": "Robert",
	                "Pseudo": "rsmith"
	            }
	        }
	    }
	},

	{
		"Entree" : 84,
		"Begin" : 1684039929.791858,
		"End" : 1684044915.3496928,
		"Film" : {
			"Titre" : "Titanic",
			"Genre" : ["Romantique", "Drama"],
			"Realisateur" : "James Cameron",
			"Acteurs" : ["Leonardo DiCaprio","Kate Winslet","Victor Garber"],
			"Duree" : 194
		},
		"Salle" : {
			"Id_salle" : 1,
			"Capacite" : 100,
			"Cinema" : {
				"Nom" : "Olympia",
				"Addresse" : "64 Rue somewhere City",
				"Gerant" : {
					"Nom" : "Daniels",
					"Prenom" : "Jack",
					"Pseudo" : "Single_Malt"
				}
			}
		}
	},

]

for seance in seances:

	db.seances.insert_one(
		seance
	)