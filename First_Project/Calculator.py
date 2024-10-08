import tkinter as tk
from math import cos, sin, tan, acos, asin, atan, radians, degrees, factorial, log10, e, pi


root = tk.Tk()
root.title("Calculator")
root.iconbitmap("Calculator.ico")
root.geometry("464x400")
root.configure(bg="#DADADA")
root.resizable(False, False)

number = tk.StringVar()
number.initialize("")
number_font = ("Arial", 27)

entry = tk.Entry(root, textvariable=number, font=number_font, state="readonly")
entry.grid(row=0, column=0, columnspan=7, padx=10, ipady=15, sticky="WE")

counter_col=0
counter_row=0

while counter_col<5:
    
    root.grid_columnconfigure(counter_col, weight=1)
    counter_col+=1

while counter_row<7:
    
    root.grid_rowconfigure(counter_row, weight=1)
    counter_row+=1

numbers_list=[]
operation=""
math_op=0
op_counter=False

#--------------------------defs-----------------------------------------------------------------------------

def change(num):
    
    try:
        if number.get()=="" or number.get()=="Syntax error" or number.get()=="MATH error":
            number.initialize(num)
        else:
            num_to_change=number.get()
            num_changed=num_to_change+num
            number.set(num_changed)
            
    except TypeError:
        number.set(num)
        
def operate(op):
    
    global operation
    global math_op
    global op_counter
    
    try:
        op_counter=True
        math_op=0
        operation=op
        first_num=number.get()
        numbers_list.append(float(first_num))
        number.initialize("")
        
    except ValueError:
        number.set("Syntax error")                         
    
def float_to_int(r):
    
    global math_op
    
    new_list=list(str(math_op))
    list_rev=new_list[::-1]
    new_list_2=[]
            
    for i in list_rev:
        if i!=".":
            new_list_2.append(i)
        else:
            break
           
    try:     
        if new_list_2[0]=="0" and len(new_list_2)==1:
            number.set(str(int(math_op)))
        else:
            number.set(str(round(float(math_op), r)))
            
    except OverflowError:
        number.set("MATH error") 
        
def other_op(op, op_type):
    
    global operation
    global math_op
    
    operation=op
    
    try:
        last_num=float(number.get())
    
        if op_type=="rad":
            
            last_num=radians(last_num)
            
            if operation=="cos":
                math_op=cos(last_num)
            elif operation=="sin":
                math_op=sin(last_num)
            elif operation=="tan":
                math_op=tan(last_num)
            elif operation=="acos":
                math_op=acos(last_num)
                math_op=degrees(math_op)
            elif operation=="asin":
                math_op=asin(last_num)
                math_op=degrees(math_op)
            elif operation=="atan":
                math_op=atan(last_num)
                math_op=degrees(math_op)
            
        float_to_int(5)
    
        if op_type=="float":
        
            if operation=="fact":
                math_op=factorial(int(last_num))
                number.set(math_op)
            elif operation=="log":
                math_op=log10(last_num)
                number.set(math_op)

    except ValueError:
        number.set("MATH error")

    if number.get()=="0.0":
        number.set("0")
    
def equal():    
                                         
    global operation
    global math_op
    global op_counter
    
    if op_counter:
        try:
            last_num=number.get()
            numbers_list.append(float(last_num))
            math_op=numbers_list[0]
            del numbers_list[0]
            
            if operation=="plus":
                for i in numbers_list:
                    math_op+=i
            elif operation=="sub":
                for i in numbers_list:
                    math_op-=i
            elif operation=="mult":
                for i in numbers_list:
                    math_op*=i
            elif operation=="div":
                for i in numbers_list:
                    math_op/=i
            elif operation=="pow":                            
                for i in numbers_list:
                    math_op=math_op**i
            elif operation=="root":                            
                for i in numbers_list:
                    math_op=i**(1/math_op)
                    
            if math_op==-0:
                math_op=0
    
            float_to_int(22)  
                
        except ZeroDivisionError:
            number.set("MATH error")
        except ValueError:
            number.set("Syntax error")
            
    numbers_list.clear()
    operation=""
    
def delete():
    
    global operation
    global math_op
    global op_counter
    
    number.initialize("")
    numbers_list.clear()
    math_op=0
    operation=""
    op_counter=False
    
#------------------------buttons-------------------------------------------------

button_0 = tk.Button(root, text="0", command=lambda: change("0"))
button_1 = tk.Button(root, text="1", command=lambda: change("1"))
button_2 = tk.Button(root, text="2", command=lambda: change("2"))
button_3 = tk.Button(root, text="3", command=lambda: change("3"))
button_4 = tk.Button(root, text="4", command=lambda: change("4"))
button_5 = tk.Button(root, text="5", command=lambda: change("5"))
button_6 = tk.Button(root, text="6", command=lambda: change("6"))
button_7 = tk.Button(root, text="7", command=lambda: change("7"))
button_8 = tk.Button(root, text="8", command=lambda: change("8"))
button_9 = tk.Button(root, text="9", command=lambda: change("9"))

