from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DBClasses import Base, Pessoa, Endereco, Telefone, engine, as_dict
from flask import Flask, jsonify

DBSession = sessionmaker(bind=engine)

def insertPessoa(nome_, datanas_):
    session = DBSession()
    p = Pessoa(Nome=nome_, DataNas=datanas_)
    session.add(p)
    session.commit()
    session.close()
    
def getPessoas():
    session = DBSession()
    pessoas = session.query(Pessoa).all()
    session.close()
    # people = []
    # for pessoa in pessoas:
    #     people.append(pessoa.__dict__)
    # return jsonify(people)
    return pessoas

def getPessoasAPI():
    session = DBSession()
    pessoas = session.query(Pessoa).all()
    # people = []
    # for pessoa in pessoas:
    #     people.append({"Lista", pessoa})
    session.close()
    data = {'pessoas' : {as_dict(pessoa) for pessoa in pessoas}}
    return data
    # return pessoas

def getPessoa(nome_):
    session = DBSession()
    pessoa = session.query(Pessoa).filter_by(Nome = nome_).all()
    session.close()
    people = []
    for pessoas in pessoa:
        people.append(pessoas.__dict__)
    return people
    

def deletePessoa(id_):
    session = DBSession()
    session.query(Pessoa).filter(Pessoa.pessoaId == id_).delete()
    session.commit()

def insertEndereco(rua_, numero_, cep_, bairro_, cidade_, estado_, pessoaId_):
    session = DBSession()
    e = Endereco(Rua=rua_, Numero=numero_, CEP=cep_, Bairro=bairro_, Cidade=cidade_, Estado=estado_, 
    pessoaId=pessoaId_)
    session.add(e)
    session.commit()
    session.close()

def getEnderecos():
    session = DBSession()
    enderecos = session.query(Endereco.enderecoId).all()
    session.close()
    return enderecos

def getEnderecoById(id_):
    session = DBSession()
    endereco = session.query(Endereco).filter_by(pessoaId = id_).all()
    session.close()
    end = []
    for enderecos in endereco:
        end.append(enderecos.__dict__)
    return end

def deleteEnderecos(id_):
    session = DBSession()
    session.query(Endereco).filter(Endereco.enderecoId == id_).delete()
    session.commit()

def insertTelefones(ddd_, numero_, pessoaId_):
    session = DBSession()
    t = Telefone(DDD=ddd_, Numero=numero_, pessoaId=pessoaId_)
    session.add(t)
    session.commit()
    session.close()

def getTelefone():
    session = DBSession()
    telefones = session.query(Telefone.telefoneId).all()
    session.close()
    return telefones

def getTelefoneById(id_):
    session = DBSession()
    telefone = session.query(Telefone).filter_by(pessoaId = id_).all()
    session.close()
    tel = []
    for telefones in telefone:
        tel.append(telefones.__dict__)
    return tel

def deleteTelefone(id_):
    session = DBSession()
    session.query(Telefone).filter(Telefone.telefoneId == id_).delete()
    session.commit()
