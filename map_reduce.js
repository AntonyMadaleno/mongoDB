//mapReduce deprecated after version 5.0 of mongoDB

var mapFunction = function() {
    emit(this.Filme.Titre, { totalEntree: this.Entree, count: 1 });
};

var reduceFunction = function(key, values) {
    var reducedObject = { totalEntree: 0, count: 0 };

    for (var i = 0; i < values.length; i++) {
        reducedObject.totalEntree += values[i].totalEntree;
        reducedObject.count += values[i].count;
    }

    return reducedObject;
};

var finalizeFunction = function(key, reducedValue) {
    reducedValue.avgEntree = reducedValue.totalEntree / reducedValue.count;
    return reducedValue;
};

db.seances.mapReduce(
    mapFunction,
    reduceFunction,
    {
        out: "film_entree_average",
        finalize: finalizeFunction
    }
);