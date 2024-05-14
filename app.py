#docstring - Yuran Zuo- airplane database application
#imoprts
import sqlite3

#contants and variables
DATABASE = "fighter.db"


#functions
def print_all_aircraft():
    '''print all the aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from fighter;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name                        speed  max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finished here
    db.close() 



#main code
while True:
    user_input = input(
"""
What would you like to do.
1. Print all aircraft
2. Print all aircraft sorted by speed
7. Exit
""")
    if user_input == "1":
        print_all_aircraft()
    elif user_input == "2":
        print_all_aircraft_by_speed()
    elif user_input == "3":
        print_all_aircraft_by_climb()
    elif user_input == "4":
        print_all_aircraft_by_range()
    elif user_input == "5":
        print_all_aircraft_by_climb()
    elif user_input == "6":
        print_all_aircraft_by_payload()
    elif user_input == "7":
        break
    else:
        print("That was not an option\n")

