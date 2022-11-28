account = {}
config = {
    'loan': 1,
    'account': {
        'withdrawal': 1,
        'mini': 1,
    },
}

def set_account(data):
    global account
    account = data

def get_account():
    return account
