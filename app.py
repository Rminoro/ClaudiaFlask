
# from flask import Flask, jsonify, request
# import pandas as pd
# import plotly.graph_objects as go
# import cx_Oracle

# app = Flask(__name__)

# # Credenciais do banco de dados Oracle
# username = "RM99988"
# password = "160698"
# dsn = "oracle.fiap.com.br:1521/orcl"

# # Mapeamento de perguntas para SQL e gráficos
# sql_mapping = {
#     "Qual é o total de vendas por mês deste ano?": """
#         SELECT TO_CHAR(DATA_PEDIDO, 'YYYY-MM') AS MES, SUM(VALOR_TOTAL) AS TOTAL_VENDAS
#         FROM Pedido
#         WHERE EXTRACT(YEAR FROM DATA_PEDIDO) = EXTRACT(YEAR FROM SYSDATE)
#         GROUP BY TO_CHAR(DATA_PEDIDO, 'YYYY-MM')
#         ORDER BY MES
#     """,
#     "Qual é o total de vendas por loja?": """
#         SELECT l.NOME_LOJA, SUM(p.VALOR_TOTAL) AS TOTAL_VENDAS
#         FROM Pedido p
#         JOIN Loja l ON p.ID_LOJA = l.ID_LOJA
#         GROUP BY l.NOME_LOJA
#         ORDER BY TOTAL_VENDAS DESC
#     """,
#     "Qual é a quantidade total de produtos em estoque por tipo?": """
#         SELECT TIPO_PRODUTO, SUM(QUANTIDADE) AS TOTAL_ESTOQUE
#         FROM Estoque
#         GROUP BY TIPO_PRODUTO
#         ORDER BY TOTAL_ESTOQUE DESC
#     """,
#     "Qual é a quantidade total vendida de cada produto?": """
#         SELECT TIPO_PRODUTO, SUM(QUANTIDADE) AS TOTAL_VENDIDO
#         FROM PEDIDOPRODUTO
#         GROUP BY TIPO_PRODUTO
#         ORDER BY TOTAL_VENDIDO DESC
#     """,
#      "Qual é a quantidade total vendida de cada produto?": """
#         SELECT TIPO_PRODUTO, SUM(QUANTIDADE) AS TOTAL_VENDIDO
#         FROM PEDIDOPRODUTO
#         GROUP BY TIPO_PRODUTO
#         ORDER BY TOTAL_VENDIDO DESC
#     """,
#     "Qual é o total de vendas do ano passado?": "SELECT * FROM vendas WHERE ano = EXTRACT(YEAR FROM CURRENT_DATE) - 1",  # Ajuste conforme necessário
#     "Qual produto teve mais vendas?": "SELECT produto, COUNT(*) as total_vendas FROM vendas GROUP BY produto ORDER BY total_vendas DESC LIMIT 1"  # Ajuste conforme necessário
# }

# plotly_mapping = {
#     "Qual é o total de vendas por mês deste ano?": "grafico_vendas_mes",
#     "Qual é o total de vendas por loja?": "grafico_vendas_loja",
#     "Qual é o total de vendas do ano passado?": "grafico_vendas_ano",
#     "Qual produto teve mais vendas?": "grafico_produto_popular",
#     "Qual é a quantidade total de produtos em estoque por tipo?": "grafico_estoque",
#     "Qual é a quantidade total vendida de cada produto?": "grafico_venda_produto"
# }

# def query_database(sql):
#     try:
#         print(f"Executando SQL: {sql}")  # Log para depuração
#         with cx_Oracle.connect(user=username, password=password, dsn=dsn) as connection:
#             df = pd.read_sql(sql, con=connection)
#         return df
#     except cx_Oracle.Error as e:
#         return f"Erro ao acessar o banco de dados: {e}"

