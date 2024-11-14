def DEFeval(expression):
  expression = expression.lower()
  print(f"1.Expressão convertida em formato de programação: {expression}\n")
  start = [False, 0, 0]
  list_split = []
  list_scientific = []
  for character in list(expression):
    if character == "(": start[0] = True
    if character == ")": start[0], start[2] = False, 1
    if start[0]: 
      if not character == "(" or character == ")": list_split.append(character)
    if start[2] == 1:
      start[2] = 0
      if "e" in list_split:
        start[1] += 1
        list_scientific.append("")
        for join in range(0, len(list_split)):
          list_scientific[start[1]-1] = list_scientific[start[1]-1] + list_split[join]
        list_split = []
        print(f"2.números de notação cientifica que serão convertidos em equação programavel:\n{list_scientific}")

  list_calc = [] # Lista para armazenar a nova expressão com a notação científica convertida
  list_positions = [positions.split("e") for positions in list_scientific] # Divide cada parte em base e expoente se houver 'e'
  print(f"\n3.números quebrados para reorganização na conversão:\n{list_positions}\n")
  for i in range(0, len(list_scientific)): # Converte a notação científica, se houver, e armazena o resultado em list_calc
    if len(list_positions[i]) == 2:  # Caso com notação científica
      calc = f"({list_positions[i][0]}*(10**({list_positions[i][1]})))"
      list_calc.append(calc)
    elif len(list_positions[i]) == 1:  # Caso sem notação científica
      list_calc.append(list_positions[i][0])
  values_change = {} # Cria o dicionário para substituição
  for original, converted in zip(list_scientific, list_calc):
    values_change[original] = converted
  for content_part, calc_part in values_change.items(): # Substitui os valores de content por list_calc em a
    expression = expression.replace(content_part, calc_part) 
  if len(expression) >= 25: expression = f"(({expression})/1)"

  print("4.Expressão convertida para evitar alguuns erros float:", expression)
  result = str(eval(expression)) # Calcula o resultado da expressão
  if str(float(result)).split(".")[1] == "0" and len(str(float(result)).split(".")[1]) == 1:
    result = str((result).split('.')[0])  # Converte para int se for inteiro
  print(f"5.Resultado bruto: {result}")

  cond_round = True
  for i in list(result): 
    if i == "e": cond_round = False
  for i in list(result):
    if i in ["-", "e"]: 
      result = f"({str(result)})" 
      break
  
  if cond_round and len(result.split(".")) == 2:
    if (len(list(filter(lambda result: result == "0" , result.split(".")[1])))) >= 8:
      len_number = [0, 0] # quantos numeros, zeros
      for numbers in (result.split(".")[1])[::-1]:
        if numbers != "0" and len_number[1] > 2: break
        if numbers != "0": len_number[0] += 1
        elif numbers == "0" and len_number[0] > 0: len_number[1] += 1
      variation = len(result.split(".")[1]) - (len_number[0] + len_number[1])

      for k in list(result):
        if k in ["-", "e"]:
          result = f"({str(round(float(result.strip("()")), variation+len(result.split(".")[0])))})"
          break
        else: result = f"{str(round(float(result.strip("()")), variation+len(result.split(".")[0])))}"

  print("6.Resultado reformulado:", result.replace('.', ','))
  return result.replace('.', ',')