import sys

users =[{"Name":"Nigita","Address":"Fedi"}]

def CreateUser(users):
    name = input("Enter your name : ")
    address= input("Enter your address : ")
    newuser = {"Name":name,"Address":address}
    users.append(newuser)
    print(users)

def ListUser(users):
    print("S.N\t\tName \t\t\t Address ")
    for index,user in enumerate(users):
        print(str(index) +"\t\t"+ user["Name"]+"\t\t\t"+user["Address"])

def EditUser(users):
    editindex = int(input("Enter the user index you want to edit : "))
    newname = input("Enter the new name : ")
    newaddress = input("Enter new address : ")
    user = users[editindex]
    user["Name"] = newname
    user["Address"] = newaddress

def DeleteUser(users):
    delname = input("Enter name of user you want to delete : ")
    for user in users:
        if user["Name"] == delname:
            users.remove(user)

def menu():
    print("\n***Choose an option***")
    print("1.Create User\n2. List the created users\n3. Edit user \n4. Delete user ")

def main():
    with open('app.txt','r+') as file:
        for line in file:
            print(line, end = '')
        while True:
            menu()
            choice = int(input("Enter your choice"))
            if choice == 1:
                CreateUser(users)
                print("User created")
            elif choice==2:
                print("List of users")
                ListUser(users)
            elif choice==3:
                ListUser(users)
                EditUser(users)
                print("The new list is\n ")
                ListUser(users)
            elif choice==4:
                DeleteUser(users)
                print("User deleted")
            else:
                print("Thank you for using")
                break

        file.writelines(str(users))
        file.close()

if __name__ == "__main__":
    sys.exit(main())

