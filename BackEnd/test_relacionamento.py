from app.database.database import SessionLocal
from app.models.categoria import Categoria
from app.models.produto import Produto


def testar_relacionamento():

    db = SessionLocal()

    try:
        categoria = Categoria(nome="Bebidas")

        produto = Produto(
            nome="Coca-Cola",
            categoria=categoria
        )

        db.add(categoria)
        db.add(produto)

        db.commit()

        print("Categoria cadastrada:", categoria.nome)
        print("Produto cadastrado:", produto.nome)
        print("Categoria do produto:", produto.categoria.nome)

    except Exception as error:
        db.rollback()
        print(f"Erro: {error}")

    finally:
        db.close()


if __name__ == "__main__":
    testar_relacionamento()