import mysql.connector
from tabulate import tabulate
con=mysql.connector.connect(host="localhost",user="root",password="root",database="python_db")
def insert(Name,Age,City):
    res=con.cursor()
    sql=" insert into users(Name, Age,City) values(%s,%s,%s)"
    user=(Name,Age,City)
    res.execute(sql,user)
    con.commit()
    print("Data Inserted Successfully")

def update(Name,Age,City,Id):
    res = con.cursor()
    sql = " update users set Name=%s,Age=%s,City=%s where Id =%s"
    user = (Name, Age, City,Id)
    res.execute(sql, user)
    con.commit()
    print("Data Updated Successfully")
def delete(id):
    res = con.cursor()
    sql = "delete from users where id=%s"
    user = (id,)
    res.execute(sql, user)
    con.commit()
    print("Data Delete Success")

def select():
    res=con.cursor()
    sql="select * from users"
    res.execute(sql)
    # result=res.fetchone()
    result=res.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))

def Exit():
    pass
while True:
    print("1. Insert:")
    print("2. Update:")
    print("3. Delete:")
    print("4.select:")
    print("5. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        Name=input("Enter your name:")
        Age=int(input("Enter your age:"))
        City=input("Enter your city:")
        insert(Name, Age, City)
    elif choice == 2:
        Id = input("Enter your Id:")
        Name=input("Enter your name:")
        Age = int(input("Enter your age:"))
        City = input("Enter your city:")
        update(Name, Age, City,Id)
    elif choice == 3:
        Id=int(input("Enter id to delete:"))
        delete(Id)
    elif choice == 4:
        select()
    elif choice==5:
        Exit()
    else:
        print('Invalid selection.Please try again!')




