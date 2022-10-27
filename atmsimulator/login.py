from pysondb import db

# take acc-id and pin as input 
# search for user with given acc-id 
# check if pin matches

db_obj = db.getDb("../backend/customers.json")

user = db_obj.reSearch("id", r"451808503720545755")
print(user[0]["pin"])
