from bson.code import Code
from pymongo import MongoClient

#connect to database
client = MongoClient()
db = client.seances

map_function = """
function() {
    emit(this.Film.Titre, this.Entree);
}
"""

reduce_function = """
function(key, values) {
    var sum = 0;
    for (var i = 0; i < values.length; i++) {
        sum += values[i];
    }
    return sum / values.length;
}
"""

result = db.seances.map_reduce(map_function, reduce_function, "average_entree_by_film", query={}, out={"replace": "results"})

for doc in result.find():
    print(doc)
