from file_eval import *
import os
import tkinter as tk
import re


class Calculadora:
  def __init__(self, root):
    self.root = root
    self.root.title("CALCULADORA ARTESANAL")  # Título da janela
    self.root.geometry("364x353")  # Largura X altura "364x306"
    self.root.resizable(False, False)  # Impede redimensionamento

    # Campo de exibição
    self.display = tk.Entry(root, font=("Arial", 18), borderwidth=1, relief="solid", justify="right")
    self.display.grid(row=0, column=0, columnspan=4, ipadx=50, ipady=20)

    self.simbolos = {
      'x': '*',  # Multiplicação
      '÷': '/',  # Divisão
      '+': '+',  # Adição
      '-': '-',  # Subtração
      ',': '.',  # Substitui vírgula por ponto
      '^': '**'  # Substitui o elevado matemático por elevado programavel
    }
    buttons = [
      'C', 'CE', '⌫', 
      "(", ")",
      '÷','7', '8', '9', 
      'x','4', '5', '6', 
      '-', '1', '2', '3', 
      '+', 'xʸ', '0', ",", '='
    ]

    row, col = 1, 0
    for num, button in enumerate(buttons):  # Adiciona os botões para interface
      action = lambda x=button: self.on_button_click(x)
      num += 1
      print(f"{num}.num row:{row} col:{col}")
      
      if num == 1: tk.Button(root, text=button, font=("Arial", 18), width=2, height=1, command=action).grid(row=row, column=col, rowspan=2, sticky="nsew")
      elif num == 3: tk.Button(root, text=button, font=("Arial", 18), width=2, height=1, command=action).grid(row=row, column=col, columnspan=2, sticky="nsew")
      elif num == 4: 
        col -= 2
        row = 2
        tk.Button(root, text=button, font=("Arial", 18), width=2, height=1, command=action).grid(row=row, column=col, sticky="nsew")
      elif num == 5: 
        row = 2
        tk.Button(root, text=button, font=("Arial", 18), width=2, height=1, command=action).grid(row=row, column=col, sticky="nsew")
      else: tk.Button(root, text=button, font=("Arial", 18), width=2, height=1, command=action).grid(row=row, column=col, sticky="nsew")
      
      col += 1
      if col > 3:
        col = 0
        row += 1
    if self.display.get() == "": self.display.insert(tk.END, "0")


  def on_button_click(self, button):
    def ERROR(button_=True):  # Função para exibir erro de sintaxe
      if button_:
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, "SyntaxError")
      if not button_ and self.display.get() == "SyntaxError":
        self.display.delete(0, tk.END)

    ERROR(button_=False)
    if button == "C":  # Apaga tudo
      self.display.delete(0, tk.END)
      self.display.insert(tk.END, "0")

    elif button == "CE":  # Apaga último número depois do operador de conta
      content = self.display.get()
      print("$+$", content)

      if "(" in content:
        start = False
        list_split = []
        list_save = []
        list_complet = {}

        for character in content:  # Identifica e armazena as expressões dentro dos parênteses
          if character == "(":
            start = True
            list_split = []
          elif character == ")":
            start = False
            list_save.append("".join(list_split))
            list_split = []
          elif start:
            list_split.append(character)

        for inter in list_save: # Substitui 'e-' e 'e+' por 'MM'; '-' por 'M', dentro das expressões armazenadas
          for E in ["e-", "e+"]:
            if E in inter:
              if "-" in inter: 
                exter = list(inter)
                exter[0] = "M"
                exter = "".join(exter)
              list_complet[inter] = exter.replace(E, "MM")
        
        for pri, seg in list_complet.items():
          content = content.replace(pri, seg)

      isolate = re.split(r"[÷x+-]", content)
      restante_isolate = 0
      if len(isolate) == 1:
        self.display.delete(0, tk.END)
      elif len(isolate) > 1:
        for i in range(0, len(isolate) - 1):
          restante_isolate += len(isolate[i])
        self.display.delete(restante_isolate + (len(isolate) - 1), tk.END)
      if self.display.get() == "": self.display.insert(tk.END, "0")

    elif button == "⌫":  # Apaga último caractere
      self.display.delete(len(self.display.get()) - 1, tk.END)
      if self.display.get() == "": self.display.insert(tk.END, "0")
      print(self.display.get())

    elif button == "xʸ":  # Calcula porcentagem
      if self.display.get() != "" and list(self.display.get())[len(list(self.display.get()))-1] in ['÷', 'x', '-', '+', '^', ","]: self.display.insert(tk.END, "")
      else: self.display.insert(tk.END, "^")
      print(self.display.get())

    elif button == "=":  # Executa a conta
      try:
        expression = self.display.get().replace(',', '.')  # Substitui vírgula por ponto
        for simbolo, substituto in self.simbolos.items():  # Substitui símbolos
          expression = expression.replace(simbolo, substituto)

        if not list(expression)[len(list(expression)) - 1] in ["-", "*", "/", "+"]:  # Verifica operador
          os.system('cls' if os.name == 'nt' else 'clear') 
          print(f"Expressão mostrada através da interface: {self.display.get()}")
          result = DEFeval(expression)
          self.display.delete(0, tk.END)
          self.display.insert(tk.END, result)  # Exibe resultado
      except Exception as e:  # Trata erro de execução
        ERROR()
        print("-"*115)
        print(f"ERROR (en):\n{e}")
        print("-"*115)
    else:
      another = True
      if self.display.get() != "" and list(self.display.get())[len(list(self.display.get()))-1] in ['÷', 'x', '-', '+', '^', ","]:
        if button in ['÷', 'x', '-', '+', 'xʸ', ","]:
          self.display.insert(tk.END, "")
          another = False
      if another:
        if self.display.get() == "0":
          if button in ['1','2','3','4','5','6','7','8','9','0',"+", "-", "(", ")"]:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, button)
          else: self.display.insert(tk.END, button)
        else: self.display.insert(tk.END, button)
      print(self.display.get())

# Inicialização do Tkinter 
root = tk.Tk()
app = Calculadora(root)
root.mainloop()