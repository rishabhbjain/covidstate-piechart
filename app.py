import plotly.express as px
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html


df = pd.read_csv("us-states.csv")
df.drop(['fips',], axis=1, inplace=True)
df = df.loc[df['date'] == '5/21/20']
df.drop(['date'], axis=1, inplace=True)

fig = px.pie(df, values='cases', names='state', title='Statewise - Distribution of COVID - 19 (date till 5/21/2020)')
fig.show()


app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
