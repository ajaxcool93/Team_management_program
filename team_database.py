# importing Class Team
import class_team

# creating Class = User_interface to store object of Class Team
class User_interface:
    # constructor
    def __init__(self):
        self.__teams = []

    # function to create team
    def create(self, team):
        self.__teams.append(team)

    # function to delete team
    def delete(self, team_id):
        for team in self.__teams:
            if team.get_id() == team_id:
                self.__teams.remove(team) # remove one team based on unique id
                break

    # function to read or provide info on a team
    def read(self, team_id):
        for team in self.__teams:
            if team.get_id() == team_id:
                return team
        return None
    
    # function to list teams based on type of team
    def list_teams(self, type):
        t_list = []
        for team in self.__teams:
            if team.get_type() == type:
                t_list.append(team)
        return t_list
    
    # function to list all the teams availiable
    def list_all(self):
        t_list = []
        for team in self.__teams:
            t_list.append(team)
        return t_list
    
    # function to list down total no of teams and also calculate % of teams who paid
    def total(self):
        t_list = []
        percent = ()
        print(f"The no of teams currently is: {self.__teams}\n")
        for team in self.__teams:
            if team.get_fee_paid() == True:
                t_list.append(team)
        percent = (len(t_list)/len(self.__teams))*100        
        print(f"The percentage of teams who have paid fees is {percent}%\n")

    # function to download all the teams data into a text file    
    def download_txt_file(self):
        #opening the file
        file = open('teams.txt','w')
        #for loop to write each attribute if each team in a new line as a string
        for teams in self.__teams:
            file.write(f"{teams.get_id()} \n")
            file.write(f"{teams.get_date()} \n")
            file.write(f"{teams.get_name()} \n")
            file.write(f"{teams.get_type()} \n")
            file.write(f"{teams.get_fee()} \n")
            file.write(f"{teams.get_fee_paid()} \n")
            file.write(f"{teams.get_cancel_date()} \n")
        #closing the file
        file.close()
        print("All teams information has been downloaded to a text file")

    # function to restore all the teams data into teams_list - the object of Class User_interface
    #Here it is not possible to restore back (date and Id) as both are immutable attribute in Class: Team

    def restore_data_txt(self):
        infile = open('teams.txt', 'r')
        id = infile.readline()
        #if a value is read the while loop continues until no value is there
        while id != '':
            # reading all values of the team object
            id = int(id)
            date = infile.readline()
            name = infile.readline()
            type = infile.readline()
            fee = infile.readline()
            fee_paid = infile.readline()
            cancel_date = infile.readline()
            name = name.rstrip('\n')
            type = type.rstrip('\n')
            fee = int(fee.rstrip('\n'))
            fee_paid = bool(fee_paid.rstrip('\n'))
            cancel_date = cancel_date.rstrip('\n')

            #Creating Team
            #Again date and Id cannot be restored as being imutable originally
            team = class_team.Team(name, type, fee, fee_paid)
            # Setting cancellation date
            team.set_cancel_date(cancel_date)

            # Appending team to the teams_list
            self.__teams.append(team)

            # reading the first value of the next record
            id = infile.readline()

    # function to update team info(change or add):
    def update(self, team_found):
        attr = (str(input("Which attribute do you want to change or add?\n"
                          "Enter the letter corresponding to your choice, from the following options:\n"
                          "a = name\n"
                          "b = type\n"
                          "c = fee paid status\n"
                          "d = Add cancellation date for a team\n"
                          ))).lower()
        if attr == "b":
            team_found.set_type(str(input("What is the team type: girl or boy?\n")))
        elif attr == "a":
            team_found.set_name(str(input("What is the name of your team\n")))
        elif attr == "c":
            team_found.set_fee_paid(bool(input("Did the team pay fees? True/False\n")))
        elif attr == "d":
            print("Please enter the day , month and year when a particular team was cancelled.")
            day = int(input("Enter the day.\n"))
            month = int(input("Enter the month.\n"))
            year = int(input("Enter the year.\n"))
            team_found.set_cancel_date(class_team.Team.datetime.datetime(year, day, month).strftime("%Y-%m-%d"))

    # defining str function for class User_interface
    def __str__(self):
        return f"No of teams in database: {len(self.__teams)}\n"
    





def main():
    # Assigning an object of Class User_interface to store the objects of Class Team
    teams_list = User_interface()

    # Menu system defined to be used for an interactive method of accessing the system
    def display_menu():
        print("MENU")
        print("1: Add a new team.")
        print("2: Select a team to get info on them.")
        print("3: Select a team by type (boy/girl).")
        print("4: List all the teams.")
        print("5: Update information of a team or add cancellation date.")
        print("6: Delete a team.")
        print("7: View no of teams and fee paying teams percentage.")
        print("8: Download team list in a text file.")
        print("9: Retrieve teams data from text file.")
        print("10: Exit from menu.")

    # define menu options:
    add_new_team = 1
    select_team_for_info = 2
    select_team_by_type = 3
    list_all_teams = 4
    update_info_of_team = 5
    delete_a_team = 6
    total_and_percent = 7
    download_txt = 8
    read_txt_file = 9
    exit = 10

    #initializig a variable choice with value 0 which will be used for while loop to run the menu
    choice = 0
    while choice != exit:
        display_menu()

        choice = int(input("Enter the number corresponding to your choice.\n"))
        if choice == add_new_team:
            team = class_team.Team("","",False,0)
            team.set_name(str(input("What is the name of your team.\n")))
            team.set_type(str(input("What is the team type: girl or boy?\n")))
            team.set_fee(int(input("What is the amount of fee, the team has promised to pay.\n")))
            team.set_fee_paid(bool(input("Did the team pay fees? True/False.\n")))
            teams_list.create(team)
            print("The team has been added. \n")

        elif choice == select_team_for_info:
            team_id = int(input("Please enter the team id to get info on the team.\n"))
            team_found = teams_list.read(team_id)
            print(team_found)

        elif choice == select_team_by_type:
            team_found = []
            type = (str(input("Which type of team do you want to list, boy or girl.\n"))).lower()
            team_found = teams_list.list_teams(type)
            for i in team_found:
                print(i)

        elif choice == list_all_teams:
            print(str(teams_list))
            team_found = []
            team_found = teams_list.list_all()
            for i in team_found:
                print(i)

        elif choice == update_info_of_team:
            team_found = []
            team_found = teams_list.list_all()
            print("\nList of all teams with Id and Name.\n")
            print("ID_of team       Teams_Name")
            for i in team_found:
                print(f"{i.get_id()}                  {i.get_name()}\n")
            team_id = int(input("Please enter the team id to update info of the team.\n"))
            team_found = teams_list.read(team_id)
            teams_list.update(team_found)
            print("The team has been updated.\n")

        elif choice == delete_a_team:
            team_id = int(input("Please enter the team id of the team to be deleted.\n"))
            teams_list.delete(team_id)
            print("The team has been deleted.\n")

        elif choice == total_and_percent:
            teams_list.total()

        elif choice == download_txt:
            teams_list.download_txt_file()

        elif choice == read_txt_file:
            teams_list.restore_data_txt()
            print("The data has been restored.\n")



if __name__ == '__main__':
    main()
