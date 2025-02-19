from flask import Flask, redirect, render_template, request, g, url_for
import dash
from dash import Dash, dcc, html, Input, Output, callback, dash_table, no_update
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from dash.exceptions import PreventUpdate
import plotly
import plotly.express as px
import pandas as pd

#####################

# creates empty pandas dataFrame
df = pd.DataFrame()

# creates empty figure: needed for no data source selected
fig = dict({"data": [{"type": "scatter",
                      "x": [],
                      "y": []}]})


sourcepaths=[ # Code removed to not share intelectial property!
              # Add sourcepaths list here.
            ]


#####################
# populates dataframe and figure with selected sourcepath
def populates_df_fig(sourcepath, dataframe, figure):

  
    # copies dataframe
    dff = dataframe

    # copies figure
    ffig = figure
        
    if sourcepath != "":

        # Code removed to not share intelectial property!
        # Add other datasource API here.
        # dff = astrophysics_api()

        # creates id column to help with user interactions with graph
        dff['id'] = dff['Filename']

        # reset index to new id column
        dff.set_index('id', inplace=True, drop=False)


        #####################
        # figure for graph
        ffig = px.scatter(
            dff, 
            x="Time", 
            y="RV", 
            color="Instrument", symbol="Instrument",
            #template="sandstone",
            error_y="Error",
            hover_data=["Filename"],
            #marginal_x="histogram", marginal_y="rug"
            )


        #####################
        # settings for legends on figure
        ffig.update_layout(legend=dict(
            orientation="h",
            entrywidth=80,
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))

        # adds a title to the figure
        # fig.update_layout(title_text=selected_datasource,
        #                   title_font=dict(size=12, weight="bold"))

    return dff, ffig

# populates dataframe and figure with one sourcepath
# selected_datasource = sourcepaths[1]
# df, fig = populates_df_fig(selected_datasource, df, fig)

# populates dataframe and figure with all sourcepaths in sourcepath array
for sp in sourcepaths:
    df, fig = populates_df_fig(sp, df, fig)

#####################

server = Flask(__name__)

#####################
# stylesheet with the .dbc class to style dcc, DataTable and AG Grid components with a Bootstrap theme
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"


#####################
# dash main application
app = dash.Dash(
    server=server, 
    routes_pathname_prefix="/dash/", 
    external_stylesheets=[
        dbc.themes.BOOTSTRAP, 
        dbc.icons.FONT_AWESOME, 
        dbc_css,
        #'/static/styles.css'
        ]
    )


#####################
# dash component with graph
div_graph=dcc.Graph(
    id='rv-graph',
    figure=fig,
    className='col-12 graph-div shadow m-1 rounded align-items-center')


#####################
# dash component with information on data point
div_info=dcc.Markdown(
    id='info-div',
    children='',
    className='col info-div shadow p-3 m-1 rounded bg-light bg-gradient text-dark overflow-auto',
    style={'display': 'none',} )


#####################
# dash component with datatable
# for adding tooltip, elipsis to long text, etc: https://dash.plotly.com/datatable/width
div_datatable = dash_table.DataTable(
                 data=df.to_dict('records'),

                 columns=[              # only allows to hide some columns
                     {"name": i, "id": i, "deletable": True, "selectable": True, "hideable": True}
                     if i == "id" or i == "SourcePath" or i == "Error"
                     else {"name": i, "id": i, "deletable": True, "selectable": True}
                     for i in df.columns
                     ],  #fazer Time e Filename não editavel

                 id='datatable',
                 
                 editable=True,
                 filter_action="native",     # allow filtering of data by user ('native') or not ('none')
                 sort_action="native",       # enables data to be sorted per-column by user or not ('none')
                 sort_mode="single",
                 column_selectable="multi",
                 row_selectable="multi",
                 row_deletable=True,
                 selected_columns=[],        # ids of columns that user selects
                 selected_rows=[],           # indices of rows that user selects
                 
                 page_current=0,             # page number that user is on
                 #page_size=10,               # number of rows visible per page

                 fixed_columns={'headers': True},
                 style_table={'overflowX': 'auto',
                              'min-width':'100%',
                              'max-width':'100%',
                              'width':'100%'},

                 style_cell={'textAlign': 'left',
                             'font-size':'9pt',
                             'minWidth': 95, 
                             'maxWidth': 95, 
                             'width': 95 },
                             
                 style_header={'backgroundColor': 'rgb(211, 211, 211)',
                               'fontWeight': 'bold'},

                
                 export_format='csv', 
                 export_headers='names',
                 export_columns='visible',

                 hidden_columns='id',

                 fixed_rows={ 'headers': True, 'data': 0 },
                 virtualization=True,
                 page_action='none', # all data is passed to the table up-front or not ('none')

                 css=[
                     {"selector": ".dash-spreadsheet-menu", "rule": 'flex-direction: row-reverse !important; padding-bottom: 5px;'},
                     {"selector": ".dash-spreadsheet-menu button", "rule": 'border-radius: 5px;'} ]
                )


