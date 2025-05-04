#LATEST code


import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector as sql
from tkinter import messagebox
import datetime as dt

#Employees: 300X
#Books: X
#Members: 100X
#Non-members: 200X
#where x belongs to 0 to 9

conn = sql.connect(host='localhost',user='root',password='pswd@123')
curr=conn.cursor()

def create():
    def database():
        quer1 = "show databases"
        curr.execute(quer1)
        r = curr.fetchall()
        l = []
        for i in r:
            l.append(i[0])
        if 'Library'.lower() in l:
            pass
        else:
            quer2 = "create database Library"
            curr.execute(quer2)
            conn.commit()
    def table():
        quer3 = "use Library"
        curr.execute(quer3)
        quer4 = "show tables"
        curr.execute(quer4)
        r = curr.fetchall()
        l = []
        for i in r:
            l.append(i[0])
        if 'employee'.lower() in l:
            pass
        else:
            quer5 = "create table employee (Id int primary key,Name varchar(50) not null,Qualifications varchar(100),Work_hours decimal(6,2),Salary decimal(10,2) ,Address varchar(200) not null)"
            curr.execute(quer5)
            conn.commit()
        if 'books'.lower() in l:
            pass
        else:
            quer7 = "create table Books(Id int primary key, Name varchar(100) not null, Author varchar(100) default 'Anonymous', Publisher varchar(100) default 'Anonymous', Number_of_copies int, Price decimal(6,1) not null, Genre varchar(50) not null)"
            curr.execute(quer7)
            conn.commit()
        if 'members'.lower() in l:
            pass
        else:
            quer9 = "create table members (Id int primary key, Name varchar(100) not null, Address varchar(200) not null, Phone_number char(10) not null, Interests varchar(100))"
            curr.execute(quer9)
            conn.commit()
        if 'non_members'.lower() in l:
            pass
        else:
            quer11 = "create table Non_members (Id int primary key, Name varchar(100) not null, Address varchar(100), Phone_number char(10) not null, Entry_time timestamp not null, Exit_time timestamp not null)"
            curr.execute(quer11)
            conn.commit()
        if 'issued' in l:
            pass
        else:
            quer12 = "create table issued(User_Id varchar(5) , User_name varchar(100), Bookid int, Date_issued date, Due_date date, Return_status varchar(75), Penalty int);"
            curr.execute(quer12)
            conn.commit() 
    database()
    table()            
create()        

def display_employees():
    ws  = Tk()
    ws.attributes('-fullscreen', True)
    ws.geometry('500x500')
    ws['bg'] = '#000000'

    lib_frame = Frame(ws)
    lib_frame.pack()
    library = ttk.Treeview(lib_frame, height=45)
    library['columns'] = ('Id', 'Name', 'Qualifications', 'Work_Hours', 'Salary','Address')
    library.column("#0", width=0,  stretch=NO)
    library.column("Id",anchor=CENTER, width=80)
    library.column("Name",anchor=CENTER,width=80)
    library.column("Qualifications",anchor=CENTER,width=80)
    library.column("Work_Hours",anchor=CENTER,width=80)
    library.column("Salary",anchor=CENTER,width=80)
    library.column("Address",anchor=CENTER,width=200)

    library.heading("#0",text="",anchor=CENTER)
    library.heading("Id",text="Id",anchor=CENTER)
    library.heading("Name",text="Name",anchor=CENTER)
    library.heading("Qualifications",text="Qualifications",anchor=CENTER)
    library.heading("Work_Hours",text="Work Hours",anchor=CENTER)
    library.heading("Salary",text="Salary",anchor=CENTER)
    library.heading("Address",text="Address",anchor=CENTER)

    query = 'select * from employee'
    curr.execute(query)
    data = curr.fetchall()
    for i in data :        
        library.insert(parent='',index='end',iid=data.index(i),text='', values=i)    
    library.pack()
    mainloop()

def add_employees() :   
    def assign_value():       
        v1 = e1.get()
        v2 = e2.get()
        v3 = e3.get()
        v4 = e4.get()           
        v5 = e5.get()
        v6 = e6.get()
        #MAKE EVERYTHING INT
        query = 'select Id from employee'
        curr.execute(query)
        r = curr.fetchall()

        if (int(v1),) in r:
            messagebox.showerror('ID','ERROR ! ID ALREADY EXISTS' )
        else: 
            x1 = True
            x2 = True
            x3 = True
            x4i = True
            x4ii = True
            x5 = True
        
            for i in v1:
                if i.isdigit():
                    continue
                else:
                    messagebox.showerror('ID','ERROR ! ID IS NOT INTEGER' )                    
                    x1 = False
                    break                    
            for i in v2 :
                if i.lower() in 'abcdefghijklmnopqrstuvwxyz ':
                    continue
                else:
                    messagebox.showerror('Name','ERROR ! NO SPECIAL CHARACTER ALLOWED' )                   
                    x2 = False
                    break            
            for i in v3 :
                if i.lower() in 'abcdefghijklmnopqrstuvwxyz .-':
                    continue
                else:
                    messagebox.showerror('Qualification','ERROR ! NO SPECIAL CHARACTER ALLOWED' )                    
                    x3 = False
                    break             
            for i in v4 :
                if i in '0123456789':
                    continue
                else:
                    messagebox.showerror('Work Hour','ERROR ! WORK HOUR IS NOT INTEGER' )                        
                    x4ii = False
                    break                
            if x4ii == True :        
                if int(v4)>12:
                    messagebox.showerror('Work Hour','ERROR ! WORK HOUR SHOULD BE < 12' )  
                    x4i = False
                else :
                    pass                         
            for i in v5 : 
                if i.isdigit():
                    continue
                else:
                    messagebox.showerror('Salary','ERROR ! SALARY IS NOT INTEGER' )                    
                    x5 = False
                    break
               
            if (x1 == True) and (x2 == True) and (x3 == True) and (x4i == True) and (x4ii == True) and (x5 == True): 
                query = 'insert into employee values ({},"{}","{}",{},{},"{}")'
                query1 = query.format(v1,v2,v3,v4,v5,v6)
                curr.execute(query1)
                conn.commit()
            else:
                pass
      
    master = Tk()
    L1 = Label(master, text='Id*').grid(row=0)
    L2 = Label(master, text='Name*').grid(row=1)
    L3 = Label(master, text='Qualifications').grid(row=2)
    L4 = Label(master, text='Work Hours').grid(row=3)
    L5 = Label(master, text='Salary').grid(row=4)
    L6 = Label(master, text='Address*').grid(row=5)
    e1 = Entry(master)
    def temp1(v):
        e1.delete(0,"end")
    e1.insert(0, "Format = 300x")
    e1.bind("<FocusIn>",temp1)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e5 = Entry(master)
    e6 = Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    e6.grid(row=5, column=1)

    button = Button(master, text="Assign Value", command=assign_value)
    button.grid(row=6)
    button = Button(master, text="Display", command=display_employees)
    button.grid(row=7)
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=8, column=3)
    mainloop()

def search_employees():    
     def assign_value():
        v1 = e1.get()
        query = 'SELECT ID FROM employee'
        query = query.format(int(v1))
        curr.execute(query)
        r = curr.fetchall()
        if (int(v1),) in r:            
            global master
            v1 = e1.get()
            
            query = 'select * from employee where Id = {}'
            query = query.format(v1)
            curr.execute(query)
            data = curr.fetchall()        

            ws  = Tk()
            ws.attributes('-fullscreen', True)            
            ws['bg'] = '#000000'
            lib_frame = Frame(ws)
            lib_frame.pack()

            library = ttk.Treeview(lib_frame)
            library['columns'] = ('Id', 'Name', 'Qualifications', 'Work_Hours', 'Salary','Address')

            library.column("#0", width=0,  stretch=NO)
            library.column("Id",anchor=CENTER, width=80)
            library.column("Name",anchor=CENTER,width=80)
            library.column("Qualifications",anchor=CENTER,width=80)
            library.column("Work_Hours",anchor=CENTER,width=80)
            library.column("Salary",anchor=CENTER,width=80)
            library.column("Address",anchor=CENTER,width=200)

            library.heading("#0",text="",anchor=CENTER)
            library.heading("Id",text="Id",anchor=CENTER)
            library.heading("Name",text="Name",anchor=CENTER)
            library.heading("Qualifications",text="Qualifications",anchor=CENTER)
            library.heading("Work_Hours",text="Work Hours",anchor=CENTER)
            library.heading("Salary",text="Salary",anchor=CENTER)
            library.heading("Address",text="Address",anchor=CENTER)
            for i in data :        
                library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
            library.pack()
            mainloop()
        else:
            messagebox.showerror('Error', 'ID does not exist in the table.')     
     master = Tk()    
     L1 = Label(master, text='Search Element').grid(row=0)
     e1 = Entry(master)
     e1.grid(row=0,column=1)
     button = Button(master, text="Search", command=assign_value)
     button.grid(row=5)    
     button = Button(master, text="Close", command=master.destroy)
     button.grid(row=7, column=3)
     mainloop()
    
