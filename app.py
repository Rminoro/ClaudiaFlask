# # from flask import Flask, jsonify, request
# # from flask_cors import CORS
# # import jaydebeapi
# # import pandas as pd
# # import plotly.express as px
# # import base64
# # from io import BytesIO

# # app = Flask(__name__)
# # CORS(app, resources={r"/*": {"origins": "*"}})

# # # Função para executar a query
# # def query_database(query):
# #     try:
# #         conn = jaydebeapi.connect(
# #             "oracle.jdbc.driver.OracleDriver",
# #             "jdbc:oracle:thin:@oracle.fiap.com.br:1521/orcl",
# #             ["RM98974", "100903"],
# #             "/Users/USER/Desktop/sqldeveloper/JDBC/lib/ojdbc11.jar"
# #         )
# #         cursor = conn.cursor()
# #         cursor.execute(query)
# #         data = cursor.fetchall()
# #         columns = [desc[0] for desc in cursor.description]
# #         df = pd.DataFrame(data, columns=columns)
# #         cursor.close()
# #         conn.close()
# #         return df
# #     except Exception as e:
# #         return str(e)

# # # Função para gerar gráfico
# # # Função para gerar gráfico
# # def generate_plot(df, plot_code):
# #     try:
# #         local_vars = {'df': df}
        
# #         # Limpar indentação
# #         plot_code_clean = "\n".join([line.lstrip() for line in plot_code.splitlines()])
# #         print("Código Plotly limpo:", plot_code_clean)  # Log do código limpo
        
# #         code = compile(plot_code_clean, '<string>', 'exec')
# #         exec(code, globals(), local_vars)
# #         fig = local_vars.get('fig')
        
# #         if fig:
# #             print("Gráfico gerado com sucesso.")  # Log do gráfico gerado
# #             buf = BytesIO()
# #             fig.write_image(buf, format="png")
# #             buf.seek(0)
            
# #             img_base64 = base64.b64encode(buf.read()).decode("utf-8")
# #             return img_base64
# #         else:
# #             print("Nenhum gráfico foi gerado.")  # Log quando não há gráfico
# #             return None
# #     except Exception as e:
# #         print(f"Erro ao gerar o gráfico: {e}")  # Log do erro
# #         return str(e)



# # # Endpoint para processar perguntas
# # @app.route('/process_question', methods=['POST'])
# # def process_question():
# #     data = request.json
# #     print("Dados recebidos:", data)  # Log dos dados recebidos
# #     question = data.get("question")
    
# #     # Mapeamento SQL
# #     sql_mapping = {
# #         "Qual é o total de vendas por mês deste ano?": """
# #             SELECT TO_CHAR(DATA_PEDIDO, 'YYYY-MM') AS MES, SUM(VALOR_TOTAL) AS TOTAL_VENDAS
# #             FROM Pedido
# #             WHERE EXTRACT(YEAR FROM DATA_PEDIDO) = EXTRACT(YEAR FROM SYSDATE)
# #             GROUP BY TO_CHAR(DATA_PEDIDO, 'YYYY-MM')
# #             ORDER BY MES
# #         """,
# #         "Qual é o total de vendas do ano passado?": """
# #             SELECT SUM(VALOR_TOTAL) AS TOTAL_VENDAS
# #             FROM Pedido
# #             WHERE EXTRACT(YEAR FROM DATA_PEDIDO) = EXTRACT(YEAR FROM SYSDATE) - 1
# #         """,
# #         "Qual produto teve mais vendas?": """
# #             SELECT NOME_PRODUTO, SUM(QUANTIDADE_VENDIDA) AS TOTAL_VENDAS
# #             FROM Pedido_Produto
# #             GROUP BY NOME_PRODUTO
# #             ORDER BY TOTAL_VENDAS DESC
# #             FETCH FIRST 1 ROWS ONLY
# #         """
# #     }

