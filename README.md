# Mini Alexa - Python Terminal Assistant 🤖

Projeto desenvolvido em Python com foco na evolução prática em lógica de programação, orientação a objetos, integração com banco de dados e organização de aplicações no terminal.

---

## 🎯 Objetivo

Consolidar conhecimentos em desenvolvimento backend através da criação de uma assistente virtual em terminal com múltiplas funcionalidades e integração com MySQL.

---

## 🧠 Conceitos Aplicados

### Fundamentos

* Estruturas condicionais (`if/else`)
* Laços de repetição (`while`)
* Tratamento de exceções (`try/except`)
* Validação de dados
* Modularização com funções
* Manipulação de datas (`datetime`)

### Programação Orientada a Objetos

* Classes e objetos
* Métodos
* Encapsulamento
* Separação de responsabilidades

### Banco de Dados

* CRUD completo com MySQL
* Integração usando `mysql-connector`
* Organização de serviços
* Persistência de dados

### Segurança e Configuração

* Uso de variáveis de ambiente com `.env`
* Proteção de credenciais usando `.gitignore`
* Arquivo `.env.example` para configuração do projeto

### Bibliotecas Utilizadas

* `mysql.connector`
* `pyttsx3`
* `pyautogui`
* `webbrowser`
* `python-dotenv`

---

## 📌 Funcionalidades

### 🔐 Sistema de autenticação

* Validação de senha forte
* Verificação de:

  * Letras maiúsculas
  * Letras minúsculas
  * Números
  * Caracteres especiais

### 🎵 Sistema de playlists

* Abertura automática de playlists no navegador
* Automação com PyAutoGUI

### ⏰ Relógio em tempo real

* Atualização dinâmica no terminal

### 🧮 Área matemática

* Conversor Real ↔ Dólar
* Conversor Celsius ↔ Fahrenheit
* Identificador de ano bissexto

### 🗂️ CRUD Alexa

#### Lembretes

* Inserir
* Atualizar
* Listar
* Deletar

#### Datas comemorativas

* Inserir aniversários
* Atualizar registros
* Listar registros
* Deletar registros

---

## 🏗️ Estrutura Atual

O projeto atualmente utiliza:

* Menus interativos
* Separação por serviços
* Integração com banco de dados
* Organização orientada a objetos
* Variáveis de ambiente
* Tratamento de erros

---

## 🚀 Evolução do Projeto

### v1

* Estrutura inicial
* Menu funcional
* Primeiros testes de lógica

### v2

* Refatoração com funções
* Área matemática
* Conversores
* Melhor organização do código

### v3

* Integração com MySQL
* CRUD completo
* Uso de `.env`
* Organização orientada a objetos
* Serviços separados
* Melhor tratamento de erros
* Refatoração geral do sistema

---

## ⚙️ Configuração do Projeto

### Instalar dependências

```bash
pip install mysql-connector-python
pip install pyttsx3
pip install pyautogui
pip install python-dotenv
```

### Configurar `.env`

```env
HOST=
USER=
PASSWORD=
DATABASE=
```

---

## 👨‍💻 Autor

NathanLabs5
Estudante de Sistemas de Informação
