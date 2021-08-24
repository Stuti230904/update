import tkinter
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

screen = tk.Tk()
screen.title("High Scores")
screen.configure(background="black")
screen.iconbitmap("icon.ico")
screen.geometry("600x400")


def close1():
    screen.destroy()


mycur = mysql.connector.connect(
    host="localhost",
    user="root",
    password="stuti23", )
cur = mycur.cursor()

databases = ("SHOW DATABASES")
cur.execute(databases)
L = []
for (databases) in cur:
    L.append(databases[0])
if "game_data_7" in L:
    cur.execute("USE game_data_7")

else:
    print("No Leaderboard exists yet")
    close1()


def setup(rows):
    for i in rows:
        trv.insert("", 'end', values=i)


def clear():
    cur.execute("DROP DATABASE game_data_7")


def admin():
    def submit():
        user = Username.get()
        pwd = Password.get()

        def close():
            new_screen.destroy()
            Username.delete(0, 'end')
            Password.delete(0, 'end')

        def clear():
            cur.execute("DROP TABLE SCORES")
            cur.execute("CREATE TABLE Scores (UserName VARCHAR(50), Score INTEGER(5), Date date)")
            close()

        def add():
            def close3():
                add_screen.destroy()

            def submit2():
                user = Username.get()
                scor = Score1.get()
                dat = Date.get()

                if user is not "" and scor is not "" and dat is not "":
                    cur.execute("USE game_data_7")
                    cur.execute("select UserName from scores")
                    data = ()
                    for i in cur:
                        data += i
                    if user in data:
                        def close6():
                            new_screen.destroy()
                            Username.delete(0, 'end')
                            Score1.delete(0, 'end')
                            Date.delete(0, 'end')

                        new_screen = tk.Tk()
                        new_screen.title("Add")
                        new_screen.configure(background="white")
                        new_screen.iconbitmap("icon.ico")
                        new_screen.geometry("200x200")
                        Label(new_screen, width="300", text="Username already exists\n Use update option instead",
                              fg="black", bg="orange").pack(pady=25)
                        okbtn = Button(new_screen, text="OK", bg='red', command=close6)
                        okbtn.pack()
                        new_screen.mainloop()
                    else:
                        statement = "INSERT INTO Scores VALUES (%s, %s, %s)"
                        data = user, scor, dat
                        cur.execute(statement, data)
                        mycur.commit()
                        close3()
                else:
                    def close6():
                        new_screen.destroy()
                        Username.delete(0, 'end')
                        Score1.delete(0, 'end')
                        Date.delete(0, 'end')

                    new_screen = tk.Tk()
                    new_screen.title("Invalid Entry")
                    new_screen.configure(background="white")
                    new_screen.iconbitmap("icon.ico")
                    new_screen.geometry("200x200")
                    Label(new_screen, width="300", text="All the fields are mandatory\n Enter values again",
                          fg="black", bg="orange").pack(pady=25)
                    okbtn = Button(new_screen, text="OK", bg='red', command=close6)
                    okbtn.pack()
                    new_screen.mainloop()

            add_screen = tk.Tk()
            add_screen.title("Login")
            add_screen.configure(background="white")
            add_screen.iconbitmap("icon.ico")
            add_screen.geometry("400x400")
            global Username
            global Score1
            global Date
            Label(add_screen, width="300", text="Please enter details below", bg="orange", fg="white").pack()
            lbl1 = tk.Label(add_screen, text="Username: ", )
            lbl1.place(x=50, y=40)
            Username = tk.Entry(add_screen, width=100)
            Username.place(x=150, y=40, width=200)
            lbl2 = tk.Label(add_screen, text="Score: ")
            lbl2.place(x=50, y=70)
            Score1 = tk.Entry(add_screen, width=100)
            Score1.place(x=150, y=70, width=200)
            lbl3 = tk.Label(add_screen, text="Date: ")
            lbl3.place(x=50, y=100)
            Date = tk.Entry(add_screen, width=100)
            Date.place(x=150, y=100, width=200)
            submitbtn = tk.Button(add_screen, text="Add", bg='orange', command=submit2)
            submitbtn.place(x=100, y=165, width=55)
            closebtn = tk.Button(add_screen, text="Close", bg='orange', command=close3)
            closebtn.place(x=200, y=165, width=55)
            add_screen.mainloop()
            close3()

        def remove():
            def close5():
                screen2.destroy()

            def submit3():
                user = Username.get()
                if user is not "":
                    cur.execute("USE game_data_7")
                    users = ("SELECT Username from Scores")
                    cur.execute(users)
                    L = []
                    for users in cur:
                        L.append(users[0])

                    if user in L:
                        cur.execute("USE game_data_7")
                        cur.execute("DELETE FROM Scores WHERE Username=%s", (user,))
                        mycur.commit()
                        close5()

                    else:
                        def close6():
                            new_screen.destroy()
                            Username.delete(0, 'end')

                        new_screen = tk.Tk()
                        new_screen.title("Remove")
                        new_screen.configure(background="white")
                        new_screen.iconbitmap("icon.ico")
                        new_screen.geometry("200x200")
                        Label(new_screen, width="300", text="Username not \n found in leaderboard", fg="black",
                              bg="orange").pack(pady=25)
                        okbtn = Button(new_screen, text="OK", bg='red', command=close6)
                        okbtn.pack()
                        new_screen.mainloop()
                else:
                    def close6():
                        new_screen.destroy()
                        Username.delete(0, 'end')

                    new_screen = tk.Tk()
                    new_screen.title("Invalid Entry")
                    new_screen.configure(background="white")
                    new_screen.iconbitmap("icon.ico")
                    new_screen.geometry("200x200")
                    Label(new_screen, width="300", text="All the fields are mandatory\n Enter values again",
                          fg="black", bg="orange").pack(pady=25)
                    okbtn = Button(new_screen, text="OK", bg='red', command=close6)
                    okbtn.pack()
                    new_screen.mainloop()

            screen2 = tk.Tk()
            screen2.title("Remove")
            screen2.configure(background="white")
            screen2.iconbitmap("icon.ico")
            screen2.geometry("400x200")
            global Username
            Label(screen2, width="300", text="Please enter Username below", bg="orange", fg="white").pack()
            Username = tk.Entry(screen2, width=100)
            Username.place(x=90, y=40, width=200)
            rmvbtn = tk.Button(screen2, text="Remove", bg='orange', command=submit3)
            rmvbtn.place(x=100, y=85, width=70)
            closebtn = tk.Button(screen2, text="Close", bg='orange', command=close5)
            closebtn.place(x=200, y=85, width=70)
            screen2.mainloop()
            close5()

        def update():
            def close3():
                update_screen.destroy()

            def submit2():
                user = Username.get()
                scor = Score1.get()
                dat = Date.get()
                if user is not "" and scor is not "" and dat is not "":
                    cur.execute("USE game_data_7")
                    cur.execute("select UserName from scores")
                    data = ()
                    for i in cur:
                        data += i
                    if user not in data:
                        def close6():
                            new_screen.destroy()
                            Username.delete(0, 'end')
                            Score1.delete(0, 'end')
                            Date.delete(0, 'end')

                        new_screen = tk.Tk()
                        new_screen.title("Update")
                        new_screen.configure(background="white")
                        new_screen.iconbitmap("icon.ico")
                        new_screen.geometry("200x200")
                        Label(new_screen, width="300", text="Username doesn't exists\n Use add option instead",
                              fg="black", bg="orange").pack(pady=25)
                        okbtn = Button(new_screen, text="OK", bg='red', command=close6)
                        okbtn.pack()
                        new_screen.mainloop()
                    else:
                        statement = "Update Scores set score= %s, date=%s where username=%s"
                        data = scor, dat, user
                        cur.execute(statement, data)
                        mycur.commit()
                        close3()

                else:
                    def close6():
                        new_screen.destroy()
                        Username.delete(0, 'end')
                        Score1.delete(0, 'end')
                        Date.delete(0, 'end')

                    new_screen = tk.Tk()
                    new_screen.title("Invalid Entry")
                    new_screen.configure(background="white")
                    new_screen.iconbitmap("icon.ico")
                    new_screen.geometry("200x200")
                    Label(new_screen, width="300", text="All the fields are mandatory\n Enter values again",
                          fg="black", bg="orange").pack(pady=25)
                    okbtn = Button(new_screen, text="OK", bg='red', command=close6)
                    okbtn.pack()
                    new_screen.mainloop()

            update_screen = tk.Tk()
            update_screen.title("Login")
            update_screen.configure(background="white")
            update_screen.iconbitmap("icon.ico")
            update_screen.geometry("400x400")
            global Username
            global Score1
            global Date
            Label(update_screen, width="300", text="Please enter details below", bg="orange", fg="white").pack()
            lbl1 = tk.Label(update_screen, text="Username: ", )
            lbl1.place(x=50, y=40)
            Username = tk.Entry(update_screen, width=100)
            Username.place(x=150, y=40, width=200)
            lbl2 = tk.Label(update_screen, text="Score: ")
            lbl2.place(x=50, y=70)
            Score1 = tk.Entry(update_screen, width=100)
            Score1.place(x=150, y=70, width=200)
            lbl3 = tk.Label(update_screen, text="Date: ")
            lbl3.place(x=50, y=100)
            Date = tk.Entry(update_screen, width=100)
            Date.place(x=150, y=100, width=200)
            submitbtn = tk.Button(update_screen, text="Add", bg='orange', command=submit2)
            submitbtn.place(x=100, y=165, width=55)
            closebtn = tk.Button(update_screen, text="Close", bg='orange', command=close3)
            closebtn.place(x=200, y=165, width=55)
            update_screen.mainloop()
            close3()

        if user == "":
            new_screen = tk.Tk()
            new_screen.title("Login")
            new_screen.configure(background="white")
            new_screen.iconbitmap("icon.ico")
            new_screen.geometry("200x200")
            Label(new_screen, width="300", text="Username cannot \n be left blank", fg="black", bg="orange").pack(
                pady=25)
            okbtn = Button(new_screen, text="OK", bg='red', command=close)
            okbtn.pack()
            new_screen.mainloop()
        elif pwd == "":
            new_screen = tk.Tk()
            new_screen.title("Login")
            new_screen.configure(background="white")
            new_screen.iconbitmap("icon.ico")
            new_screen.geometry("200x200")
            Label(new_screen, width="300", text=" Please enter \n the password", fg="black", bg="orange").pack(pady=25)
            okbtn = Button(new_screen, text="OK", bg='red', command=close)
            okbtn.pack()
            new_screen.mainloop()
        else:
            if user == "admin" and pwd == "admin123":
                new_screen = tk.Tk()
                new_screen.title("Admin Screen")
                new_screen.configure(background="white")
                new_screen.iconbitmap("icon.ico")
                new_screen.geometry("400x400")
                Label(new_screen, width="300", text="Welcome Admin", fg="black", bg='orange').pack(pady=15)
                clrbtn = Button(new_screen, text="Clear Leaderboard", command=clear)
                clrbtn.pack(pady=12)
                addbtn = Button(new_screen, text="Add an entry on the leaderboard", command=add)
                addbtn.pack(pady=12)
                removebtn = Button(new_screen, text="Remove an entry from the leaderboard", command=remove)
                removebtn.pack(pady=12)
                updbtn = Button(new_screen, text="Update an already existing entry on the leaderboard", command=update)
                updbtn.pack(pady=12)
                quitbtn = Button(new_screen, text="Log out", command=close)
                quitbtn.pack(pady=12)
                new_screen.mainloop()
            else:
                new_screen = tk.Tk()
                new_screen.title("Login")
                new_screen.configure(background="white")
                new_screen.iconbitmap("icon.ico")
                new_screen.geometry("200x200")
                Label(new_screen, width="300", text="Invalid credentials \n Try Again", fg="black", bg="orange").pack(
                    pady=25)
                okbtn = Button(new_screen, text="OK", bg='red', command=close)
                okbtn.pack()
                new_screen.mainloop()

    def close2():
        close_screen.destroy()
        screen.destroy()

    close_screen = tk.Tk()
    close_screen.title("Login")
    close_screen.configure(background="white")
    close_screen.iconbitmap("icon.ico")
    close_screen.geometry("400x400")
    global Username
    global Password

    Label(close_screen, width="300", text="Please enter details below", bg="orange", fg="white").pack()
    lbl1 = tk.Label(close_screen, text="Username: ", )
    lbl1.place(x=50, y=40)

    Username = tk.Entry(close_screen, width=100)
    Username.place(x=150, y=40, width=200)

    lbl2 = tk.Label(close_screen, text="Password: ")
    lbl2.place(x=50, y=70)

    Password = tk.Entry(close_screen, width=100, show='*')
    Password.place(x=150, y=70, width=200)

    def show():
        Password.configure(show='')

        def hide():
            Password.configure(show='*')
            pwdtogglebtn.configure(text="Show password", command=show)

        pwdtogglebtn.configure(text="Hide password", command=hide)

    submitbtn = tk.Button(close_screen, text="Login", bg='orange', command=submit)
    submitbtn.place(x=125, y=155, width=55)

    closebtn = tk.Button(close_screen, text="Close", bg='orange', command=close2)
    closebtn.place(x=225, y=155, width=55)

    pwdtogglebtn = tk.Button(close_screen, text="Show password", command=show)
    pwdtogglebtn.place(x=160, y=105, width=90)

    close_screen.mainloop()


wrapper1 = LabelFrame(screen, text="Leaderboard", bg="brown", fg="black", height=4, width=10)
wrapper2 = LabelFrame(screen, text="Clear")
wrapper1.pack(fill='both', padx=20, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1, 2, 3), show='headings', height='6')
trv.pack()

trv.heading(1, text="UserName")
trv.heading(2, text="Score")
trv.heading(3, text="Date")

cur.execute("SELECT * FROM Scores ORDER BY Score DESC")
rows = cur.fetchall()
setup(rows)

cbtn = Button(screen, text="Close", command=close1, bg='orange', width=10, height=2)
cbtn.place(x=350, y=200)

cbtn2 = Button(screen, text="Admin Mode", command=admin, bg='orange', width=10, height=2)
cbtn2.place(x=160, y=200)

screen.mainloop()
