from Database import getPessoas, getPessoasAPI, insertPessoa, deletePessoa, getEnderecoById, getTelefoneById, deleteTelefone, insertTelefones, getPessoaByIdAPI, getPessoaByNameAPI, getPessoaByMonthAPI
from flask import Flask, render_template, jsonify, request, Markup
app = Flask(__name__)

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

@app.route("/contato/<id>")
def contatoUsuario(id):
    return render_template('/contato.html', enderecos = getEnderecoById(id), telefones = getTelefoneById(id))

@app.route("/cadastrar", methods = ['POST'])
def addContato():
    user = request.form.get('user')
    datanas = request.form.get('datanas')
    insertPessoa(user, datanas)
    message = Markup("<h1>Usuário cadastrado com sucesso!</h1>")
    return message

@app.route("/cadastrar/telefone", methods = ['POST'])
def addTelefone():
    ddd = request.form.get('ddd')
    numero = request.form.get('numero')
    pessoaId = request.form.get('id')
    insertTelefones(ddd, numero, pessoaId)
    message = Markup("<h1>Telefone cadastrado com sucesso!</h1>")
    return message

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

