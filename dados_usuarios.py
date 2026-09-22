def cadastrar(cursor, conn):
    print("\n--- CADASTRO DE USUÁRIO ---")
    nome = input("Digite o nome do usuário: ")
    cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome,))
    conn.commit()
    print("Usuário cadastrado com sucesso!")
