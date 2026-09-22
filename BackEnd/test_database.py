from app.database.database import engine


def testar_conexao():
    try:
        with engine.connect() as connection:
            print("Conexão com o banco realizada com sucesso!")

    except Exception as error:
        print(f"Erro ao conectar ao banco: {error}")


if __name__ == "__main__":
    testar_conexao()