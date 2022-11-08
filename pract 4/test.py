from tkinter import *    

def clicked_false1():      
    que1.configure(text="Ответ не верен!")   
    btn1_que1.configure(text="")
    btn2_que1.configure(text="")  
def clicked_true1(): 
    que1.configure(text="Ответ верен!")   
    btn1_que1.configure(text="")
    btn2_que1.configure(text="")     
def clicked_false2():      
    que2.configure(text="Ответ не верен!")   
    btn1_que2.configure(text="")
    btn2_que2.configure(text="")  
def clicked_true2(): 
    que2.configure(text="Ответ верен!")   
    btn1_que2.configure(text="")
    btn2_que2.configure(text="")  
def clicked_false3():      
    que3.configure(text="Ответ не верен!")   
    btn1_que3.configure(text="")
    btn2_que3.configure(text="")  
def clicked_true3(): 
    que3.configure(text="Ответ верен!")   
    btn1_que3.configure(text="")
    btn2_que3.configure(text="")  
def clicked_false4():      
    que4.configure(text="Ответ не верен!")   
    btn1_que4.configure(text="")
    btn2_que4.configure(text="")  
def clicked_true4(): 
    que4.configure(text="Ответ верен!")   
    btn1_que4.configure(text="")
    btn2_que4.configure(text="") 
def clicked_false5():      
    que5.configure(text="Ответ не верен!")   
    btn1_que5.configure(text="")
    btn2_que5.configure(text="")  
def clicked_true5(): 
    que5.configure(text="Ответ верен!")   
    btn1_que5.configure(text="")
    btn2_que5.configure(text="")  
window = Tk()  
window.title("Test")  
window.geometry('900x450') 
start=Label(window, text="Вам необходимо ответить на несколько вопросов", font=("Arial Bold", 10) )
que1 = Label(window, text="Сколько героев в доте?", font=("Arial Bold", 20), )    
que2 = Label(window, text="Сколько чисел существует?", font=("Arial Bold", 20), )  
que3 = Label(window, text="Сколько часов в сутках?", font=("Arial Bold", 20), )  
que4 = Label(window, text="Сколько минут в сутках?", font=("Arial Bold", 20), )  
que5 = Label(window, text="Какой сейчас год?", font=("Arial Bold", 20), )  



btn1_que1 = Button(window, text="112",font=("Arial Bold", 20), command=clicked_false1)
btn2_que1 = Button(window, text="121", font=("Arial Bold", 20),command=clicked_true1)
btn1_que2 = Button(window, text="9", font=("Arial Bold", 20),command=clicked_false2)
btn2_que2 = Button(window, text="бесконечность", font=("Arial Bold", 20),command=clicked_true2)
btn1_que3 = Button(window, text="12", font=("Arial Bold", 20),command=clicked_false3)
btn2_que3 = Button(window, text="24", font=("Arial Bold", 20),command=clicked_true3)
btn1_que4 = Button(window, text="1880", font=("Arial Bold", 20),command=clicked_false4)
btn2_que4 = Button(window, text="1440", font=("Arial Bold", 20),command=clicked_true4)
btn1_que5 = Button(window, text="2012", font=("Arial Bold", 20),command=clicked_false5)
btn2_que5 = Button(window, text="2022", font=("Arial Bold", 20),command=clicked_true5)
btn1_que1.grid(column=2, row=0) 
btn2_que1.grid(column=3, row=0)  

btn1_que2.grid(column=2, row=1) 
btn2_que2.grid(column=3, row=1)  

btn1_que3.grid(column=2, row=2) 
btn2_que3.grid(column=3, row=2)  

btn1_que4.grid(column=2, row=3) 
btn2_que4.grid(column=3, row=3)  

btn1_que5.grid(column=2, row=4) 
btn2_que5.grid(column=3, row=4)  
que1.grid(column=0, row=0) 
que2.grid(column=0, row=1)   
que3.grid(column=0, row=2)   
que4.grid(column=0, row=3)   
que5.grid(column=0, row=4)     
window.mainloop()