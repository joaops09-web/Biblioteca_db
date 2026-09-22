def cadastrar(cursor, conn):
    print("\n--- VINCULAR LIVRO AO EMPRÉSTIMO ---")
    emp_id = int(input("ID do Empréstimo: "))
    livro_id = int(input("ID do Livro: "))
    data_dev = input("Data de devolução prevista (DD/MM/AAAA): ")
    cursor.execute("""
        INSERT INTO emprestimos_livros (emprestimo_id, livro_id, data_devolucao)
        VALUES (?, ?, ?)
    """, (emp_id, livro_id, data_dev))
    conn.commit()
    print("Livro adicionado ao empréstimo")
