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

# Imprime texto com cores. Por exemplo, para imprimir "Oi mundo!" em vermelho, basta usar
#
# printCores('Oi mundo!', RED)
# printCores('Texto amarelo e negrito', YELLOW + BOLD)

def printCores(texto, cor) :
  print(cor + texto + RESET)
  

def adicionar(descricao, extras): #completo
  string = ""
  lista = []
  listaResposta = []
  for elemento in extras:
    lista.append(elemento)
  if descricao  == '' :
    return False
  else:
      listaResposta.append(descricao)
      if dataValida(lista[0]) == True:
          listaResposta.append(lista[0])
          lista.pop(0)
      else:
          lista.pop(0)
      if horaValida(lista[0]) == True:
          listaResposta.append(lista[0])
          lista.pop(0)
      else:
          lista.pop(0)
      if prioridadeValida(lista[0]) == True:
          listaResposta.append(lista[0])
          lista.pop(0)
      else:
          lista.pop(0)
      if contextoValido(lista[0]) == True:
          listaResposta.append(lista[0])
          lista.pop(0)
      else:
          lista.pop(0)
      if projetoValido(lista[0]) == True:
          listaResposta.append(lista[0])
          lista.pop(0)
      else:
          lista.pop(0)
          
  for n in listaResposta:
    string = string + n + " "

  return string
          

def horaValida(horaMin): #completo
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

def soDigitos(numero) : #completo
  if type(numero) != str :
    return False
  for x in numero :
    if x < '0' or x > '9' :
      return False
  return True

def dataValida(data): #completo (4 6 9 11) < meses de 30 dias
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


def projetoValido(projeto): #completo
    if len(projeto) < 2:
        return False
    else:
        if projeto[0] != "+":
            return False
    return True

def contextoValido(projeto): #completo
    if len(projeto) < 2:
        return False
    else:
        if projeto[0] != "@":
            return False
    return True

def prioridadeValida(prioridade): #completo
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

        

def organizar(linhas): #completo
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
    
  for i in range(len(tokens)):
    if dataValida(tokens[0]) == True:
      data = tokens.pop(0)
    elif horaValida(tokens[0]) == True:
      hora = tokens.pop(0)
    elif prioridadeValida(tokens[0]) == True:
      pri = tokens.pop(0)
    elif contextoValido(tokens[0]) ==  True:
      contexto = tokens.pop(0)
    elif projetoValido(tokens[0]) == True:
      projeto += tokens.pop(0)
    elif (dataValida(tokens[0]) == False) and (horaValida(tokens[0]) == False) and (prioridadeValida(tokens[0]) == False) and (contextoValido(tokens[0]) == False) and (projetoValido(tokens[0]) == False):
      desc += tokens.pop(0) + " "
       
  itens.append((desc, (data, hora, pri, contexto, projeto)))
  if desc == "":
    return False

  return itens


def listar(): #COMPLETO!!
  lista = []
  listaTemp = []
  listaResposta = []
  listaNovaTemp1 = []
  listaNovaTemp2 = []
  cont = 1
  
  
  dataFormatada = ""
  horaFormatada = ""
  arquivo = open("todo.txt","r")
  for n in arquivo:
    lista.append(organizar([n]))
  lista = ordenarPorDataHora(lista)
  lista = ordenarPorPrioridade(lista)
  for n in lista:
    if listaTemp == []:
      listaTemp.append(n)
    elif n[0][1][2].upper() == listaTemp[0][0][1][2].upper():
      listaTemp.append(n)

    listaResposta = listaResposta + listaTemp
    listaTemp = []
  print(listaResposta)
    
  '''
    for n in range(len(listaTemp)):
    if listaTemp[n][0][1][0] == "":
      listaNovaTemp1.append(listaTemp[n])
    else:
      listaNovaTemp2.append(listaTemp[n])
      
  listaTemp = listaNovaTemp2 + listaNovaTemp1
  listaResposta = listaResposta + listaTemp

  if listaTemp != []:
    listaTemp = []
  '''
  

    
      
  
      

      
      
        
  '''
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
    
  return lista
    '''
def ordenarPorDataHora(lista):  #COMPLETÍSSIMO
  listaDoida2 = [] #Lista dos Vazios
  listaDoida1 = [] #Lista dos Numerados
  listaResposta = []
  for n in lista:
    if n[0][1][1] == "" or n[0][1][0]== "":
      listaDoida2.append(n)
    else:
      listaDoida1.append(n)
  for n in range(len(listaDoida1)):
    for n in range(len(listaDoida1)-1): #Algoritimo Blubble Sort para ordenar a lista conforme o pedido.
      if inverterData(listaDoida1[n][0][1][0]) > inverterData(listaDoida1[n+1][0][1][0]): #Estudo da Data!
        listaDoida1[n], listaDoida1[n+1] = listaDoida1[n+1], listaDoida1[n]
      
      elif inverterData(listaDoida1[n][0][1][0]) == inverterData(listaDoida1[n+1][0][1][0]): #Estudo da Hora!
          if int(listaDoida1[n][0][1][1]) > int(listaDoida1[n+1][0][1][1]):
            listaDoida1[n], listaDoida1[n+1] = listaDoida1[n+1], listaDoida1[n]

  listaResposta = listaDoida1 + listaDoida2
  return listaResposta

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

