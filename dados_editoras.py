def cadastrar(cursor, conn):
    print("\n--- CADASTRO DE EDITORA ---")
    nome = input("Digite o nome da editora: ")
    cursor.execute("INSERT INTO editoras (nome) VALUES (?)", (nome,))
    conn.commit()
    print("Editora cadastrada com sucesso!")
