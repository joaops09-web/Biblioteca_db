def listar(cursor):
    print("\n--- LISTA DE USUÁRIOS ---")
    cursor.execute("SELECT * FROM usuarios")
    linhas = cursor.fetchall()
    if not linhas:
        print("Nenhum usuário cadastrado.")
    for linha in linhas:
        print(linha)
        