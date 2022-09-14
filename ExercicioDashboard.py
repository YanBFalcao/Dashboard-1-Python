from dash import Dash, html, dcc #dcc = componentes do dashboard
import plotly.express as px #cria gráficos
import pandas as pd #ler base de dados

# =================================== - IMPORTAÇÕES - ==================================

# ==================== - LEITURA E CRIAÇÃO/CONSTRUÇÃO DE GRÁFICOS - ====================

app = Dash(__name__) #criando o aplicativo por meio de uso do flask

#df = data frame do python
df = pd.read_excel("Producao.xlsx")

fig = px.bar(df, x="TIPO CONT.", y="OPERADOR", color="BANCO", barmode="group")
#fig -> onde ele cria o gráfico

#fig2 = px.bar(df, x="BANCO", y="STATUS", color="STATUS", barmode="group")


# ================== - INFORMAÇÕES APRESENTAÇÃO EM NAVEGADOR (HTML) - ==================
app.layout = html.Div(children=[
    html.H1(children='Produção Loja'),
    html.H2(children='Gráfico de Toda a produção da Loja'),
    html.Div(children=''' OBS: Esse gráfico mostra parcialmente a produção, devido a fins de estudo '''),

    dcc.Graph
    (
        id='example-graph',
        figure=fig
    )

])

if __name__ == '__main__':
    app.run_server(debug=True) #Vai ler dentro de um navegador localhost