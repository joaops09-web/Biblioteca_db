def cadastrar(cursor, conn):
    print("\n--- CADASTRO DE AUTOR ---")
    nome = input("Digite o nome do autor: ")
    cursor.execute("INSERT INTO autores (nome) VALUES (?)", (nome,))
    conn.commit()
    print("Autor cadastrado com sucesso!")
