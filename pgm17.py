import mysql.connector

conn=mysql.connector.connect(host="localhost", user="root", password="")
cur= conn.cursor()
cur.execute("create database if not exists lib")
cur.execute("use lib")
cur.execute("""create table if not exists pgm(id int unique,
            title varchar(30),
            author varchar(30),
            publisher varchar(30),
            price int,
            copies int
            )
            """)
cur.close()
conn.close()

class library():
    def connect(self):
        return mysql.connector.connect(host="localhost", user="root", passwd="", db="lib")

    def insert(self,id,title,author,pub,price,copies):
        con=self.connect()
        cur=con.cursor()

        cur.execute("insert into pgm values(%s, %s, %s, %s, %s, %s)",(id,title,author,pub,price,copies))
        con.commit()
        cur.close()
        con.close()

    def dta(self,data):
        print("Tiltle\tTitle\tAuthor\tPublisher\tPrice\tCopies")

        for row in data:
            for i in row:
                print(i, end="\t")
            print()

    def view(self):
        con=self.connect()
        cur=con.cursor()

        cur.execute("select * from pgm")
        self.dta(cur.fetchall())
        cur.close()
        con.close()

    def high(self):
        con=self.connect()
        cur=con.cursor()

        cur.execute("select * from pgm where price = (select max(price) from pgm)")
        self.dta(cur.fetchall())
        cur.close()
        con.close()

    def cal(self):
        con=self.connect()
        cur=con.cursor()

        cur.execute("select sum(price * copies) from pgm")
        print("Total Cost:", cur.fetchone() [0])
        cur.close()
        con.close()

    def search(self):
        con=self.connect()
        cur=con.cursor()

        num=int(input("Enter the book number: "))
        cur.execute("select * from pgm where id=%s",(num,))
        d=cur.fetchall()
        if not d:
            print("Error, Please Enter correct book number")
        else:
            self.dta(d)
        cur.close()
        con.close()

l=library()
print()
print("1.Add Book\n2. Search Book\n3. View book\n4. Costliest Book\n5. Total Cost\n6. Exit\n")
while(True):
    op= int(input("Enter The Option: "))
    if (op==1):
        id=int(input("Enter Book Number: "))
        title=input("Enter title: ")
        author=input("Enter Author Name: ")
        pub=input("Enter Publisher Name: ")
        price=int(input("Enter Book Price: "))
        copies=int(input("Enter no. of Copies: "))
        l.insert(ano,title,author,pub,price,copies)
    
    elif (op==2):
        l.search()
    
    elif (op==3):
        l.view()
    
    elif (op==4):
        l.high()

    elif (op==5):
        l.cal()

    elif (op==6):
        print("Exiting")
        exit()
    else:
        print("Please Enter Valid Option")


        