def fazer(indice):
  if type(indice) != str:
    return print("Meu consagrado você só pode ser jogador de FREE FIRE. Buga meu trabalho ae n po, 4:50 da manhã e to eu aq e tu querendo bugar meu projeto #revolt >:( ")
  lista = []
  listaIndice = []
  cont = 1
  ###################################################################################
  arquivo = open("todo.txt","r")
  for n in arquivo:
    lista.append(organizar([n]))
  lista = ordenarPorDataHora(lista)
  lista = ordenarPorPrioridade(lista)
  arquivo.close()
  arquivo = open("todo.txt","w")
  arquivo2 = open("done.txt","a")
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
      
    string = texto1 + texto2 + texto3 + texto4 + texto5 + texto6 #STRING FORMATADA
    
    posicao = str(cont),n
    if posicao[0] != indice: #POSICAO QUE VARIA DE ACORDO COM A REMOÇÃO, PORÉM É UM VALOR CONSISTENTE
      arquivo.write(string+"\n")
      cont += 1
    else:
      arquivo2.write(string+"\n")
      cont += 1
  if int(indice) > (len(lista)) or int(indice) < 1:
    return print("O indice desejado não existe")

  

  



# prioridade é uma letra entre A a Z, onde A é a mais alta e Z a mais baixa.
# num é o número da atividade cuja prioridade se planeja modificar, conforme
# exibido pelo comando 'l'. 
def priorizar(indice, prioridade):
  if type(indice) != str or type(prioridade) != str:
    return print("Pode não fera, só string plz")
  if prioridadeValida(prioridade) == False:
    return print("Coloca uma prioridade namoral ae po, buga meu projeto não =(")
  lista = []
  listaIndice = []
  cont = 1
  
  arquivo = open("todo.txt","r")
  for n in arquivo:
    lista.append(organizar([n]))
  lista = ordenarPorDataHora(lista)
  lista = ordenarPorPrioridade(lista)
  arquivo.close()
  arquivo = open("todo.txt","w")
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
      
    string = texto1 + texto2 + texto3 + texto4 + texto5 + texto6 #STRING FORMATADA

    posicao = str(cont),n
    if posicao[0] == indice: #POSICAO QUE VARIA DE ACORDO COM A ALTERAÇÃO, PORÉM É UM VALOR CONSISTENTE
      texto4 = prioridade + " "
      string = texto1 + texto2 + texto3 + texto4 + texto5 + texto6 #STRING FORMATADA
      arquivo.write(string+"\n")
      cont += 1
    else:
      arquivo.write(string+"\n")
      cont += 1
      
  if int(indice) > (len(lista)) or int(indice) < 1:
    return print("O indice desejado não existe")
      




# Esta função processa os comandos e informações passados através da linha de comando e identifica
# que função do programa deve ser invocada. Por exemplo, se o comando 'adicionar' foi usado,
# isso significa que a função adicionar() deve ser invocada para registrar a nova atividade.
# O bloco principal fica responsável também por tirar espaços em branco no início e fim dos strings
# usando o método strip(). Além disso, realiza a validação de horas, datas, prioridades, contextos e
# projetos. 
def processarComandos(comandos) :
  
  if len(comandos) < 2 :
    return print("Você precisa digitar algo meu consagrado")
  
  elif comandos[1].lower() == ADICIONAR:
    palavra = ""
    arquivo = open("todo.txt","a")
    comandos.pop(0) 
    comandos.pop(0)
    for n in comandos:
      palavra = palavra + n + " "
    palavraOrganizada = organizar([palavra])
    
    arquivo.write(adicionar(palavraOrganizada[0][0],palavraOrganizada[0][1])+"\n")

  elif comandos[1].lower() == LISTAR:
    return listar()
    

  elif comandos[1].lower() == REMOVER: #completo
    comandos.pop(0)
    comandos.pop(0)
    return remover(comandos[0])


  elif comandos[1].lower() == FAZER: #completo
    comandos.pop(0)
    comandos.pop(0)
    return fazer(comandos[0])


  elif comandos[1].lower() == PRIORIZAR: #completo
    comandos.pop(0)
    comandos.pop(0)
    return priorizar(comandos[0],comandos[1])


def remover(indice):
  if type(indice) != str:
    return print("Meu consagrado você só pode ser jogador de FREE FIRE. Buga meu trabalho ae n po, 4:50 da manhã e to eu aq e tu querendo bugar meu projeto #revolt >:( ")
  lista = []
  listaIndice = []
  cont = 1
  ###################################################################################
  arquivo = open("todo.txt","r")
  for n in arquivo:
    lista.append(organizar([n]))
  lista = ordenarPorDataHora(lista)
  lista = ordenarPorPrioridade(lista)
  arquivo.close()
  arquivo = open("todo.txt","w")
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
      
    string = texto1 + texto2 + texto3 + texto4 + texto5 + texto6 #STRING FORMATADA
    
    posicao = str(cont),n
    if posicao[0] != indice: #POSICAO QUE VARIA DE ACORDO COM A REMOÇÃO, PORÉM É UM VALOR CONSISTENTE
      arquivo.write(string+"\n")
      cont += 1
    else:
      cont += 1
  if int(indice) > (len(lista)) or int(indice) < 1:
    return print("O indice desejado não existe")
   

def inverterData(string):
  lista = []
  for n in string:
    lista.append(n)
  dataInvertida = lista[4] + lista[5] + lista[6] + lista[7] +lista[0] + lista[1] + lista[2] + lista[3]
  
  return int(dataInvertida)

    
  
# sys.argv é uma lista de strings onde o primeiro elemento é o nome do programa
# invocado a partir da linha de comando e os elementos restantes são tudo que
# foi fornecido em sequência. Por exemplo, se o programa foi invocado como
#
# python3 agenda.py a Mudar de nome.
#
# sys.argv terá como conteúdo
#
# ['agenda.py', 'a', 'Mudar', 'de', 'nome']
#processarComandos(sys.argv)

