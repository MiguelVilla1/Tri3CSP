user_balance = 200


def update_user_balance(amount):
    global user_balance
    user_balance += amount

def get_user_balance():
    return user_balance