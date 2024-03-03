import hashlib

class User:
    users = {}
    
    def __init__(self, account, password, role):
        self.account = account
        self.password = password
        self.role = role
        
        User.users[account] = self
    
    @staticmethod
    def add_user(account, password, role):
        if account not in User.users:
            password_encode = hashlib.sha256(password.encode()).hexdigest()
            User(account, password_encode, role)
        else:
            print(f"Account with {account} has exists.")
    
    @staticmethod
    def delete_user(account, password):
        if account in User.users:
            user = User.users[account]
            if hashlib.sha256(password.encode()).hexdigest() == user.password:
                del User.users[account]
                print(f"User with account {account} deleted successfully.")
            else:
                print("Incorrect password")
        else:
            print(f"User with account {account} does not exist.")
    
    @staticmethod
    def login(account, password):
        if account in User.users:
            user = User.users[account]
            password_encode = hashlib.sha256(password.encode()).hexdigest()
            if password_encode == user.password:
                return user
            else:
                return None
        else:
            return None
    
if __name__ == '__main__':
    pass