def update_employees():
    def assign():
        v1 = e1.get() #id
        v2 = e2.get() #menu
        v3 = e3.get() #value
        query = 'select Id from employee'
        curr.execute(query)
        r = curr.fetchall()
        if (int(v1),) in r:        
            if int(v2) == 1:
                for i in v3 :
                    if i.lower() in 'abcdefghijklmnopqrstuvwxyz ':
                        query = 'update employee set Name="{}" where Id={}'
                        query = query.format(v3, int(v1))
                        curr.execute(query)
                        conn.commit()                        
                        query = 'select * from employee where Id = {}'
                        query = query.format(int(v1))
                        curr.execute(query)
                        data = curr.fetchall()

                        ws  = Tk()
                        ws.geometry('500x500')
                        ws['bg'] = '#000000'                        
                        lib_frame = Frame(ws)
                        lib_frame.pack()
                        library = ttk.Treeview(lib_frame)
                        library['columns'] = ('Id', 'Name', 'Qualifications', 'Work_Hours', 'Salary','Address')

                        library.column("#0", width=0,  stretch=NO)
                        library.column("Id",anchor=CENTER, width=80)
                        library.column("Name",anchor=CENTER,width=80)
                        library.column("Qualifications",anchor=CENTER,width=80)
                        library.column("Work_Hours",anchor=CENTER,width=80)
                        library.column("Salary",anchor=CENTER,width=80)
                        library.column("Address",anchor=CENTER,width=200)

                        library.heading("#0",text="",anchor=CENTER)
                        library.heading("Id",text="Id",anchor=CENTER)
                        library.heading("Name",text="Name",anchor=CENTER)
                        library.heading("Qualifications",text="Qualifications",anchor=CENTER)
                        library.heading("Work_Hours",text="Work Hours",anchor=CENTER)
                        library.heading("Salary",text="Salary",anchor=CENTER)
                        library.heading("Address",text="Address",anchor=CENTER)
                        for i in data :        
                            library.insert(parent='',index='end',iid=data.index(i),text='', values=i)                          
                        library.pack()
                        mainloop()
                    else:
                        messagebox.showerror('Name','ERROR ! NO SPECIAL CHARACTER ALLOWED' )
                        break

                
                
            elif int(v2) == 2:
                for i in v3 :
                    if i.lower() in 'abcdefghijklmnopqrstuvwxyz .-':
                        query = 'update employee set qualifications="{}" where id={}'
                        query = query.format(v3, int(v1))
                        curr.execute(query)
                        conn.commit()
                        query = 'select * from employee where id = {}'
                        query = query.format(int(v1))
                        curr.execute(query)
                        data = curr.fetchall()
                        ws  = Tk()
                        ws.geometry('500x500')
                        ws['bg'] = '#000000'
                        
                        lib_frame = Frame(ws)
                        lib_frame.pack()

                        library = ttk.Treeview(lib_frame)

                        library['columns'] = ('Id', 'Name', 'Qualifications', 'Work_Hours', 'Salary','Address')

                        library.column("#0", width=0,  stretch=NO)
                        library.column("Id",anchor=CENTER, width=80)
                        library.column("Name",anchor=CENTER,width=80)
                        library.column("Qualifications",anchor=CENTER,width=80)
                        library.column("Work_Hours",anchor=CENTER,width=80)
                        library.column("Salary",anchor=CENTER,width=80)
                        library.column("Address",anchor=CENTER,width=200)

                        library.heading("#0",text="",anchor=CENTER)
                        library.heading("Id",text="Id",anchor=CENTER)
                        library.heading("Name",text="Name",anchor=CENTER)
                        library.heading("Qualifications",text="Qualifications",anchor=CENTER)
                        library.heading("Work_Hours",text="Work Hours",anchor=CENTER)
                        library.heading("Salary",text="Salary",anchor=CENTER)
                        library.heading("Address",text="Address",anchor=CENTER)

                        for i in data :        
                            library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
                        
                        
                        library.pack()
                        mainloop()
                    else:
                        messagebox.showerror('Qualification','ERROR ! NO SPECIAL CHARACTER ALLOWED' )                        
                        break            
                
                
            elif int(v2) == 3:
                #add: work hours > 12 validation
                for i in v3 :
                    if i in '0123456789':
                            query = 'update employee set work_hours="{}" where id={}'
                            query = query.format(v3, int(v1))
                            curr.execute(query)
                            conn.commit()
                            query = 'select * from employee where id = {}'
                            query = query.format(int(v1))
                            curr.execute(query)
                            data = curr.fetchall()

                            ws  = Tk()
                            ws.geometry('500x500')
                            ws['bg'] = '#000000'
                            
                            lib_frame = Frame(ws)
                            lib_frame.pack()

                            library = ttk.Treeview(lib_frame)

                            library['columns'] = ('Id', 'Name', 'Qualifications', 'Work_Hours', 'Salary','Address')

                            library.column("#0", width=0,  stretch=NO)
                            library.column("Id",anchor=CENTER, width=80)
                            library.column("Name",anchor=CENTER,width=80)
                            library.column("Qualifications",anchor=CENTER,width=80)
                            library.column("Work_Hours",anchor=CENTER,width=80)
                            library.column("Salary",anchor=CENTER,width=80)
                            library.column("Address",anchor=CENTER,width=80)

                            library.heading("#0",text="",anchor=CENTER)
                            library.heading("Id",text="Id",anchor=CENTER)
                            library.heading("Name",text="Name",anchor=CENTER)
                            library.heading("Qualifications",text="Qualifications",anchor=CENTER)
                            library.heading("Work_Hours",text="Work Hours",anchor=CENTER)
                            library.heading("Salary",text="Salary",anchor=CENTER)
                            library.heading("Address",text="Address",anchor=CENTER)

                            for i in data :        
                                library.insert(parent='',index='end',iid=data.index(i),text='', values=i)                           
                            
                            library.pack()
                            mainloop()

                    else:
                        messagebox.showerror('Work Hour','ERROR ! WORK HOUR IS NOT INTEGER' )      
                        break            
 
                
            elif int(v2) == 4: 
                for i in v3 : 
                    if i.isdigit():
                                query = 'update employee set salary={} where id={}'
                                query = query.format(int(v3), int(v1))
                                curr.execute(query)
                                conn.commit()
                                query = 'select * from employee where id = {}'
                                query = query.format(int(v1))
                                curr.execute(query)
                                data = curr.fetchall()

                                ws  = Tk()
                                ws.geometry('500x500')
                                ws['bg'] = '#000000'
                                
                                lib_frame = Frame(ws)
                                lib_frame.pack()

                                library = ttk.Treeview(lib_frame)

                                library['columns'] = ('Id', 'Name', 'Qualifications', 'Work_Hours', 'Salary','Address')

                                library.column("#0", width=0,  stretch=NO)
                                library.column("Id",anchor=CENTER, width=80)
                                library.column("Name",anchor=CENTER,width=80)
                                library.column("Qualifications",anchor=CENTER,width=80)
                                library.column("Work_Hours",anchor=CENTER,width=80)
                                library.column("Salary",anchor=CENTER,width=80)
                                library.column("Address",anchor=CENTER,width=200)

                                library.heading("#0",text="",anchor=CENTER)
                                library.heading("Id",text="Id",anchor=CENTER)
                                library.heading("Name",text="Name",anchor=CENTER)
                                library.heading("Qualifications",text="Qualifications",anchor=CENTER)
                                library.heading("Work_Hours",text="Work Hours",anchor=CENTER)
                                library.heading("Salary",text="Salary",anchor=CENTER)
                                library.heading("Address",text="Address",anchor=CENTER)

                                for i in data :        
                                    library.insert(parent='',index='end',iid=data.index(i),text='', values=i)                    
                                
                                library.pack()
                                mainloop()
                    else:
                        messagebox.showerror('Salary','ERROR ! SALARY IS NOT INTEGER' )
                        break           


            elif int(v2) == 5:            
                query = 'update employee set address="{}" where id={}'
                query = query.format(v3, int(v1))
                curr.execute(query)
                conn.commit()
                query = 'select * from employee where id = {}'
                query = query.format(int(v1))
                curr.execute(query)
                data = curr.fetchall()

                ws  = Tk()
                ws.geometry('500x500')
                ws['bg'] = '#000000'
                
                lib_frame = Frame(ws)
                lib_frame.pack()

                library = ttk.Treeview(lib_frame)

                library['columns'] = ('Id', 'Name', 'Qualifications', 'Work_Hours', 'Salary','Address')

                library.column("#0", width=0,  stretch=NO)
                library.column("Id",anchor=CENTER, width=80)
                library.column("Name",anchor=CENTER,width=80)
                library.column("Qualifications",anchor=CENTER,width=80)
                library.column("Work_Hours",anchor=CENTER,width=80)
                library.column("Salary",anchor=CENTER,width=80)
                library.column("Address",anchor=CENTER,width=80)

                library.heading("#0",text="",anchor=CENTER)
                library.heading("Id",text="Id",anchor=CENTER)
                library.heading("Name",text="Name",anchor=CENTER)
                library.heading("Qualifications",text="Qualifications",anchor=CENTER)
                library.heading("Work_Hours",text="Work Hours",anchor=CENTER)
                library.heading("Salary",text="Salary",anchor=CENTER)
                library.heading("Address",text="Address",anchor=CENTER)

                for i in data :        
                    library.insert(parent='',index='end',iid=data.index(i),text='', values=i)                
                   
                library.pack()
                mainloop()
        
            else:
                messagebox.showinfo("Status",'The number entered is not in the given range of choices.')

        else :
            messagebox.showerror("Status",'Id entered does not exist in the database')
            
        

    master = Tk()
    idsearch = Label(master, text='Enter id to update the details').grid(row=0)
    Display = Label(master, text='''Enter one of the following numbers to change :
1. Name
2. Qualifications
3. Work hours
4. Salary
5. Address''').grid(row=1)
    Newval = Label(master, text='Enter corresponding new value').grid(row=7)
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e1.grid(row=0, column = 1)
    e2.grid(row=1, column = 1)
    e3.grid(row=7, column = 1)

    button = Button(master, text="Update",command=assign)
    button.grid(row=9)
    button = Button(master, text="Display Database", command=display_employees)
    button.grid(row=11)
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=14 , column=3)
    mainloop()

def delete_employees():
    def assign():
        v = e1.get()
        query = 'SELECT * FROM employee WHERE id = {}'
        query = query.format(int(v))
        curr.execute(query)
        data = curr.fetchone()

        if data:
            delete_query = 'DELETE FROM employee WHERE id = {}'
            delete_query = delete_query.format(int(v))
            curr.execute(delete_query)
            conn.commit()
            messagebox.showinfo('Status', 'Successfully deleted.')
        else:
            messagebox.showerror('Error', 'ID does not exist in the table.')



    master= Tk()
    L1 = Label(master, text='ID').grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0,column=1)
    button = Button(master, text="Delete", command=assign)
    button.grid(row=5)
    button = Button(master, text="Display", command=display_employees)
    button.grid(row=7)
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=9, column=3)
    mainloop()       


def display_books():
    ws  = Tk()
    ws.geometry('500x500')
    ws.attributes('-fullscreen', True)
    ws['bg'] = '#000000'

    lib_frame = Frame(ws)
    lib_frame.pack()

    library = ttk.Treeview(lib_frame, height=45)

    library['columns'] = ('Id', 'Name', 'Author', 'Publisher', 'Number_of_copies','Price','Genre')

    library.column("#0", width=0,  stretch=NO)
    library.column("Id",anchor=CENTER, width=80)
    library.column("Name",anchor=CENTER,width=80)
    library.column("Author",anchor=CENTER,width=80)
    library.column("Publisher",anchor=CENTER,width=80)
    library.column("Number_of_copies",anchor=CENTER,width=80)
    library.column("Price",anchor=CENTER,width=80)
    library.column("Genre",anchor=CENTER,width=80)


    library.heading("#0",text="",anchor=CENTER)
    library.heading("Id",text="Id",anchor=CENTER)
    library.heading("Name",text="Name",anchor=CENTER)
    library.heading("Author",text="Author",anchor=CENTER)
    library.heading("Publisher",text="Publisher",anchor=CENTER)
    library.heading("Number_of_copies",text="Number of copies",anchor=CENTER)
    library.heading("Price",text="Price",anchor=CENTER)
    library.heading("Genre",text="Genre",anchor=CENTER)


    query = 'select * from books'
    curr.execute(query)
    data = curr.fetchall()
    for i in data :        
        library.insert(parent='',index='end',iid=data.index(i),text='', values=i)    
    library.pack()
    mainloop()

