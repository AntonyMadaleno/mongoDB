from pymongo import MongoClient
from datetime import datetime

#connect to database
client = MongoClient()
db = client.seances

result = []

#les seances ayant eu lieu dans le cinema Rex
result.append( db.seances.find( {"Salle.Cinema.Nom": "Rex"} ) )
#les seances ayant montré un filme de genre "Crime"
result.append( db.seances.find( {"Film.Genre": "Crime"} ) )
#les seances ayant comptabilisées entre 90 et 130 entrées
result.append( db.seances.find( { "Entree": { "$gte": 90, "$lte": 130 } } ) )
#les cinemas et leurs nombre total d'entrees
pipeline = [
    {
        '$group': {
            '_id': '$Salle.Cinema.Nom',
            'total_entree': {'$sum': '$Entree'}
        }
    }
]
result.append( db.seances.aggregate(pipeline) )

start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 1, 1)

pipeline_2 = [
    {
        "$match": {
            "Date": {
                "$gte": start_date,
                "$lte": end_date
            }
        }
    },
    {
        "$group": {
            "_id": "$Salle.Cinema.Nom",
            "total_entree": {"$sum": "$Entree"},
            "total_seances": {"$sum": 1}
        }
    },
    {
        "$project": {
            "_id": 0,
            "cinema": "$_id",
            "avg_entree": {"$divide": ["$total_entree", "$total_seances"]}
        }
    }
]

result.append(db.seances.aggregate(pipeline_2))


print("\n Seances displayed in Rex Theater :\n")
for seance in result[0]:
	print(seance)

print("\n Seances wich displayed Crime movies :\n")
for seance in result[1]:
	print(seance)

print("\n Seances wich have in between 90 and 130 entry counted :\n")
for seance in result[2]:
	print(seance)

print("\n Cinema and their total number of entry :\n")
for res in result[3]:
	print(res)

print("\n Cinema and their average number of entry from 2023 to 2024:\n")
for res in result[4]:
    print(res)