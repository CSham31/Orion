import tkinter as tk
from tkinter.constants import X
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from tkinter import messagebox
from tkinter import simpledialog as sd
from tkinter import Tk, Label, StringVar, Button, Entry
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming



root = tk.Tk()
root.title("ORION")

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)


#logo
logo = Image.open('logo.jpg')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions

instructions = tk.Label(root, text="Select an option")
instructions.grid(columnspan=3, column=0, row=1)


    
def route():

    #change button text
    browse_text1.set("loading...")

    
    #take no.of showrooms
    n=sd.askstring("Input", "How Many Showrooms are available withouth DC ?",parent=root)
    if n.isnumeric() :
       
        N=int(n)
       
        #find route  
        distance_matrix=np.zeros((N+1,N+1))

        #taking distances            
        for i in range(N+1):
            for j in range (i+1,N+1):
                x=sd.askstring("Input", "Enter distances from "+str(i)+" to "+str(j)+"\nX when route is not defined.",parent=root)
                if x.upper()!="X":
                    distance_matrix[i,j]=distance_matrix[j,i]=x
                else:
                    distance_matrix[i,j]=distance_matrix[j,i]=10000
        print(distance_matrix)

        #results
        permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
        messagebox.showinfo("Result","Cost-effective path : "+">".join(list(map(str,permutation)))+">0"+"\nMinimum Distance: "+str(distance))
     
        
    else:
        messagebox.showerror("Error", "Enter Valid Number")
    
    browse_text1.set("Cost-effective Route")
    
    
      

#route button
browse_text1 = tk.StringVar()
browse_btn1 = tk.Button(root, textvariable=browse_text1, command=lambda:route(), font="Raleway", bg="#20bebe", fg="white", height=2, width=20)
browse_text1.set("Cost-effective Route")
browse_btn1.grid(column=1, row=2)

#assignment button
browse_text2 = tk.StringVar()
browse_btn2 = tk.Button(root, textvariable=browse_text2, command=lambda:assignment(), font="Raleway", bg="#20bebe", fg="white", height=2, width=20)
browse_text2.set("Optimal Locating")
browse_btn2.grid(column=1, row=3)

canvas = tk.Canvas(root, width=600, height=200)
canvas.grid(columnspan=3)

root.mainloop()