def add_books() :   
    def assign_value():
        
        global v1
        global v2
        v1 = e1.get()
        v2 = e2.get()
        v3 = e3.get()
        v4 = e4.get()
        v5 = e5.get()
        v6 = e6.get()
        v7 = e7.get()
         #MAKE EVERYTHING INT 
        x1 = True 
        x2 = True
        x3 = True
        x4 = True
        x5 = True
        x6 = True
        x7 = True
        query = 'select Id from books'
        curr.execute(query)
        r = curr.fetchall()

        if (int(v1),) in r:
            messagebox.showerror('ID','ERROR ! ID ALREADY EXISTS' )
        else:
            for i in v1 :            
                if str(i).isdigit():
                    continue
                else:
                    messagebox.showerror('ID','ERROR ! ID IS NOT INTEGER' )                            
                    break
                    x1 = False
                
            for i in v2 :
                if i.lower() in 'abcdefghijklmnopqrstuvwqxyz ':
                    continue
                else:
                    messagebox.showerror('Name','ERROR ! NO SPECIAL CHARACTER ALLOWED' )
                    break
                    x2 = False

            for i in v3 :
                if i.lower() in 'abcdefghijklmnopqrstuvwqxyz ':
                    continue
                else:
                    messagebox.showerror('Author','ERROR ! NO SPECIAL CHARACTER ALLOWED' )
                    break
                    x3 = False

            for i in v4 :
                if i.lower() in 'abcdefghijklmnopqrstuvwqxyz ':
                    continue
                else:
                    messagebox.showerror('Publisher','ERROR ! NO SPECIAL CHARACTER ALLOWED' )
                    break
                    x4 = False

            for i in v5 : 
                if str(i).isdigit():
                    continue
                else:
                    messagebox.showerror('Price','ERROR ! PRICE IS NOT INTEGER' )
                    break
                    x5 = False

            for i in v6 : 
                if str(i).isdigit():
                    continue
                else:
                    messagebox.showerror('Number_of_copies','ERROR ! NUMBER OF COPIES IS NOT INTEGER' )
                    break
                    x6 = False
                    
            for i in v7 :
                if i.lower() in 'abcdefghijklmnopqrstuvwqxyz ':
                    continue
                else:
                    messagebox.showerror('Genre','ERROR ! NO SPECIAL CHARACTER ALLOWED' )
                    break
                    x7 = False            

               
            if (x1 == True) and (x2 == True) and (x3 == True) and (x4 == True) and (x5 == True) and(x6 == True) and (x7 == True): 
                query = 'insert into books values ({},"{}","{}","{}",{},{},"{}")'
                query1 = query.format(v1,v2,v3,v4,v5,v6,v7)
                curr.execute(query1)
                conn.commit()
            else:
                pass
        
      
    master = Tk()
    L1 = Label(master, text='Id*').grid(row=0)
    L2 = Label(master, text='Name*').grid(row=1)
    L3 = Label(master, text='Author').grid(row=2)
    L4 = Label(master, text='Publisher').grid(row=3)
    L5 = Label(master, text='Number of copies').grid(row=4)
    L6 = Label(master, text='Price*').grid(row=5)
    L7 = Label(master, text='Genre*').grid(row=6)
    e1 = Entry(master)
    def temp2(u):
        e1.delete(0,"end")
    e1.insert(0, "Format = x")
    e1.bind("<FocusIn>",temp2)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e5 = Entry(master)
    e6 = Entry(master)
    e7 = Entry(master)
    e1.grid(row=0, column=1)
    
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    e6.grid(row=5, column=1)
    e7.grid(row=6, column=1)

    button = Button(master, text="Assign Value", command=assign_value)
    button.grid(row=7)
    button = Button(master, text="Display", command=display_books)
    button.grid(row=8)
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=9, column=3)
    mainloop()
    
def search_books():
     def assign_value():
        v1 = e1.get()
        query = 'SELECT ID FROM books'
        query = query.format(int(v1))
        curr.execute(query)
        r = curr.fetchall()
        

        if (int(v1),) in r:
        
            # ID exists, display the record
            global master
            v1 = e1.get()
            query = 'select * from books where Id = {}'
            query = query.format(v1)
            curr.execute(query)
            data = curr.fetchall()        

            ws  = Tk()
            ws.geometry('500x500')
            ws.attributes('-fullscreen', True)
            ws['bg'] = '#000000'

            lib_frame = Frame(ws)
            lib_frame.pack()

            library = ttk.Treeview(lib_frame)

            library['columns'] = ('Id', 'Name', 'Author', 'Publisher', 'Number_of_copies','Price','Genre')

            library.column("#0", width=0,  stretch=NO)
            library.column("Id",anchor=CENTER, width=80)
            library.column("Name",anchor=CENTER,width=120)
            library.column("Author",anchor=CENTER,width=80)
            library.column("Publisher",anchor=CENTER,width=80)
            library.column("Number_of_copies",anchor=CENTER,width=120)
            library.column("Price",anchor=CENTER,width=80)
            library.column("Genre",anchor=CENTER,width=80)


            library.heading("#0",text="",anchor=CENTER)
            library.heading("Id",text="Id",anchor=CENTER)
            library.heading("Name",text="Name",anchor=CENTER)
            library.heading("Author",text="Author",anchor=CENTER)
            library.heading("Publisher",text="Publisher",anchor=CENTER)
            library.heading("Number_of_copies",text="Number of copies",anchor=CENTER)
            library.heading("Price",text="Price",anchor=CENTER)
            library.heading("Genre",text="Genre",anchor=CENTER)
            for i in data :        
                library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
            
               
            library.pack()
            mainloop()
        else:
            # ID doesn't exist, show error message
            messagebox.showerror('Error', 'ID does not exist in the table.')     

        
     master = Tk()    
     L1 = Label(master, text='Search Element').grid(row=0)
     e1 = Entry(master)
     e1.grid(row=0,column=1)
     button = Button(master, text="Search", command=assign_value)
     button.grid(row=5)    
     button = Button(master, text="Close", command=master.destroy)
     button.grid(row=7, column=3)
     mainloop()

def update_books():
    # UPDATE – if any number corresponding to columns apart from allowed ones are entered, raise error
    def assign():
        v1 = e1.get() #rollno
        v2 = e2.get() #menu
        v3 = e3.get() #value
        x = True 

        query = 'select Id from books'
        curr.execute(query)
        r = curr.fetchall()
        if (int(v1),) in r:
            if int(v2) == 1:
                for i in v3 :
                    if i.lower() in 'abcdefghijklmnopqrstuvwqxyz ':
                        query = 'update books set Name="{}" where Id={}'
                        query = query.format(v3, int(v1))
                        curr.execute(query)
                        conn.commit()

                        query = 'select * from books where Id = {}'
                        query = query.format(int(v1))
                        curr.execute(query)
                        data = curr.fetchall()

                        ws  = Tk()
                        ws.geometry('500x500')
                        ws.attributes('-fullscreen', True)
                        ws['bg'] = '#000000'
                        
                        lib_frame = Frame(ws)
                        lib_frame.pack()

                        library = ttk.Treeview(lib_frame,  height=45)

                        library['columns'] = ('Id', 'Name', 'Author', 'Publisher', 'Number_of_copies','Price','Genre')

                        library.column("#0", width=0,  stretch=NO)
                        library.column("Id",anchor=CENTER, width=80)
                        library.column("Name",anchor=CENTER,width=80)
                        library.column("Author",anchor=CENTER,width=80)
                        library.column("Publisher",anchor=CENTER,width=80)
                        library.column("Number_of_copies",anchor=CENTER,width=80)
                        library.column("Price",anchor=CENTER,width=80)
                        library.column("Genre",anchor=CENTER,width=80)


                        library.heading("#0",text="",anchor=CENTER)
                        library.heading("Id",text="Id",anchor=CENTER)
                        library.heading("Name",text="Name",anchor=CENTER)
                        library.heading("Author",text="Author",anchor=CENTER)
                        library.heading("Publisher",text="Publisher",anchor=CENTER)
                        library.heading("Number_of_copies",text="Number of copies",anchor=CENTER)
                        library.heading("Price",text="Price",anchor=CENTER)
                        library.heading("Genre",text="Genre",anchor=CENTER)
                        for i in data :        
                            library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
                        
                           
                        library.pack()
                        mainloop()
                    else:
                        messagebox.showerror('Name','ERROR ! NO SPECIAL CHARACTER ALLOWED' )
                        break
                        x = False

                
            elif int(v2) == 2:
                for i in v3 :
                    if i.lower() in 'abcdefghijklmnopqrstuvwqxyz ':
                        query = 'update books set Author="{}" where id={}'
                        query = query.format(v3, int(v1))
                        curr.execute(query)
                        conn.commit()

                        query = 'select * from books where id = {}'
                        query = query.format(int(v1))
                        curr.execute(query)
                        data = curr.fetchall()

                        ws  = Tk()
                        ws.geometry('500x500')
                        ws.attributes('-fullscreen', True)
                        ws['bg'] = '#000000'
                        
                        lib_frame = Frame(ws)
                        lib_frame.pack()

                        library = ttk.Treeview(lib_frame)

                        library['columns'] = ('Id', 'Name', 'Author', 'Publisher', 'Number_of_copies','Price','Genre')

                        library.column("#0", width=0,  stretch=NO)
                        library.column("Id",anchor=CENTER, width=80)
                        library.column("Name",anchor=CENTER,width=80)
                        library.column("Author",anchor=CENTER,width=80)
                        library.column("Publisher",anchor=CENTER,width=80)
                        library.column("Number_of_copies",anchor=CENTER,width=80)
                        library.column("Price",anchor=CENTER,width=80)
                        library.column("Genre",anchor=CENTER,width=80)


                        library.heading("#0",text="",anchor=CENTER)
                        library.heading("Id",text="Id",anchor=CENTER)
                        library.heading("Name",text="Name",anchor=CENTER)
                        library.heading("Author",text="Author",anchor=CENTER)
                        library.heading("Publisher",text="Publisher",anchor=CENTER)
                        library.heading("Number_of_copies",text="Number of copies",anchor=CENTER)
                        library.heading("Price",text="Price",anchor=CENTER)
                        library.heading("Genre",text="Genre",anchor=CENTER)

                        for i in data :        
                            library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
                        
                           
                        library.pack()
                        mainloop()
                    else:
                        messagebox.showerror('Author','ERROR ! NO SPECIAL CHARACTER ALLOWED' )
                        break
                
                
            elif int(v2) == 3:
                for i in v3 :
                    if i.lower() in 'abcdefghijklmnopqrstuvwqxyz ':
                        query = 'update books set Publisher="{}" where id={}'
                        query = query.format(v3, int(v1))
                        curr.execute(query)
                        conn.commit()
                        query = 'select * from books where id = {}'
                        query = query.format(int(v1))
                        curr.execute(query)
                        data = curr.fetchall()

                        ws  = Tk()
                        ws.geometry('500x500')
                        ws.attributes('-fullscreen', True)
                        ws['bg'] = '#000000'
                        
                        lib_frame = Frame(ws)
                        lib_frame.pack()

                        library = ttk.Treeview(lib_frame)

                        library['columns'] = ('Id', 'Name', 'Author', 'Publisher', 'Number_of_copies','Price','Genre')

                        library.column("#0", width=0,  stretch=NO)
                        library.column("Id",anchor=CENTER, width=80)
                        library.column("Name",anchor=CENTER,width=80)
                        library.column("Author",anchor=CENTER,width=80)
                        library.column("Publisher",anchor=CENTER,width=80)
                        library.column("Number_of_copies",anchor=CENTER,width=80)
                        library.column("Price",anchor=CENTER,width=80)
                        library.column("Genre",anchor=CENTER,width=80)


                        library.heading("#0",text="",anchor=CENTER)
                        library.heading("Id",text="Id",anchor=CENTER)
                        library.heading("Name",text="Name",anchor=CENTER)
                        library.heading("Author",text="Author",anchor=CENTER)
                        library.heading("Publisher",text="Publisher",anchor=CENTER)
                        library.heading("Number_of_copies",text="Number of copies",anchor=CENTER)
                        library.heading("Price",text="Price",anchor=CENTER)
                        library.heading("Genre",text="Genre",anchor=CENTER)

                        for i in data :        
                            library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
                        
                           
                        library.pack()
                        mainloop()
                    else:
                        messagebox.showerror('Publisher','ERROR ! NO SPECIAL CHARACTER ALLOWED' )
                        break
                        
                
                
            elif int(v2) == 4:
                for i in v3 : 
                    if str(i).isdigit():
                        query = 'update books set number_of_copies={} where id={}'
                        query = query.format(int(v3), int(v1))
                        curr.execute(query)
                        conn.commit()
                        query = 'select * from books where id = {}'
                        query = query.format(int(v1))
                        curr.execute(query)
                        data = curr.fetchall()

                        ws  = Tk()
                        ws.geometry('500x500')
                        ws.attributes('-fullscreen', True)
                        ws['bg'] = '#000000'
                        
                        lib_frame = Frame(ws)
                        lib_frame.pack()

                        library = ttk.Treeview(lib_frame)

                        library['columns'] = ('Id', 'Name', 'Author', 'Publisher', 'Number_of_copies','Price','Genre')

                        library.column("#0", width=0,  stretch=NO)
                        library.column("Id",anchor=CENTER, width=80)
                        library.column("Name",anchor=CENTER,width=80)
                        library.column("Author",anchor=CENTER,width=80)
                        library.column("Publisher",anchor=CENTER,width=80)
                        library.column("Number_of_copies",anchor=CENTER,width=80)
                        library.column("Price",anchor=CENTER,width=80)
                        library.column("Genre",anchor=CENTER,width=80)


                        library.heading("#0",text="",anchor=CENTER)
                        library.heading("Id",text="Id",anchor=CENTER)
                        library.heading("Name",text="Name",anchor=CENTER)
                        library.heading("Author",text="Author",anchor=CENTER)
                        library.heading("Publisher",text="Publisher",anchor=CENTER)
                        library.heading("Number_of_copies",text="Number of copies",anchor=CENTER)
                        library.heading("Price",text="Price",anchor=CENTER)
                        library.heading("Genre",text="Genre",anchor=CENTER)

                        for i in data :        
                            library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
                        
                           
                        library.pack()
                        mainloop()
                    else:
                        messagebox.showerror('Number_of_copies','ERROR ! NUMBER OF COPIES IS NOT INTEGER' )
                        break
                

            elif int(v2) == 5:
                for i in v3 : 
                    if str(i).isdigit():
                        query = 'update books set price="{}" where id={}'
                        query = query.format(v3, int(v1))
                        curr.execute(query)
                        conn.commit()
                        query = 'select * from books where id = {}'
                        query = query.format(int(v1))
                        curr.execute(query)
                        data = curr.fetchall()

                        ws  = Tk()
                        ws.geometry('500x500')
                        ws.attributes('-fullscreen', True)
                        ws['bg'] = '#000000'
                        
                        lib_frame = Frame(ws)
                        lib_frame.pack()

                        library = ttk.Treeview(lib_frame)

                        library['columns'] = ('Id', 'Name', 'Author', 'Publisher', 'Number_of_copies','Price','Genre')

                        library.column("#0", width=0,  stretch=NO)
                        library.column("Id",anchor=CENTER, width=80)
                        library.column("Name",anchor=CENTER,width=80)
                        library.column("Author",anchor=CENTER,width=80)
                        library.column("Publisher",anchor=CENTER,width=80)
                        library.column("Number_of_copies",anchor=CENTER,width=80)
                        library.column("Price",anchor=CENTER,width=80)
                        library.column("Genre",anchor=CENTER,width=80)


                        library.heading("#0",text="",anchor=CENTER)
                        library.heading("Id",text="Id",anchor=CENTER)
                        library.heading("Name",text="Name",anchor=CENTER)
                        library.heading("Author",text="Author",anchor=CENTER)
                        library.heading("Publisher",text="Publisher",anchor=CENTER)
                        library.heading("Number_of_copies",text="Number of copies",anchor=CENTER)
                        library.heading("Price",text="Price",anchor=CENTER)
                        library.heading("Genre",text="Genre",anchor=CENTER)

                        for i in data :        
                            library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
                        
                           
                        library.pack()
                        mainloop()
                    else:
                        messagebox.showerror('Price','ERROR ! PRICE IS NOT INTEGER' )
                        break
                    
                

            elif int(v2) == 6:
                for i in v3 :
                    if i.lower() in 'abcdefghijklmnopqrstuvwqxyz ':
                        query = 'update books set genre="{}" where id={}'
                        query = query.format(v3, int(v1))
                        curr.execute(query)
                        conn.commit()
                        query = 'select * from books where id = {}'
                        query = query.format(int(v1))
                        curr.execute(query)
                        data = curr.fetchall()

                        ws  = Tk()
                        ws.geometry('500x500')
                        ws.attributes('-fullscreen', True)
                        ws['bg'] = '#000000'
                        
                        lib_frame = Frame(ws)
                        lib_frame.pack()

                        library = ttk.Treeview(lib_frame)

                        library['columns'] = ('Id', 'Name', 'Author', 'Publisher', 'Number_of_copies','Price','Genre')

                        library.column("#0", width=0,  stretch=NO)
                        library.column("Id",anchor=CENTER, width=80)
                        library.column("Name",anchor=CENTER,width=80)
                        library.column("Author",anchor=CENTER,width=80)
                        library.column("Publisher",anchor=CENTER,width=80)
                        library.column("Number_of_copies",anchor=CENTER,width=80)
                        library.column("Price",anchor=CENTER,width=80)
                        library.column("Genre",anchor=CENTER,width=80)


                        library.heading("#0",text="",anchor=CENTER)
                        library.heading("Id",text="Id",anchor=CENTER)
                        library.heading("Name",text="Name",anchor=CENTER)
                        library.heading("Author",text="Author",anchor=CENTER)
                        library.heading("Publisher",text="Publisher",anchor=CENTER)
                        library.heading("Number_of_copies",text="Number of copies",anchor=CENTER)
                        library.heading("Price",text="Price",anchor=CENTER)
                        library.heading("Genre",text="Genre",anchor=CENTER)

                        for i in data :        
                            library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
                        
                           
                        library.pack()
                        mainloop()

                    else:
                        messagebox.showerror('Genre','ERROR ! NO SPECIAL CHARACTER ALLOWED' )
                        break
            

            
            else:

                messagebox.showinfo("Status",'The number entered is not in the given range of choices.')
        else:
             messagebox.showerror("Status",'Id entered does not exist in the database')
            




    master = Tk()
    idsearch = Label(master, text='Enter id to update the details').grid(row=0)
    Display = Label(master, text='''Enter one of the following numbers to change :
1. Name
2. Author
3. Publisher
4. Number of copies
5. Price
6. Genre''').grid(row=1)
    Newval = Label(master, text='Enter corresponding new value').grid(row=7)
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e1.grid(row=0, column = 1)
    e2.grid(row=1, column = 1)
    e3.grid(row=7, column = 1)

    button = Button(master, text="Update",command=assign)
    button.grid(row=9)
    button = Button(master, text="Display Database", command=display_books)
    button.grid(row=11)
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=14 , column=3)
    mainloop()

