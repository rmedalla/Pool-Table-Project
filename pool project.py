import time

class PoolTable:
    def __init__(self, table_number):
        self.start_time = ""
        self.end_time = ""
        self.table_number = table_number
        self.status = "OPEN"
        self.cost = 10
        

    def __repr__(self):
        return (f"\n Table: {self.table_number} status: {self.status} start time: {self.start_time} end time: {self.end_time}")

class Pool_Manager:
    def __init__(self):
        self.tables_list = []
        self.add_tables()
        self.options()

    def options(self):
        print("*" * 76)
        user = int(input(" 1 - Show Pool Tables | 2 - Checkout | 3 - Close | 4 - Reopen | 5 - Exit: "))
        
        if user == 1:    
            print(self.tables_list)
            self.options()
                
        if user == 2:
            selected_table_number = int(input("Select table number to CHECKOUT: "))-1
            the_table = self.tables_list[selected_table_number]
            self.change_status(the_table)

        if user == 3:
            selected_table_number = int(input("Select table number to CLOSE: "))-1
            the_table = self.tables_list[selected_table_number]
            self.close(the_table)

        if user == 4:
            selected_table_number = int(input("Select table number to REOPEN: "))-1
            the_table = self.tables_list[selected_table_number]
            self.reopen(the_table)
          
        if user == 5:
            quit_table = input("Are you sure you want to EXIT? y or n: ")
        
            if quit_table == "n":
                self.options()

            else:
                self.exit()

    def add_tables(self):
        for index in range(1, 13):
            table = PoolTable(index)
            self.tables_list.append(table)
        print(self.tables_list)

    def change_status(self, table):
        if table.status == "OPEN":
            table.status = "IN USE"
            table.start_time = time.strftime("%d/%m/%y | %H:%M:%S")

        elif table.status == "IN USE":
            print("Table is already reserved")

        else:
            table.status = "OPEN"
            
        self.options()

    def close(self, table):

        if table.status == "IN USE":
            table.status = "CLOSED"
            table.end_time = time.strftime("%d/%m/%y | %H:%M:%S")

        self.options()

    def reopen(self, table):
        if table.status == "CLOSED":
            table.status = "OPEN"
            table.start_time = ""
            table.end_time = ""

        self.options()

    def exit(self):

        return

    

    


pools_list = Pool_Manager()










