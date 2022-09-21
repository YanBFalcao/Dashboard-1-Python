from dash import Dash, html, dcc, Input, Output #dcc = componentes do dashboard
import plotly.express as px #cria gráficos
import pandas as pd #ler base de dados

# =================================== - IMPORTAÇÕES - ==================================

# ==================== - LEITURA E CRIAÇÃO/CONSTRUÇÃO DE GRÁFICOS - ====================

app = Dash(__name__) #criando o aplicativo por meio de uso do flask

#df = data frame do python
df = pd.read_excel("Producao.xlsx")

fig = px.bar(df, x="TIPO CONT.", y="OPERADOR", color="BANCO", barmode="group")
#fig -> onde ele cria o gráfico

opcoes = list(df['BANCO'].unique())
opcoes.append("Todos os Bancos")
#Sempre que você quer selecionar uma coluna de uma tabela, colocar o nome da coluna entre colchetes

#fig2 = px.bar(df, x="BANCO", y="STATUS", color="STATUS", barmode="group")


# ================== - INFORMAÇÕES APRESENTAÇÃO EM NAVEGADOR (HTML) - ==================
app.layout = html.Div(children=[
    html.H1(children='Produção Loja'),
    html.H2(children='Gráfico de Toda a produção da Loja'),
    html.Div(children=''' OBS: Esse gráfico mostra parcialmente a produção, devido a fins de estudo '''),

    dcc.Dropdown(opcoes, value ='Todos os Bancos', id='botao-selecao'),
    #insere dentro do site, uma caixa com um botão de seleção

    dcc.Graph
    (
        id='Grafico-Bancos', #Nome do Gráfico
        figure=fig
    )
])

# ===================== CALL BACK =====================

@app.callback(
    Output('Grafico-Bancos', 'figure'),
    Input('botao-selecao', 'value')
)

def update_output(value):
    
    if value == "Todos os Bancos":
        fig = px.bar(df, x="TIPO CONT.", y="OPERADOR", color="BANCO", barmode="group")
    
    else:
        tabela_filtro = df.loc[df['TIPO CONT.'] == value, : ]
        fig = px.bar(tabela_filtro, x="TIPO CONT.", y="OPERADOR", color="BANCO", barmode="group")
        fig = px.bar()    

    return fig

# ===================== CALL BACK =====================


# ===================== DEBUG PRINCIPAL DO GRÁFICO =====================
if __name__ == '__main__':
    app.run_server(debug=True) #Vai ler dentro de um navegador localhost
