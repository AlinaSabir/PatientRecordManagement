from tkcalendar import Calendar, DateEntry
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.ttk as ttk


import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pakistani1")

db_cursor = db_connection.cursor(buffered=True)  
class PatientApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Patient Record Management System")
        self.geometry("800x650+351+174")
        self.lblTitle = tk.Label(self, text="Patient Record Management System", font=("Helvetica", 12), bg="pink", fg="green")
        self.lblFName = tk.Label(self, text="Enter FirstName:", font=("Helvetica", 10), bg="purple", fg="pink")
        self.lblLName = tk.Label(self, text="Enter LastName:", font=("Helvetica", 10), bg="purple", fg="pink")
        self.lblContactNo = tk.Label(self, text="Enter Contact No:", font=("Helvetica", 10), bg="purple", fg="pink")
        self.lblCity = tk.Label(self, text="Enter City:", font=("Helvetica", 10), bg="purple", fg="pink")
        self.lbldisease = tk.Label(self, text="Disease:", font=("Helvetica", 10), bg="purple", fg="pink")
        self.lblDOB = tk.Label(self, text="Choose Date of Birth:", font=("Helvetica", 10), bg="purple", fg="pink")
        self.lblSelect = tk.Label(self, text="Please select one record below to update or delete", font=("Helvetica", 10), bg="purple", fg="pink")
        self.lblSearch = tk.Label(self, text="Please Enter Patient ID:",font=("Helvetica", 10), bg="purple", fg="pink")

        self.entFName = tk.Entry(self)
        self.entLName = tk.Entry(self)
        self.entContact = tk.Entry(self)
        self.entCity = tk.Entry(self)
        self.entdisease = tk.Entry(self)
        self.calDOB = DateEntry(self, width=12, background='darkblue',
                    foreground='white', borderwidth=2, year=1950,locale='en_US', date_pattern='y-mm-dd')

        self.entSearch = tk.Entry(self)


        self.btn_register = tk.Button(self, text="CREATE", font=("Helvetica", 11), bg="pink", fg="blue",
                                      command=self.register_patient)
        self.btn_update = tk.Button(self,text="Update",font=("Helvetica",11),bg="pink", fg="blue",command=self.update_patient_data)
        self.btn_delete = tk.Button(self, text="Delete", font=("Helvetica", 11), bg="pink", fg="blue",
                                    command=self.delete_patient_data)
        self.btn_clear = tk.Button(self, text="Clear", font=("Helvetica", 11), bg="pink", fg="blue",
                                    command=self.clear_form)
        self.btn_show_all = tk.Button(self, text="READ ALL", font=("Helvetica", 11), bg="pink", fg="blue",
                                   command=self.load_patient_data)
        self.btn_search = tk.Button(self, text="Search", font=("Helvetica", 11), bg="pink", fg="blue",
                                   command=self.show_search_record)
        self.btn_exit = tk.Button(self, text="Exit", font=("Helvetica", 16), bg="pink", fg="blue",command=self.exit)

        columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7")
        self.tvpatient= ttk.Treeview(self,show="headings",height="5", columns=columns)
        self.tvpatient.heading('#1', text='idno', anchor='center')
        self.tvpatient.column('#1', width=60, anchor='center', stretch=False)
        self.tvpatient.heading('#2', text='FirstName', anchor='center')
        self.tvpatient.column('#2', width=10, anchor='center', stretch=True)
        self.tvpatient.heading('#3', text='LastName', anchor='center')
        self.tvpatient.column('#3',width=10, anchor='center', stretch=True)
        self.tvpatient.heading('#4', text='City', anchor='center')
        self.tvpatient.column('#4',width=10, anchor='center', stretch=True)
        self.tvpatient.heading('#5', text='Disease', anchor='center')
        self.tvpatient.column('#5',width=10, anchor='center', stretch=True)
        self.tvpatient.heading('#6', text='PhoneNumber', anchor='center')
        self.tvpatient.column('#6', width=10, anchor='center', stretch=True)
        self.tvpatient.heading('#7', text='Date of Birth', anchor='center')
        self.tvpatient.column('#7', width=10, anchor='center', stretch=True)

        vsb= ttk.Scrollbar(self, orient=tk.VERTICAL,command=self.tvpatient.yview)
        vsb.place(x=40 + 640 + 1, y=310, height=180 + 20)
        self.tvpatient.configure(yscroll=vsb.set)
        hsb = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.tvpatient.xview)
        hsb.place(x=40 , y=310+200+1, width=620 + 20)
        self.tvpatient.configure(xscroll=hsb.set)
        self.tvpatient.bind("<<TreeviewSelect>>", self.show_selected_record)

        self.lblTitle.place(x=280, y=30,  height=27, width=300)
        self.lblFName.place(x=175, y=70,  height=23, width=100)
        self.lblLName.place(x=175, y=100,  height=23, width=100)
        self.lblContactNo.place(x=171, y=129,  height=23, width=104)
        self.lblCity.place(x=210, y=158,  height=23, width=65)
        self.lbldisease.place(x=205, y=187,  height=23, width=71)
        self.lblDOB.place(x=148, y=217, height=23, width=128)
        self.lblSelect.place(x=150, y=280, height=23, width=400)
        self.lblSearch.place(x=174, y=560, height=23, width=134)

        self.entFName.place(x=277, y=72, height=21, width=186)
        self.entLName.place(x=277, y=100, height=21, width=186)
        self.entContact.place(x=277, y=129, height=21, width=186)
        self.entCity.place(x=277, y=158, height=21, width=186)
        self.entdisease.place(x=278, y=188, height=21, width=186)
        self.calDOB.place(x=278, y=218, height=21, width=186)

        self.entSearch.place(x=310, y=560, height=21, width=186)
        self.btn_register.place(x=290, y=245, height=25, width=76)
        self.btn_update.place(x=370, y=245, height=25, width=76)
        self.btn_delete.place(x=460, y=245, height=25, width=76)
        self.btn_clear.place(x=548, y=245, height=25, width=76)
        self.btn_show_all.place(x=630, y=245, height=25, width=76)
        self.btn_search.place(x=498, y=558, height=26, width=60)
        self.btn_exit.place(x=320, y=610,  height=31, width=60)
        self.tvpatient.place(x=40, y=310, height=200, width=640)
        self.create_table()
        self.load_patient_data()

    def clear_form(self):
      self.entFName.delete(0, tk.END)
      self.entLName.delete(0, tk.END)
      self.entContact.delete(0, tk.END)
      self.entCity.delete(0, tk.END)
      self.entdisease.delete(0, tk.END)
      self.calDOB.delete(0, tk.END)



    def exit(self):
      MsgBox = mb.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
      if MsgBox == 'yes':
        self.destroy()
    def delete_patient_data(self):
      MsgBox = mb.askquestion('Delete Record', 'Are you sure! you want to delete selected patient record', icon='warning')
      if MsgBox == 'yes':
          if db_connection.is_connected() == False:
              db_connection.connect()
          db_cursor.execute("use patient") 
         
          Delete = "delete from patient_master2 where idno='%s'" % (idno)
          db_cursor.execute(Delete)
          db_connection.commit()
          mb.showinfo("Information", "patient Record Deleted Succssfully")
          self.load_patient_data()
          self.entFName.delete(0, tk.END)
          self.entLName.delete(0, tk.END)
          self.entContact .delete(0, tk.END)
          self.entCity.delete(0, tk.END)
          self.entdisease.delete(0, tk.END)
          self.calDOB.delete(0, tk.END)




    def create_table(self):
        if db_connection.is_connected() == False:
          db_connection.connect()
       
        db_cursor.execute("CREATE DATABASE IF NOT EXISTS patient")  # Create a Database Named patient
        db_cursor.execute("use patient")  # Interact with patient Database
        # creating required tables
        db_cursor.execute("create table if not exists patient_master2(Id INT(10) NOT NULL  PRIMARY KEY AUTO_INCREMENT,idno INT(15),fname VARCHAR(30),lname VARCHAR(30),city VARCHAR(20),dis VARCHAR(30),mobileno VARCHAR(10),dob date)AUTO_INCREMENT=1")
        db_connection.commit()

    def register_patient(self):
        if db_connection.is_connected() == False:
          db_connection.connect()
        fname = self.entFName.get()  
        lname = self.entLName.get()  
        contact_no = self.entContact.get()  
        city = self.entCity.get() 
        dis = self.entdisease.get()  
        dob = self.calDOB.get() 

        if fname == "":
            mb.showinfo('Information', "Please Enter Firstname")
            self.entFName.focus_set()
            return
        if lname == "":
            mb.showinfo('Information', "Please Enter Lastname")
            self.entLName.focus_set()
            return

        if contact_no == "":
            mb.showinfo('Information', "Please Enter Contact Number")
            self.entContact.focus_set()
            return
        if city == "":
            mb.showinfo('Information', "Please Enter City Name")
            self.entCity.focus_set()
            return
        if dis == "":
            mb.showinfo('Information', "Please Enter Disease Name")
            self.entdis.focus_set()
            return
        if dob == "":
            mb.showinfo('Information', "Please Choose Date of Birth")
            self.calDOB.focus_set()
            return


      
        try:
            idno =int(self.fetch_max_idno())
            print("New patient Id: " + str(idno))
            query2 = "INSERT INTO patient_master2 (idno, fname,lname,city,dis,mobileno,dob) VALUES (%s, %s,%s, %s,%s, %s, %s)"
         
            db_cursor.execute(query2, (idno, fname, lname, city, dis, contact_no,dob))
            mb.showinfo('Information', "patient Registration Successfully")
    
            db_connection.commit()
            self.load_patient_data()
        except mysql.connector.Error as err:
            print(err)
        
            db_connection.rollback()
            mb.showinfo('Information', "Data insertion failed!!!")
        finally:
           db_connection.close()

    def fetch_max_idno(self):
        if db_connection.is_connected() == False:
            db_connection.connect()
        db_cursor.execute("use patient")  
        idno  = 0
        query1 = "SELECT idno FROM patient_master2 order by  id DESC LIMIT 1"
     
        db_cursor.execute(query1)  
        print("No of Record Fetched:" + str(db_cursor.rowcount))
        if db_cursor.rowcount == 0:
            idno = 1
        else:
            rows = db_cursor.fetchall()
            for row in rows:
                idno = row[0]
            idno = idno + 1
        print("Max patient Id: " + str(idno))
        return idno

    def show_search_record(self):
        if db_connection.is_connected() == False:
            db_connection.connect()
        s_idno = self.entSearch.get()  # Retrieving entered first name
        print(s_idno)
        if  s_idno == "":
            mb.showinfo('Information', "Please Enter patient id")
            self.entSearch.focus_set()
            return
        self.tvpatient.delete(*self.tvpatient.get_children())  
    
        db_cursor.execute("use patient")  
        sql = "SELECT idno,fname,lname,city,dis,mobileno,date_format(dob,'%d-%m-%Y') FROM patient_master2 where idno='" + s_idno + "'"
        db_cursor.execute(sql)
        total = db_cursor.rowcount
   
        print("Total Data Entries:" + str(total))
        rows = db_cursor.fetchall()

        idno = ""
        First_Name = ""
        Last_Name = ""
        City = ""
        disease = ""
        Phone_Number = ""
        DOB =""
        for row in rows:
            idno = row[0]
            First_Name = row[1]
            Last_Name = row[2]
            City = row[3]
            disease = row[4]
            Phone_Number = row[5]
            DOB = row[6]
            print( Phone_Number)
            self.tvpatient.insert("", 'end', text=idno, values=(idno, First_Name, Last_Name, City, disease, Phone_Number,DOB))


    def show_selected_record(self, event):
        self.clear_form()
        for selection in self.tvpatient.selection():
            item = self.tvpatient.item(selection)
        global idno
        idno,first_name,last_name,city,disease,contact_no,dob = item["values"][0:7]
        self.entFName.insert(0, first_name)
        self.entLName.insert(0, last_name)
        self.entCity.insert(0, city)
        self.entdisease .insert(0, disease)
        self.entContact.insert(0, contact_no)
        self.calDOB.insert(0, dob)
        return idno

    def update_patient_data(self):
        if db_connection.is_connected() == False:
            db_connection.connect()
        print("Updating")
        db_cursor.execute("use patient")  
        First_Name = self.entFName.get()
        Last_Name = self.entLName.get()
        Phone_Number = self.entContact.get()
        City = self.entCity.get()
        disease = self.entdis.get()
        DOB = self.calDOB.get()
        print( idno)
        Update = "Update patient_master2 set fname='%s', lname='%s', mobileno='%s', city='%s', dis='%s', dob='%s' where idno='%s'" % (
        First_Name, Last_Name, Phone_Number, City, disease,DOB, idno)
        db_cursor.execute(Update)
        db_connection.commit()
        mb.showinfo("Info", "Selected patient Record Updated Successfully ")
        self.load_patient_data()

    def load_patient_data(self):
        if db_connection.is_connected() == False:
            db_connection.connect()
        self.calDOB.delete(0, tk.END)#clears the date entry widget
        self.tvpatient.delete(*self.tvpatient.get_children())  # clears the treeview tvpatient
      
        db_cursor.execute("use patient")  # Interact with Bank Database
        sql = "SELECT idno,fname,lname,city,dis,mobileno,date_format(dob,'%d-%m-%Y') FROM patient_master2"
        db_cursor.execute(sql)
        total = db_cursor.rowcount
      
        print("Total Data Entries:" + str(total))
        rows = db_cursor.fetchall()

        idno = ""
        First_Name = ""
        Last_Name = ""
        City = ""
        disease = ""
        Phone_Number = ""
        DOB =""
        for row in rows:
            idno = row[0]
            First_Name = row[1]
            Last_Name = row[2]
            City = row[3]
            disease = row[4]
            Phone_Number = row[5]
            DOB = row[6]
            self.tvpatient.insert("", 'end', text=idno, values=(idno, First_Name, Last_Name, City, disease, Phone_Number,DOB))



if __name__ == "__main__":
    app = PatientApp()
    app.mainloop()