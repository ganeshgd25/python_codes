# Mini database system
# Create table
# Insert record
# Update record
# Delete record
# Search record
# Multiple tables
# Unique validation
# Record count

database = {}

while True:
    print("/n1.create Table")
    print("2.insert record")
    print("3.view records")
    print("4.exit")

    choice = input("enter your choice: ")

# Table logic

    if choice=="1" :
        table_name = input("Enter table name: ")

        if table_name in database:
            print("Table already exists!")
        else:
            database[table_name] = {}
            print("Table created sucessfully!")

# Insert Record 
    elif choice == "2":
        table_name = input("Enter table name: ")

        if table_name in database :
            record_id = int(input("Enter your ID :"))
            name = input("Enter name:")
            email = input("Enter Email: ")

            database[table_name] = {
            "ID" : record_id,
            "name" :name,
            "email": email
            }
            print("Record Inserted Sucessfully..!")
        else:
            print("Table not exist!")

# view Records 
    elif choice == "3":
        table_name = input("please Enter Table name: ")
    
        if table_name in database:
            for id , record in database[table_name].items():
             print(id,record)
        else:
            print("Table does not exist!")
# exit 
    elif choice =="4":
        print("exit..")
        break
    else:
        print("Invalid Choice!")

