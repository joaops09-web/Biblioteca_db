import sqlite3
import Biblioteca_db.dados_usuarios as dados_usuarios
import Biblioteca_db.dados_autores as dados_autores
import Biblioteca_db.dados_editoras as dados_editoras
import Biblioteca_db.dados_livros as dados_livros
import Biblioteca_db.dados_emprestimos as dados_emprestimos
import Biblioteca_db.dados_emprestimos_livro as dados_emprestimos_livro

import Biblioteca_db.lista_usuarios as lista_usuarios

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT);")
cursor.execute("CREATE TABLE IF NOT EXISTS autores (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT);")
cursor.execute("CREATE TABLE IF NOT EXISTS editoras (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT);")
cursor.execute("CREATE TABLE IF NOT EXISTS livros (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, autor_id INTEGER, editora_id INTEGER, ano_publicacao INTEGER, edicao TEXT, disponivel TEXT);")
cursor.execute("CREATE TABLE IF NOT EXISTS emprestimos (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario_id INTEGER, data TEXT);")
cursor.execute("CREATE TABLE IF NOT EXISTS emprestimos_livros (emprestimo_id INTEGER, livro_id INTEGER, data_devolucao TEXT);")
conn.commit()

while True:
    print("\n==============================")
    print("     SISTEMA DA BIBLIOTECA    ")
    print("==============================")
    print("1. Cadastrar Usuário      2. Listar Usuários")
    print("3. Cadastrar Autor")
    print("5. Cadastrar Editora")
    print("7. Cadastrar Livro")
    print("9. Criar Empréstimo")
    print("11. Vincular Livro/Emp.")
    print("0. Sair")
    print("==============================")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        dados_usuarios.cadastrar(cursor, conn)
    elif opcao == "2":
        lista_usuarios.listar(cursor)
    elif opcao == "3":
        dados_autores.cadastrar(cursor, conn)
    elif opcao == "5":
        dados_editoras.cadastrar(cursor, conn)
    elif opcao == "7":
        dados_livros.cadastrar(cursor, conn)
    elif opcao == "9":
        dados_emprestimos.cadastrar(cursor, conn)
    elif opcao == "11":
        dados_emprestimos_livro.cadastrar(cursor, conn)
    elif opcao == "0":
        print("Fechando o programa... Valeu!")
        break
    else:
        print("Opção inválida!")

conn.close()
