import webbrowser
from datetime import datetime

print("Dica! A senha poode ter no maximo 12 caracteres")

def programa_principal():
    while True:
        try:
            senha = input("Confirme a senha para liberar acesso: ")
        except ValueError:
            print("Erro! Digite um número válido!")
            continue
        if validar_senha(senha):
            print("Acesso Permitido")
            Menu()
        else:
            print("Acesso Negado")
        
        
def validar_senha(senha):
    tem_letra = False
    tem_Numero = False
    for caractere in senha:
        if caractere.isnumeric():
            tem_Numero = True
        elif caractere.isalpha():
            tem_letra = True
            
    certo = "Nathan123"
    if senha == certo:
        return True
    elif len(senha) >= 9 and len(senha) < 12 and tem_Numero and tem_letra:
        return True
    else:
        return False
 
def Menu():
    while True:
        print("1-playlist(YT)Forró\n2-Data\n3-Sair\n4-SO PEDRADA\n5-Área Matematica")
        try:
            numero = int(input("Digite seu número:"))
        except ValueError:
            print("Erro! Digite um número válido!")
            continue
        if numero == 1:
            Abrir_Playlist_1()
        elif numero == 2:
            Abrir_data_2()
        elif numero == 3:
            print("Saindo do programa!")
            break
        elif numero == 4:
            Playlist_Funk_4()
        elif numero == 5:
            Area_Matemática_5()
            print("1-Coverter Real em Dolar\n2-Coversor Dolar em Real\n3-Indentificador de ano bissexto\n4-Sair")
        else:
            print("Opção inválida!")
 
def Abrir_Playlist_1():
        webbrowser.open(
"https://youtube.com/playlist?list=PLCCa9PWFPxCNY83ZJyZ4kwHTyECSbHNPU&si=WUwCZLp7pUxFDwBC"
)
    
def Abrir_data_2():
        atualmente = datetime.now()
        print("Hora atual", atualmente.strftime("%H:%M:%S:"))

def Sair_3():
    print("Saindo do programa!")

def Playlist_Funk_4():
    webbrowser.open(
            "http://youtube.com/playlist?list=PL9DYbNmWUV5kK4EAwullMNMEcD-ZLllsE"
        )
def Area_Matemática_5():
    while True:
        print("1-Coverter Real em Dolar\n2-Coversor Dolar em Real\n3-Indentificador de ano bissexto\n4-Sair")
        try:
            escolha = int(input("Escolha a opçaão: "))
        except:
            print("Digite um numero")
            continue
        
        if escolha == 1:
            valor=float(input("Digite seu valor: "))
            resultado=Coverter_Real_em_Dolar(valor)
            print("Seu valor é: %.1f" % resultado)
            
        elif escolha == 2:
            valor=float(input("Digite seu valor: "))
            resultado=Coversor_Dolar_em_Real(valor)
            print("Seu valor é: %.1f" % resultado)
            
        elif escolha == 3:
            valor=float(input("Digite seu valor: "))
            if Indentificador_de_ano_bissexto(valor):
                print("È ano Bissexto")
            else:
                print("não é ano Bissexto")
        elif escolha == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

def Coverter_Real_em_Dolar(valor):
    return valor / 5.23
    
def Coversor_Dolar_em_Real(valor):
    return valor * 5.23
    
def Indentificador_de_ano_bissexto(valor):
    if (valor % 400 == 0) or (valor % 4 == 0 and valor % 100 != 0):
        return True
    return False

programa_principal()
