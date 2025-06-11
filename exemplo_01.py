from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine("sqlite:///meubanco.db", echo=True)


Base = declarative_base()
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)        
# Criar um usuário
novo_usuario = Usuario(nome='João', idade=30)
# Adicionar o usuário à sessão
session.add(novo_usuario)
# Salvar as alterações no banco de dados        
session.commit()
# Consultar todos os usuários           
usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(f'ID: {usuario.id}, Nome: {usuario.nome}, Idade: {usuario.idade}')
# Fechar a sessão
session.close()
# Exemplo de uso do SQLAlchemy com SQLite
# Este exemplo cria um banco de dados SQLite, define uma tabela de usuários,    
# adiciona um usuário e consulta todos os usuários existentes.
# Certifique-se de ter o SQLAlchemy instalado: poetry add sqlalchemy

# Para executar este código, certifique-se de ter o SQLAlchemy instalado:
# poetry add sqlalchemy
# O banco de dados será criado no mesmo diretório do script com o nome "meubanco.db"