# #      # Mapeamento dos gráficos com plotly
# #     plotly_mapping = {
# #         "Qual é o total de vendas por mês deste ano?": """
# # fig = px.line(df, x='MES', y='TOTAL_VENDAS', title='Total de Vendas por Mês')
# # fig.update_layout(xaxis_title='Mês', yaxis_title='Total de Vendas')
# # """,
# #         "Qual é o total de vendas do ano passado?": """
# # fig = px.bar(df, x=['TOTAL_VENDAS'], y='TOTAL_VENDAS', title='Total de Vendas do Ano Passado')
# # fig.update_layout(xaxis_title='Total de Vendas', yaxis_title='Valor')
# # """,
# #         "Qual produto teve mais vendas?": """
# # fig = px.bar(df, x=['NOME_PRODUTO'], y='TOTAL_VENDAS', title='Produto com Mais Vendas')
# # fig.update_layout(xaxis_title='Produto', yaxis_title='Total de Vendas')
# # """
# #     }

# #     if question in sql_mapping:
# #         sql = sql_mapping[question]
# #         print(f"Executando query: {sql}")
# #         df = query_database(sql)
# #         if isinstance(df, pd.DataFrame):
# #             if df.empty:
# #                 return jsonify({"error": "Nenhum dado encontrado para a consulta."}), 404

# #             # Retornar tabela e gráfico se a consulta for bem-sucedida
# #             plot_code = plotly_mapping.get(question)
# #             print(f"Gerando gráfico para a pergunta: {question}")
# #             img_base64 = generate_plot(df, plot_code) if plot_code else None
# #             print(f"Imagem Base64 gerada: {img_base64[:100]}...")  # Log do gráfico gerado (primeiros 100 caracteres)
# #             return jsonify({
# #                 "data": df.to_dict(orient='records'),
# #                 "graph": img_base64
# #             })
# #         else:
# #             print(f"Erro na query: {df}")
# #             return jsonify({"error": df}), 400
# #     else:
# #         print(f"Pergunta não encontrada: {question}")
# #         return jsonify({"error": "Pergunta não encontrada."}), 404

# # # Para evitar conflitos com o Streamlit, usamos o modo threaded
# # if __name__ == "__main__":
# #     app.run(debug=True, host='0.0.0.0', port=5001, threaded=True)
# from flask import Flask, jsonify, request
# from flask_cors import CORS
# import jaydebeapi
# import pandas as pd
# import plotly.express as px
# import base64
# from io import BytesIO

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})

# def generate_plot(df, plot_code):
#     try:
#         # Cria o gráfico com base no código Plotly fornecido
#         local_vars = {'df': df}
#         code = compile(plot_code, '<string>', 'exec')
#         exec(code, globals(), local_vars)
#         fig = local_vars.get('fig')
        
#         if fig:
#             buffer = BytesIO()
#             fig.write_image(buffer, format="png")
#             buffer.seek(0)
#             img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
#             return img_base64
#         else:
#             return "Nenhum gráfico gerado."
#     except Exception as e:
#         return str(e)

# # Função para executar a query
# def query_database(query):
#     try:
#         conn = jaydebeapi.connect(
#             "oracle.jdbc.driver.OracleDriver",
#             "jdbc:oracle:thin:@oracle.fiap.com.br:1521/orcl",
#             ["RM98974", "100903"],
#             "/Users/USER/Desktop/sqldeveloper/JDBC/lib/ojdbc11.jar"
#         )
#         cursor = conn.cursor()
#         cursor.execute(query)
#         data = cursor.fetchall()
#         columns = [desc[0] for desc in cursor.description]
#         df = pd.DataFrame(data, columns=columns)
#         cursor.close()
#         conn.close()
#         return df
#     except Exception as e:
#         return str(e)

# # Endpoint para processar perguntas
# @app.route('/process_question', methods=['POST'])
# def process_question():
#     data = request.json
#     question = data.get("question")
    