def delete_books():
    def assign():
        v = e1.get()
        query = 'SELECT * FROM books WHERE id = {}'
        query = query.format(int(v))
        curr.execute(query)
        data = curr.fetchone()

        if data:
            # ID exists, delete the record
            delete_query = 'DELETE FROM books WHERE id = {}'
            delete_query = delete_query.format(int(v))
            curr.execute(delete_query)
            conn.commit()
            messagebox.showinfo('Status', 'Successfully deleted.')
        else:
            # ID doesn't exist, show error message
            messagebox.showerror('Error', 'ID does not exist in the table.')



    master= Tk()
    L1 = Label(master, text='ID').grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0,column=1)
    button = Button(master, text="Delete", command=assign)
    button.grid(row=5)
    button = Button(master, text="Display", command=display_books)
    button.grid(row=7)
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=9, column=3)
    mainloop()

#ISSUED Button
def check():
    def assign_values():
        v1 = e1.get()
        query = 'select number_of_copies from books where id = {}'.format(v1)
        curr.execute(query)
        r = curr.fetchall()
        for i in r:
            if i[0] != 0:
                messagebox.showinfo("Status",'Book in stock')
                break
        else:
            messagebox.showinfo("Status",'Book not in stock')
    master = Tk()
    L1 = Label(master, text='Enter Book Id').grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0, column=1)
    button = Button(master, text="Check availability", command=assign_values)
    button.grid(row=7)
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=8, column=3)
    mainloop()

def add_issued() :
    combo_list = ['Returned','Not-returned']
    def assign_value1():
        global v1
        global v2
        v1 = e1.get()
        v2 = e2.get()
        v3 = e3.get()
        v4 = e4.get()
        v5 = e5.get()
        v6 = L61.get()
        v7 = e7.get()

        quer = 'select number_of_copies from books where id = {}'.format(int(v3))
        curr.execute(quer)
        r = curr.fetchone()
        print(r)

        if r == (0,):
            messagebox.showerror('Error', 'Book not in stock')

        elif v6 == 'Returned':
            messagebox.showerror('Error', "Check return status")

        else:
            query = 'update books set number_of_copies = number_of_copies - 1 where id = {}'.format(int(v3))
            curr.execute(query)
            conn.commit()
                            
            query = 'insert into issued values ({},"{}",{},"{}","{}","{}",{})'
            query1 = query.format(int(v1),v2,v3,v4,v5,v6,v7)
            curr.execute(query1)
            conn.commit()
    master = Tk()
    L1 = Label(master, text='User_Id').grid(row=0)
    L2 = Label(master, text='User_Name').grid(row=1)
    L3 = Label(master, text='Book_Id').grid(row=2)
    L4 = Label(master, text='Date_issued').grid(row=3)
    L5 = Label(master, text='Due_date').grid(row=4)
    L6 = Label(master, text='Return status').grid(row=5)
    L61 = ttk.Combobox(master, values = combo_list)
    L61.current(0)
    L61.grid(row=5,column=1,sticky="ew")
    L7 = Label(master, text='Penalty').grid(row=6)
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    def temp3(v):
        e4.delete(0,"end")
    e4.insert(0, "yyyy-mm-dd")
    e4.bind("<FocusIn>",temp3)
    e5 = Entry(master)
    def temp4(v):
        e5.delete(0,"end")
    e5.insert(0, "yyyy-mm-dd")
    e5.bind("<FocusIn>",temp4)
    e7 = Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    e7.grid(row=6, column=1)
    button = Button(master, text="Issue book", command=assign_value1)
    button.grid(row=7)
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=8, column=3)
    mainloop()

def return_status():
    combo_list = ['Returned','Not returned']
    def assign():
        v1 = e1.get()
        v2 = return1.get()
        v3 =e2.get()

        if v2 == 'Returned':
            query = 'update books set number_of_copies = number_of_copies + 1 where id = {}'.format(int(v3))
            curr.execute(query)
            conn.commit()
        else:
            messagebox.showinfo("Error",'Check return status')
            
        query = 'update issued set return_status = "{}" where user_Id={} and bookid={}'
        query1 = query.format(v2,int(v1), int(v3))
        curr.execute(query1)
        conn.commit()

    master = Tk()
    user_id = Label(master, text='Enter user Id').grid(row=0)
    book_id = Label(master, text='Enter book Id').grid(row=1)
    return1 = Label(master, text='Return status').grid(row=2)
    return1 = ttk.Combobox(master, values = combo_list)
    return1.current(0)
    return1.grid(row=2,column=1,sticky="ew")
    e1 = Entry(master)
    e1.grid(row=0, column=1)
    e2=Entry(master)
    e2.grid(row=1,column=1)

    button = Button(master, text="Update", command=assign)
    button.grid(row=3)
    button = Button(master, text='Close', command=master.destroy)
    button.grid(row=4, column=3)
    mainloop()
    
def penalty():
    def assign():
        v1 = e1.get()
        v2 = e2.get()
        v3 = e3.get()
        
        query = 'update issued set penalty = "{}" where user_Id={} and bookid={}'
        query = query.format(int(v3), int(v1), int(v2))
        curr.execute(query)
        conn.commit()

    master = Tk()
    id = Label(master, text='Enter user Id').grid(row=0)
    book_id=Label(master, text='Enter book Id').grid(row=1)
    date = Label(master, text='Enter updated penalty').grid(row=2)
    e1 = Entry(master)
    e2 = Entry(master)
    e3=Entry(master)
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    e3.grid(row=2, column=1)
    button = Button(master, text="Update",command=assign)
    button.grid(row=9)
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=14 , column=3)
    mainloop()


