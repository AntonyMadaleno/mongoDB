from pymongo import MongoClient
from datetime import datetime

#connect to database
client = MongoClient()
db = client.seances

results = {}
year = 2023

for t in range(1, 13):

	# Define start and end dates
	start_date = datetime.timestamp(datetime(year, t, 1))
	print(start_date)
	if t < 12:
		end_date = datetime.timestamp(datetime(year, t + 1, 1))
	else:
		end_date = datetime.timestamp(datetime(year + 1, 1, 1))

	# Create aggregation pipeline
	pipeline = [
	    {
	        "$match": {
	            "Begin": {
	                "$gte": start_date,
	                "$lt": end_date
	            }
	        }
	    },
	    {
	        "$group": {
	            "_id": "$Salle.Cinema.Nom",
	            "total_entree": {
	                "$sum": "$Entree"
	            }
	        }
	    }
	]

	# Execute aggregation pipeline and print results
	results[datetime(year, t, 1).strftime("%m/%Y")] = db.seances.aggregate(pipeline)

for key in results:
	print(f"\n{key} :\n")
	for doc in results[key]:
		print(doc)
