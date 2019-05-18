# Find on condition
db.log.findOne({"cy" : "San Francisco"})
# find the count of condition
db.log.find({"cy" : "San Francisco"}).count()

# find distinct values for a specific key
db.log.distinct("a")
# count the number of distinct values for a specific key
db.log.distinct("a").length

# find the type of a key
typeof db.log.findOne({'t': {$exists: true}}).t

# Change datetime to an ISOdate
db.log.find({'t': {$exists: true}}).forEach(function(entry) {
    db.log.update({"_id": entry._id} , {$set: {'t' : new Date(entry.t *1000)}})
})
