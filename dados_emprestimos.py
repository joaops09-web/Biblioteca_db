def cadastrar(cursor, conn):
    print("\n--- NOVO EMPRÉSTIMO ---")
    usuario_id = int(input("ID do Usuário: "))
    data = input("Data do empréstimo (DD/MM/AAAA): ")
    cursor.execute("INSERT INTO emprestimos (usuario_id, data) VALUES (?, ?)", (usuario_id, data))
    conn.commit()
    print(f"Empréstimo registrado! ID gerado: {cursor.lastrowid}")