#     # Mapeamento SQL
#     sql_mapping = {
#         "Qual é o total de vendas por mês deste ano?": """
#             SELECT TO_CHAR(DATA_PEDIDO, 'YYYY-MM') AS MES, SUM(VALOR_TOTAL) AS TOTAL_VENDAS
#             FROM Pedido
#             WHERE EXTRACT(YEAR FROM DATA_PEDIDO) = EXTRACT(YEAR FROM SYSDATE)
#             GROUP BY TO_CHAR(DATA_PEDIDO, 'YYYY-MM')
#             ORDER BY MES
#         """,
#         "Qual é o total de vendas do ano passado?": """
#             SELECT SUM(VALOR_TOTAL) AS TOTAL_VENDAS
#             FROM Pedido
#             WHERE EXTRACT(YEAR FROM DATA_PEDIDO) = EXTRACT(YEAR FROM SYSDATE) - 1
#         """,
#         "Qual produto teve mais vendas?": """
#             SELECT NOME_PRODUTO, SUM(QUANTIDADE_VENDIDA) AS TOTAL_VENDAS
#             FROM Pedido_Produto
#             GROUP BY NOME_PRODUTO
#             ORDER BY TOTAL_VENDAS DESC
#             FETCH FIRST 1 ROWS ONLY
#         """
#     }

#     # Mapeamento dos gráficos com plotly
#     plotly_mapping = {
#         "Qual é o total de vendas por mês deste ano?": """
#             fig = px.line(df, x='MES', y='TOTAL_VENDAS', title='Total de Vendas por Mês')
#             fig.update_layout(xaxis_title='Mês', yaxis_title='Total de Vendas')
#         """,
#         "Qual é o total de vendas do ano passado?": """
#             fig = px.bar(df, x=['TOTAL_VENDAS'], y='TOTAL_VENDAS', title='Total de Vendas do Ano Passado')
#             fig.update_layout(xaxis_title='Total de Vendas', yaxis_title='Valor')
#         """,
#         "Qual produto teve mais vendas?": """
#             fig = px.bar(df, x='NOME_PRODUTO', y='TOTAL_VENDAS', title='Produto com Mais Vendas')
#             fig.update_layout(xaxis_title='Produto', yaxis_title='Total de Vendas')
#         """
#     }

#     if question in sql_mapping:
#         sql = sql_mapping[question]
#         df = query_database(sql)
#         if isinstance(df, pd.DataFrame):
#             if df.empty:
#                 return jsonify({"error": "Nenhum dado encontrado para a consulta."}), 404

#             # Retornar tabela e gráfico se a consulta for bem-sucedida
#             plot_code = plotly_mapping.get(question)
#             img_base64 = generate_plot(df, plot_code) if plot_code else None
            
#             return jsonify({
#                 "data": df.to_dict(orient='records'),
#                 "graph": img_base64
#             })
#         else:
#             return jsonify({"error": df}), 400
#     else:
#         return jsonify({"error": "Pergunta não encontrada."}), 404

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=5001)
# from flask import Flask, jsonify, request
# from flask_cors import CORS
# import jaydebeapi
# import pandas as pd
# import plotly.express as px
# import base64
# from io import BytesIO

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})

# def generate_plot(df, plot_code):
#     try:
#         # Cria o gráfico com base no código Plotly fornecido
#         local_vars = {'df': df}
#         code = compile(plot_code, '<string>', 'exec')
#         exec(code, globals(), local_vars)
#         fig = local_vars.get('fig')
        
#         if fig:
#             buffer = BytesIO()
#             fig.write_image(buffer, format="png")
#             buffer.seek(0)
#             img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
#             return img_base64
#         else:
#             return "Nenhum gráfico gerado."
#     except Exception as e:
#         return str(e)

# # Função para executar a query
# def query_database(query):
#     try:
#         conn = jaydebeapi.connect(
#             "oracle.jdbc.driver.OracleDriver",
#             "jdbc:oracle:thin:@oracle.fiap.com.br:1521/orcl",
#             ["RM98974", "100903"],
#             "/Users/USER/Desktop/sqldeveloper/JDBC/lib/ojdbc11.jar"
#         )
#         cursor = conn.cursor()
#         cursor.execute(query)
#         data = cursor.fetchall()
#         columns = [desc[0] for desc in cursor.description]
#         df = pd.DataFrame(data, columns=columns)
#         cursor.close()
#         conn.close()
#         return df
#     except Exception as e:
#         return str(e)

# # Endpoint para processar perguntas
# @app.route('/process_question', methods=['POST'])
# def process_question():
#     data = request.json
#     question = data.get("question")
    
