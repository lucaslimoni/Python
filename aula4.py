from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Bem vindo a calculadora da maldade"

@app.route("/template/<operacao>/<num1>/<num2>")

def operacao(operacao = None, num1 = None, num2 = None):
    if operacao == None :
        res = 'Nenhuma operação escolhida'
    elif (operacao == '+') | (operacao == 'soma'):
        res = int(num1) + int(num2)
        ct = num1 + ' + ' + num2
    elif (operacao == '-') | (operacao == 'subtracao'):
        res = int(num1) - int(num2)
        ct = num1 + ' - ' + num2
    elif (operacao == '*') | (operacao == 'multiplicacao'):
        res = int(num1) * int(num2)
        ct = num1 + ' * ' + num2
    elif (operacao == '%') | (operacao == 'divisao'):
        res = int(num1) / int(num2)
        ct = num1 + ' / ' + num2
    return render_template("template.html",res = str(res), op = operacao, conta = ct)

@app.route("/hello")
@app.route("/hello/<nome>")
@app.route("/hello/<nome>/<sobrenome>")
def echo_name(nome = None, sobrenome = None):
    cpf = request.args.get("cpf")
    return cpf

@app.route("/template/<nome>")
def html_page(nome):
    return render_template("template.html", nome=nome)

@app.route("/json")
def json_api():
    pessoas = [{"nome": "Gustavo"},
    {"nome": "Larissa"}]
    return jsonify(pessoas=pessoas, total=len(pessoas))
app.run(debug=True, use_reloader=True)