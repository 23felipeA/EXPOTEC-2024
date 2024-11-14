import random

def X_erros(nome, resposta, resultado, while_erros, conta):
  if while_erros > 3: while_erros = 3

  def DEFrelembrando(tipo=conta):
    num_ex = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
    if tipo in [1, 2]: return f"2.Relembrando {nome} que: (-{num_ex[0]}) - {num_ex[1]} = (-{num_ex[0]+num_ex[1]}) ou (-{num_ex[0]}) + (-{num_ex[1]}) = (-{num_ex[0]+num_ex[1]}); \
{num_ex[2]} + {num_ex[3]} = {num_ex[2]+num_ex[3]} ou {num_ex[2]} - (-{num_ex[3]}) = {num_ex[2]+num_ex[3]}"
    elif tipo == 3: return f"2.Relembrando {nome} que: (+{num_ex[0]}) x (-{num_ex[1]}) = ({num_ex[0]*num_ex[1]*(-1)}); (-{num_ex[2]}) x (-{num_ex[3]}) = ({num_ex[2]*num_ex[3]})"
    elif tipo == 4: 
      while ((num_ex[0] == 0 or (num_ex[1]*(-1)) == 0 or abs((num_ex[1]*(-1))) == 1) or abs(num_ex[0]) == abs((num_ex[1]*(-1))) or num_ex[0] % (num_ex[1]*(-1)) != 0):
        num_ex[0], num_ex[1] = random.randint(1, 100), random.randint(1, 100)
      while ((num_ex[2] == 0 or (num_ex[3]*(-1)) == 0 or abs((num_ex[3]*(-1))) == 1) or abs(num_ex[2]) == abs((num_ex[3]*(-1))) or num_ex[2] % (num_ex[3]*(-1)) != 0):
        num_ex[2], num_ex[3] = random.randint(1, 100), random.randint(1, 100)
      return f"2.Relembrando {nome} que: (+{num_ex[0]}) / (-{num_ex[1]}) = ({int(num_ex[0]/num_ex[1]*(-1))}); (-{num_ex[2]}) / (-{num_ex[3]}) = ({int(num_ex[2]/num_ex[3])})"

  if resposta != resultado and abs(resposta) == abs(resultado):
    num_ex = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
    MSGs = [f"1.Relembrando {nome} que: -(-{num_ex[0]}) = +{num_ex[0]}; +(-{num_ex[1]}) = -{num_ex[1]}; +(+{num_ex[2]}) = +{num_ex[2]}.",
            DEFrelembrando(),
            f"{nome}, preste bastante atenção em questão ao sinal da conta.",
            f"Tão perto {nome}, mas será que o sinal do resultado não está errado?", 
            f"O inverso de algo talvez funcione.",
            f"Menos com menos é mais, e menos com mais é menos."]
  elif abs(resultado-resposta)>=500:
    MSGs = [f"Acho que você errou na hora de digitar {nome}.",
            f"{nome}, eu acho que você errou um pouquinho.", 
            f"Com certeza isso não está certo {nome}.",]
  elif resposta in [resultado-1, resultado+1]:
    MSGs = [f"Por UMA unidade, tente novamente {nome}.",
            f"Acho que está faltando retirar ou adicionar UMA coisa aí {nome}.",
            f"{nome}, você prefere o número sucessor ou antecessor?",
            f"Vamos brincar de quente ou frio {nome}? O número é quente."]
  elif ((resposta > 0 and resultado > 0) or (resposta < 0 and resultado < 0)) and (abs(resultado-resposta)>=100): 
    num_ex = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
    MSGs = [f"1.Relembrando {nome} que: -(-{num_ex[0]}) = +{num_ex[0]}; +(-{num_ex[1]}) = -{num_ex[1]}; +(+{num_ex[2]}) = +{num_ex[2]}.",
            DEFrelembrando(),
            f"Sinal certo {nome}, mas com um número longe.",
            f"{nome}, sua resposta está distante do resultado, olhe o tipo de conta e faça o jogo de sinais.",
            f"Positivamente muito longe {nome}." if (resposta > 0 and resultado > 0) else f"Negativamente muito longe {nome}.",
            f"{nome}, o resultado é maior que 0 (um número positivo(+))." if (resposta > 0 and resultado > 0) else f"{nome}, o resultado é menor que 0 (um número negativo(-))."]
    
  elif resposta != resultado:
    numOne, numTwo = random.randint(2, 100)*(-1), random.randint(1, 100)
    num_ex = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
    MSGs = [f"1.Relembrando {nome} que: -(-{num_ex[0]}) = +{num_ex[0]}; +(-{num_ex[1]}) = -{num_ex[1]}; +(+{num_ex[2]}) = +{num_ex[2]}.",
            DEFrelembrando(),
            f"{nome}, ({numOne}) < ({numOne+1}) e (+{numTwo}) < (+{numTwo+1}), da mesma forma que (-3) < (-2) < (-1) < 0 < (+1) < (+2) < (+3)."]

    if while_erros/3 >= random.random():
      if resultado > 0 and resultado-resposta > 0: MSGs.append(f"{nome}, o resultado da conta é menor que (+{resultado+random.randint(4, 7)}).")
      elif resultado > 0 and resultado-resposta < 0: 
        maior = resultado-random.randint(4, 7)
        MSGs.append(f"{nome}, o resultado da conta é maior que ({f"+{maior}" if maior > 0 else f"{maior}"}).")

      elif resultado < 0 and resultado-resposta > 0: MSGs.append(f"{nome}, o resultado da conta é maior que ({resultado-random.randint(4, 7)}).")
      elif resultado < 0 and resultado-resposta < 0: 
        menor = resultado+random.randint(4, 7)
        MSGs.append(f"{nome}, o resultado da conta é menor que ({f"+{menor}" if menor > 0 else f"{menor}"}).")
      
      if (while_erros/3)/1.25 >= random.random() + 0.1:
        if resultado > 0: 
          menor = resultado-random.randint(4, 7)
          MSGs.append(f"{nome}, o resultado da conta está entre ({f"+{menor}" if menor > 0 else f"{menor}"}) e (+{resultado+random.randint(4, 7)}).")
        elif resultado < 0: 
          maior = resultado-random.randint(4, 7)
          MSGs.append(f"{nome}, o resultado da conta está entre ({f"+{maior}" if maior > 0 else f"{maior}"}) e ({resultado+random.randint(4, 7)}).")

  return f"\033[93m{random.choice(MSGs)}\033[0m"