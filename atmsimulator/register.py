from pysondb import db

# name, initial bank balance, type of account, address, DOB
# acc no will be randomly generated

db_obj = db.getDb("../backend/customers.json")

status = db_obj.add({
    "name": "chuck norris",
    "balance": 1000,
    "type": "savings",
    "address":"USA",
    "dob": "10-03-1940",
    "pin": 5050,
    "transactions": ""
})
print(status)