#     # Mapeamento SQL
#     sql_mapping = {
#         "Qual é o total de vendas por mês deste ano?": """
#             SELECT TO_CHAR(DATA_PEDIDO, 'YYYY-MM') AS MES, SUM(VALOR_TOTAL) AS TOTAL_VENDAS
#             FROM Pedido
#             WHERE EXTRACT(YEAR FROM DATA_PEDIDO) = EXTRACT(YEAR FROM SYSDATE)
#             GROUP BY TO_CHAR(DATA_PEDIDO, 'YYYY-MM')
#             ORDER BY MES
#         """,
#         "Qual é o total de vendas do ano passado?": """
#             SELECT SUM(VALOR_TOTAL) AS TOTAL_VENDAS
#             FROM Pedido
#             WHERE EXTRACT(YEAR FROM DATA_PEDIDO) = EXTRACT(YEAR FROM SYSDATE) - 1
#         """,
#         "Qual produto teve mais vendas?": """
#             SELECT NOME_PRODUTO, SUM(QUANTIDADE_VENDIDA) AS TOTAL_VENDAS
#             FROM Pedido_Produto
#             GROUP BY NOME_PRODUTO
#             ORDER BY TOTAL_VENDAS DESC
#             FETCH FIRST 1 ROWS ONLY
#         """
#     }

#     # Mapeamento dos gráficos com plotly
#     plotly_mapping = {
#         "Qual é o total de vendas por mês deste ano?": """
#             fig = px.line(df, x='MES', y='TOTAL_VENDAS', title='Total de Vendas por Mês')
#             fig.update_layout(xaxis_title='Mês', yaxis_title='Total de Vendas')
#         """,
#         "Qual é o total de vendas do ano passado?": """
#             fig = px.bar(x=['Ano Passado'], y=[df['TOTAL_VENDAS'].values[0]], title='Total de Vendas do Ano Passado')
#             fig.update_layout(xaxis_title='Ano', yaxis_title='Total de Vendas')
#         """,
#         "Qual produto teve mais vendas?": """
#             fig = px.bar(df, x='NOME_PRODUTO', y='TOTAL_VENDAS', title='Produto com Mais Vendas')
#             fig.update_layout(xaxis_title='Produto', yaxis_title='Total de Vendas')
#         """
#     }

#     if question in sql_mapping:
#         sql = sql_mapping[question]
#         df = query_database(sql)
#         if isinstance(df, pd.DataFrame):
#             if df.empty:
#                 return jsonify({"error": "Nenhum dado encontrado para a consulta."}), 404

#             # Retornar tabela e gráfico se a consulta for bem-sucedida
#             plot_code = plotly_mapping.get(question)
#             img_base64 = generate_plot(df, plot_code) if plot_code else None
            
#             return jsonify({
#                 "data": df.to_dict(orient='records'),
#                 "graph": img_base64
#             })
#         else:
#             return jsonify({"error": df}), 400
#     else:
#         return jsonify({"error": "Pergunta não encontrada."}), 404

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=5001)
# from flask import Flask, jsonify, request
# from flask_cors import CORS
# import jaydebeapi
# import pandas as pd
# import plotly.express as px
# import base64
# from io import BytesIO

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})

# # Funções de mapeamento SQL e Plotly
# sql_mapping = {
#     "Qual é o total de vendas por mês deste ano?": """
#         SELECT TO_CHAR(DATA_PEDIDO, 'YYYY-MM') AS MES, SUM(VALOR_TOTAL) AS TOTAL_VENDAS
#         FROM Pedido
#         WHERE EXTRACT(YEAR FROM DATA_PEDIDO) = EXTRACT(YEAR FROM SYSDATE)
#         GROUP BY TO_CHAR(DATA_PEDIDO, 'YYYY-MM')
#         ORDER BY MES
#     """,
#     "Qual é o total de vendas do ano passado?": """
#         SELECT SUM(VALOR_TOTAL) AS TOTAL_VENDAS
#         FROM Pedido
#         WHERE EXTRACT(YEAR FROM DATA_PEDIDO) = EXTRACT(YEAR FROM SYSDATE) - 1
#     """,
#     "Qual produto teve mais vendas?": """
#         SELECT NOME_PRODUTO, SUM(QUANTIDADE_VENDIDA) AS TOTAL_VENDAS
#         FROM Pedido_Produto
#         GROUP BY NOME_PRODUTO
#         ORDER BY TOTAL_VENDAS DESC
#         FETCH FIRST 1 ROWS ONLY
#     """
# }

