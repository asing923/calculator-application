import tkinter as tk

class ProCalculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.keypad = ['MS', 'MR', 'M', 'MC','7', '8', '9', '/','4', '5', '6', '*','1', '2', '3', '-','0', '.', '', '+','CE', 'C', '', 'Enter']
        self.result = 0
        self.diskspace= []
        self.vals = []
        self.val_numer = "0"
        self.val_opr = ' '
        self.button = ' '

        self.lambdas = [
            lambda a: self.num_keys_handler(((a.widget).cget("text"))),
            lambda a: self.operators_keys_handler(((a.widget).cget("text"))),
            lambda a: self.erase_entered_vals(),
            lambda a: self.erase(),
            lambda a: self.operation_mem_save(),
            lambda a: self.opr_ent(),
            lambda a: self.operation_mem_rec(((a.widget).cget("text")))
            
        ]

        self.E1 = tk.Entry(self, width=18, font=('Helvetica 26'), border=3, fg="red", bg="#000000")
        self.E2 = tk.Entry(self, width=18, font=('Helvetica 26'), border=3, fg="red", bg="#000000")
        self.E3 = tk.Entry(self, width=18, font=('Helvetica 26'), border=3, fg="red", bg="#000000")
        self.E4 = tk.Entry(self, width=18, font=('Helvetica 26'), border=3, fg="red", bg="#000000")
        
        self.keysArr = []
        
        self.gen_dial()

    def operation_mem_rec(self, text):

        if text == 'M':
            self.E4.delete(0, tk.END)
            self.E4.insert(tk.END, str(self.diskspace))

        elif text == 'MR':
            if self.diskspace:
                self.E4.delete(0, tk.END)
                self.E4.insert(tk.END, str(self.diskspace[-1]))
            else:
                self.E4.delete(0, tk.END)

        elif text == 'MC':
            self.E4.delete(0, tk.END)
            self.diskspace =[]
        

    def operators_keys_handler(self, text):
        if self.result != 0:
            self.result = 0
        self.val_opr = text     

        self.result = str(eval(self.vals[-1] + self.val_opr + self.val_numer))
        self.val_numer = self.result
        self.vals.pop()

        self.E4.delete(0, tk.END)
        self.E4.insert(tk.END, self.result)

        self.func_disp()
        

    def num_keys_handler(self, text):
        if self.result != 0:
            self.vals.append(self.result)
            self.val_numer ="0"
            self.result = 0
            self.func_disp()  
        
        self.button = text
        if self.button == '.' and '.' in self.val_numer:
            return
        if self.val_numer == '0' and self.button != '.':
            self.val_numer = self.button
        else:
            self.val_numer = self.val_numer + self.button
        self.E4.delete(0, tk.END)
        self.E4.insert(tk.END, self.val_numer)

    def erase(self):
        self.E4.delete(0, tk.END)
        self.E3.delete(0, tk.END)
        self.E2.delete(0, tk.END)
        self.E1.delete(0, tk.END)
        self.val_numer = "0"
        self.result = 0
        self.val_opr = ' '
        self.vals=[]

    def operation_mem_save(self):
        if self.E4.get():
            self.diskspace.append(float(self.E4.get()))


    def erase_entered_vals(self):
        self.E4.delete(0, tk.END)
        self.val_numer = "0"

    
    def opr_ent(self):
        self.vals.append(self.val_numer)
        self.val_numer = '0'
        self.E4.delete(0, tk.END)
        self.E4.insert(tk.END, self.val_numer)
        self.func_disp()


    def func_disp(self):
        if len(self.vals) >= 3:
            self.E1.delete(0, tk.END)
            self.E1.insert(tk.END, self.vals[-3])
            self.E2.delete(0, tk.END)
            self.E2.insert(tk.END, self.vals[-2])
            self.E3.delete(0, tk.END)
            self.E3.insert(tk.END, self.vals[-1])
        elif len(self.vals) == 2:
            self.E1.delete(0, tk.END)
            self.E1.insert(tk.END, "")
            self.E2.delete(0, tk.END)
            self.E2.insert(tk.END, self.vals[-2])
            self.E3.delete(0, tk.END)
            self.E3.insert(tk.END, self.vals[-1])
        elif len(self.vals) == 1:
            self.E1.delete(0, tk.END)
            self.E1.insert(tk.END, "")
            self.E2.delete(0, tk.END)
            self.E2.insert(tk.END, "")
            self.E3.delete(0, tk.END)
            self.E3.insert(tk.END, self.vals[-1])
        else:
            self.E1.delete(0, tk.END)
            self.E1.insert(tk.END, "")
            self.E2.delete(0, tk.END)
            self.E2.insert(tk.END, "")
            self.E3.delete(0, tk.END)
            self.E3.insert(tk.END, "")


    def gen_dial(self):
        self.E1.grid(row=0, column=0, columnspan=4)
        self.E2.grid(row=1, column=0, columnspan=4)
        self.E3.grid(row=2, column=0, columnspan=4)
        self.E4.grid(row=3, column=0, columnspan=4)

        for j in range(len(self.keypad)):
            col = j % 4
            row = j // 4 + 4
            if self.keypad[j] == 'Enter':
                btn = tk.Button(self, text=self.keypad[j], width=9, height=2, fg="white", bg="#FA8072", font="Segoe 12")
            else:
                btn = tk.Button(self, text=self.keypad[j], width=9, height=2, fg="white", bg="#333333", font="Segoe 12")
            btn.grid(row=row, column=col)
            btn.bind("<Button-1>", self.lambdas[0] if btn.cget("text").isdigit() or btn.cget("text") == '.' else \
                                      self.lambdas[1] if btn.cget("text") not in ('CE', 'C', 'MS', 'MR', 'M', 'MC','Enter') else \
                                      self.lambdas[2] if btn.cget("text") == 'CE' else \
                                      self.lambdas[3] if btn.cget("text") == 'C' else \
                                      self.lambdas[4] if btn.cget("text") == 'MS' else \
                                      self.lambdas[5] if btn.cget("text") == 'Enter' else \
                                      self.lambdas[6])
            self.keysArr.append(btn)
    

root = tk.Tk()
root.title("Calculator Mode - RPN")
root.geometry("600x900")
root.resizable(1000, 1000)
root.config(bg="#F0F0FF")
app = ProCalculator(master=root)
app.grid()
root.mainloop()