# def generate_plot_html(df, plot_code):
#     # Exemplo de geração de gráfico usando Plotly
#     if plot_code == "grafico_vendas_mes":
#         fig = go.Figure(data=[
#             go.Bar(x=df['MES'], y=df['TOTAL_VENDAS'])
#         ])
#     elif plot_code == "grafico_vendas_loja":
#         fig = go.Figure(data=[
#             go.Bar(x=df['NOME_LOJA'], y=df['TOTAL_VENDAS'])
#         ])
#     elif plot_code == "grafico_estoque":  # Adicionando a geração do gráfico para estoque
#         print("Gerando gráfico de estoque...")  # Log para confirmar a geração do gráfico
#         fig = go.Figure(data=[
#             go.Bar(x=df['TIPO_PRODUTO'], y=df['TOTAL_ESTOQUE'])
#         ])
#     elif plot_code == "grafico_venda_produto":  # Geração do gráfico para vendas por produto
#         print("Gerando gráfico de venda_produto...")  # Log para confirmar a geração do gráfico
#         fig = go.Figure(data=[
#             go.Bar(x=df['TIPO_PRODUTO'], y=df['TOTAL_VENDIDO'], marker_color='rgb(0,128,255)')
#         ])
#     else:
#         return "<h1>Gráfico não disponível</h1>"
    
#     # Retorna o HTML do gráfico
#     return fig.to_html(full_html=False)

# @app.route('/process_question', methods=['POST'])
# def process_question():
#     data = request.json
#     question = data.get("question")

#     if question in sql_mapping:
#         sql = sql_mapping[question]
#         df = query_database(sql)

#         if isinstance(df, pd.DataFrame):
#             if df.empty:
#                 return jsonify({"error": "Nenhum dado encontrado para a consulta."}), 404

#             plot_code = plotly_mapping.get(question)
#             print(f"Código para gerar gráfico: {plot_code}")  # Log para verificar o código do gráfico
            
#             html_graph = generate_plot_html(df, plot_code) if plot_code else None
            
#             return jsonify({
#                 "data": df.to_dict(orient='records'),
#                 "graph_html": html_graph  # Retorna o HTML do gráfico
#             })
#         else:
#             return jsonify({"error": df}), 400
#     else:
#         return jsonify({"error": "Pergunta não encontrada."}), 404

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5001)
from flask import Flask, jsonify, request
import pandas as pd
import plotly.graph_objects as go
import cx_Oracle

app = Flask(__name__)

# Credenciais do banco de dados Oracle
username = "RM99988"
password = "160698"
dsn = "oracle.fiap.com.br:1521/orcl"

# Mapeamento de perguntas para SQL e gráficos
sql_mapping = {
    "Qual é o total de vendas por mês deste ano?": """
        SELECT TO_CHAR(DATA_PEDIDO, 'YYYY-MM') AS MES, SUM(VALOR_TOTAL) AS TOTAL_VENDAS
        FROM Pedido
        WHERE EXTRACT(YEAR FROM DATA_PEDIDO) = EXTRACT(YEAR FROM SYSDATE)
        GROUP BY TO_CHAR(DATA_PEDIDO, 'YYYY-MM')
        ORDER BY MES
    """,
    "Qual é o total de vendas por loja?": """
        SELECT l.NOME_LOJA, SUM(p.VALOR_TOTAL) AS TOTAL_VENDAS
        FROM Pedido p
        JOIN Loja l ON p.ID_LOJA = l.ID_LOJA
        GROUP BY l.NOME_LOJA
        ORDER BY TOTAL_VENDAS DESC
    """,
    "Qual é a quantidade total de produtos em estoque por tipo?": """
        SELECT TIPO_PRODUTO, SUM(QUANTIDADE) AS TOTAL_ESTOQUE
        FROM Estoque
        GROUP BY TIPO_PRODUTO
        ORDER BY TOTAL_ESTOQUE DESC
    """,
    "Qual é a quantidade total vendida de cada produto?": """
        SELECT TIPO_PRODUTO, SUM(QUANTIDADE) AS TOTAL_VENDIDO
        FROM PEDIDOPRODUTO
        GROUP BY TIPO_PRODUTO
        ORDER BY TOTAL_VENDIDO DESC
    """,
    "Qual é o total de vendas do ano passado?": """
        SELECT * FROM vendas WHERE ano = EXTRACT(YEAR FROM CURRENT_DATE) - 1
    """, 
    "Qual produto teve mais vendas?": """
        SELECT produto, COUNT(*) as total_vendas 
        FROM vendas 
        GROUP BY produto 
        ORDER BY total_vendas DESC 
        FETCH FIRST 1 ROWS ONLY
    """ ,
       "Qual é o número total de pedidos por tipo de produto?": """
        SELECT e.TIPO_PRODUTO, COUNT(p.ID_PEDIDO) AS NUM_PEDIDOS
        FROM Pedido p
        JOIN Estoque e ON p.ID_LOJA = e.ID_LOJA
        GROUP BY e.TIPO_PRODUTO
        ORDER BY NUM_PEDIDOS DESC
    """,
}

