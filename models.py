from sqlalchemy import Column, Date, Integer, Numeric, String, text,Table
from conexao import Base,engine

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    nome = Column(String(80), nullable=False)
    senha = Column(String(80), nullable=False)

    def __init__ (self, nome, senha):
        self.nome = nome 
        self.senha = senha

    def to_dict(self):
        dic = {
            'nome' : self.nome

        }
        return dic
