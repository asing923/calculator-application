import tkinter as tk

class ProCalculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.num_vals = []
        self.result = 0
        self.diskspace = []
        self.keypad = ['MS', 'MR', 'M', 'MC','7', '8', '9', '/','4', '5', '6', 'X','1', '2', '3', '-','0', '.', '(', '+','CE', 'C', ')', '=']
        self.val_numers = "0"
        self.lambdas = [
            lambda a: self.num_keys_handler(((a.widget).cget("text"))),
            lambda a: self.operators_keys_handler(((a.widget).cget("text"))),
            lambda a: self.erase_entered_vals(),
            lambda a: self.erase(),
            lambda a: self.operation_mem_save(),
            lambda a: self.operation_mem_rec(((a.widget).cget("text"))),
            lambda a: self.operation_key_brackets(((a.widget).cget("text")))
        ]
        self.val_oprs = ' '
        self.imp = {'+': 1, '-': 1, 'X': 2, '/': 2}
        self.button = ' '
        self.val_prevs = ' '
        self.E1 = tk.Entry(self, width=18, font=('Helvetica 26'), border=3, fg="red", bg="#000000")
        self.key_oprs = []        
        self.buttons = []
        self.gen_dial()
        

    def gen_dial(self):
        self.E1.grid(row=0, column=0, columnspan=4)

        for j in range(len(self.keypad)):
            row = j // 4 + 1
            col = j % 4
            if self.keypad[j] == '=':
                btn = tk.Button(self, text=self.keypad[j], width=9, height=2, fg="white", bg="#7F7FFF", font="Segoe 12")
            else:
                btn = tk.Button(self, text=self.keypad[j], width=9, height=2, fg="white", bg="#7F7FFF", font="Segoe 12")
            btn.grid(row=row, column=col)
            btn.bind("<Button-1>", self.lambdas[0] if btn.cget("text").isdigit() or btn.cget("text") == '.' else \
                                      self.lambdas[1] if btn.cget("text") not in ('CE', 'C', 'MS', 'MR','M','MC', '(', ')') else \
                                      self.lambdas[2] if btn.cget("text") == 'CE' else \
                                      self.lambdas[3] if btn.cget("text") == 'C' else \
                                      self.lambdas[4] if btn.cget("text") == 'MS' else \
                                      self.lambdas[5] if btn.cget("text") == 'MR' or btn.cget("text") == 'M' or btn.cget("text") == 'MC' else \
                                      self.lambdas[6])
            self.buttons.append(btn)

    def num_keys_handler(self, text):
        self.button = text
        
        if self.val_numers == '0' and self.button != '.':
            self.val_numers = self.button
        else:
            self.val_numers += self.button
        if self.button == '.' and '.' in self.val_numers:
            return
        if self.val_prevs == ')':
            self.val_prevs = ' '
        self.E1.delete(0, tk.END)
        self.E1.insert(tk.END, self.val_numers)

    def operators_keys_handler(self, text):
        if self.val_numers != '0':
            self.num_vals.append(self.val_numers)
            self.val_numers ='0'
        self.button = text

        if self.button == '=':
            if len(self.key_oprs) >= 1:
                self.operation_cal()

            else:
                self.val_numers = self.result
                self.key_oprs = []
                self.val_numers='0'

        elif len(self.key_oprs) >= 1 and self.key_oprs[-1] != '(' and self.val_prevs != ')':
            if len(self.key_oprs) >=2:
                self.val_numers='0'
                while self.key_oprs and self.imp.get(self.key_oprs[-1]) >= self.imp.get(self.key_oprs[-2]):
                    self.operation_cal()
            else:
                self.val_numers='0'
                self.operation_cal()
        if self.button != '=':
            self.key_oprs.append(self.button)
        self.val_numers = '0'

        
    def operation_key_brackets(self, text):
        if text == '(':
            self.key_oprs.append(text)
            self.val_numers = '0'
        elif text == ')':
            self.num_vals.append(self.val_numers)
            self.val_numers = '0'
            self.val_prevs = ')'
            while self.key_oprs[-1] != '(':
                self.operation_cal()
            self.key_oprs.pop()

    def operation_cal(self):
        self.val_numers = '0'
        while len(self.key_oprs) >= 1 and len(self.num_vals) >= 2 and self.key_oprs[-1] != '(':
            self.val_oprs = self.key_oprs.pop()
            x = float(self.num_vals.pop())
            y = float(self.num_vals.pop())
            
            
            if self.val_oprs == '-':
                self.result = y - x
            elif self.val_oprs == '+':
                self.result = y + x
            elif self.val_oprs == '/':
                self.result = y / x
            elif self.val_oprs == 'X':
                self.result = y * x                
            
            self.num_vals.append(str(self.result))
            
       
        self.E1.delete(0, tk.END)
        self.E1.insert(tk.END, str(self.result))

    def erase_entered_vals(self):
        self.E1.delete(0, tk.END)
        self.val_numers = '0'

    def erase(self):
        self.E1.delete(0, tk.END)
        self.key_oprs = []
        self.result = 0
        self.button = ' '
        self.val_numers = '0'
        self.num_vals = []
        self.val_oprs = ' '
        self.val_prevs = ' '

    def operation_mem_save(self):
        if self.E1.get():
            self.diskspace.append(float(self.E1.get()))

    def operation_mem_rec(self, text):
        
        if text == 'M':
            self.E1.delete(0, tk.END)
            self.E1.insert(tk.END, str(self.diskspace))

        elif text == 'MR':
            if self.diskspace:
                self.E1.delete(0, tk.END)
                self.E1.insert(tk.END, str(self.diskspace[-1]))
            else:
                self.E1.delete(0, tk.END)

        elif text == 'MC':
            self.E1.delete(0, tk.END)
            self.diskspace =[]


root = tk.Tk()
root.title("Calculator Mode - Infix")
root.geometry("600x900")
root.resizable(1000, 1000)
root.config(bg="#F0F0FF")
app = ProCalculator(master=root)
app.grid()
root.mainloop()
