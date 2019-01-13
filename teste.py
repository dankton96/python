import platform, os, time

###############################################################constants#######################################################
delaySecond=time.sleep()
MenuText="""
            1)Registrar chamada
            2)Ler Ficheiro
            3)Listar Clientes
            4)Fatura
            5)Terminar
          """
allowPhoneChar=['1','2','3','4','5','6','7','8','9','0','+']
#################################################################################################################################
def isPhoneValid(string):
    if(string[0]=='+'):
        if(len(string)<4):return False
    else:
        if(len(string)<3):return False
    if(string[0] not in allowPhoneChar):return False
    for c in string[1:]:
        if(c not in allowPhoneChar[:-1]):return False
    return True

def ClearScreen():
    if(platform.system()=="Windows"): os.system("cls")
    if(platform.system()=="Linux"): os.system("clear")

def safeFileOpen(mode,filePath):
    if mode not in ['r','w','x','a','t','b','r+','w+','x+','a+','t+','b+']:
        return "InvalidOpenMode"
    else:
        try:
            arq=open(mode,filePath)
            return arq
        except IOError as e:
            arq=e.strerror()
            return arq

def inputPhone(message):
    var=input(message)
    if(isPhoneValid(var)): return var
    else: return "InvalidPhone"

def RegCall():
    arq=safeFileOpen("arq.txt","a")
    if(arq=="IOError"):
        print("Erro ao abrir o arquivo. Verifique o caminho do mesmo e/ou permissoes no local")
    else:
        while(True):
            ClearScreen()
            SourcePhone=inputPhone("Telefone de origem: ")
            while(SourcePhone=="InvalidPhone"):
                SourcePhone=inputPhone("Telefone de origem invalido. Insira um numero valido:")
            DestPhone=inputPhone("Telefone de destino: ")
            while(DestPhone=="InvalidPhone"):
                DestPhone=inputPhone("Telefone de destino invalido. Insira um numero valido:")

def menu():
    ClearScreen()
    op="InvalidOption"
    while(op=="InvalidOption" or op!=5):
        try:    
            op=int(input(MenuText))
            ClearScreen()
            if(op not in list(range(1,6))):
                print("Opcao invalida. Selecione as opcoes disponiveis (1-5)")
                delaySecond(3)
                op="InvalidOption"
            elif(op==1):
                
        except TypeError:
            print("Opcao invalida. Selecione as opcoes disponiveis (1-5)")
            delaySecond(3)
            op="InvalidOption"
    return op
#op=0
#while(op!=5):
 #   if(op==1)
