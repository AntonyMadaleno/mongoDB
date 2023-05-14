## THIS FILE IS MADE TO INITIALISE A DATABASE CONTAINING INFORMATIONS ABOUT CINEMAS ROOMS ##

from pymongo import MongoClient

#connect to database
client = MongoClient()
db = client.seances

salles = [

    {
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
    },

    {
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
    },

    {
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
    },

    {
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
        },

]

for salle in salles:

    db.salles.insert_one(
        salle
    )