from Database import getPessoas, getPessoasAPI, insertPessoa, deletePessoa, insertEndereco, getEnderecoById, getTelefoneById, deleteEndereco, deleteTelefone, insertTelefones, getPessoaByIdAPI, getPessoaByNameAPI, getPessoaByMonthAPI
from flask import Flask, render_template, jsonify, request, Markup, session
import secrets
app = Flask(__name__)

app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"

@app.route("/sharabadaias/api/getContatos")
def getContatosApi():
    return getPessoasAPI()

@app.route("/sharabadaias/api/getContatoID/<id>")
def getContatoByIdApi(id = None):
    return getPessoaByIdAPI(id)

@app.route("/sharabadaias/api/getContatoNome/<nome>")
def getContatoByNameApi(nome = None):
    return getPessoaByNameAPI(nome)

@app.route("/sharabadaias/api/getContatoAniversario/<mes>")
def getContatoByMonthApi(mes = None):
    return getPessoaByMonthAPI(mes)

@app.route("/")
def getContatos():
    return render_template('/template.html', pessoas = getPessoas())

@app.route("/form")
def formContatos():
    return render_template('/form.html')

@app.route("/telefone")
def formTelefone():
    return render_template('/addtelefone.html')

@app.route("/endereco")
def formEndereco():
    return render_template('/addEndereco.html')

@app.route("/contato/<id>")
def contatoUsuario(id):
    session["ID_USUARIO"] = id
    return render_template('/contato.html', enderecos = getEnderecoById(id), telefones = getTelefoneById(id))

@app.route("/cadastrar", methods = ['POST'])
def addContato():
    user = request.form.get('user')
    datanas = request.form.get('datanas')
    
    if (datanas and user):
        insertPessoa(user, datanas)
        message = Markup("<h1>Usuário cadastrado com sucesso!</h1>")
        return message

@app.route("/cadastrar/telefone", methods = ['POST'])
def addTelefone():
    ddd = request.form.get('ddd')
    numero = request.form.get('numeroTel')
    pessoaId = session.get('ID_USUARIO')
    insertTelefones(ddd, numero, pessoaId)
    message = Markup("<h1>Telefone cadastrado com sucesso!</h1>")
    
    return message

@app.route("/cadastrar/endereco", methods = ['POST'])
def addEndereco():
    rua = request.form.get('rua')
    numero = request.form.get('numero')
    CEP = request.form.get('CEP')
    bairro = request.form.get('bairro')
    cidade = request.form.get('cidade')
    estado = request.form.get('estado')
    pessoaId = session.get('ID_USUARIO')
    insertEndereco(rua, numero, CEP, bairro, cidade, estado, pessoaId)
    message = Markup("<h1>Endereço cadastrado com sucesso!</h1>")
    return message

@app.route("/editar/<id>", methods = ["PUT"])
def editarContato():
    return null

@app.route("/deletar", methods = ['POST'])
def deleteContato():
    id = request.form.get('id')
    deletePessoa(id)
    message = Markup("<h1>Usuário deletado com sucesso!</h1>")
    return message

@app.route("/endereco", methods = ['POST'])
def deletarEndereco():
    id = request.form.get('endereco')
    deleteEndereco(id)
    message = Markup("<h1>Endereço deletado com sucesso!</h1>")
    return message

@app.route("/telefone", methods = ['POST'])
def deletarTelefone():
    id = request.form.get('telefone')
    deleteTelefone(id)
    message = Markup("<h1>Telefone deletado com sucesso!</h1>")
    return message

app.run(debug=True, use_reloader=True)

