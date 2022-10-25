'''

Este código é uma API para "produtos", entretanto apenas alguns conceitos
de REST são implementados.

O intuito é realizar ajustes na tentativa de transformá-la em uma API RESTFul!
Utilize como referência o documento "Design da API Restful" disponibilizado.

'''

import sqlite3
from sqlite3 import Error
from flask import Flask, request, jsonify
from datetime import date


app = Flask(__name__)

#######################################################
#  1) GET: pesquisar
#######################################################

@app.route('/api-loja/produtos/', methods=['GET'])
@app.route('/api-loja/produtos/<int:idproduto>', methods=['GET'])
def pesquisar(idproduto=None):
    if request.method == 'GET':
        if idproduto is not None:
            sql = '''SELECT * FROM produtos WHERE idproduto = ''' + str(idproduto)
        else:
            sql = '''SELECT * FROM produtos'''


        try:
            conn = sqlite3.connect('database/db-loja.db')

            cur = conn.cursor()
            cur.execute(sql)
            registros = cur.fetchall()

            if registros:
                nomes_colunas = [x[0] for x in cur.description]

                json_dados = []
                for reg in registros:
                    json_dados.append(dict(zip(nomes_colunas, reg)))

                return jsonify(json_dados)
            else:
                return jsonify({'mensagem': 'registro nao encontrado'})

        except Error as e:
            return jsonify({'mensagem': e})
        finally:
            conn.close()



#######################################################
#  2) POST: inserir
#######################################################

@app.route('/api-loja/produtos', methods=['POST'])
def inserir():
    if request.method == 'POST':
        dados = request.get_json()

        descricao = dados['descricao']
        ganhopercentual = dados['ganhopercentual']
        datacriacao = date.today()

        if descricao and ganhopercentual and datacriacao:
            registro = (descricao, ganhopercentual, datacriacao)

            try:
                conn = sqlite3.connect('database/db-loja.db')

                sql = ''' INSERT INTO produtos(descricao, ganhopercentual, datacriacao) VALUES(?,?,?) '''
                cur = conn.cursor()
                cur.execute(sql, registro)
                conn.commit()

                return jsonify({'mensagem': 'registro inserido com sucesso'})

            except Error as e:
                return jsonify({'mensagem': e})
            finally:
                conn.close()

        else:
            return jsonify({'mensagem': 'campos <descricao> e <ganhopercentual> sao obrigatorios'})


#######################################################
#  3) DELETE: excluir
#######################################################

@app.route('/api-loja/produtos/<int:idproduto>', methods=['DELETE'])
def excluir(idproduto):
    if request.method == 'DELETE':
        if idproduto:
            try:
                conn = sqlite3.connect('database/db-loja.db')

                sql = '''DELETE FROM produtos WHERE idproduto = ''' + str(idproduto)

                cur = conn.cursor()
                cur.execute(sql)

                conn.commit()

                return jsonify({'mensagem': 'registro excluido'})

            except Error as e:
                return jsonify({'mensagem': e})
            finally:
                conn.close()
        else:
            return jsonify({'mensagem': 'campo <idproduto> obrigatorio'})


#######################################################
#  4) PUT: alterar
#######################################################

@app.route('/api-loja/produtos/', methods=['PUT'])
def alterar():
    if request.method == 'PUT':
        dados = request.get_json()

        descricao = dados['descricao']
        ganhopercentual = dados['ganhopercentual']
        idproduto = dados['idproduto']

        if descricao and ganhopercentual and idproduto:
            registro = (descricao, ganhopercentual, idproduto)

            try:
                conn = sqlite3.connect('database/db-loja.db')

                sql = ''' UPDATE produtos SET descricao=?, ganhopercentual=? WHERE idproduto = ?'''
                cur = conn.cursor()
                cur.execute(sql, registro)
                conn.commit()

                return jsonify({'mensagem': 'registro alterado com sucesso'})

            except Error as e:
                return jsonify({'mensagem': e})
            finally:
                conn.close()

    else:
        return jsonify({'mensagem': 'campos <descricao>, <ganhopercentual> e <idproduto> sao obrigatorios'})


#######################################################
# 5) UrlPoint nao localizado
#######################################################

@app.errorhandler(404)
def endpoint_nao_encontrado(e):
    return jsonify({'mensagem': 'erro - endpoint nao encontrado'}), 404

@app.errorhandler(405)
def endpoint_nao_encontrado(e):
    return jsonify({'mensagem': 'erro - endpoint nao encontrado'}), 405


#######################################################
# XX Execucao da Aplicacao
#######################################################

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