button_plus = tk.Button(root, text="+", command=lambda: operate("plus"))
button_subt = tk.Button(root, text="-", command=lambda: operate("sub"))
button_multi = tk.Button(root, text="*", command=lambda: operate("mult"))
button_div = tk.Button(root, text="/", command=lambda: operate("div"))
button_exp = tk.Button(root, text="^", command=lambda: operate("pow"))
button_base = tk.Button(root, text="√", command=lambda: operate("root"))
button_equal = tk.Button(root, text="=", command=equal)
button_delete = tk.Button(root, text="DEL", command=delete)

button_subt_symbol = tk.Button(root, text="-", command=lambda: change("-"))
button_coma = tk.Button(root, text=".", command=lambda: change("."))
button_pi = tk.Button(root, text="π", command=lambda: change(pi))
button_e = tk.Button(root, text="e", command=lambda: change(e))

button_cos = tk.Button(root, text="cos", command=lambda: other_op("cos", "rad")) 
button_sin = tk.Button(root, text="sin", command=lambda: other_op("sin", "rad"))
button_tan = tk.Button(root, text="tan", command=lambda: other_op("tan", "rad"))
button_acos = tk.Button(root, text="acos", command=lambda: other_op("acos", "rad"))
button_asin = tk.Button(root, text="asin", command=lambda: other_op("asin", "rad"))
button_atan = tk.Button(root, text="atan", command=lambda: other_op("atan", "rad"))
button_log = tk.Button(root, text="log", command=lambda: other_op("log", "float"))
button_fact = tk.Button(root, text="!", command=lambda: other_op("fact", "float"))

#------------------------------------button-grid-------------------------------------------------

button_cos.grid(row=1, column=0, padx=5, pady=5, sticky="NSEW")
button_sin.grid(row=1, column=1, padx=5, pady=5, sticky="NSEW")
button_tan.grid(row=1, column=2, padx=5, pady=5, sticky="NSEW")
button_log.grid(row=1, column=3, padx=5, pady=5, sticky="NSEW")
button_e.grid(row=1, column=4, padx=5, pady=5, sticky="NSEW")

button_acos.grid(row=2, column=0, padx=5, pady=5, sticky="NSEW")
button_asin.grid(row=2, column=1, padx=5, pady=5, sticky="NSEW")
button_atan.grid(row=2, column=2, padx=5, pady=5, sticky="NSEW")
button_fact.grid(row=2, column=3, padx=5, pady=5, sticky="NSEW")
button_pi.grid(row=2, column=4, padx=5, pady=5, sticky="NSEW")

button_7.grid(row=3, column=0, padx=5, pady=5, sticky="NSEW")
button_8.grid(row=3, column=1, padx=5, pady=5, sticky="NSEW")
button_9.grid(row=3, column=2, padx=5, pady=5, sticky="NSEW")
button_exp.grid(row=3, column=3, padx=5, pady=5, sticky="NSEW")
button_base.grid(row=3, column=4, padx=5, pady=5, sticky="NSEW")

button_4.grid(row=4, column=0, padx=5, pady=5, sticky="NSEW")
button_5.grid(row=4, column=1, padx=5, pady=5, sticky="NSEW")
button_6.grid(row=4, column=2, padx=5, pady=5, sticky="NSEW")
button_multi.grid(row=4, column=3, padx=5, pady=5, sticky="NSEW")
button_div.grid(row=4, column=4, padx=5, pady=5, sticky="NSEW")

button_1.grid(row=5, column=0, padx=5, pady=5, sticky="NSEW")
button_2.grid(row=5, column=1, padx=5, pady=5, sticky="NSEW")
button_3.grid(row=5, column=2, padx=5, pady=5, sticky="NSEW")
button_plus.grid(row=5, column=3, padx=5, pady=5, sticky="NSEW")
button_subt.grid(row=5, column=4, padx=5, pady=5, sticky="NSEW")

button_coma.grid(row=6, column=0, padx=5, pady=5, sticky="NSEW")
button_0.grid(row=6, column=1, padx=5, pady=5, sticky="NSEW")
button_subt_symbol.grid(row=6, column=2, padx=5, pady=5, sticky="NSEW")
button_equal.grid(row=6, column=3, padx=5, pady=5, sticky="NSEW")
button_delete.grid(row=6, column=4, padx=5, pady=5, sticky="NSEW")

root.mainloop()
