def cadastrar(cursor, conn):
    print("\n--- CADASTRO DE LIVRO ---")
    titulo = input("Título do livro: ")
    autor_id = int(input("ID do Autor: "))
    editora_id = int(input("ID da Editora: "))
    ano = int(input("Ano de publicação: "))
    edicao = input("Edição: ")
    disponivel = input("Está disponível? (S/N): ").upper()
    
    cursor.execute("""
        INSERT INTO livros (titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (titulo, autor_id, editora_id, ano, edicao, disponivel))
    conn.commit()
    print("Livro cadastrado!")