#####################
# card bootstrap component with dash datatable
card_datatable=dbc.Card(
    div_datatable, body=True, #color="secondary"
    className='shadow p-3 m-1 rounded bg-light bg-gradient border-0',
)

#####################
# dash component dropdown
div_dropdown = dcc.Dropdown(
                sourcepaths, #df['SourcePath'].unique(),
                'Select a Source Path',
                id='dropdown',
            )

#####################
# dash general layout
app.layout = dbc.Container(
    [
        html.Br(),
        dbc.Row([
            dbc.Col( div_dropdown )
        ]),

        html.Br(),
        # row with graph and info box
        dbc.Row(
            [
            html.Div(id='graph-container', className='col-12 graph-div shadow m-1 rounded align-items-center'),
            div_info,
            ], id='graph-info-div'
       ),
        
        html.Br(),
        dbc.Row( 
            dbc.Col( card_datatable )
        ),

        html.Br(),
        
    ],
    fluid=True,
    className="dbc container",
    )




#####################
# callback for creating a graph chart, with updated data from datatable
@app.callback(
    Output(component_id='graph-container', component_property='children'),
    [Input(component_id='datatable', component_property="derived_virtual_data"),
     Input(component_id='datatable', component_property='derived_virtual_selected_rows')]
)
def update_graph(all_rows_data, slctd_row_indices):

    # creates a copy of dataframe
    dff = pd.DataFrame(all_rows_data)

    # used to highlight selected countries on graph
    colors = ['#008000' if i in slctd_row_indices else ''
              for i in range(len(dff))]

    if "Time" in dff and "RV" in dff:
        figure_graph = px.scatter(
            data_frame=dff,
            x="Time",
            y='RV',
            color="Instrument", symbol="Instrument",
            error_y="Error",
            labels={"RV"},
            hover_data=["Filename"],
            )
        
        figure_graph.update_layout(legend=dict(
            orientation="h",
            entrywidth=80,
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
            ))
        
        dcc_graph = dcc.Graph(
            id='graph-chart',
            figure=figure_graph,
            #className='col-12 graph-div shadow m-2 rounded align-items-center'
            )

        return [dcc_graph]


#####################
# callback for dropdown
@callback(
    #[Output(component_id='graph-container', component_property='children')],
    [Input('dropdown', 'value')],
    prevent_initial_call=True
)
def update_output(dropdown_selected):
     if dropdown_selected is None:
        raise PreventUpdate
     
     selected_datasource = dropdown_selected
     
     dff, ffig = populates_df_fig(selected_datasource, df, fig)



#####################
# callback to show info div when clicking data on graph
@callback(
    [Output(component_id='info-div', component_property='style'),
    Output(component_id='info-div', component_property='children'),
    Output(component_id='graph-container', component_property='className')],
    [Input (component_id='graph-chart', component_property='clickData'),
     Input('dropdown', 'value')],
    prevent_initial_call=True
)
def update_text(user_selected, dropdown_selected): 
# function arguments come from the component property of the Input or State
    if user_selected:
        raw_value = user_selected.get('points')[0]
        selected_datasource = dropdown_selected

        # extraction of values to be displayed
        value_filename = raw_value.get('customdata')
        value_rv =  raw_value.get('y')
        value_time = raw_value.get('x')
        value_error_rv = raw_value.get('error_y.array')
        instrument_index = raw_value.get('curveNumber')
        value_instrument = fig.data[instrument_index].legendgroup
        value_sourcepath = selected_datasource

        # use markdown style in info_div_content
        info_div_content = f'''
        ##### Data Point Info:
        * __Instrument:__ {value_instrument}
        * __Time:__ {value_time}
        * __RV:__ {value_rv}
        * __Error RV:__ {value_error_rv}
        * __Filename:__ {value_filename}
        * __SourcePath:__ {value_sourcepath}
        '''

        new_style = {'display': 'block'}
        new_children = [info_div_content]
        new_className = 'col-8 graph-div shadow p-3 m-1 rounded'

        # returned objects assigned to the component properties of the Output
        return [ new_style, new_children, new_className ]



#####################
# flask endpoints
@server.route("/", methods=("POST", "GET"))
@server.route('/dashboard')
def index():
    df_html = df.to_html(classes='table-data table table-striped', header="true"
        ).replace('<tr style="text-align: right;">', '<tr>')

    return render_template(
        "dashboard.html",
        title="Dashboard", 
        tables=[df_html]
        )


#####################
# dash application is set to run as server
if __name__ == '__main__':
   app.run_server(debug = True)