plotly_mapping = {
    "Qual é o total de vendas por mês deste ano?": "grafico_vendas_mes",
    "Qual é o total de vendas por loja?": "grafico_vendas_loja",
    "Qual é o total de vendas do ano passado?": "grafico_vendas_ano",
    "Qual produto teve mais vendas?": "grafico_produto_popular",
    "Qual é a quantidade total de produtos em estoque por tipo?": "grafico_estoque",
    "Qual é a quantidade total vendida de cada produto?": "grafico_venda_produto",
    "Qual é o número total de pedidos por tipo de produto?" : "grafico_pedido_tipo",
    "Qual é o total de pedidos e o valor total de vendas por vendedor?" :"grafico_vendedor"
}

def query_database(sql):
    try:
        print(f"Executando SQL: {sql}")  # Log para depuração
        with cx_Oracle.connect(user=username, password=password, dsn=dsn) as connection:
            df = pd.read_sql(sql, con=connection)
        return df
    except cx_Oracle.Error as e:
        return f"Erro ao acessar o banco de dados: {e}"

def generate_plot_html(df, plot_code):
    # Exemplo de geração de gráfico usando Plotly
    if plot_code == "grafico_vendas_mes":
        fig = go.Figure(data=[
            go.Bar(x=df['MES'], y=df['TOTAL_VENDAS'])
        ])
    elif plot_code == "grafico_produto_popular":
        fig = go.Figure(data=[
            go.Bar(x=df['NOME_LOJA'], y=df['TOTAL_VENDAS'])
        ])
    elif plot_code == "grafico_vendas_loja":
        fig = go.Figure(data=[
            go.Bar(x=df['NOME_LOJA'], y=df['TOTAL_VENDAS'])
        ])
    elif plot_code == "grafico_estoque":  # Adicionando a geração do gráfico para estoque
        print("Gerando gráfico de estoque...")  # Log para confirmar a geração do gráfico
        fig = go.Figure(data=[
            go.Bar(x=df['TIPO_PRODUTO'], y=df['TOTAL_ESTOQUE'])
        ])
    elif plot_code == "grafico_venda_produto":  # Geração do gráfico para vendas por produto
        print("Gerando gráfico de venda_produto...")  # Log para confirmar a geração do gráfico
        fig = go.Figure(data=[
            go.Bar(x=df['TIPO_PRODUTO'], y=df['TOTAL_VENDIDO'])
        ])
    elif plot_code == "grafico_pedido_tipo":  # Geração do gráfico para vendas por produto
        print("Gerando gráfico de venda_produto...")  # Log para confirmar a geração do gráfico
        fig = go.Figure(data=[
            go.Bar(x=df['TIPO_PRODUTO'], y=df['NUM_PEDIDOS'])
        ])
    elif plot_code == "grafico_vendedor":  # Geração do gráfico para vendas por produto
        print("Gerando gráfico de venda_produto...")  # Log para confirmar a geração do gráfico
        fig = go.Figure(data=[
            go.Bar(x=df['NOME_VENDEDOR'], y=df['TOTAL_VENDAS'])
        ])
    else:
        return "<h1>Gráfico não disponível</h1>"
    
    # Retorna o HTML do gráfico
    return fig.to_html(full_html=False)

@app.route('/process_question', methods=['POST'])
def process_question():
    data = request.json
    question = data.get("question")

    if question in sql_mapping:
        sql = sql_mapping[question]
        df = query_database(sql)

        if isinstance(df, pd.DataFrame):
            if df.empty:
                return jsonify({"error": "Nenhum dado encontrado para a consulta."}), 404

            plot_code = plotly_mapping.get(question)
            print(f"Código para gerar gráfico: {plot_code}")  # Log para verificar o código do gráfico
            
            html_graph = generate_plot_html(df, plot_code) if plot_code else None
            
            return jsonify({
                "data": df.to_dict(orient='records'),
                "graph_html": html_graph  # Retorna o HTML do gráfico
            })
        else:
            return jsonify({"error": df}), 400
    else:
        return jsonify({"error": "Pergunta não encontrada."}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
