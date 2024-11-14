from msg_random import *
import random, os

class Calculadora_random:
  def __init__(self):
    self.nome = ""

  def iniciar(self, TF=False):
    os.system('cls' if os.name == 'nt' else 'clear')
    nome_temporario = input("\033[1mOlá, eu sou o robô CR-0103, serei o seu guia durante a prática da lógica de matemática.\nPara eu prosseguir, preciso saber qual é seu nome: \033[0m")
    while len(nome_temporario) == None or len(nome_temporario) <= 1:
      os.system('cls' if os.name == 'nt' else 'clear') 
      nome_temporario = input(f"\033[1mO nome {f"'\033[1;91m{nome_temporario}\033[0;1m'" if nome_temporario != "" else f"\033[1;91m''\033[0;1m"} é menor ou igual que 1 caractere. Por favor, digite outro nome maior: \033[0m")
    while len(nome_temporario) >= 15:
      os.system('cls' if os.name == 'nt' else 'clear') 
      nome_temporario = input(f"\033[1mO nome '\033[1;91m{nome_temporario}\033[0;1m' é maior ou igual que 15 caracteres. Por favor, digite outro nome menor: \033[0m")
    self.nome = nome_temporario
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
      msg_continuar = [f"\033[1m{self.nome}, agora que já terminamos de nos apresentarmos, gostaria de começar a nossa prática em lógica matemática?\033[0m\n",
                       "\033[1mDigite '\033[1;92msim\033[0;1m' para continuar, ou caso não queira digite '\033[1;91mnão\033[0;1m': \033[0m",
                       f"{f"\033[1;95mPor favor {self.nome}, digite uma opção válida.\033[0m\n" if TF else ""}"]
      os.system('cls' if os.name == 'nt' else 'clear')
      continuar = input(f"{msg_continuar[0]}{msg_continuar[2]}{msg_continuar[1]}").lower()
      
      os.system('cls' if os.name == 'nt' else 'clear')
      if continuar == "sim": self.contas()
      if (continuar == "sim") or (continuar == "não" or continuar == "nao"): 
        print("\033[1mCaso tenha interesse de ver ou rever o projeto, estaremos te esperando. Que tenha uma boa EXPOTEC 2024 no Maria Pires Lima.\033[0m")
        break
      else: TF = True

  def LVLs(self, AA, BB, LVL, tip=0):
    LVLsom = {1:((AA == 0 or BB == 0) or (abs(AA) == 1 or abs(BB) == 1) or (abs(AA) > 50 or abs(BB) > 25)), 
              2:((AA == 0 or BB == 0) or (abs(AA) == 1 or abs(BB) == 1) or (abs(AA) > 50 or abs(BB) > 75)), 
              3:((AA == 0 or BB == 0) or (abs(AA) == 1 or abs(BB) == 1) or (abs(AA) > 100 or abs(BB) > 75)), 
              4:((AA == 0 or BB == 0) or (abs(AA) == 1 or abs(BB) == 1) or (abs(AA) > 100 or abs(BB) > 125))}
    
    LVLsub = {1:((AA == 0 or BB == 0) or (abs(AA) == 1 or abs(BB) == 1) or (abs(AA) > 50 or abs(BB) > 25)), 
              2:((AA == 0 or BB == 0) or (abs(AA) == 1 or abs(BB) == 1) or (abs(AA) > 50 or abs(BB) > 75)), 
              3:((AA == 0 or BB == 0) or (abs(AA) == 1 or abs(BB) == 1) or (abs(AA) > 100 or abs(BB) > 75)), 
              4:((AA == 0 or BB == 0) or (abs(AA) == 1 or abs(BB) == 1) or (abs(AA) > 100 or abs(BB) > 125))}
    
    LVLmul = {1:(AA * BB == 0 or (abs(AA) == 1 or abs(BB) == 1) or (abs(AA) > 11 or abs(BB) > 10)), 
              2:(AA * BB == 0 or (abs(AA) == 1 or abs(BB) == 1) or (abs(AA) > 15 or abs(BB) > 10)), 
              3:(AA * BB == 0 or (abs(AA) == 1 or abs(BB) == 1) or (abs(AA) > 35 or abs(BB) > 10)), 
              4:(AA * BB == 0 or (abs(AA) == 1 or abs(BB) == 1) or (abs(AA) > 55 or abs(BB) > 10))}
    
    LVLdiv = {1:((AA == 0 or BB == 0 or abs(BB) == 1) or abs(AA) == abs(BB) or AA % BB != 0 or abs(AA / BB) == 2 or (abs(AA) > 100 or abs(BB) > 35)), 
              2:((AA == 0 or BB == 0 or abs(BB) == 1) or abs(AA) == abs(BB) or AA % BB != 0 or abs(AA / BB) == 2 or (abs(AA) > 115 or abs(BB) > 45)), 
              3:((AA == 0 or BB == 0 or abs(BB) == 1) or abs(AA) == abs(BB) or AA % BB != 0 or abs(AA / BB) == 2 or (abs(AA) > 130 or abs(BB) > 55)), 
              4:((AA == 0 or BB == 0 or abs(BB) == 1) or abs(AA) == abs(BB) or AA % BB != 0 or abs(AA / BB) == 2 or (abs(AA) > 145 or abs(BB) > 95))}
    
    if tip == 1: return LVLsom[LVL]
    elif tip == 2: return LVLsub[LVL]
    elif tip == 3: return LVLmul[LVL]
    elif tip == 4: return LVLdiv[LVL]

  def contas(self, TF=True):
    XP = [2, 2, 2, 2] # SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO
    LVL = [int(XP[0]/2) if XP[0]/2 <= 4 else 4 for xp in XP]  
    
    def nums():
      dado = random.randint(1, 4)
      num_A, num_B = random.randint(-150, 150), random.randint(-150, 150)
      while self.LVLs(num_A, num_B, LVL[dado - 1], tip=dado):
        num_A, num_B = random.randint(-150, 150), random.randint(-150, 150)
      return dado, num_A, num_B
    
    dado, num_A, num_B = nums()
    while TF:
      LVL = [int(XP[0]/2) if XP[0]/2 <= 4 else 4 for xp in XP]       
      sinal, resultado, str_conta = {1: "+", 2: "-", 3: "x", 4: "/"}, {1:int(num_A + num_B), 2:int(num_A - num_B), 3:int(num_A * num_B), 4:int(num_A / num_B)}, {1: "SOMA", 2: "SUBTRAÇÃO", 3: "MULTIPLICAÇÃO", 4: "DIVISÃO"}
      In = {1:"+" if num_A > 0 else "", 2:"+" if num_B > 0 else "", 3:"+" if int(resultado[dado]) > 0 else ""}
      while_erros = 1

      msg_resposta = f'\033[1;96m(Digite a letra "\033[1;97mS\033[1;96m" para sair, ou a letra "\033[1;97mP\033[1;96m" para pular a questão) \
\n(\033[1;97m{str_conta[dado]} \033[1;96m\ \033[1;97mNÍVEL {LVL[dado-1]}/4\033[1;96m) Qual é o resultado de \
(\033[1;97m{In[1]}{num_A}\033[1;96m) \033[1;97m{sinal[dado]} \033[1;96m(\033[1;97m{In[2]}{num_B}\033[1;96m): \033[0m' # pergunta

      msg_respondida = f'\033[1;96m(\033[1;97m{str_conta[dado]} \033[1;96m\ \033[1;97mNÍVEL {LVL[dado-1]}/4\033[1;96m) Qual é o resultado de \
(\033[1;97m{In[1]}{num_A}\033[1;96m) \033[1;97m{sinal[dado]} \033[1;96m(\033[1;97m{In[2]}{num_B}\033[1;96m): \033[0m' # pergunta já feita

      msg_True = f'\033[1;92mCerto, o resultado de \
(\033[1;97m{In[1]}{num_A}\033[1;92m) \033[1;97m{sinal[dado]} \033[1;92m(\033[1;97m{In[2]}{num_B}\033[1;92m) é: \033[1;97m{In[3]}{int(resultado[dado])}\033[0m' # certo

      msg_pulada = f'\033[1;92mO resultado correto de \
(\033[1;97m{In[1]}{num_A}\033[1;92m) \033[1;97m{sinal[dado]} \033[1;92m(\033[1;97m{In[2]}{num_B}\033[1;92m) é: \033[1;97m{In[3]}{int(resultado[dado])}\033[0m' # pulou
      
      msg_error = '\033[1;95m||Entrada inválida. Por favor, digite um número ou uma opção válida||\n\033[0m' # erro Value

      resposta = input(msg_resposta) # Local aonde o usuário vai responder a questão matemática
      os.system('cls' if os.name == 'nt' else 'clear') 
      if resposta.lower() == 's': break # Caso responda com "s", ele encerra o programa
      if resposta.lower() == "p": 
        print(f"{msg_respondida}{resposta}\n{msg_pulada}\n")
        dado, num_A, num_B = nums()
        continue
      try: 
        resposta = int(resposta) 
        if resposta == resultado[dado]: # resposta está certa
          print(f"{msg_respondida}{resposta}\n{msg_True}\n")
          dado, num_A, num_B = nums()
          XP[dado-1] += 1
          while_erros = 0
          continue
        else:  # resposta está errada
          print(f"{X_erros(self.nome, resposta, resultado[dado], while_erros, dado)}\n{msg_respondida}{resposta}\n")
          while True:
            resposta = input(f"{msg_resposta}")
            os.system('cls' if os.name == 'nt' else 'clear')
            if resposta.lower() == 's':
              TF = False
              break # Caso reposda com "s", ele encerra o programa
            if resposta.lower() == "p": 
              print(f"{msg_respondida}{resposta}\n{msg_pulada}\n")
              dado, num_A, num_B = nums()
              break
            try:
              resposta = int(resposta)
              if resposta == resultado[dado]: 
                os.system('cls' if os.name == 'nt' else 'clear') 
                print(f"{msg_respondida}{resposta}\n{msg_True}\n")
                dado, num_A, num_B = nums()
                XP[dado-1] += 1
                while_erros = 0
                break
              else:
                while_erros += 1
                print(f"{X_erros(self.nome, resposta, resultado[dado], while_erros, dado)}\n{msg_respondida}{resposta}\n")
            except ValueError:
              os.system('cls' if os.name == 'nt' else 'clear') 
              print(msg_error)
              continue
          continue
      except ValueError: # Caso use um caractere que não seja número ou a letra de saída, acontece isso
        os.system('cls' if os.name == 'nt' else 'clear')
        print(msg_error)
        continue

Player = Calculadora_random()
Player.iniciar()