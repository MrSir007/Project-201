from tkinter import *
window = Tk()

window.title("SimpleInterest Calculator")
window.geometry("380x400")
window.configure(bg="lightcyan")

def calculate_interest () :
  p = float(principle_entry.get())
  r = float(interest_rate_entry.get)
  t = float(time_entry.get)
  i = (p * r * t) / 100
  interest = round(i, 2)

  result_label.destroy()
  message = Label(result_frame, text=str(interest))

heading_label = Label(window, text="SimpleInterest Calculator", fg="black", bg="lightcyan", font=("Calibri", 20), bd=5)
heading_label.place(x=50, y=20)

principle_label = Label(window, text="Principle", fg="black", bg="lightcyan", font=("Calibri", 12), bd=5)
principle_label.place(x=20, y=100)

principle_entry = Entry(window, text="Principle", bd=2, width=22)
principle_entry.place(x=150, y=102)

interest_rate_label = Label(window, text="Rate of Interest", fg="black", bg="lightcyan", font=("Calibri", 12), bd=5)
interest_rate_label.place(x=20, y=140)

interest_rate_entry = Label(window, text="Rate of Interest", fg="black", bg="lightcyan", font=("Calibri", 12), bd=5)
interest_rate_entry.place(x=150, y=144)

time_label = Label(window, text="Time", fg="black", bg="lightcyan", font=("Calibri", 12), bd=5)
time_label.place(x=20, y=180)

time_entry = Label(window, text="Time", fg="black", bg="lightcyan", font=("Calibri", 12), bd=5)
time_entry.place(x=150, y=187)

calculation = Button(window, text="Calculate", fg="black", bg="cyan", command=calculate_interest)
calculation.place(x=20, y=250)

result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack() 