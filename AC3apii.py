import mysql.connector
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/registros', methods=['GET'])
def get_registros():
    
    con = mysql.connector.connect(host='localhost',database='pessoas',user='root',password='1234')
    cursor = con.cursor()

    
    cursor.execute('SELECT * FROM registros')
    registros = cursor.fetchall()

    
    registros_json = []
    for registro in registros:
        registro_json = {'id': registro[0], 'nome': registro[1], 'idade': registro[2], 'ra': registro[3]}
        registros_json.append(registro_json)   
    con.close()

    return jsonify(registros_json)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    
    ID = request.form['ID']
    Nome = request.form['nome']
    RA = request.form['ra']

    
    con = mysql.connector.connect(host='localhost',database='pessoas',user='root',password='1234')
    cursor = con.cursor()

   
    cursor.execute('INSERT INTO registros (ID, Nome, RA) VALUES (?, ?, ?)', (ID, Nome, RA))
    con.commit()

    
    con.close()

    return 'Registro cadastrado com sucesso!'

@app.route('/registros/<campo>/<valor>', methods=['DELETE'])
def excluir_registro(campo, valor):
  
    con = mysql.connector.connect(host='localhost',database='pessoas',user='root',password='1234')
    cursor = con.cursor()

    
    cursor.execute(f"DELETE FROM registros WHERE {campo}=?", (valor,))
    con.commit()

    
    if cursor.rowcount == 0:
        return jsonify({'message': 'Registro não encontrado.'}), 404

   
    con.close()

    
    return jsonify({'message': 'Registro excluído com sucesso.'}), 200