# plotly_mapping = {
#     "Qual é o total de vendas por mês deste ano?": """
#         fig = px.line(df, x='MES', y='TOTAL_VENDAS', title='Total de Vendas por Mês')
#         fig.update_layout(xaxis_title='Mês', yaxis_title='Total de Vendas')
#     """,
#     "Qual é o total de vendas do ano passado?": """
#         fig = px.bar(x=['Ano Passado'], y=[df['TOTAL_VENDAS'].values[0]], title='Total de Vendas do Ano Passado')
#         fig.update_layout(xaxis_title='Ano', yaxis_title='Total de Vendas')
#     """,
#     "Qual produto teve mais vendas?": """
#         fig = px.bar(df, x='NOME_PRODUTO', y='TOTAL_VENDAS', title='Produto com Mais Vendas')
#         fig.update_layout(xaxis_title='Produto', yaxis_title='Total de Vendas')
#     """
# }

# # Função para executar a query
# def query_database(query):
#     try:
#         conn = jaydebeapi.connect(
#             "oracle.jdbc.driver.OracleDriver",
#             "jdbc:oracle:thin:@oracle.fiap.com.br:1521/orcl",
#             ["RM98974", "100903"],
#             "/Users/USER/Desktop/sqldeveloper/JDBC/lib/ojdbc11.jar"
#         )
#         cursor = conn.cursor()
#         cursor.execute(query)
#         data = cursor.fetchall()
#         columns = [desc[0] for desc in cursor.description]
#         df = pd.DataFrame(data, columns=columns)
#         cursor.close()
#         conn.close()
#         return df
#     except Exception as e:
#         return str(e)

# # Endpoint para processar perguntas
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

#             # Retornar tabela e gráfico se a consulta for bem-sucedida
#             plot_code = plotly_mapping.get(question)
#             img_base64 = generate_plot(df, plot_code) if plot_code else None
            
#             return jsonify({
#                 "data": df.to_dict(orient='records'),
#                 "graph": img_base64
#             })
#         else:
#             return jsonify({"error": df}), 400
#     else:
#         return jsonify({"error": "Pergunta não encontrada."}), 404

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=5001)

#################################################################
# from flask import Flask, jsonify, request,send_from_directory
# from flask_cors import CORS
# import jaydebeapi
# import pandas as pd
# import plotly.express as px
# import base64
# import plotly.graph_objs as go
# import os  # Adicione essa importação
# from datetime import datetime  # Para nomear arquivos com data/hora

# from io import BytesIO

# app = Flask(__name__)
# CORS(app)

# # def generate_plot(df, plot_code):
# #     try:
# #         local_vars = {'df': df}
# #         code = compile(plot_code, '<string>', 'exec')
# #         exec(code, globals(), local_vars)
# #         fig = local_vars.get('fig')
        
# #         if fig:
# #             buffer = BytesIO()
# #             fig.write_image(buffer, format="png")
# #             buffer.seek(0)
# #             img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
# #             return img_base64
# #         else:
# #             return None
# #     except Exception as e:
# #         return str(e)
# # def generate_plot(df, plot_code):
# #     try:
# #         local_vars = {'df': df}
# #         code = compile(plot_code, '<string>', 'exec')
# #         exec(code, globals(), local_vars)
# #         fig = local_vars.get('fig')

# #         if fig:
# #             buffer = BytesIO()
# #             fig.write_image(buffer, format="png")
# #             buffer.seek(0)
# #             img_base64 = base64.b64encode(buffer.read()).decode('utf-8')
# #             print("Imagem do gráfico gerada:", img_base64)  # Adicione este log
# #             return img_base64
# #         else:
# #             return None
# #     except Exception as e:
# #         return str(e)
# # def generate_plot(df, plot_code):
# #     try:
# #         local_vars = {'df': df}
# #         code = compile(plot_code, '<string>', 'exec')
        