def display_members():
    ws  = Tk()
    ws.geometry('500x500')
    ws.attributes('-fullscreen', True)
    ws['bg'] = '#000000'

    lib_frame = Frame(ws)
    lib_frame.pack()

    library = ttk.Treeview(lib_frame, height=45)

    library['columns'] = ('Id', 'Name', 'Address', 'Phone_number', 'Interests')

    library.column("#0", width=0,  stretch=NO)
    library.column("Id",anchor=CENTER, width=80)
    library.column("Name",anchor=CENTER,width=80)
    library.column("Address",anchor=CENTER,width=80)
    library.column("Phone_number",anchor=CENTER,width=80)
    library.column("Interests",anchor=CENTER,width=80)


    library.heading("#0",text="",anchor=CENTER)
    library.heading("Id",text="Id",anchor=CENTER)
    library.heading("Name",text="Name",anchor=CENTER)
    library.heading("Address",text="Address",anchor=CENTER)
    library.heading("Phone_number",text="Phone number",anchor=CENTER)
    library.heading("Interests",text="Interests",anchor=CENTER)


    query = 'select * from members'
    curr.execute(query)
    data = curr.fetchall()
    for i in data :        
        library.insert(parent='',index='end',iid=data.index(i),text='', values=i)    
    library.pack()
    mainloop()

def add_members() :   
    def assign_value():
        global v1
        global v2
        v1 = e1.get()
        v2 = e2.get()
        v3 = e3.get()
        v4 = e4.get()
        v5 = e5.get()
        #MAKE EVERYTHING INT 
        x1 = True 
        x2 = True
        
        x4i = True
        x4ii= True
        x5 = True
        query = 'select Id from members'
        curr.execute(query)
        r = curr.fetchall()

        if (int(v1),) in r:
            messagebox.showerror('ID','ERROR ! ID ALREADY EXISTS' )
        else:
            for i in v1 :            
                if i.isdigit():
                    continue
                else:
                    messagebox.showerror('ID','ERROR ! ID IS NOT INTEGER' )                            
                    x1 = False
                    break      
            for i in v2 :
                if i.lower() in 'abcdefghijklmnopqrstuvwqxyz ':
                    continue
                else:
                    messagebox.showerror('Name','ERROR ! NO SPECIAL CHARACTER ALLOWED' )
                    
                    x2 = False
                    break

            
            for i in v4 :
                if i.isdigit():
                    if len(v4)==10 :
                        continue
                    else:
                        messagebox.showerror('Phone Number','ERROR! PHONE NUMBER CANNOT EXCEED 10 DIGITS' )
                        
                        x4i = False
                        break
                else:
                    messagebox.showerror('Phone Number','ERROR ! PHONE NUMBER IS NOT INTEGER' )
                    
                    x4ii = False
                    break
                    
            for i in v5 :
                if i.lower() in 'abcdefghijklmnopqrstuvwqxyz ':
                    continue
                else:
                    messagebox.showerror('Interests','ERROR ! NO SPECIAL CHARACTER ALLOWED' )
                    
                    x5 = False 
                    break  
            

               
            if (x1 == True) and (x2 == True) and (x4i == True) and (x4ii == True) and (x5 == True) : 
                query = 'insert into members values ({},"{}","{}","{}","{}")'
                query1 = query.format(v1,v2,v3,v4,v5)
                curr.execute(query1)
                conn.commit()
            else:
                pass
        
      
    master = Tk()
    L1 = Label(master, text='Id*').grid(row=0)
    L2 = Label(master, text='Name*').grid(row=1)
    L3 = Label(master, text='Address*').grid(row=2)
    L4 = Label(master, text='Phone number*').grid(row=3)
    L5 = Label(master, text='Interests').grid(row=4)
    e1 = Entry(master)
    def temp6(x):
        e1.delete(0,"end")
    e1.insert(0, "Format = 100x")
    e1.bind("<FocusIn>",temp6)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e5 = Entry(master)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)

    button = Button(master, text="Assign Value", command=assign_value)
    button.grid(row=6)
    button = Button(master, text="Display", command=display_members)
    button.grid(row=7)
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=8, column=3)
    mainloop()

def search_members():
    def assign_value():
        global v1
        global master
        v1 = e1.get()        
        query = 'select ID from members '
        query = query.format(v1)
        curr.execute(query)
        r = curr.fetchall()  
    
        if (int(v1),) in r:
            
            ws  = Tk()
            ws.geometry('500x500')
            ws.attributes('-fullscreen', True)
            ws['bg'] = '#000000'

            global master
            v1 = e1.get()
            query = 'select * from members where Id = {}'
            query = query.format(v1)
            curr.execute(query)
            data = curr.fetchall() 

            lib_frame = Frame(ws)
            lib_frame.pack()

            library = ttk.Treeview(lib_frame)

            library['columns'] = ('Id', 'Name', 'Address', 'Phone_number', 'Interests')

            library.column("#0", width=0,  stretch=NO)
            library.column("Id",anchor=CENTER, width=80)
            library.column("Name",anchor=CENTER,width=80)
            library.column("Address",anchor=CENTER,width=80)
            library.column("Phone_number",anchor=CENTER,width=80)
            library.column("Interests",anchor=CENTER,width=80)


            library.heading("#0",text="",anchor=CENTER)
            library.heading("Id",text="Id",anchor=CENTER)
            library.heading("Name",text="Name",anchor=CENTER)
            library.heading("Address",text="Address",anchor=CENTER)
            library.heading("Phone_number",text="Phone number",anchor=CENTER)
            library.heading("Interests",text="Interests",anchor=CENTER)


            for i in data :        
                library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
            
            
            library.pack()
            mainloop()
        else:
            messagebox.showerror('Error', 'ID does not exist in the table.')
        
    master = Tk()    
    L1 = Label(master, text='Search Element').grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0,column=1)
    button = Button(master, text="Search", command=assign_value)
    button.grid(row=5)    
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=7, column=3)
    mainloop()

def update_members():
    
    def assign():
        v1 = e1.get() #rollno
        v2 = e2.get() #menu
        v3 = e3.get() #value
        query = 'select Id from members'
        curr.execute(query)
        r = curr.fetchall()
        print(r)
        if (int(v1),) in r:
            if int(v2) == 1:
                for i in v3 :
                    if i.lower() in 'abcdefghijklmnopqrstuvwqxyz ':
                                    query = 'update members set Name="{}" where Id={}'
                                    query = query.format(v3, int(v1))
                                    curr.execute(query)
                                    conn.commit()

                                    query = 'select * from members where Id = {}'
                                    query = query.format(int(v1))
                                    curr.execute(query)
                                    data = curr.fetchall()

                                    ws  = Tk()
                                    ws.geometry('500x500')
                                    ws.attributes('-fullscreen', True)
                                    ws['bg'] = '#000000'
                                    
                                    lib_frame = Frame(ws)
                                    lib_frame.pack()

                                    library = ttk.Treeview(lib_frame)

                                    library['columns'] = ('Id', 'Name', 'Address', 'Phone_number', 'Interests')

                                    library.column("#0", width=0,  stretch=NO)
                                    library.column("Id",anchor=CENTER, width=80)
                                    library.column("Name",anchor=CENTER,width=80)
                                    library.column("Address",anchor=CENTER,width=80)
                                    library.column("Phone_number",anchor=CENTER,width=80)
                                    library.column("Interests",anchor=CENTER,width=80)


                                    library.heading("#0",text="",anchor=CENTER)
                                    library.heading("Id",text="Id",anchor=CENTER)
                                    library.heading("Name",text="Name",anchor=CENTER)
                                    library.heading("Address",text="Address",anchor=CENTER)
                                    library.heading("Phone_number",text="Phone number",anchor=CENTER)
                                    library.heading("Interests",text="Interests",anchor=CENTER)


                                    for i in data :        
                                        library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
                                    
                                    
                                    library.pack()
                                    mainloop()
                    else:
                        messagebox.showerror('Name','ERROR ! NO SPECIAL CHARACTER ALLOWED' )
                    
                        break
         
            elif int(v2) == 2:     
                    for i in v3 :
                        if i.lower() in 'abcdefghijklmnopqrstuvwqxyz #-,;:0123456789.':
                                        query = 'update members set address="{}" where id={}'
                                        query = query.format(v3, int(v1))
                                        curr.execute(query)
                                        conn.commit()

                                        query = 'select * from members where id = {}'
                                        query = query.format(int(v1))
                                        curr.execute(query)
                                        data = curr.fetchall()

                                        ws  = Tk()
                                        ws.geometry('500x500')
                                        ws.attributes('-fullscreen', True)
                                        ws['bg'] = '#000000'
                                        
                                        lib_frame = Frame(ws)
                                        lib_frame.pack()

                                        library = ttk.Treeview(lib_frame)

                                        library['columns'] = ('Id', 'Name', 'Address', 'Phone_number', 'Interests')

                                        library.column("#0", width=0,  stretch=NO)
                                        library.column("Id",anchor=CENTER, width=80)
                                        library.column("Name",anchor=CENTER,width=80)
                                        library.column("Address",anchor=CENTER,width=80)
                                        library.column("Phone_number",anchor=CENTER,width=80)
                                        library.column("Interests",anchor=CENTER,width=80)


                                        library.heading("#0",text="",anchor=CENTER)
                                        library.heading("Id",text="Id",anchor=CENTER)
                                        library.heading("Name",text="Name",anchor=CENTER)
                                        library.heading("Address",text="Address",anchor=CENTER)
                                        library.heading("Phone_number",text="Phone number",anchor=CENTER)
                                        library.heading("Interests",text="Interests",anchor=CENTER)

                                

                                        for i in data :        
                                            library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
                                        
                                        
                                        library.pack()
                                        mainloop()
                        else:
                            messagebox.showerror('Address','ERROR ! INVALID !' )
                            
                            
                            break       

        #CHECK Ph no. validation        
            elif int(v2) == 3:
                    for i in v3 :
                        if i.isdigit():
                            if len(v3)==10 :
                                            query = 'update members set phone_number="{}" where id={}'
                                            query = query.format(v3, int(v1))
                                            curr.execute(query)
                                            conn.commit()
                                            query = 'select * from members where id = {}'
                                            query = query.format(int(v1))
                                            curr.execute(query)
                                            data = curr.fetchall()

                                            ws  = Tk()
                                            ws.geometry('500x500')
                                            ws.attributes('-fullscreen', True)
                                            ws['bg'] = '#000000'
                                            
                                            lib_frame = Frame(ws)
                                            lib_frame.pack()

                                            library = ttk.Treeview(lib_frame)

                                            library['columns'] = ('Id', 'Name', 'Address', 'Phone_number', 'Interests')

                                            library.column("#0", width=0,  stretch=NO)
                                            library.column("Id",anchor=CENTER, width=80)
                                            library.column("Name",anchor=CENTER,width=80)
                                            library.column("Address",anchor=CENTER,width=80)
                                            library.column("Phone_number",anchor=CENTER,width=80)
                                            library.column("Interests",anchor=CENTER,width=80)


                                            library.heading("#0",text="",anchor=CENTER)
                                            library.heading("Id",text="Id",anchor=CENTER)
                                            library.heading("Name",text="Name",anchor=CENTER)
                                            library.heading("Address",text="Address",anchor=CENTER)
                                            library.heading("Phone_number",text="Phone number",anchor=CENTER)
                                            library.heading("Interests",text="Interests",anchor=CENTER)



                                            for i in data :        
                                                library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
                                            
                                            
                                            library.pack()
                                            mainloop()
                            else:
                                messagebox.showerror('Phone Number','ERROR! PHONE NUMBER CANNOT EXCEED 10 DIGITS' )
                                break
                        else:
                            messagebox.showerror('Phone Number','ERROR ! PHONE NUMBER IS NOT INTEGER' )
                            break
                                                    
            elif int(v2) == 4:
                    for i in v3 :
                        if i.lower() in 'abcdefghijklmnopqrstuvwqxyz ':
                                        query = 'update members set interests="{}" where id={}'
                                        query = query.format(v3, int(v1))
                                        curr.execute(query)
                                        conn.commit()
                                        query = 'select * from members where id = {}'
                                        query = query.format(int(v1))
                                        curr.execute(query)
                                        data = curr.fetchall()

                                        ws  = Tk()
                                        ws.geometry('500x500')
                                        ws.attributes('-fullscreen', True)
                                        ws['bg'] = '#000000'
                                        
                                        lib_frame = Frame(ws)
                                        lib_frame.pack()

                                        library = ttk.Treeview(lib_frame)

                                        library['columns'] = ('Id', 'Name', 'Address', 'Phone_number', 'Interests')

                                        library.column("#0", width=0,  stretch=NO)
                                        library.column("Id",anchor=CENTER, width=80)
                                        library.column("Name",anchor=CENTER,width=80)
                                        library.column("Address",anchor=CENTER,width=80)
                                        library.column("Phone_number",anchor=CENTER,width=80)
                                        library.column("Interests",anchor=CENTER,width=80)


                                        library.heading("#0",text="",anchor=CENTER)
                                        library.heading("Id",text="Id",anchor=CENTER)
                                        library.heading("Name",text="Name",anchor=CENTER)
                                        library.heading("Address",text="Address",anchor=CENTER)
                                        library.heading("Phone_number",text="Phone number",anchor=CENTER)
                                        library.heading("Interests",text="Interests",anchor=CENTER)



                                        for i in data :        
                                            library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
                                        
                                        
                                        library.pack()
                                        mainloop()
                        else:
                            messagebox.showerror('Interests','ERROR ! NO SPECIAL CHARACTER ALLOWED' )
                            
                            
                            break              

            else:
                messagebox.showinfo("Status",'The number entered is not in the given range of choices.')
        else:
            messagebox.showerror("Status",'Id entered does not exist in the database')



    master = Tk()
    idsearch = Label(master, text='Enter id to update the details').grid(row=0)
    Display = Label(master, text='''Enter one of the following numbers to change :
1. Name
2. Address
3. Phone number
4. Interests''').grid(row=1)
    Newval = Label(master, text='Enter corresponding new value').grid(row=7)
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e1.grid(row=0, column = 1)
    e2.grid(row=1, column = 1)
    e3.grid(row=7, column = 1)

    button = Button(master, text="Update",command=assign)
    button.grid(row=9)
    button = Button(master, text="Display Database", command=display_members)
    button.grid(row=11)
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=14 , column=3)
    mainloop()

