import requests 
# pip install requests - this installs autopep8, pycodestyle and toml
import json
# install not required - json is inbuilt in python

def get_users():
    return requests.get('http://localhost:3000/users').json()


# to retrieve the index of the user(given his username) from json object(users)
def get_user(users, username):
    for index in range(len(users)):
        if users[index]['username'] == username:
            return index    


def deposit():
    users = get_users()
    # print(users[0]['id']) -- prints '1'

    account_type = int(input('0. Savings Account\n1. Current Account\n Enter your choice: '))
    deposit_amount = int(input('Enter amount(in Rs.) to be deposited: '))
    
    
    # update customer json object 
    # retrieve username from initial login api request -todo
    username='Achyuta'
    index = get_user(users,username)
    users[index]['accounts'][account_type]['balance']+=deposit_amount


    # patch request - update balance
    header={'Content-Type':'application/json'}
    try:
        response = requests.patch('http://localhost:3000/users/'+str(index+1),data=json.dumps(users[index]), headers=header)
    except:
        print("Your transaction could not follow through. We're looking into it! Please try again later.")

    print('Transaction successful. Current balance: ',  users[index]['accounts'][account_type]['balance'])

deposit()