# #         # Execução do código e verificação
# #         exec(code, globals(), local_vars)
        
# #         fig = local_vars.get('fig')
        
# #         if fig is None:
# #             raise ValueError("A variável 'fig' não foi gerada pelo código Plotly.")

# #         output_dir = 'static/plots'
# #         os.makedirs(output_dir, exist_ok=True)

# #         # Gere um nome de arquivo com timestamp
# #         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# #         file_path = os.path.join(output_dir, f"plot_{timestamp}.png")

# #         # Salve a imagem
# #         fig.write_image(file_path)
# #         print(f"Imagem do gráfico salva em: {file_path}")

# #         return file_path  # Retorna o caminho do arquivo
# #     except Exception as e:
# #         print("Erro ao gerar gráfico:", e)
# #         return str(e)

# ################################################
# # def generate_plot(df, plot_code):
# #     try:
# #         local_vars = {'df': df}
# #         code = compile(plot_code, '<string>', 'exec')
# #         exec(code, globals(), local_vars)
        
# #         fig = local_vars.get('fig')

# #         if fig is None:
# #             raise ValueError("A variável 'fig' não foi gerada pelo código Plotly.")

# #         # Crie um diretório para armazenar as imagens se não existir
# #         output_dir = 'static/plots'
# #         os.makedirs(output_dir, exist_ok=True)

# #         # Salve a imagem com um nome fixo para facilitar o teste
# #         file_path = os.path.join(output_dir, "plot.png")  
# #         fig.write_image(file_path)
# #         print(f"Imagem do gráfico salva em: {file_path}")  # Log do caminho do arquivo

# #         return file_path  # Retorna o caminho do arquivo
# #     except Exception as e:
# #         print("Erro ao gerar gráfico:", e)
# #         return str(e)
# ################################################################################################
# def generate_plot_html(df, plot_code):
#     try:
#         local_vars = {'df': df}
#         code = compile(plot_code, '<string>', 'exec')
#         exec(code, globals(), local_vars)
        
#         fig = local_vars.get('fig')

#         if fig is None:
#             raise ValueError("A variável 'fig' não foi gerada pelo código Plotly.")
        
#         # Retorna o gráfico em HTML
#         return fig.to_html(full_html=False)
#     except Exception as e:
#         print("Erro ao gerar gráfico:", e)
#         return str(e)



# # # Função para executar a query
# # def query_database(query):
# #     try:
# #         conn = jaydebeapi.connect(
# #             "oracle.jdbc.driver.OracleDriver",
# #             "jdbc:oracle:thin:@oracle.fiap.com.br:1521/orcl",
# #             ["RM98974", "100903"],
# #             "/Users/USER/Desktop/sqldeveloper/JDBC/lib/ojdbc11.jar"
# #         )
# #         cursor = conn.cursor()
# #         cursor.execute(query)
# #         data = cursor.fetchall()
# #         columns = [desc[0] for desc in cursor.description]
# #         df = pd.DataFrame(data, columns=columns)
# #         cursor.close()
# #         conn.close()
# #         return df
# #     except Exception as e:
# #         return str(e)
# def query_database(query):
#     try:
#         print("Conectando ao banco de dados...")  # Log para verificar a conexão
#         conn = jaydebeapi.connect(
#             "oracle.jdbc.driver.OracleDriver",
#             "jdbc:oracle:thin:@oracle.fiap.com.br:1521/orcl",
#             ["RM98974", "100903"],
#             "/Users/USER/Desktop/sqldeveloper/JDBC/lib/ojdbc11.jar"
#         )
#         cursor = conn.cursor()
#         print(f"Executando consulta: {query}")  # Log da consulta
#         cursor.execute(query)
#         data = cursor.fetchall()
#         columns = [desc[0] for desc in cursor.description]
#         df = pd.DataFrame(data, columns=columns)
#         cursor.close()
#         conn.close()
#         print("DataFrame retornado:", df)  # Log do DataFrame
#         return df
#     except Exception as e:
#         print("Erro na consulta:", e)  # Log de erro
#         return str(e)