def delete_members():
    def assign():
        v = e1.get()
        query = 'SELECT * FROM members WHERE id = {}'
        query = query.format(int(v))
        curr.execute(query)
        data = curr.fetchone()

        if data:
            # ID exists, delete the record
            delete_query = 'DELETE FROM members WHERE id = {}'
            delete_query = delete_query.format(int(v))
            curr.execute(delete_query)
            conn.commit()
            messagebox.showinfo('Status', 'Successfully deleted.')
        else:
            # ID doesn't exist, show error message
            messagebox.showerror('Error', 'ID does not exist in the table.')
    

    master= Tk()
    L1 = Label(master, text='ID').grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0,column=1)
    button = Button(master, text="Delete", command=assign)
    button.grid(row=5)
    button = Button(master, text="Display", command=display_members)
    button.grid(row=7)
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=9, column=3)
    mainloop()

#BORROWED BUTTON
def books_borrowed_members():
    def assign_value():
        global v1
        global master
        v1 = e1.get()
        query = 'select ID from members '
        query = query.format(v1)
        curr.execute(query)
        r = curr.fetchall()        
        if (int(v1),) in r:
            query = 'select user_id,user_name,bookid,date_issued,return_status from issued where user_Id = {}'
            query = query.format(v1)
            curr.execute(query)
            data = curr.fetchall()        

            ws  = Tk()
            ws.geometry('500x500')
            ws.attributes('-fullscreen', True)
            ws['bg'] = '#000000'

            lib_frame = Frame(ws)
            lib_frame.pack()

            library = ttk.Treeview(lib_frame)

            library['columns'] = ('User_Id', 'User_name', 'Bookid', 'Date_issued', 'Return_status')
            
            library.column("#0", width=0,  stretch=NO)
            library.column("User_Id",anchor=CENTER, width=80)
            library.column("User_name",anchor=CENTER,width=80)
            library.column("Bookid",anchor=CENTER,width=80)
            library.column("Date_issued",anchor=CENTER,width=80)
            library.column("Return_status",anchor=CENTER,width=80)


            library.heading("#0",text="",anchor=CENTER)
            library.heading("User_Id",text="User Id",anchor=CENTER)
            library.heading("User_name",text="User name",anchor=CENTER)
            library.heading("Bookid",text="Book Id",anchor=CENTER)
            library.heading("Date_issued",text="Date issued",anchor=CENTER)
            library.heading("Return_status",text="Return status",anchor=CENTER)


            for i in data :        
                library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
            library.pack()
            mainloop()
            
        else:
            messagebox.showerror('Error', 'ID does not exist in the table.')        
                
    
    master = Tk()
    L1 = Label(master, text='Enter user Id').grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0,column=1)
    button = Button(master, text="Get record", command=assign_value)
    button.grid(row=5)    
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=7, column=3)
    mainloop()



def display_non_members():
    ws  = Tk()
    ws.geometry('500x500')
    ws.attributes('-fullscreen', True)
    ws['bg'] = '#000000'

    lib_frame = Frame(ws)
    lib_frame.pack()

    library = ttk.Treeview(lib_frame, height=45)

    library['columns'] = ('Id', 'Name', 'Address', 'Phone_number', 'Entry_time','Exit_time')

    library.column("#0", width=0,  stretch=NO)
    library.column("Id",anchor=CENTER, width=80)
    library.column("Name",anchor=CENTER,width=80)
    library.column("Address",anchor=CENTER,width=80)
    library.column("Phone_number",anchor=CENTER,width=80)
    library.column("Entry_time",anchor=CENTER,width=80)
    library.column("Exit_time",anchor=CENTER,width=200)


    library.heading("#0",text="",anchor=CENTER)
    library.heading("Id",text="Id",anchor=CENTER)
    library.heading("Name",text="Name",anchor=CENTER)
    library.heading("Address",text="Address",anchor=CENTER)
    library.heading("Phone_number",text="Phone number",anchor=CENTER)
    library.heading("Entry_time",text="Entry time",anchor=CENTER)
    library.heading("Exit_time",text="Exit time",anchor=CENTER)


    query = 'select * from non_members'
    curr.execute(query)
    data = curr.fetchall()
    for i in data :        
        library.insert(parent='',index='end',iid=data.index(i),text='', values=i)    
    library.pack()
    mainloop()

def add_non_members() :   
    def assign_value():
        global v1
        global v2
        v1 = e1.get()
        v2 = e2.get()
        v3 = e3.get()
        v4 = e4.get()
        v5 = e5.get()
        v6 = e6.get()
        #MAKE EVERYTHING INT 
        x1 = True 
        x2 = True
        x4i = True
        x4ii= True
        x5 = True

            
        for i in v1 :            
            if i.isdigit():
                continue
            else:
                messagebox.showerror('ID','ERROR ! ID IS NOT INTEGER' )                            
                
                x1 = False
                break
              
        for i in v2 :
            if i.lower() in 'abcdefghijklmnopqrstuvwqxyz ':
                continue
            else:
                messagebox.showerror('Name','ERROR ! NO SPECIAL CHARACTER ALLOWED' )
                
                x2 = False
                break


        for i in v4 :
            if i.isdigit():
                if len(v4)==10 :
                    continue
                else:
                    messagebox.showerror('Phone Number','ERROR! PHONE NUMBER CANNOT EXCEED 10 DIGITS' )
                    
                    x4i = False
                    break
            else:
                messagebox.showerror('Phone Number','ERROR ! PHONE NUMBER IS NOT INTEGER' )
                
                x4ii = False
                break

               
        if (x1 == True) and (x2 == True) and (x4i == True) and (x4ii == True) : 
            query = 'insert into non_members values ({},"{}","{}","{}","{}", "{}")'
            query1 = query.format(v1,v2,v3,v4,v5, v6)
            curr.execute(query1)
            conn.commit()
        else:
            pass
        
      
    master = Tk()
    L1 = Label(master, text='Id*').grid(row=0)
    L2 = Label(master, text='Name*').grid(row=1)
    L3 = Label(master, text='Address*').grid(row=2)
    L4 = Label(master, text='Phone number*').grid(row=3)
    L5 = Label(master, text='Entry time*').grid(row=4)
    L6 = Label(master, text='Exit time*').grid(row=5)
    e1 = Entry(master)
    def temp7(p):
        e1.delete(0,"end")
    e1.insert(0, "Format = 200x")
    e1.bind("<FocusIn>",temp7)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e5 = Entry(master)
    def temp8(v):
        e5.delete(0,"end")
    e5.insert(0, "yyyy-mm-dd HH:MI:SS")
    e5.bind("<FocusIn>",temp8)
    e6 = Entry(master)
    def temp9(v):
        e6.delete(0,"end")
    e6.insert(0, "yyyy-mm-dd HH:MI:SS")
    e6.bind("<FocusIn>",temp9)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    e6.grid(row=5, column=1)

    button = Button(master, text="Assign Value", command=assign_value)
    button.grid(row=6)
    button = Button(master, text="Display", command=display_non_members)
    button.grid(row=7)
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=8, column=3)
    mainloop()

def search_non_members():
    def assign_value():
        global v1
        global master
        v1 = e1.get()
        query = 'select ID from non_members '
        query = query.format(v1)
        curr.execute(query)
        r = curr.fetchall()        
        if (int(v1),) in r:
            query = 'select * from non_members where Id = {}'
            query = query.format(v1)
            curr.execute(query)
            data = curr.fetchall()        

            ws  = Tk()
            ws.geometry('500x500')
            ws.attributes('-fullscreen', True)
            ws['bg'] = '#000000'

            lib_frame = Frame(ws)
            lib_frame.pack()

            library = ttk.Treeview(lib_frame)

            library['columns'] = ('Id', 'Name', 'Address', 'Phone_number', 'Entry_time','Exit_time')

            library.column("#0", width=0,  stretch=NO)
            library.column("Id",anchor=CENTER, width=80)
            library.column("Name",anchor=CENTER,width=80)
            library.column("Address",anchor=CENTER,width=80)
            library.column("Phone_number",anchor=CENTER,width=80)
            library.column("Entry_time",anchor=CENTER,width=80)
            library.column("Exit_time",anchor=CENTER,width=200)


            library.heading("#0",text="",anchor=CENTER)
            library.heading("Id",text="Id",anchor=CENTER)
            library.heading("Name",text="Name",anchor=CENTER)
            library.heading("Address",text="Address",anchor=CENTER)
            library.heading("Phone_number",text="Phone number",anchor=CENTER)
            library.heading("Entry_time",text="Entry time",anchor=CENTER)
            library.heading("Exit_time",text="Exit time",anchor=CENTER)
            for i in data :        
                library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
            
            
            library.pack()
            mainloop()
        else:
            messagebox.showerror('Error', 'ID does not exist in the table.')
        
    master = Tk()    
    L1 = Label(master, text='Search Element').grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0,column=1)
    button = Button(master, text="Search", command=assign_value)
    button.grid(row=5)    
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=7, column=3)
    mainloop()

