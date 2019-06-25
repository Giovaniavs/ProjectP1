import sys

TODO_FILE = 'todo.txt'
ARCHIVE_FILE = 'done.txt'

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[0;33m"

ADICIONAR = 'a'
REMOVER = 'r'
FAZER = 'f'
PRIORIZAR = 'p'
LISTAR = 'l'



def printCores(texto, cor) :
  print(cor + texto + RESET)
  
##############################################################################################################################################################################################################

def adicionar(descricao, extras): 
  lista = [(descricao, extras)]

  texto1 = lista[0][0] #DESCRIÇÃO
  texto2 = lista[0][1][0] #DATA
  texto3 = lista[0][1][1] #HORA
  texto4 = lista[0][1][2] #PRIORIDADE
  texto5 = lista[0][1][3] #CONTEXTO
  texto6 = lista[0][1][4] #PROJETO
    
  if lista[0][1][0] != "":
    texto2 = lista[0][1][0] + " "
  else:
    texto2 = lista[0][1][0]
      
  if lista[0][1][1] != "":
    texto3 = lista[0][1][1] + " "
  else:
    texto3 = lista[0][1][1]
      
  if lista[0][1][2] != "":
    texto4 = lista[0][1][2] + " "
  else:
    texto4 = lista[0][1][2]

  if lista[0][1][3] != "":
    texto5 = lista[0][1][3] + " "
  else:
    texto5 = lista[0][1][3] 
      
  if lista[0][1][4] != "":
    texto6 = lista[0][1][4] + " "
  else:
    texto6 = lista[0][1][4]
      
  string = texto2 + texto3 + texto4 + texto1 + texto5 + texto6
  
  try: 
    fp = open(TODO_FILE, 'a')
    fp.write(string + "\n")
    fp.close()
    
  except IOError as err:
    print("Não foi possível escrever para o arquivo " + TODO_FILE)
    print(err)
    return False

  return print("Atividade registrada com sucesso!")
  
  


##############################################################################################################################################################################################################
          

def horaValida(horaMin): 
    if type(horaMin) != str:
      return False
    elif len(horaMin) != 4 or not soDigitos(horaMin):
      return False
    else:
        if int(horaMin[0]) > 2:
            return False
        elif int(horaMin[0]) == 2: 
            if int(horaMin[1]) > 3:
                return False
        elif int(horaMin[2]) > 5:
            return False
    return True
  
##############################################################################################################################################################################################################

def soDigitos(numero) : 
  if type(numero) != str :
    return False
  for x in numero :
    if x < '0' or x > '9' :
      return False
  return True

##############################################################################################################################################################################################################

def dataValida(data): #(4 6 9 11) < meses de 30 dias
    if type(data) != str:
      return False
    elif len(data) != 8:
        return False
    elif "9" < data[2] > "0" and "9" < data[3] > "0":
      return False
    else:
        if int(data[0]) < 0:
            return False
        elif int(data[0]) > 3:
            return False
        elif int(data[0]) == 3 and int(data[1]) > 1:
            return False
        elif int(data[2]) > 1:
            return False
        elif int(data[2]) == 1 and int(data[3]) > 2:
            return False
        elif int(data[2]) == 0 and int(data[3]) < 1:
            return False
        elif data[2] + data[3] == "04" or data[2] + data[3] == "06" or data[2] + data[3] == "09" or data[2] + data[3] == "11":
            if data[0] + data[1] == "31":
                return False
        elif data[2] + data[3] == "02":
            if int(data[0]) > 2:
                return False
    return True
  
##############################################################################################################################################################################################################


def projetoValido(projeto): 
    if len(projeto) < 2:
        return False
    else:
        if projeto[0] != "+":
            return False
    return True
  
##############################################################################################################################################################################################################

def contextoValido(projeto): 
    if len(projeto) < 2:
        return False
    else:
        if projeto[0] != "@":
            return False
    return True
  
##############################################################################################################################################################################################################

def prioridadeValida(prioridade): 
    if len(prioridade) != 3:
        return False
    else:
        if prioridade[0] + prioridade[2] != "()":
            return False
        elif (prioridade[1] >= "A" and prioridade[1] <= "Z") or (prioridade[1] >= "a" and prioridade[1] <= "z"):
            return True
        else:
            return False
    return True

##############################################################################################################################################################################################################

def organizar(linhas): 
  itens = []

  for l in linhas:
    data = '' 
    hora = ''
    pri = ''
    desc = ''
    contexto = ''
    projeto = ''
  
    l = l.strip()
    tokens = l.split()
    
    if tokens != [] and dataValida(tokens[0]) == True:
      data = tokens.pop(0)

    if tokens != [] and horaValida(tokens[0]) == True:
      hora = tokens.pop(0)
  
    if tokens != [] and prioridadeValida(tokens[0]) == True:
      pri = tokens.pop(0)
      
    if tokens != [] and projetoValido(tokens[-1]) == True:
      projeto = tokens.pop()
      
    if tokens != [] and contextoValido(tokens[-1]) ==  True:
      contexto = tokens.pop()

    for n in tokens:
      desc += n + " "

  
  itens.append((desc, (data, hora, pri, contexto, projeto)))
  return itens

##############################################################################################################################################################################################################


def listar(): 
  lista = []
  listaTemp = []
  listaResposta = []
  cont = 1
  dataFormatada = ""
  horaFormatada = ""
  
  try: 
    arquivo = open(TODO_FILE, "r")
    
  except IOError as err:
    print("Não foi possível escrever para o arquivo " + TODO_FILE)
    print(err)
    return False
  
  for n in arquivo:
    lista.append(organizar([n]))
  lista = ordenarPorDataHora(lista)
  lista = ordenarPorPrioridade(lista)

  for n in lista:
    texto1 = n[0][0] #DESCRIÇÃO
    texto2 = n[0][1][0] #DATA
    texto3 = n[0][1][1] #HORA
    texto4 = n[0][1][2] #PRIORIDADE
    texto5 = n[0][1][3] #CONTEXTO
    texto6 = n[0][1][4] #PROJETO
    
    if n[0][1][2] != "": 
      texto1 = n[0][1][2] + " "
    else:
      texto1 = n[0][1][2]
  
    if n[0][1][0] != "": 
      dataFormatada = n[0][1][0][0:2] + "/" + n[0][1][0][2:4] + "/" + n[0][1][0][4:8]
      texto2 = dataFormatada + " "
    else:
      texto2 = n[0][1][0]
      
    if n[0][1][1] != "": 
      horaFormatada = n[0][1][1][0:2] + " Horas e " + n[0][1][1][2:4] + " Minutos"
      texto3 = horaFormatada + " "
    else:
      texto3 = n[0][1][1]
      
    if n[0][1][3] != "": 
      texto5 = n[0][1][3] + " " 
    else:
      texto5 = n[0][1][3] 
      
    if n[0][1][4] != "": 
      texto6 = n[0][1][4] + " "
    else:
      texto6 = n[0][1][4]

    texto4 = n[0][0] 
    
    textao = str(cont) + " " + texto1 + texto2 + texto3 + texto4 + texto5 + texto6 #TEXTO FORMATADO DESEJADO
    

    if n[0][1][2] != "": 
      if n[0][1][2] == "(A)" or n[0][1][2] == "(a)":
        printCores(textao, BLUE + BOLD)
      elif n[0][1][2] == "(B)" or n[0][1][2] == "(b)":
        printCores(textao, RED)
      elif n[0][1][2] == "(C)" or n[0][1][2] == "(c)":
        printCores(textao, GREEN)
      elif n[0][1][2] == "(D)" or n[0][1][2] == "(d)":
        printCores(textao, YELLOW)
      else:
        print(textao) #TODOS AQUELES QUE NÃO SÃO [(A)(a)  (B)(b)  (C)(c)  (D)(d)]
    else:
      print(textao)
  
    cont += 1

##############################################################################################################################################################################################################

def ordenarPorDataHora(lista):  
  listaDoida2 = [] #Lista dos Vazios
  listaDoida1 = [] #Lista dos Numerados
  listaResposta = []
  for n in lista:
    if n[0][1][1] == "" and n[0][1][0] == "":
      listaDoida2.append(n)
    else:
      listaDoida1.append(n)
      
  for n in range(len(listaDoida1)):
    for n in range(len(listaDoida1)-1): #Algoritimo Blubble Sort para ordenar a lista conforme o pedido.
      
      if listaDoida1[n][0][1][0] != "" and listaDoida1[n+1][0][1][0] != "":
        if inverterData(listaDoida1[n][0][1][0]) > inverterData(listaDoida1[n+1][0][1][0]): #Estudo da Data!
          listaDoida1[n], listaDoida1[n+1] = listaDoida1[n+1], listaDoida1[n]
      
        elif listaDoida1[n][0][1][0] == listaDoida1[n+1][0][1][0]: #Estudo da Hora!
          if listaDoida1[n][0][1][1] != "" and listaDoida1[n+1][0][1][1] != "":
            if int(listaDoida1[n][0][1][1]) > int(listaDoida1[n+1][0][1][1]):
              listaDoida1[n], listaDoida1[n+1] = listaDoida1[n+1], listaDoida1[n]
              
          elif listaDoida1[n][0][1][1] == "" and listaDoida1[n+1][0][1][1] != "":
            listaDoida1[n], listaDoida1[n+1] = listaDoida1[n+1], listaDoida1[n]

          
              
      elif listaDoida1[n][0][1][0] == "" and listaDoida1[n+1][0][1][0] != "":
        listaDoida1[n], listaDoida1[n+1] = listaDoida1[n+1], listaDoida1[n]

      
  listaResposta = listaDoida1 + listaDoida2
  return listaResposta

##############################################################################################################################################################################################################

def ordenarPorPrioridade(lista):
  listaDoida2 = [] #Lista dos Vazios!
  listaDoida1 = [] #Lista das Prioridades!
  for n in lista:
    if n[0][1][2] == "":
      listaDoida2.append(n)
    else:
      listaDoida1.append(n)
  for n in range(len(listaDoida1)):
    for n in range(len(listaDoida1)-1):
      if (listaDoida1[n][0][1][2].upper() > listaDoida1[n+1][0][1][2].upper()) == True:
        listaDoida1[n], listaDoida1[n+1] = listaDoida1[n+1], listaDoida1[n]
        
  listaResposta = listaDoida1 + listaDoida2
  return listaResposta

##############################################################################################################################################################################################################

def fazer(indice):
  if indice.isnumeric() == False:
    return print("Apenas numérico no indice!")
  lista = []
  listaIndice = []
  cont = 1
  
  try: 
    arquivo = open(TODO_FILE, "r")
    
  except IOError as err:
    print("Não foi possível escrever para o arquivo " + TODO_FILE)
    print(err)
    return False
  
  for n in arquivo:
    lista.append(organizar([n]))
  lista = ordenarPorDataHora(lista)
  lista = ordenarPorPrioridade(lista)
  arquivo.close()
  arquivo = open(TODO_FILE,"w")
  arquivo2 = open(ARCHIVE_FILE,"a")
  for n in lista:
    texto1 = n[0][0] #DESCRIÇÃO
    texto2 = n[0][1][0] #DATA
    texto3 = n[0][1][1] #HORA
    texto4 = n[0][1][2] #PRIORIDADE
    texto5 = n[0][1][3] #CONTEXTO
    texto6 = n[0][1][4] #PROJETO
    
    if n[0][1][0] != "":
      texto2 = n[0][1][0] + " "
    else:
      texto2 = n[0][1][0]
      
    if n[0][1][1] != "":
      texto3 = n[0][1][1] + " "
    else:
      texto3 = n[0][1][1]
      
    if n[0][1][2] != "":
      texto4 = n[0][1][2] + " "
    else:
      texto4 = n[0][1][2]
      
    if n[0][1][3] != "":
      texto5 = n[0][1][3] + " "
    else:
      texto5 = n[0][1][3] 
      
    if n[0][1][4] != "":
      texto6 = n[0][1][4] + " "
    else:
      texto6 = n[0][1][4]
      
    string =  texto2 + texto3 + texto4 +  texto1 + texto5 + texto6 #STRING FORMATADA
    
    posicao = str(cont),n
    if posicao[0] != indice: #POSICAO QUE VARIA DE ACORDO COM A REMOÇÃO, PORÉM É UM VALOR CONSISTENTE
      arquivo.write(string+"\n")
      cont += 1
    else:
      arquivo2.write(string+"\n")
      cont += 1
  if int(indice) > (len(lista)) or int(indice) < 1:
    return print("O indice desejado não existe")

  arquivo.close()
  arquivo2.close()
  
  return print("Atividade feita com sucesso!")

##############################################################################################################################################################################################################

def priorizar(indice, prioridade):
  lista = []
  cont = 1
  
  try: 
    arquivo = open(TODO_FILE, "r")
    
  except IOError as err:
    print("Não foi possível escrever para o arquivo " + TODO_FILE)
    print(err)
    return False
  
  for n in arquivo:
    lista.append(organizar([n]))
  lista = ordenarPorDataHora(lista)
  lista = ordenarPorPrioridade(lista)
  
  arquivo.close()
  
  arquivo = open(TODO_FILE,"w")
  for n in lista:
    texto1 = n[0][0] #DESCRIÇÃO
    texto2 = n[0][1][0] #DATA
    texto3 = n[0][1][1] #HORA
    texto4 = n[0][1][2] #PRIORIDADE
    texto5 = n[0][1][3] #CONTEXTO
    texto6 = n[0][1][4] #PROJETO
    
    if n[0][1][0] != "":
      texto2 = n[0][1][0] + " "
    else:
      texto2 = n[0][1][0]
      
    if n[0][1][1] != "":
      texto3 = n[0][1][1] + " "
    else:
      texto3 = n[0][1][1]
      
    if n[0][1][2] != "":
      texto4 = n[0][1][2] + " "
    else:
      texto4 = n[0][1][2]
      
    if n[0][1][3] != "":
      texto5 = n[0][1][3] + " "
    else:
      texto5 = n[0][1][3] 
      
    if n[0][1][4] != "":
      texto6 = n[0][1][4] + " "
    else:
      texto6 = n[0][1][4]
      
    string = texto2 + texto3 + texto4 + texto1 + texto5 + texto6 #STRING FORMATADA

    posicao = str(cont),n
    if posicao[0] == indice: #POSICAO QUE VARIA DE ACORDO COM A ALTERAÇÃO, PORÉM É UM VALOR CONSISTENTE
      texto4 = prioridade + " "
      string = texto2 + texto3 + texto4 + texto1 + texto5 + texto6 #STRING FORMATADA
      arquivo.write(string+"\n")
      cont += 1
    else:
      arquivo.write(string+"\n")
      cont += 1
      
  if int(indice) > (len(lista)) or int(indice) < 1:
    return print("O indice desejado não existe")
  
  arquivo.close()
  
  return print("Atividade priorizada com sucesso!")
      
##############################################################################################################################################################################################################

def processarComandos(comandos):
  if len(comandos) < 2 :
    return print("Você precisa digitar algo meu consagrado")

  if len(comandos) == 2 and comandos[1].lower() != "l":
    return print("Comando inválido")
  
  if comandos[1].lower() == "f" and len(comandos) != 3:
    return print("Comando inválido")

  if comandos[1].lower() == "r" and len(comandos) != 3:
    return print("Comando inválido")
    
  
  elif comandos[1].lower() == ADICIONAR:
    palavra = ""
    comandos.pop(0) 
    comandos.pop(0)
    for n in comandos:
      palavra = palavra + n + " "
    palavraFormatada = organizar([palavra])
    return adicionar(palavraFormatada[0][0], palavraFormatada[0][1]) #DESCRIÇÃO E EXTRAS

  
  elif comandos[1].lower() == LISTAR: #LISTAR
    return listar()
  
    
  elif comandos[1].lower() == REMOVER: #REMOVER
    comandos.pop(0)
    comandos.pop(0)
    return remover(comandos[0])


  elif comandos[1].lower() == FAZER: #FAZER
    comandos.pop(0)
    comandos.pop(0)
    return fazer(comandos[0])


  elif comandos[1].lower() == PRIORIZAR: #PRIORIZAR
    if len(comandos) != 4:
      return print("Comando Inválido")
      
    if (prioridadeValida(comandos[3]) == False):
      return print("Comando inválido")
    comandos.pop(0)
    comandos.pop(0)
    return priorizar(comandos[0],comandos[1])

##############################################################################################################################################################################################################

def remover(indice):
  if "1" < indice > "9":
    return print("Digite apenas numeros")
  
  lista = []
  listaIndice = []
  cont = 1
  
  try: 
    arquivo = open(TODO_FILE, "r")
    
  except IOError as err:
    print("Não foi possível escrever para o arquivo " + TODO_FILE)
    print(err)
    return False
  
  for n in arquivo:
    lista.append(organizar([n]))
  lista = ordenarPorDataHora(lista)
  lista = ordenarPorPrioridade(lista)
  
  arquivo.close()
  
  arquivo = open(TODO_FILE,"w")
  for n in lista:
    texto1 = n[0][0] #DESCRIÇÃO
    texto2 = n[0][1][0] #DATA
    texto3 = n[0][1][1] #HORA
    texto4 = n[0][1][2] #PRIORIDADE
    texto5 = n[0][1][3] #CONTEXTO
    texto6 = n[0][1][4] #PROJETO
    
    if n[0][1][0] != "":
      texto2 = n[0][1][0] + " "
    else:
      texto2 = n[0][1][0]
      
    if n[0][1][1] != "":
      texto3 = n[0][1][1] + " "
    else:
      texto3 = n[0][1][1]
      
    if n[0][1][2] != "":
      texto4 = n[0][1][2] + " "
    else:
      texto4 = n[0][1][2]

    if n[0][1][3] != "":
      texto5 = n[0][1][3] + " "
    else:
      texto5 = n[0][1][3] 
      
    if n[0][1][4] != "":
      texto6 = n[0][1][4] + " "
    else:
      texto6 = n[0][1][4]
      
    string = texto2 + texto3 + texto4 + texto1 + texto5 + texto6 #STRING FORMATADA
    
    posicao = str(cont),n
    if posicao[0] != indice: #POSICAO QUE VARIA DE ACORDO COM A REMOÇÃO, PORÉM É UM VALOR CONSISTENTE
      arquivo.write(string+"\n")
      cont += 1
    else:
      cont += 1

  if int(indice) > (len(lista)) or int(indice) < 1:
    return print("O indice desejado não existe")

  arquivo.close()
  return print("Atividade removida com sucesso!")
   

def inverterData(string):
  lista = []
  for n in string:
    lista.append(n)
  dataInvertida = lista[4] + lista[5] + lista[6] + lista[7] +lista[0] + lista[1] + lista[2] + lista[3]
  
  return int(dataInvertida)

processarComandos(sys.argv)