# # Mapeamento SQL e de gráficos
# sql_mapping = {
#     "Qual é o total de vendas por mês deste ano?": """
#         SELECT TO_CHAR(DATA_PEDIDO, 'YYYY-MM') AS MES, SUM(VALOR_TOTAL) AS TOTAL_VENDAS
#         FROM Pedido
#         WHERE EXTRACT(YEAR FROM DATA_PEDIDO) = EXTRACT(YEAR FROM SYSDATE)
#         GROUP BY TO_CHAR(DATA_PEDIDO, 'YYYY-MM')
#         ORDER BY MES
#     """,
#     "Qual é o total de vendas do ano passado?": """
#         SELECT SUM(VALOR_TOTAL) AS TOTAL_VENDAS
#         FROM Pedido
#         WHERE EXTRACT(YEAR FROM DATA_PEDIDO) = EXTRACT(YEAR FROM SYSDATE) - 1
#     """,
#     "Qual produto teve mais vendas?": """
#         SELECT NOME_PRODUTO, SUM(QUANTIDADE_VENDIDA) AS TOTAL_VENDAS
#         FROM Pedido_Produto
#         GROUP BY NOME_PRODUTO
#         ORDER BY TOTAL_VENDAS DESC
#         FETCH FIRST 1 ROWS ONLY
#     """
# }
# plotly_mapping = {
#     "Qual é o total de vendas por mês deste ano?": """
# fig = px.line(df, x='MES', y='TOTAL_VENDAS', title='Total de Vendas por Mês')
# """,
#     "Qual é o total de vendas do ano passado?": """
# fig = px.bar(x=['Ano Passado'], y=[df['TOTAL_VENDAS'].values[0]], title='Total de Vendas do Ano Passado')
# """,
#     "Qual produto teve mais vendas?": """
# fig = px.bar(df, x='NOME_PRODUTO', y='TOTAL_VENDAS', title='Produto com Mais Vendas')
# """
# }


# # Endpoint para processar perguntas
# # @app.route('/process_question', methods=['POST'])
# # def process_question():
# #     data = request.json
# #     question = data.get("question")

# #     if question in sql_mapping:
# #         sql = sql_mapping[question]
# #         df = query_database(sql)

# #         if isinstance(df, pd.DataFrame):
# #             if df.empty:
# #                 return jsonify({"error": "Nenhum dado encontrado para a consulta."}), 404

# #             # Retornar tabela e gráfico se a consulta for bem-sucedida
# #             plot_code = plotly_mapping.get(question)
# #             img_base64 = generate_plot(df, plot_code) if plot_code else None
            
# #             return jsonify({
# #                 "data": df.to_dict(orient='records'),
# #                 "graph": img_base64
# #             })
# #         else:
# #             return jsonify({"error": df}), 400
# #     else:
# #         return jsonify({"error": "Pergunta não encontrada."}), 404
# # Endpoint para processar perguntas
# # 
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
#             print(f"Código para gerar gráfico: {plot_code}")  # Adicione este log
            
#             # image_path = generate_plot(df, plot_code) if plot_code else None
#             html_graph = generate_plot_html(df, plot_code) if plot_code else None
            
#             # # Construir a URL da imagem
#             # if image_path:
#             #     image_url = f"http://{request.host}/static/plots/{os.path.basename(image_path)}"
#             # else:
#             #     image_url = None

#             return jsonify({
#                 "data": df.to_dict(orient='records'),
#                 "graph": html_graph  # Retorna a HTML da imagem
#             })
#         else:
#             return jsonify({"error": df}), 400
#     else:
#         return jsonify({"error": "Pergunta não encontrada."}), 404

# @app.route('/static/<path:filename>')
# def static_files(filename):
#     return send_from_directory('static', filename)

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0', port=5001)



# from flask import Flask, jsonify, request
# import pandas as pd
# import plotly.graph_objects as go

# app = Flask(__name__)

# # Mapeamento de perguntas para SQL e gráficos
# sql_mapping = {
#     "Qual é o total de vendas por mês deste ano?": "SELECT * FROM vendas WHERE ano = EXTRACT(YEAR FROM CURRENT_DATE)",
#     "Qual é o total de vendas do ano passado?": "SELECT * FROM vendas WHERE ano = EXTRACT(YEAR FROM CURRENT_DATE) - 1",
#     "Qual produto teve mais vendas?": "SELECT produto, COUNT(*) as total_vendas FROM vendas GROUP BY produto ORDER BY total_vendas DESC LIMIT 1"
# }