def update_non_members():
    
    def assign():
        v1 = e1.get() #rollno
        v2 = e2.get() #menu
        v3 = e3.get() #value
        query = 'select Id from non_members '
        query = query.format(v1)
        curr.execute(query)
        r = curr.fetchall()
        if (int(v1),) in r:
            if int(v2) == 1:
                    for i in v3 :            
                        if i.lower() in 'abcdefghijklmnopqrstuvwqxyz ':
                                    query = 'update non_members set Name="{}" where Id={}'
                                    query = query.format(v3, int(v1))
                                    curr.execute(query)
                                    conn.commit()

                                    query = 'select * from non_members where Id = {}'
                                    query = query.format(int(v1))
                                    curr.execute(query)
                                    data = curr.fetchall()

                                    ws  = Tk()
                                    ws.geometry('500x500')
                                    ws.attributes('-fullscreen', True)
                                    ws['bg'] = '#000000'
                                            
                                    lib_frame = Frame(ws)
                                    lib_frame.pack()

                                    library = ttk.Treeview(lib_frame)

                                    library['columns'] = ('Id', 'Name', 'Address', 'Phone_number', 'Entry_time','Exit_time')

                                    library.column("#0", width=0,  stretch=NO)
                                    library.column("Id",anchor=CENTER, width=80)
                                    library.column("Name",anchor=CENTER,width=80)
                                    library.column("Address",anchor=CENTER,width=80)
                                    library.column("Phone_number",anchor=CENTER,width=80)
                                    library.column("Entry_time",anchor=CENTER,width=80)
                                    library.column("Exit_time",anchor=CENTER,width=200)


                                    library.heading("#0",text="",anchor=CENTER)
                                    library.heading("Id",text="Id",anchor=CENTER)
                                    library.heading("Name",text="Name",anchor=CENTER)
                                    library.heading("Address",text="Address",anchor=CENTER)
                                    library.heading("Phone_number",text="Phone number",anchor=CENTER)
                                    library.heading("Entry_time",text="Entry time",anchor=CENTER)
                                    library.heading("Exit_time",text="Exit time",anchor=CENTER)
                                    for i in data :        
                                            library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
                                            
                                            
                                    library.pack()
                                    mainloop()
                        else:
                            messagebox.showerror('Name','ERROR ! NO SPECIAL CHARACTER ALLOWED' )                            
                            break

            elif int(v2) == 2:
                    for i in v3 :
                        if i.lower() in 'abcdefghijklmnopqrstuvwqxyz #-,;:0123456789.':  
                                        query = 'update non_members set address="{}" where id={}'
                                        query = query.format(v3, int(v1))
                                        curr.execute(query)
                                        conn.commit()

                                        query = 'select * from non_members where id = {}'
                                        query = query.format(int(v1))
                                        curr.execute(query)
                                        data = curr.fetchall()

                                        ws  = Tk()
                                        ws.geometry('500x500')
                                        ws.attributes('-fullscreen', True)
                                        ws['bg'] = '#000000'
                                        
                                        lib_frame = Frame(ws)
                                        lib_frame.pack()

                                        library = ttk.Treeview(lib_frame)

                                        library['columns'] = ('Id', 'Name', 'Address', 'Phone_number', 'Entry_time','Exit_time')

                                        library.column("#0", width=0,  stretch=NO)
                                        library.column("Id",anchor=CENTER, width=80)
                                        library.column("Name",anchor=CENTER,width=80)
                                        library.column("Address",anchor=CENTER,width=80)
                                        library.column("Phone_number",anchor=CENTER,width=80)
                                        library.column("Entry_time",anchor=CENTER,width=80)
                                        library.column("Exit_time",anchor=CENTER,width=200)


                                        library.heading("#0",text="",anchor=CENTER)
                                        library.heading("Id",text="Id",anchor=CENTER)
                                        library.heading("Name",text="Name",anchor=CENTER)
                                        library.heading("Address",text="Address",anchor=CENTER)
                                        library.heading("Phone_number",text="Phone number",anchor=CENTER)
                                        library.heading("Entry_time",text="Entry time",anchor=CENTER)
                                        library.heading("Exit_time",text="Exit time",anchor=CENTER)

                                        for i in data :        
                                            library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
                                        
                                        
                                        library.pack()
                                        mainloop()
                        else:
                            messagebox.showerror('Address','ERROR ! Invalid!' )
                            break
   
            elif int(v2) == 3:
                    for i in v3 :
                        if i.isdigit():
                            if len(v3)==10 :
                                    query = 'update non_members set phone_number="{}" where id={}'
                                    query = query.format(v3, int(v1))
                                    curr.execute(query)
                                    conn.commit()
                                    query = 'select * from non_members where id = {}'
                                    query = query.format(int(v1))
                                    curr.execute(query)
                                    data = curr.fetchall()

                                    ws  = Tk()
                                    ws.geometry('500x500')
                                    ws.attributes('-fullscreen', True)
                                    ws['bg'] = '#000000'
                                    
                                    lib_frame = Frame(ws)
                                    lib_frame.pack()

                                    library = ttk.Treeview(lib_frame)

                                    library['columns'] = ('Id', 'Name', 'Address', 'Phone_number', 'Entry_time','Exit_time')

                                    library.column("#0", width=0,  stretch=NO)
                                    library.column("Id",anchor=CENTER, width=80)
                                    library.column("Name",anchor=CENTER,width=80)
                                    library.column("Address",anchor=CENTER,width=80)
                                    library.column("Phone_number",anchor=CENTER,width=80)
                                    library.column("Entry_time",anchor=CENTER,width=80)
                                    library.column("Exit_time",anchor=CENTER,width=200)


                                    library.heading("#0",text="",anchor=CENTER)
                                    library.heading("Id",text="Id",anchor=CENTER)
                                    library.heading("Name",text="Name",anchor=CENTER)
                                    library.heading("Address",text="Address",anchor=CENTER)
                                    library.heading("Phone_number",text="Phone number",anchor=CENTER)
                                    library.heading("Entry_time",text="Entry time",anchor=CENTER)
                                    library.heading("Exit_time",text="Exit time",anchor=CENTER)

                                    for i in data :        
                                        library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
                                    
                                    
                                    library.pack()
                                    mainloop()
                            else:
                                messagebox.showerror('Phone Number','ERROR! PHONE NUMBER CANNOT EXCEED 10 DIGITS' )
                                break
                        else:
                            messagebox.showerror('Phone Number','ERROR ! PHONE NUMBER IS NOT INTEGER' )                            
                            break              

                
            elif int(v2) == 4:            
                query = 'update non_members set entry_time="{}" where id={}'
                query = query.format(v3, int(v1))
                curr.execute(query)
                conn.commit()
                query = 'select * from non_members where id = {}'
                query = query.format(int(v1))
                curr.execute(query)
                data = curr.fetchall()

                ws  = Tk()
                ws.geometry('500x500')
                ws.attributes('-fullscreen', True)
                ws['bg'] = '#000000'
                
                lib_frame = Frame(ws)
                lib_frame.pack()

                library = ttk.Treeview(lib_frame)

                library['columns'] = ('Id', 'Name', 'Address', 'Phone_number', 'Entry_time','Exit_time')

                library.column("#0", width=0,  stretch=NO)
                library.column("Id",anchor=CENTER, width=80)
                library.column("Name",anchor=CENTER,width=80)
                library.column("Address",anchor=CENTER,width=80)
                library.column("Phone_number",anchor=CENTER,width=80)
                library.column("Entry_time",anchor=CENTER,width=80)
                library.column("Exit_time",anchor=CENTER,width=200)


                library.heading("#0",text="",anchor=CENTER)
                library.heading("Id",text="Id",anchor=CENTER)
                library.heading("Name",text="Name",anchor=CENTER)
                library.heading("Address",text="Address",anchor=CENTER)
                library.heading("Phone_number",text="Phone number",anchor=CENTER)
                library.heading("Entry_time",text="Entry time",anchor=CENTER)
                library.heading("Exit_time",text="Exit time",anchor=CENTER)

                for i in data :        
                    library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
                
                
                library.pack()
                mainloop()

            elif int(v2) == 5:            
                query = 'update non_members set exit_time="{}" where id={}'
                query = query.format(v3, int(v1))
                curr.execute(query)
                conn.commit()
                query = 'select * from exit_time where id = {}'
                query = query.format(int(v1))
                curr.execute(query)
                data = curr.fetchall()

                ws  = Tk()
                ws.geometry('500x500')
                ws.attributes('-fullscreen', True)
                ws['bg'] = '#000000'
                
                lib_frame = Frame(ws)
                lib_frame.pack()

                library = ttk.Treeview(lib_frame)

                library['columns'] = ('Id', 'Name', 'Address', 'Phone_number', 'Entry_time','Exit_time')

                library.column("#0", width=0,  stretch=NO)
                library.column("Id",anchor=CENTER, width=80)
                library.column("Name",anchor=CENTER,width=80)
                library.column("Address",anchor=CENTER,width=80)
                library.column("Phone_number",anchor=CENTER,width=80)
                library.column("Entry_time",anchor=CENTER,width=80)
                library.column("Exit_time",anchor=CENTER,width=200)


                library.heading("#0",text="",anchor=CENTER)
                library.heading("Id",text="Id",anchor=CENTER)
                library.heading("Name",text="Name",anchor=CENTER)
                library.heading("Address",text="Address",anchor=CENTER)
                library.heading("Phone_number",text="Phone number",anchor=CENTER)
                library.heading("Entry_time",text="Entry time",anchor=CENTER)
                library.heading("Exit_time",text="Exit time",anchor=CENTER)

                for i in data :        
                    library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
                
                
                library.pack()
                mainloop()
        
            else:
                messagebox.showinfo("Status",'The number entered is not in the given range of choices.')
        else:
            messagebox.showerror("Status",'Id entered does not exist in the database')



    master = Tk()
    idsearch = Label(master, text='Enter id to update the details').grid(row=0)
    Display = Label(master, text='''Enter one of the following numbers to change :
1. Name
2. Address
3. Phone number
4. Entry time
5. Exit time''').grid(row=1)
    Newval = Label(master, text='Enter corresponding new value').grid(row=7)
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e1.grid(row=0, column = 1)
    e2.grid(row=1, column = 1)
    e3.grid(row=7, column = 1)

    button = Button(master, text="Update",command=assign)
    button.grid(row=9)
    button = Button(master, text="Display Database", command=display_non_members)
    button.grid(row=11)
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=14 , column=3)
    mainloop()

def delete_non_members():
    def assign():
        v = e1.get()
        query = 'SELECT * FROM non_members WHERE id = {}'
        query = query.format(int(v))
        curr.execute(query)
        data = curr.fetchone()

        if data:
            # ID exists, delete the record
            delete_query = 'DELETE FROM non_members WHERE id = {}'
            delete_query = delete_query.format(int(v))
            curr.execute(delete_query)
            conn.commit()
            messagebox.showinfo('Status', 'Successfully deleted.')
        else:
            # ID doesn't exist, show error message
            messagebox.showerror('Error', 'ID does not exist in the table.')
    master= Tk()
    L1 = Label(master, text='ID').grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0,column=1)
    button = Button(master, text="Delete", command=assign)
    button.grid(row=5)
    button = Button(master, text="Display", command=display_non_members)
    button.grid(row=7)
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=9, column=3)
    mainloop()

