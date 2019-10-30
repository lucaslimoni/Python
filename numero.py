# class Numero(object):
#     def __init__(self, numero):
#         self.numero = numero
    
#     def par_ou_impar(self):
#         num = self.numero % 2
#         if (num == 0):
#             return print("PAR")
#         else:
#             return print("IMPAR")
#     def proximo(self):
#         return self.numero + 1

from flask import Flask
app = Flask(__name__)

@app.route("/peso/<float:quilos>")
def seu_peso(quilos):
    return "Você pesa "+str(quilos)+" Kg", 200
app.run(debug=True, use_reloader=True)