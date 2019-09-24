import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import inspect

Base = declarative_base()


def as_dict(obj):
    mapper = inspect(obj).mapper
    data = {c.key: getattr(obj, c.key)
            for c in mapper.column_attrs}

    for relation in mapper.relationships :
        if relation.direction.name == 'MANYTOONE' : continue
        items = getattr(obj, relation.key)
        array = []
        for item in items:
            array.append(as_dict(item))
        data[relation.key] = array

    return data

class Pessoa(Base):
    __tablename__='Pessoa'
    pessoaId = Column(Integer, primary_key = True, autoincrement = True)
    Nome = Column(String(140), nullable = False)
    DataNas = Column(DateTime, default=datetime.datetime.utcnow)
    endereco = relationship("Endereco")
    telefone = relationship("Telefone")

class Endereco(Base):
    __tablename__='Endereco'
    enderecoId = Column(Integer, primary_key = True, autoincrement = True)
    Rua = Column(String(140), nullable = False)
    Numero = Column(Integer, nullable = False)
    CEP = Column(Integer, nullable = False)
    Bairro = Column(String(140), nullable = False)
    Cidade = Column(String(140), nullable = False)
    Estado = Column(String(140), nullable = False)
    pessoaId = Column(Integer, ForeignKey('Pessoa.pessoaId'))
    

class Telefone(Base):
    __tablename__='Telefone'
    telefoneId = Column(Integer, primary_key = True, autoincrement = True)
    DDD = Column(Integer, nullable = False)
    Numero = Column(Integer, nullable = False)
    pessoaId = Column(Integer, ForeignKey('Pessoa.pessoaId'))

engine = create_engine('mysql+pymysql://root:@localhost:3306/Sharabadaias')
Base.metadata.create_all(engine)