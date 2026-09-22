from app.database.database import Base, engine
from app.models.categoria import Categoria
from app.models.produtos import Produto

Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")