class Team:
    import datetime
    date = datetime.datetime.now()
    id = 1
    
    #constructor
    def __init__(self,name = str, type = str, fee = int, fee_paid = bool) -> None:
        self.__date = Team.date
        self.__id = Team.id
        Team.id += 1
        self.__name = name
        self.__type = type
        self.__fee_paid = fee_paid
        self.__fee = fee
        self.__cancel_date = None 
    # setters
    def set_name(self, name):
        self.__name = name
    def set_type(self, type):
        self.__type = type
    def set_fee_paid(self, fee_paid):
        self.__fee_paid = fee_paid
    def set_fee(self, fee):
        self.__fee = fee
    def set_cancel_date(self, cancel_date):
        self.__cancel_date = cancel_date 

    # getters          
    def get_name(self):
        return self.__name
    def get_type(self):
        return self.__type
    def get_fee_paid(self):
        return self.__fee_paid
    def get_fee(self):
        return self.__fee
    def get_id(self):
        return self.__id
    def get_date(self):
        return self.__date
    def get_cancel_date(self):
        return self.__cancel_date
    
    def __str__(self) -> str:
        if self.__cancel_date == None:
            return (f"This team with id {self.__id} is called {self.__name}.\n"
                f"It belongs to the type {self.__type}.\n"
                f"It was created on {self.__date}.\n"
                f"fees = {self.__fee} ; fee paid = {self.__fee_paid}.\n")
        else:
            return (f"This team with id {self.__id} is called {self.__name}.\n"
                f"It belongs to the type {self.__type}.\n"
                f"It was created on {self.__date}.\n"
                f"fees = {self.__fee} ; fee paid = {self.__fee_paid}.\n"
                f"The cancellation date is {self.__cancel_date}")



