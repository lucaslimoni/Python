from Database import getPessoas, getPessoasAPI
from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/sharabadaias/api/getContatos")
def getContatosApi():
    return getPessoasAPI()

@app.route("/")
def getContatos():
    return render_template('/template.html', pessoas = getPessoas())

app.run(debug=True, use_reloader=True)

