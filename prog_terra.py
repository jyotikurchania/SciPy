# Python Program for View and Edit Flight Schedule
#
# This program will perform ADD/DELETE/UPDATE/SELECT ON Flight Schedule table
#
# Jyoti Kurchanin

import cx_Oracle

ADD_RECORD = 1
DELETE_RECORD = 2
UPDATE_RECORD = 3
VIEW_RECORD = 4
QUIT = 5
def main():
    try:
        # Open ORACLE Connection
        con = cx_Oracle.connect('system/oracle2019@localhost/orcl')           
        cursor = con.cursor()
             
        choice = 0
        while choice != QUIT:
            #Call a function to Choose what operation need to perform 
            choice = get_choice_menu()

            if choice == ADD_RECORD:    #Add Record in Schedule Table
                add_record(cursor)
            elif choice == DELETE_RECORD:   #Delete Record in Schedule Table
                delete_record(cursor)
            elif choice == UPDATE_RECORD:
                update_record(cursor)   #Update Record in Schedule Table
            elif choice == VIEW_RECORD:
                view_record(cursor)
                
    except cx_Oracle.DatabaseError as e: 
        print("There is a problem with Oracle", e) 

    finally: 
        if cursor: 
            cursor.close() 
        if con: 
            con.close()
            
# Function to make a choice
def  get_choice_menu():
    print()
    print('Terra Firma Airlines')
    print('='*20)
    print('1. Add Flight Schedule')
    print('2. Delete Flight Schedule')
    print('3. Update Flight Schedule')
    print('4. View Flight Schedule')
    print('5. Quit')
    choice = int(input("What operation you need to perfomed: "))

    while choice < ADD_RECORD or choice > QUIT:
        choice = int(input("What opration you need to perfomed: "))
        
    return choice

#Function to ADD recored in Flight Schedule Table
def add_record(cursor): 
   flt_nbr = input("Enter a Flight Number: ")
   flt_date = input("Enter a Flight Date(MM/DD/YYYY): ")
   tod = input("Enter a Time of Departure(hh:mm): ")
   toa = input("Enter a Time of Arrival(hh:mm): ")
   serial = input("Enter a Serial Number: ")

   sql_str= "INSERT INTO T_Flt_Schedule(flt_nbr,flt_date ,tod,toa ,serial#) VALUES(:flt_nbr1 , TO_DATE(:flt_date1,'MM/DD/YYYY') ,:tod1, :toa1 ,:serial1)"
    
   cursor.execute(sql_str, flt_nbr1= flt_nbr,flt_date1= flt_date ,tod1= tod, toa1= toa ,serial1=serial)
   cursor.execute("commit")

   view_record(cursor)

#Function to DELETE recored in Flight Schedule Table
def delete_record(cursor):
   flt_nbr = input("Enter a Flight Number: ")
   flt_date = input("Enter a Flight Date(MM/DD/YYYY): ")

   sql_str= "DELETE FROM T_Flt_Schedule WHERE flt_nbr =:flt_nbr1 AND flt_date = TO_DATE(:flt_date1,'MM/DD/YYYY')"
    
   cursor.execute(sql_str, flt_nbr1= flt_nbr,flt_date1= flt_date)
   cursor.execute("commit")

   view_record(cursor)

#Function to UPDATE recored in Flight Schedule Table
def update_record(cursor):
   flt_nbr = input("Enter a Flight Number: ")
   flt_date = input("Enter a Flight Date(MM/DD/YYYY): ")
   tod = input("Enter a Time of Departure(hh:mm): ")
   toa = input("Enter a Time of Arrival()hh:mm: ")
   serial = input("Enter a Serial Number: ")   

   sql_str= "UPDATE T_Flt_Schedule SET tod =:tod1 ,toa=:toa1 ,serial#= :serial1 WHERE flt_nbr =:flt_nbr1 AND flt_date = TO_DATE(:flt_date1,'MM/DD/YYYY')"
    
   cursor.execute(sql_str, flt_nbr1= flt_nbr,flt_date1= flt_date ,tod1= tod, toa1= toa ,serial1=serial)
   cursor.execute("commit")

   view_record(cursor)
   
#Function to VIEW recored in Flight Schedule Table    
def view_record(cursor):
    sql_str= "SELECT flt_nbr,TO_CHAR(flt_date,'MM/DD/YYYY'),tod,toa ,serial# FROM T_Flt_Schedule"
    
    cursor.execute(sql_str)
    result = cursor.fetchall()
    print("Flt_Nbr\t","Flt_Date\t","TOD\t\t","TOA\t\t","Serail#")
    print("="*75)
    for row in result:      
        print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])    

main()
