import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

########### Define your variables ######

myheading1='What is ADDIE'
tabtitle = 'ADDIE'
list_of_options=['Assessment', 'Design', 'development', 'Implementation','Evaluation']
list_of_images=['Assessment-1.jpg', 'the-most-valuable-skills-for-instructional-designers-01.jpg', 'Web-design-Website-Development-Company-in-jodhpur-copy-1140x641.jpg', 'MKTCO14957-Implementation-infographic-for-TL-Blog-F.png', 'cite-infographic3.jpg']
sourceurl = 'https://xkcd.com/'
githublink = 'https://github.com/caroleonor/dash-callbacks-radio/edit/master/app.py'


########## Set up the chart

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    dcc.RadioItems( #dashboard components
        id='your_input_here',
        options=[ #unique features specific to the dc components, 
                #label and values to show what you want user to see, not the real name
                {'label':list_of_options[1], 'value':list_of_images[1]},
                {'label':list_of_options[2], 'value':list_of_images[2]},
                {'label':list_of_options[3], 'value':list_of_images[3]},
                {'label':list_of_options[4], 'value':list_of_images[4]},
                ],
        value=list_of_images[0], #which one is the default picture to show before they choosing 
        ),
    html.Div(id='your_output_here', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


########## Define Callback
@app.callback(Output('your_output_here', 'children'),
              [Input('your_input_here', 'value')])
def radio_results(image_you_chose):
    return html.Img(src=app.get_asset_url(image_you_chose), style={'width': 'auto', 'height': '50%'}),#can also use 200px, percentage will auto adjust


############ Deploy
if __name__ == '__main__':
    app.run_server()
