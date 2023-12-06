from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3


class ConnectorDB:
    def __init__(self, root):
        self.root = root
        title = " "
        self.root.title(95 * title + "SQLite Connector")
        self.root.geometry("820x700+300+0")
        self.root.resizable(width=False, height=False)

        MainFrame = Frame(self.root, width=770, height=700, bd=10, relief=RIDGE, bg='cadet blue')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width=810, height=100, bd=7, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        TopFrame3 = Frame(MainFrame, width=770, height=500, bd=5, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, width=770, height=400, padx=2, bd=5, relief=RIDGE, bg='cadet blue')
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, width=750, height=180, padx=12, pady=9, bd=5, relief=RIDGE)
        LeftFrame1.pack(side=TOP)

        RightFrame1 = Frame(TopFrame3, width=100, height=400, padx=2, bd=5, relief=RIDGE, bg='cadet blue')
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, width=90, height=300, padx=2, pady=2, bd=5, relief=RIDGE)
        RightFrame1a.pack(side=TOP)
        # =============================================================================
        StudentID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Gender = StringVar()
        Mobile = StringVar()

        # =============================================================================
        def i_exit():
            i_xit = tkinter.messagebox.askyesno("SQLite Connection", "Confirm if you want to exit")
            if i_xit > 0:
                root.destroy()
                return

        def i_reset():
            self.ent_StudentID.delete(0, END)
            self.ent_Firstname.delete(0, END)
            self.ent_Surname.delete(0, END)
            self.txt_Address.delete(0, END)
            self.cbo_Gender.set("")
            self.ent_Mobile.delete(0, END)

        def i_submit():
            if StudentID.get() == "" or Firstname.get() == "" or Surname.get() == "":
                tkinter.messagebox.showinfo("SQLite Connection", "Please enter all the details")
            else:
                con = sqlite3.connect("trainee.db")
                cur = con.cursor()
                cur.execute("insert into train "
                            "(studentid,firstname, surname, address, gender, mobile)"
                            "VALUES (?,?,?,?, ?,?)",
                            (StudentID.get(),
                             Firstname.get(),
                             Surname.get(),
                             Address.get(),
                             Gender.get(),
                             Mobile.get(),))
                con.commit()
                con.close()
                tkinter.messagebox.showinfo("Data Entry Form", "Record Entered Successfully!")
                i_display()

        def i_display():
            con = sqlite3.connect("trainee.db")
            cur = con.cursor()
            cur.execute("select * from train")
            result = cur.fetchall()
            if len(result) != 0:
                self.student_records.delete(*self.student_records.get_children())
                for row in result:
                    self.student_records.insert('', END, values=row)
                con.commit()
                con.close()

        def trainee_info(ev):
            view_info = self.student_records.focus()
            learner_data = self.student_records.item(view_info)
            row = learner_data['values']
            StudentID.set(row[0])
            Firstname.set(row[1])
            Surname.set(row[2])
            Address.set(row[3])
            Gender.set(row[4])
            Mobile.set(row[5])

        def i_update():
            if StudentID.get() == "":
                tkinter.messagebox.showinfo("SQLite Connection", "Please enter all the details")
            else:
                con = sqlite3.connect("trainee.db")
                cur = con.cursor()
                cur.execute("update train set Firstname=?, Surname=?, Address=?, Gender=?, Mobile=? where StudentID=?",
                            (Firstname.get(),
                             Surname.get(),
                             Address.get(),
                             Gender.get(),
                             Mobile.get(),
                             StudentID.get()))
                con.commit()
                con.close()
                tkinter.messagebox.showinfo("Data Entry Form", "Record Updated Successfully!")
                i_display()

        def i_delete():
            if StudentID.get() == "":
                tkinter.messagebox.showinfo("SQLite Connection", "Please choose one!")
            else:
                con = sqlite3.connect("trainee.db")
                cur = con.cursor()
                cur.execute("delete from train where StudentID=?", (StudentID.get(),))
                con.commit()
                con.close()
                tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Deleted!")
                i_reset()
                i_display()

        def i_search():

            con = sqlite3.connect("trainee.db")
            cur = con.cursor()

            # 使用占位符来防止 SQL 注入
            cur.execute("SELECT * FROM train WHERE StudentID=?", (StudentID.get(),))

            # 仅获取一行记录
            row = cur.fetchone()

            if row:
                # 将查询结果设置给各个变量
                StudentID.set(row[0])
                Firstname.set(row[1])
                Surname.set(row[2])
                Address.set(row[3])
                Gender.set(row[4])
                Mobile.set(row[5])
            else:
                tkinter.messagebox.showinfo("Data Entry Form", "No Such Record Exists!")
                i_reset()

            con.close()

        # =============================================================================

        self.lbl_title = Label(TitleFrame, text="SQLite Connection", font=('arial', 40, 'bold'), bd=9)
        self.lbl_title.grid(row=0, column=0, padx=148)

        self.lbl_StudentID = Label(LeftFrame1, text="Student ID", font=('arial', 12, 'bold'), bd=7)
        self.lbl_StudentID.grid(row=1, column=0, padx=5, sticky=W)
        self.ent_StudentID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                   textvariable=StudentID)
        self.ent_StudentID.grid(row=1, column=1, padx=5, sticky=W)

        self.lbl_Firstname = Label(LeftFrame1, text="Firstname", font=('arial', 12, 'bold'), bd=7)
        self.lbl_Firstname.grid(row=2, column=0, padx=5, sticky=W)
        self.ent_Firstname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                   textvariable=Firstname)
        self.ent_Firstname.grid(row=2, column=1, padx=5, sticky=W)

        self.lbl_Surname = Label(LeftFrame1, text="Surname", font=('arial', 12, 'bold'), bd=7)
        self.lbl_Surname.grid(row=3, column=0, padx=5, sticky=W)
        self.ent_Surname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                 textvariable=Surname)
        self.ent_Surname.grid(row=3, column=1, padx=5, sticky=W)

        self.lbl_Address = Label(LeftFrame1, text="Address", font=('arial', 12, 'bold'), bd=7)
        self.lbl_Address.grid(row=4, column=0, padx=5, sticky=W)
        self.txt_Address = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                 textvariable=Address)
        self.txt_Address.grid(row=4, column=1, padx=5, sticky=W)

        self.lbl_Gender = Label(LeftFrame1, text="Gender", font=('arial', 12, 'bold'), bd=7)
        self.lbl_Gender.grid(row=5, column=0, padx=5, sticky=W)
        self.cbo_Gender = ttk.Combobox(LeftFrame1, font=('arial', 12, 'bold'), state='readonly', width=42,
                                       textvariable=Gender)
        self.cbo_Gender['values'] = (' ', 'Female', 'Male')
        self.cbo_Gender.current(0)
        self.cbo_Gender.grid(row=5, column=1)

        self.lbl_Mobile = Label(LeftFrame1, text="Mobile", font=('arial', 12, 'bold'), bd=7)
        self.lbl_Mobile.grid(row=6, column=0, padx=5, sticky=W)
        self.ent_Mobile = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                textvariable=Mobile)
        self.ent_Mobile.grid(row=6, column=1, padx=5, sticky=W)
        # ====================================Table Treeview=========================================
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        self.student_records = ttk.Treeview(LeftFrame, height=14, columns=(
            "Student ID", "Firstname", "Surname", "Address", "Gender", "Mobile"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_records.heading("Student ID", text="Student ID")
        self.student_records.heading("Firstname", text="Firstname")
        self.student_records.heading("Surname", text="Surname")
        self.student_records.heading("Address", text="Address")
        self.student_records.heading("Gender", text="Gender")
        self.student_records.heading("Mobile", text="Mobile")

        self.student_records['show'] = 'headings'

        self.student_records.column("Student ID", width=70)
        self.student_records.column("Firstname", width=100)
        self.student_records.column("Surname", width=100)
        self.student_records.column("Address", width=100)
        self.student_records.column("Gender", width=100)
        self.student_records.column("Mobile", width=100)

        self.student_records.pack(fill=BOTH, expand=1)
        self.student_records.bind("<ButtonRelease-1>", trainee_info)
        # =============================================================================
        self.btnAddNew = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Add New", bd=4, pady=1, padx=24,
                                width=8, height=2, command=i_submit)
        self.btnAddNew.grid(row=0, column=0, padx=1)
        self.btnDisplay = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                 width=8, height=2, command=i_display)
        self.btnDisplay.grid(row=1, column=0, padx=1)
        self.btnUpdate = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24,
                                width=8, height=2, command=i_update)
        self.btnUpdate.grid(row=2, column=0, padx=1)
        self.btnDelete = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24,
                                width=8, height=2, command=i_delete)
        self.btnDelete.grid(row=3, column=0, padx=1)
        self.btnSearch = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24,
                                width=8, height=2, command=i_search)
        self.btnSearch.grid(row=4, column=0, padx=1)
        self.btnReset = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24,
                               width=8, height=2, command=i_reset)
        self.btnReset.grid(row=5, column=0, padx=1)
        self.btnExit = Button(RightFrame1a, font=('arial', 16, 'bold'), text="Exit", bd=4, pady=1, padx=24,
                              width=8, height=2, command=i_exit)
        self.btnExit.grid(row=6, column=0, padx=1)
        # =============================================================================


if __name__ == '__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()
