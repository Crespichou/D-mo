class Sleevy :
    def __init__(self, n_serie) :
        self.n_serie = n_serie

class Interface(Sleevy) :
    def __init__(self, username, password) :
        self.username = username
        self.password = password

    def log_in(self) : 
        print(f"To connect, please enter your {self.username} and your {self.password}")