# plotly_mapping = {
#     "Qual é o total de vendas por mês deste ano?": "grafico_vendas_mes",
#     "Qual é o total de vendas do ano passado?": "grafico_vendas_ano",
#     "Qual produto teve mais vendas?": "grafico_produto_popular"
# }

# def query_database(sql):
#     # Implemente aqui a lógica para consultar o banco de dados usando o SQL fornecido
#     # Por enquanto, vamos retornar um DataFrame de exemplo
#     # Exemplo: return pd.DataFrame({'x_column': [1, 2, 3], 'y_column': [10, 20, 30]})
#     return pd.DataFrame({'x_column': ['Jan', 'Feb', 'Mar'], 'y_column': [10, 20, 30]})

# def generate_plot_html(df, plot_code):
#     # Exemplo de geração de gráfico usando Plotly
#     if plot_code == "grafico_vendas_mes":
#         fig = go.Figure(data=[
#             go.Bar(x=df['x_column'], y=df['y_column'])
#         ])
#     else:
#         # Crie outros gráficos conforme necessário
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
#             print(f"Código para gerar gráfico: {plot_code}")  # Adicione este log
            
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
#     app.run(debug=True)




# from flask import Flask, jsonify, request
# import pandas as pd
# import plotly.graph_objects as go
# import cx_Oracle

# app = Flask(__name__)

# # Credenciais do banco de dados Oracle
# username = "RM98974"
# password = "100903"
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
#     "Qual é o total de vendas do ano passado?": "SELECT * FROM vendas WHERE ano = EXTRACT(YEAR FROM CURRENT_DATE) - 1",  # Ajuste conforme necessário
#     "Qual produto teve mais vendas?": "SELECT produto, COUNT(*) as total_vendas FROM vendas GROUP BY produto ORDER BY total_vendas DESC LIMIT 1"  # Ajuste conforme necessário
# }

# plotly_mapping = {
#     "Qual é o total de vendas por mês deste ano?": "grafico_vendas_mes",
#     "Qual é o total de vendas por loja?": "grafico_vendas_loja",
#     "Qual é o total de vendas do ano passado?": "grafico_vendas_ano",
#     "Qual produto teve mais vendas?": "grafico_produto_popular",
#     "Qual é a quantidade total de produtos em estoque por tipo?": "grafico_estoque",
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
#     else:
#         # Crie outros gráficos conforme necessário
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
#             print(f"Código para gerar gráfico: {plot_code}")  # Adicione este log
            
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
username = "RM98974"
password = "100903"
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
    "Qual é o total de vendas do ano passado?": "SELECT * FROM vendas WHERE ano = EXTRACT(YEAR FROM CURRENT_DATE) - 1",  # Ajuste conforme necessário
    "Qual produto teve mais vendas?": "SELECT produto, COUNT(*) as total_vendas FROM vendas GROUP BY produto ORDER BY total_vendas DESC LIMIT 1"  # Ajuste conforme necessário
}

plotly_mapping = {
    "Qual é o total de vendas por mês deste ano?": "grafico_vendas_mes",
    "Qual é o total de vendas por loja?": "grafico_vendas_loja",
    "Qual é o total de vendas do ano passado?": "grafico_vendas_ano",
    "Qual produto teve mais vendas?": "grafico_produto_popular",
    "Qual é a quantidade total de produtos em estoque por tipo?": "grafico_estoque",
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
    elif plot_code == "grafico_vendas_loja":
        fig = go.Figure(data=[
            go.Bar(x=df['NOME_LOJA'], y=df['TOTAL_VENDAS'])
        ])
    elif plot_code == "grafico_estoque":  # Adicionando a geração do gráfico para estoque
        print("Gerando gráfico de estoque...")  # Log para confirmar a geração do gráfico
        fig = go.Figure(data=[
            go.Bar(x=df['TIPO_PRODUTO'], y=df['TOTAL_ESTOQUE'])
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
