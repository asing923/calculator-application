import tkinter as tk

class ProCalculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.gt_E_Q = 0
        self.gt_OP_R = 0
        self.result = 0
        self.val_numer = "0"
        self.opr = ' '
        self.button = ' '
        self.diskspace= []
        self.E1 = tk.Entry(self, width=18, font=('Helvetica 26'), border=2, fg="red", bg="#000000")
        self.keypad = ['MS', 'MR', 'M', 'MC','7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', ' ', '+', 'CE', 'C', ' ', '=']
        self.keysArr = []
        self.lambdas = [
            lambda a: self.num_keys_handler(((a.widget).cget("text"))),
            lambda a: self.operators_keys_handler(((a.widget).cget("text"))),
            lambda a: self.erase_entered_vals(),
            lambda a: self.erase(),
            lambda a: self.operation_mem_save(),
            lambda a: self.operation_mem_rec(((a.widget).cget("text")))
        ]
        self.gen_dial()

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
            self.diskspace = []


    def operators_keys_handler(self, text):
        self.button = text
        if self.gt_E_Q == 1:
            self.val_numer = self.result
        if self.gt_OP_R == 0:
            self.result = self.result + float(self.val_numer) if self.opr == '+' else \
                       self.result - float(self.val_numer) if self.opr == '-' else \
                       self.result * float(self.val_numer) if self.opr == '*' else \
                       self.result / float(self.val_numer) if self.opr == '/' else float(self.val_numer)
        self.E1.delete(0, tk.END)
        self.E1.insert(tk.END, str(self.result))
        self.opr = self.button
        self.val_numer = "0"
        
        if self.button != '=':
            self.gt_OP_R = 1
        else:
            self.gt_OP_R = 0

        if self.button == '=':
            self.gt_E_Q = 1
        else:
            self.gt_E_Q = 0
        
    def num_keys_handler(self, text):
        self.button = text
        if self.button == '.' and '.' in self.val_numer:
            return
        if self.val_numer == '0' and self.button != '.':
            self.val_numer = self.button
        else:
            self.val_numer += self.button
        self.E1.delete(0, tk.END)
        self.E1.insert(tk.END, self.val_numer)
        self.gt_E_Q = 0
        self.gt_OP_R = 0

    def erase(self):
        self.E1.delete(0, tk.END)
        self.val_numer = "0"
        self.result = 0
        self.opr = ' '
        self.gt_E_Q = 0
        self.gt_OP_R = 0

    def operation_mem_save(self):
        if self.E1.get():
            self.diskspace.append(float(self.E1.get()))

    def erase_entered_vals(self):
        self.E1.delete(0, tk.END)
        self.val_numer = "0"

    def gen_dial(self):
        self.E1.grid(row=0, column=0, columnspan=4)

        for j in range(len(self.keypad)):
            row = j // 4 + 1
            col = j % 4
            if self.keypad[j] == '=':
                button = tk.Button(self, text=self.keypad[j], width=10, height=3, fg="white", bg="#7F7FFF", font="Helvetica 13")
            else:
                button = tk.Button(self, text=self.keypad[j], width=10, height=3, fg="white", bg="#7F7FFF", font="Helvetica 13")
            button.grid(row=row, column=col)
            button.bind("<Button-1>", self.lambdas[0] if button.cget("text").isdigit() or button.cget("text") == '.' else \
                                      self.lambdas[1] if button.cget("text") not in ('CE', 'C', 'MS', 'MR','M', 'MC') else \
                                      self.lambdas[2] if button.cget("text") == 'CE' else \
                                      self.lambdas[3] if button.cget("text") == 'C' else \
                                      self.lambdas[4] if button.cget("text") == 'MS' else \
                                      self.lambdas[5])
            self.keysArr.append(button)

root = tk.Tk()
root.title("Calculator Mode - Infix")
root.geometry("600x900")
root.resizable(1000, 1000)
root.config(bg="#F0F0FF")
app = ProCalculator(master=root)
app.grid()
root.mainloop()
