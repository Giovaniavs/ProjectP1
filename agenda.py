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
  

  return listaResposta
          
          
        

  ################ COMPLETAR

'''
  # Escreve no TODO_FILE. 
  try: 
    fp = open(TODO_FILE, 'a')
    fp.write(novaAtividade + "\n")
    fp.close()
  except IOError as err:
    print("Não foi possível escrever para o arquivo " + TODO_FILE)
    print(err)
    return False

  return True
'''
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
  cont = 0
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


# Datas e horas são armazenadas nos formatos DDMMAAAA e HHMM, mas são exibidas
# como se espera (com os separadores apropridados). 
#
# Uma extensão possível é listar com base em diversos critérios: (i) atividades com certa prioridade;
# (ii) atividades a ser realizadas em certo contexto; (iii) atividades associadas com
# determinado projeto; (vi) atividades de determinado dia (data específica, hoje ou amanhã). Isso não
# é uma das tarefas básicas do projeto, porém. 
def listar():
  lista = []
  arquivo = open("todo.txt","r")
  for n in arquivo:
    lista.append(organizar([n]))
  return lista
  ################ COMPLETAR

def ordenarPorDataHora(itens):

  ################ COMPLETAR

  return itens
   
def ordenarPorPrioridade(itens):

  ################ COMPLETAR

  return itens

def fazer(num):

  ################ COMPLETAR

  return 

def remover():

  ################ COMPLETAR

  return

# prioridade é uma letra entre A a Z, onde A é a mais alta e Z a mais baixa.
# num é o número da atividade cuja prioridade se planeja modificar, conforme
# exibido pelo comando 'l'. 
def priorizar(num, prioridade):

  ################ COMPLETAR

  return 



# Esta função processa os comandos e informações passados através da linha de comando e identifica
# que função do programa deve ser invocada. Por exemplo, se o comando 'adicionar' foi usado,
# isso significa que a função adicionar() deve ser invocada para registrar a nova atividade.
# O bloco principal fica responsável também por tirar espaços em branco no início e fim dos strings
# usando o método strip(). Além disso, realiza a validação de horas, datas, prioridades, contextos e
# projetos. 
def processarComandos(comandos) :
  if comandos[1] == ADICIONAR:
    comandos.pop(0) # remove 'agenda.py'
    comandos.pop(0) # remove 'adicionar'
    itemParaAdicionar = organizar([' '.join(comandos)])[0]
    # itemParaAdicionar = (descricao, (prioridade, data, hora, contexto, projeto))
    adicionar(itemParaAdicionar[0], itemParaAdicionar[1]) # novos itens não têm prioridade
  elif comandos[1] == "l":
    return listar()
    ################ COMPLETAR

  elif comandos[1] == REMOVER:
    return    

    ################ COMPLETAR    

  elif comandos[1] == FAZER:
    return    

    ################ COMPLETAR

  elif comandos[1] == PRIORIZAR:
    return    

    ################ COMPLETAR

  else :
    print("Comando inválido.")
    
  
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
