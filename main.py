from tkinter import *
from tkinter.ttk import Combobox  # Import Combobox from ttk
from tkinter import messagebox
BACKEND_URL =r":\\Users\\tannu\\PycharmProjects\\pythonProject\\dicerolling.py"
base = Tk()
base.geometry("500x500")
base.title("Dice Game Registration Form")
# Labels
lbl_0 = Label(base, text="Dice Game Registration Form", width=22, font=("bold", 22))
lbl_0.place(x=110, y=80)
lb1 = Label(base, text="Enter Name", width=10, font=("arial", 12))
lb1.place(x=20, y=120)
lb3 = Label(base, text="Enter Email", width=10, font=("arial", 12))
lb3.place(x=19, y=160)
lb4 = Label(base, text="Contact Number", width=13, font=("arial", 12))
lb4.place(x=19, y=200)
lb5 = Label(base, text="Select Gender", width=15, font=("arial", 12))
lb5.place(x=5, y=240)
lb6 = Label(base, text="Select Country", width=15, font=("arial", 12))
lb6.place(x=5, y=280)
# Entry fields
en1 = Entry(base)
en1.place(x=200, y=120)

en3 = Entry(base)
en3.place(x=200, y=160)

en4 = Entry(base)
en4.place(x=200, y=200)

# Radio buttons for gender
vars = IntVar()
Radiobutton(base, text="Male", padx=5, variable=vars, value=1).place(x=180, y=240)
Radiobutton(base, text="Female", padx=10, variable=vars, value=2).place(x=240, y=240)
Radiobutton(base, text="Others", padx=15, variable=vars, value=3).place(x=310, y=240)

# Dropdown for country selection
list_of_country = ("United States", "India", "Nepal", "Germany", "France", "Korea", "China")
cv = StringVar()
country_dropdown = Combobox(base, textvariable=cv, values=list_of_country)
country_dropdown.place(x=200, y=280)
# Submit Button
def submit_form():
  # Get data from entry fields and radio buttons/dropdown
  name = en1.get()
  email = en3.get()
  contact_number = en4.get()
  gender = vars.get()  # Assuming you want to access the selected gender value
  country = cv.get()
  # Improve error handling (optional)
  # You can add checks for valid email format, etc.
  # Display confirmation message (optional)
  confirmation_message = f"Registration Successful!\nName: {name}\nEmail: {email}\nContact: {contact_number}\nGender: {gender}\nCountry: {country}"
  messagebox.showinfo("Registration Confirmation", confirmation_message)
# ... rest of your code ...
# Alternatively, store data in a database or file (optional)
submit_button = Button(base, text="Submit Registration", command=submit_form)
submit_button.place(x=200, y=320)

base.mainloop()