def books_borrowed_non_members():
    def assign_value():
        global v1
        global master
        v1 = e1.get()
            
        query = 'select * from issued where user_Id = {}'
        query = query.format(v1)
        curr.execute(query)
        data = curr.fetchall()        

        ws  = Tk()
        ws.geometry('500x500')
        ws.attributes('-fullscreen', True)
        ws['bg'] = '#000000'

        lib_frame = Frame(ws)
        lib_frame.pack()

        library = ttk.Treeview(lib_frame)

        library['columns'] = ('User_Id', 'User_name', 'Book_id', 'Date_issued','Due_date','Return_status','Penalty')
        
        library.column("#0", width=0,  stretch=NO)
        library.column("User_Id",anchor=CENTER, width=80)
        library.column("User_name",anchor=CENTER,width=80)
        library.column("Book_id",anchor=CENTER,width=80)
        library.column("Date_issued",anchor=CENTER,width=80)
        library.column("Due_date",anchor=CENTER,width=80)
        library.column("Return_status",anchor=CENTER,width=80)
        library.column("Penalty",anchor=CENTER,width=80)



        library.heading("#0",text="",anchor=CENTER)
        library.heading("User_Id",text="User Id",anchor=CENTER)
        library.heading("User_name",text="User name",anchor=CENTER)
        library.heading("Book_id",text="Book Id",anchor=CENTER)
        library.heading("Date_issued",text="Date issued",anchor=CENTER)
        library.heading("Due_date",text="Due date",anchor=CENTER)
        library.heading("Return_status",text="Return status",anchor=CENTER)
        library.heading("Penalty",text="Penalty",anchor=CENTER)


        for i in data :        
            library.insert(parent='',index='end',iid=data.index(i),text='', values=i)
            
               
        library.pack()
        mainloop()

            
    master = Tk()
    L1 = Label(master, text='Enter user Id').grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0,column=1)
    button = Button(master, text="Get record", command=assign_value)
    button.grid(row=5)    
    button = Button(master, text="Close", command=master.destroy)
    button.grid(row=7, column=3)
    mainloop()




def open_issued_window():
    books_window = Toplevel(root)
    books_window.title("Issued")
    
    books_window.configure(bg="turquoise")
    Button(books_window, text="Check availability", width=15, height=2, font=("Times New Roman", 18), bg="#E91E63", fg="white",command=check).pack(pady=5)
    Button(books_window, text="Issue", width=15, height=2, font=("Times New Roman", 18), bg="#FF5722", fg="white",command=add_issued).pack(pady=5)
    Button(books_window, text="Return check", width=15, height=2, font=("Times New Roman", 18), bg="#4CAF50", fg="white",command=open_update_window).pack(pady=5)

def open_update_window():
    books_window = Toplevel(root)
    books_window.title("Return")
    
    books_window.configure(bg="turquoise")
    Button(books_window, text="Return status", width=15, height=2, font=("Times New Roman", 18), bg="#4CAF50", fg="white",command=return_status).grid(row=0, column=1, padx=10, pady=10)
    Button(books_window, text="Penalty", width=15, height=2, font=("Times New Roman", 18), bg="#E91E63", fg="white",command=penalty).grid(row=0, column=3, padx=10, pady=10)

def open_employees_window():
    employees_window = Toplevel(root)
    employees_window.title("Employees")
    employees_window.configure(bg="turquoise")
    Label(employees_window, text='Employees', font=("Papyrus", 20, 'bold'), bg='black', fg='white').pack(side=TOP, fill=BOTH, pady=10)
    rt_frame = Frame(employees_window, bg='turquoise')
    rt_frame.pack(side=LEFT, fill=Y, padx=20)
    # Buttons
    Button(rt_frame, text="Display", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white", command=display_employees).grid(row=0, column=1, padx=10, pady=10)
    Button(rt_frame, text="Add", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white", command=add_employees).grid(row=0, column=2, padx=10, pady=10)
    Button(rt_frame, text="Update", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white", command=update_employees).grid(row=1, column=1, padx=10, pady=10)
    Button(rt_frame, text="Delete", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white", command=delete_employees).grid(row=1, column=2, padx=10, pady=10)
    Button(rt_frame, text="Search", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white",command=search_employees).grid(row=0, column=3, padx=10, pady=10)
    Button(rt_frame, text='Exit', font=('Times New Roman', 14), bg='black', fg='white', width=10, command=employees_window.destroy).grid(row=1, column=7, padx=10, pady=10)
    
def open_books_window():
    books_window = Toplevel(root)
    books_window.title("Books")
    books_window.geometry('1900x1000')
    books_window.configure(bg="turquoise")  
    # Frames
    Label(books_window, text='Books', font=("Papyrus", 20, 'bold'), bg='black', fg='white').pack(side=TOP, fill=BOTH, pady=10)
    rt_frame = Frame(books_window, bg='turquoise')
    rt_frame.pack(side=LEFT, fill=Y, padx=20)
    # Buttons
    Button(rt_frame, text="Display", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white", command=display_books).grid(row=0, column=1, padx=10, pady=10)
    Button(rt_frame, text="Add", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white", command=add_books).grid(row=0, column=2, padx=10, pady=10)
    Button(rt_frame, text="Update", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white", command=update_books).grid(row=1, column=1, padx=10, pady=10)
    Button(rt_frame, text="Delete", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white", command=delete_books).grid(row=1, column=2, padx=10, pady=10)
    Button(rt_frame, text="Search", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white",command=search_books).grid(row=0, column=3, padx=10, pady=10)
    Button(rt_frame, text="Issued", width=25, height=10, font=("Times New Roman", 18), bg="#2196F3", fg="white",command=open_issued_window).grid(row=1, column=3, padx=10, pady=10)
    Button(rt_frame, text='Exit', font=('Times New Roman', 14), bg='black', fg='white', width=10, command=books_window.destroy).grid(row=7, column=7, padx=10, pady=10)

def open_members_window():
    members_window = Toplevel(root)
    members_window.title("Members")
    members_window.geometry('1900x1000')
    members_window.configure(bg="turquoise")
    Label(members_window, text='Members', font=("Papyrus", 20, 'bold'), bg='black', fg='white').pack(side=TOP, fill=BOTH, pady=10)
    rt_frame = Frame(members_window, bg='turquoise')
    rt_frame.pack(side=LEFT, fill=Y, padx=20)
    # Buttons
    Button(rt_frame, text="Display", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white", command=display_members).grid(row=0, column=1, padx=10, pady=10)
    Button(rt_frame, text="Add", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white", command=add_members).grid(row=0, column=2, padx=10, pady=10)
    Button(rt_frame, text="Update", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white", command=update_members).grid(row=1, column=1, padx=10, pady=10)
    Button(rt_frame, text="Delete", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white", command=delete_members).grid(row=1, column=2, padx=10, pady=10)
    Button(rt_frame, text="Search", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white",command=search_members).grid(row=0, column=3, padx=10, pady=10)
    Button(rt_frame, text="Books borrowed", width=25, height=10, font=("Times New Roman", 18), bg="#2196F3", fg="white",command=books_borrowed_members).grid(row=1, column=3, padx=10, pady=10)
    Button(rt_frame, text='Exit', font=('Times New Roman', 14), bg='black', fg='white', width=10, command=members_window.destroy).grid(row=2, column=4, padx=10, pady=10)


def open_nonmembers_window():
    nonmembers_window = Toplevel(root)
    nonmembers_window.title("Non-Members")
    nonmembers_window.geometry('1900x1000')
    nonmembers_window.configure(bg="turquoise")
    Label(nonmembers_window, text='Non-members', font=("Papyrus", 20, 'bold'), bg='black', fg='white').pack(side=TOP, fill=BOTH, pady=10)
    rt_frame = Frame(nonmembers_window, bg='turquoise')
    rt_frame.pack(side=LEFT, fill=Y, padx=20)
    # Buttons
    Button(rt_frame, text="Display", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white",command=display_non_members).grid(row=0, column=1, padx=10, pady=10)
    Button(rt_frame, text="Add", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white",command=add_non_members).grid(row=0, column=2, padx=10, pady=10)
    Button(rt_frame, text="Update", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white",
    command=update_non_members).grid(row=1, column=1, padx=10, pady=10)
    Button(rt_frame, text="Delete", width=25, height=10, font=("Times New Roman", 18), bg="black", fg="white",command=delete_non_members).grid(row=1, column=2, padx=10, pady=10)
    Button(rt_frame, text="Search", width=25, height=10, font=("Times New Roman", 18), bg="black",fg="white",command=search_non_members).grid(row=0, column=3,padx=10, pady=10)
    Button(rt_frame, text="Books borrowed", width=25,height=10, font=("Times New Roman", 18), bg="#2196F3",fg="white",command=books_borrowed_non_members).grid(row=1, column=3,
    padx=10, pady=10)
    Button(rt_frame, text='Exit', font=('Times New Roman', 14), bg='black', fg='white', width=10, command=nonmembers_window.destroy).grid(row=2, column=4, padx=10, pady=10)


def open_users_window():
    users_window = Toplevel(root)
    users_window.title("Users")
    users_window.geometry('1900x1000')
    users_window.configure(bg="turquoise")
    Label(users_window, text='USERS', font=("Papyrus", 20, 'bold'), bg='black', fg='white').pack(side=TOP, fill=BOTH, pady=10)
    rt_frame = Frame(users_window, bg='turquoise')
    rt_frame.pack(side=LEFT, fill=Y, padx=20)
    # Buttons
    Button(rt_frame, text="Members", width=28, height=7, font=("Times New Roman", 18), bg="black", fg="white", command=open_members_window).grid(row=0, column=1, padx=10, pady=10)
    Button(rt_frame, text="Non-members", width=28, height=7, font=("Times New Roman", 18), bg="black", fg="white", command=open_nonmembers_window).grid(row=0, column=3, padx=10, pady=110)
    Button(rt_frame, text='Exit', font=('Times New Roman', 14), bg='black', fg='white', width=10, command=users_window.destroy).grid(row=7, column=7, padx=10, pady=10)

        
root = Tk()
root.title("Library Management System")
root.geometry('1900x1000')
root.configure(bg='turquoise')

# Heading Label
Label(root, text='LIBRARY MANAGEMENT SYSTEM', font=("Papyrus", 20, 'bold'), bg='black', fg='white').pack(side=TOP, fill=BOTH, pady=10)

# Date Label
date_label = Label(root, text=f"{dt.datetime.now():%a, %b %d, %Y}", font=('Times New Roman', 14))
date_label.pack(padx=10, pady=5, anchor=NE)

# Frames
rt_frame = Frame(root, bg='turquoise')
rt_frame.pack(side=LEFT, fill=Y, padx=20)

# Buttons
Button(rt_frame, text='Employees', font=('Times New Roman', 14), bg='black', fg='white', width=15, command=open_employees_window).grid(row=0, column=1, padx=10, pady=10)
Button(rt_frame, text='Books', font=('Times New Roman', 14), bg='black', fg='white', width=15, command=open_books_window).grid(row=0, column=3, padx=10, pady=10)
Button(rt_frame, text='Users', font=('Times New Roman', 14), bg='black', fg='white', width=15, command=open_users_window).grid(row=0, column=5, padx=10, pady=10)
Button(rt_frame, text='Quit', font=('Times New Roman', 14), bg='black', fg='white', width=15, command=root.destroy).grid(row=3, column=7, padx=10, pady=10)

root.mainloop()
