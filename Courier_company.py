import sqlite3 as sq
import datetime as dt

def create():

      conn = sq.connect("Creation.sqlite3")

      return conn

def cursor_1():

      cn = create()
      cr = cn.cursor()

      sql = "create table if not exists Courier (Serial_no INTEGER PRIMARY KEY AUTOINCREMENT," \
            "product_name TEXT,product_type TEXT,location TEXT, amount REAL," \
            "receiving_date TEXT (40),phone_num INTEGER NOT NULL)"


      cr.execute(sql)

def insert_data():

      product_name = input("Enter Product name:")
      product_type = input("Enter the Product type:")
      location = input("Enter the location:")
      amount = float(input("Enter the Payable Amount:"))
      receiving_date = str(dt.datetime.now())
      phone_num = input("Entr Customer Phone Number:")

      cn = create()
      cr = cn.cursor()

      sql = "insert into courier(product_name,product_type,location,amount,receiving_date,phone_num)" \
            "values(?,?,?,?,?,?)"
      val = (product_name,product_type,location,amount,receiving_date,phone_num)

      cr.execute(sql,val)

      cn.commit()
      Menu()

def show_db():
      cn = create()

      cr = cn.cursor()

      sql = "select * from courier"

      cr.execute(sql)
      data = cr.fetchall()

      for item in data:
            for i in item:
                  print(i,end=' ')
            print(" ")
      Menu()

def update_db():

      cn = create()
      cr = cn.cursor()

      print("Enter 1 to change product name")
      print("Enter 2 to change Product type")
      print("Enter 3 to change location")
      print("Enter 4 to change Payable Amount")
      print("Enter 5 to change Phone Number")
      print(" ")

      a = int(input("Enter 1/2/3/4/5 to change desire option!:"))


      if a == 1:

            sql = "update courier set product_name = ? where Serial_no =?"
            val = (input("Enter product name:"),int(input("Serial Number:")))

            cr.execute(sql,val)
            cn.commit()
      elif a == 2:
            sql = "update courier set product_type = ? where Serial_no =?"
            val = (input("Enter product type:"), int(input("Serial Number:")))
            cr.execute(sql, val)
            cn.commit()
      elif a ==3:
            sql = "update courier set location = ? where Serial_no =?"
            val = (input("Enter Location:"), int(input("Serial Number:")))
            cr.execute(sql, val)
            cn.commit()
      elif a== 4:
            sql = "update courier set amount = ? where Serial_no =?"
            val = (input("Enter changed amount:"), int(input("Serial Number:")))
            cr.execute(sql, val)
            cn.commit()
      elif a == 5:
            sql = "update courier set phone_num = ? where Serial_no =?"
            val = (input("Enter new phone number:"), int(input("Serial Number:")))
            cr.execute(sql, val)
            cn.commit()
      else:

            print("Wrong Input!")
            update_db()

      Menu()
def sum_amount():

      cn = create()
      cr = cn.cursor()

      sql = "select amount from Courier"

      cr.execute(sql)
      total = cr.fetchall()

      sum1 = 0

      for i in total:
            for j in i:
                  sum1 = sum1 + j

      print("Total amount = ", sum1, " Taka ")
      print(" ")
      Menu()

def Menu():

      print("---Super Fast Bangladesh---")
      print("------Courier Company------")

      print("Enter 1 to Insert data.\n"
            "Enter 2 to Show data base.\n"
            "Enter 3 to update data base.\n"
            "enter 4 to Show the total amount .")

      choice = int(input("Enter 1/2/3/4 :"))

      if choice == 1:
            insert_data()
      elif choice == 2:
            show_db()
      elif choice == 3:
            update_db()
      elif choice == 4:
            sum_amount()
      else:
            print("Wrong Input !")
            Menu()
Menu()