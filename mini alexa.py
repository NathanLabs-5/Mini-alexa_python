import pyautogui
import os
import time
import webbrowser
from datetime import datetime
import mysql.connector
import pyttsx3
from dotenv import load_dotenv

load_dotenv()

engine = pyttsx3.init()

print("Dica! A senha pode ter no máximo 12 caracteres")

simbolos = ["@", "#", "$", "_", ".", "="]


# ========================= BANCO =========================

class BancoEnv:

    def __init__(self):
        self.conexao = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE")
        )

        self.cursor = self.conexao.cursor()

    def fechar(self):

        if self.cursor:
            self.cursor.close()

        if self.conexao:
            self.conexao.close()


# ========================= LEMBRETES =========================

class LembreteService:

    def __init__(self, banco):
        self.banco = banco

    def inserir_lembrete(self, descricao):

        try:
            sql = "INSERT INTO lembretes (descricao) VALUES (%s)"

            self.banco.cursor.execute(sql, (descricao,))
            self.banco.conexao.commit()

            print("Lembrete inserido com sucesso!")

        except mysql.connector.Error as erro:
            print(f"Erro ao inserir lembrete: {erro}")

    def listar_lembretes(self):

        try:
            self.banco.cursor.execute("SELECT * FROM lembretes")

            return self.banco.cursor.fetchall()

        except mysql.connector.Error as erro:
            print(f"Erro ao listar lembretes: {erro}")

            return []

    def atualizar_lembrete(self, nova_descricao, id_lembrete):

        try:
            sql = "UPDATE lembretes SET descricao = %s WHERE id = %s"

            self.banco.cursor.execute(sql, (nova_descricao, id_lembrete))
            self.banco.conexao.commit()

            if self.banco.cursor.rowcount == 0:
                print("Nenhum registro encontrado!")
            else:
                print("Lembrete atualizado com sucesso!")

        except mysql.connector.Error as erro:
            print(f"Erro ao atualizar lembrete: {erro}")

    def deletar_lembrete(self, id_lembrete):

        try:
            sql = "DELETE FROM lembretes WHERE id = %s"

            self.banco.cursor.execute(sql, (id_lembrete,))
            self.banco.conexao.commit()

            if self.banco.cursor.rowcount == 0:
                print("Nenhum registro encontrado!")
            else:
                print("Lembrete deletado com sucesso!")

        except mysql.connector.Error as erro:
            print(f"Erro ao deletar lembrete: {erro}")


# ========================= ANIVERSÁRIOS =========================

class AniversarioService:

    def __init__(self, banco):
        self.banco = banco

    def inserir_aniversario(self, nome, data):

        try:
            sql = "INSERT INTO data_aniversario (nome, data) VALUES (%s, %s)"

            self.banco.cursor.execute(sql, (nome, data))
            self.banco.conexao.commit()

            print("Aniversário inserido com sucesso!")

        except mysql.connector.Error as erro:
            print(f"Erro ao inserir aniversário: {erro}")

    def listar_aniversarios(self):

        try:
            self.banco.cursor.execute("SELECT * FROM data_aniversario")

            return self.banco.cursor.fetchall()

        except mysql.connector.Error as erro:
            print(f"Erro ao listar aniversários: {erro}")

            return []

    def atualizar_aniversario(self, nome, data, id_aniversario):

        try:
            sql = """
            UPDATE data_aniversario
            SET nome = %s, data = %s
            WHERE id = %s
            """

            self.banco.cursor.execute(sql, (nome, data, id_aniversario))
            self.banco.conexao.commit()

            if self.banco.cursor.rowcount == 0:
                print("Nenhum registro encontrado!")
            else:
                print("Aniversário atualizado com sucesso!")

        except mysql.connector.Error as erro:
            print(f"Erro ao atualizar aniversário: {erro}")

    def deletar_aniversario(self, id_aniversario):

        try:
            sql = "DELETE FROM data_aniversario WHERE id = %s"

            self.banco.cursor.execute(sql, (id_aniversario,))
            self.banco.conexao.commit()

            if self.banco.cursor.rowcount == 0:
                print("Nenhum registro encontrado!")
            else:
                print("Aniversário deletado com sucesso!")

        except mysql.connector.Error as erro:
            print(f"Erro ao deletar aniversário: {erro}")


# ========================= MENUS CRUD =========================

def menu_lembretes(lembrete_service):

    while True:

        print("""
MENU LEMBRETES
1 - Inserir
2 - Atualizar
3 - Deletar
4 - Listar
5 - Sair
""")

        try:
            escolha = int(input("Escolha: "))

        except ValueError:
            print("Digite apenas números!")
            continue

        match escolha:

            case 1:

                descricao = input("Informe o lembrete: ")

                lembrete_service.inserir_lembrete(descricao)

            case 2:

                dados = lembrete_service.listar_lembretes()

                for item in dados:
                    print(f"ID: {item[0]} | Lembrete: {item[1]}")

                try:
                    id_lembrete = int(input("Informe o ID: "))

                except ValueError:
                    print("Digite apenas números!")
                    continue

                nova_descricao = input("Novo lembrete: ")

                lembrete_service.atualizar_lembrete(
                    nova_descricao,
                    id_lembrete
                )

            case 3:

                dados = lembrete_service.listar_lembretes()

                for item in dados:
                    print(f"ID: {item[0]} | Lembrete: {item[1]}")

                try:
                    id_lembrete = int(input("Informe o ID: "))

                except ValueError:
                    print("Digite apenas números!")
                    continue
                lembrete_service.deletar_lembrete(id_lembrete)

            case 4:
                dados = lembrete_service.listar_lembretes()
                for item in dados:
                    print(f"ID: {item[0]} | Lembrete: {item[1]}")
            case 5:
                break
            case _:
                print("Opção inválida!")


def menu_aniversarios(aniversario_service):

    while True:

        print("""
MENU ANIVERSÁRIOS
1 - Inserir
2 - Atualizar
3 - Deletar
4 - Listar
5 - Sair
""")

        try:
            escolha = int(input("Escolha: "))

        except ValueError:
            print("Digite apenas números!")
            continue

        match escolha:

            case 1:
                nome = input("Nome: ")
                data = input("Data (AAAA-MM-DD): ")
                aniversario_service.inserir_aniversario(nome, data)

            case 2:
                dados = aniversario_service.listar_aniversarios()

                for item in dados:
                    print(f"ID: {item[0]} | Nome: {item[1]} | Data: {item[2]}")
                try:
                    id_aniversario = int(input("Informe o ID: "))

                except ValueError:
                    print("Digite apenas números!")
                    continue

                nome = input("Novo nome: ")
                data = input("Nova data: ")

                aniversario_service.atualizar_aniversario(
                    nome,
                    data,
                    id_aniversario
                )

            case 3:

                dados = aniversario_service.listar_aniversarios()

                for item in dados:
                    print(f"ID: {item[0]} | Nome: {item[1]} | Data: {item[2]}")
                try:
                    id_aniversario = int(input("Informe o ID: "))

                except ValueError:
                    print("Digite apenas números!")
                    continue
                aniversario_service.deletar_aniversario(id_aniversario)

            case 4:
                dados = aniversario_service.listar_aniversarios()

                for item in dados:
                    print(f"ID: {item[0]} | Nome: {item[1]} | Data: {item[2]}")

            case 5:
                break
            case _:
                print("Opção inválida!")


def menu_crud(aniversario_service, lembrete_service):
    while True:
        print("""
MENU CRUD
1 - Aniversários
2 - Lembretes
3 - Sair
""")

        try:
            escolha = int(input("Escolha: "))

        except ValueError:
            print("Digite apenas números!")
            continue

        match escolha:
            case 1:
                menu_aniversarios(aniversario_service)
            case 2:
                menu_lembretes(lembrete_service)
            case 3:
                break
            case _:
                print("Opção inválida!")


# ========================= UTILIDADES =========================

def falar(texto):
    engine.say(texto)
    engine.runAndWait()

def validar_senha(senha):

    tem_numero = any(i.isdigit() for i in senha)
    tem_maiuscula = any(i.isupper() for i in senha)
    tem_minuscula = any(i.islower() for i in senha)
    tem_simbolo = any(i in simbolos for i in senha)
    quantidade = 6 < len(senha) <= 12
    if (
        quantidade and
        tem_numero and
        tem_maiuscula and
        tem_minuscula and
        tem_simbolo
    ):
        return True
    return False

# ========================= PLAYLIST =========================

def playlist():

    links = [
        "https://youtube.com/playlist?list=PLCCa9PWFPxCNY83ZJyZ4kwHTyECSbHNPU",
        "https://www.youtube.com/playlist?list=PL9DYbNmWUV5kK4EAwullMNMEcD-ZLllsE"
    ]

    escolha = input("Escolha sua playlist: ")

    indice = int(escolha) - 1

    if 0 <= indice < len(links):

        webbrowser.open(links[indice])

        time.sleep(4)

        pyautogui.click(x=420, y=512)

    else:
        print("Playlist inválida!")


# ========================= RELÓGIO =========================

def relogio():
    try:
        while True:
            agora = datetime.now()
            os.system("cls")
            print(agora.strftime("%H:%M:%S"))
            time.sleep(1)

    except KeyboardInterrupt:
        os.system("cls")
        print("Voltando ao menu...")

# ========================= MENU PRINCIPAL =========================

def menu_principal():

    banco = BancoEnv()

    lembrete_service = LembreteService(banco)

    aniversario_service = AniversarioService(banco)

    while True:

        print("""
MENU PRINCIPAL
1 - Playlist
2 - Relógio
3 - Área matemática
4 - CRUD Alexa
5 - Sair
""")

        falar("Escolha uma opção")
        try:
            escolha = int(input("Escolha: "))

        except ValueError:
            print("Digite apenas números!")
            continue

        match escolha:

            case 1:
                playlist()
            case 2:
                relogio()
            case 3:
                print("Área matemática em construção")
            case 4:
                menu_crud(
                    aniversario_service,
                    lembrete_service
                )
            case 5:
                banco.fechar()
                print("Saindo...")
                break
            case _:
                print("Opção inválida!")


# ========================= LOGIN =========================

def programa_principal():
    while True:
        falar("Confirme a senha")

        senha = input("Senha: ")

        if validar_senha(senha):
            print("Acesso permitido!")
            menu_principal()
            break
        else:
            print("Acesso negado!")


programa_principal()