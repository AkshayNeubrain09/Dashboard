#!/usr/bin/env python
# coding: utf-8

# # loading the required libraries

# In[1]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State#, Event
import random
import plotly
import plotly.express as px
import dash_bootstrap_components as dbc


# # Google sheet link

# In[2]:


#https://docs.google.com/spreadsheets/d/1TBWzMhDOdz1z3v3Rqy3TxuHnkBaBXrLV3BgIgrXykm8/edit?usp=sharing


# # Loading the Data from above google sheet link

# In[3]:


import pandas as pd

sheet_id='1TBWzMhDOdz1z3v3Rqy3TxuHnkBaBXrLV3BgIgrXykm8'

xls=pd.ExcelFile(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx")

df=pd.read_excel(xls,'2023',header=0)
 


# # creating the pivote table for product , Month, year, category columns

# In[4]:


pivot_7 = pd.pivot_table(df,index=['PRODUCT'],aggfunc= 'sum')
pivot_7['PRODUCT'] = pivot_7.index                                  


# In[5]:


pivot_1 = pd.pivot_table(df,index=['MONTH'],aggfunc= 'sum')
pivot_6 = pd.pivot_table(df,index=['YEAR'],aggfunc= 'sum')           


# In[6]:


pivot_1['MONTH'] = pivot_1.index


# In[7]:


pivot_3 = pd.pivot_table(df,index=['CATEGORY'],aggfunc= 'sum')

pivot_3['CATEGORY'] = pivot_3.index


# # creating Mosaic Plot  for categories column

# In[8]:


fig3 = px.treemap(pivot_3,path=[px.Constant("Category"), 'CATEGORY'],values='TOTAL SELLING VALUE')


# In[9]:


pivot = pd.pivot_table(df,index=['DAY'],aggfunc= 'sum')          #pivot table for Day column


# In[10]:


pivot['DAY'] = pivot.index


# In[11]:


pivot_4 = pd.pivot_table(df,index=['SALE TYPE'],aggfunc= 'sum')
pivot_5 = pd.pivot_table(df,index=['PAYMENT MODE'],aggfunc= 'sum')   #pivot table for sales type column


# In[12]:


pivot_4['SALE TYPE'] = pivot_4.index
pivot_5['PAYMENT MODE'] = pivot_5.index              #adding the index values as new column to the  pivot table 


# In[13]:


df['YEAR']=df['YEAR'].astype(str)
df['MONTH']=df['MONTH'].astype(str)   #converting year and month as str data type


# In[ ]:


from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px

# Instantiate our App and incorporate BOOTSTRAP theme stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
# Incorporate data into App

# Build the layout to define what will be displayed on the page
app.layout = dbc.Container([
    dbc.Row([
       dbc.Col([
           html.H1("Customer Sales Analysis")           #headding tag for dash board
       ], width=12)
    ], justify="center"),
    
    dbc.Row([
       dbc.Col([
           html.H2("Total Sales 4014119$")                    # adding total sales, total profit, total profit% in the second row of our dash board
       ], width=4),
        dbc.Col([
           html.H2("Total profit 68907.92$")
       ], width=4),
        dbc.Col([
           html.H2("Total profit% 17.16")
       ], width=4)
    ]),
    html.Br(),
    html.Br(),
    
    dbc.Row([
       dbc.Col([
           html.H3("Please Select the Year and Month")          #in the third row of our dash board creating the heading tag 
       ], width=6),
        dbc.Col([
            
                 html.Div([
            html.Label('select year'),                          # adding common filters for all the figures in dash board
             dcc.RadioItems(id='linedropdown@1',               #creating radio button for selecting year
                options=['2021','2022'],
                value='2021'
               
            ),
            ],className='six columns'),
            
            
       ], width=4),
        dbc.Col([
            
           html.Div([
            html.Label('select month'),
            dcc.Dropdown(id='linedropdown@2',
                options=[
                         {'label': 'JAN', 'value': '1'},
                         {'label': 'FEB', 'value': '2'},
                    {'label': 'MAR', 'value': '3'},                 # creating dropdown for selecting month 
                    {'label': 'APR', 'value': '4'},
                    {'label': 'MAY', 'value': '5'},
                    {'label': 'JUN', 'value': '6'},
                    {'label': 'JUL', 'value': '7'},
                    {'label': 'AUG', 'value': '8'},
                    {'label': 'SEP', 'value': '9'},
                    {'label': 'OCT', 'value': '10'},
                    {'label': 'NUV', 'value': '11'},
                    {'label': 'DEC', 'value': '12'}
                    
                ],
                value='1',
                multi=False,
                clearable=False
            ),
            ],className='six columns'),
            
       ], width=2)
    ]),
    
    dbc.Row([
        dbc.Col([
                 html.Div([
            html.Label('Sales Type'),
            dcc.Dropdown(id='linedropdown',                        # crating filter of dropdown for sales type
                options=[
                         {'label': 'TOTAL BUYING VALUE', 'value': 'TOTAL BUYING VALUE'},
                         {'label': 'TOTAL SELLING VALUE', 'value': 'TOTAL SELLING VALUE'},
                         {'label': 'profit', 'value': 'profit'} 
                    
                ],
                value='TOTAL BUYING VALUE',
                multi=False,
                clearable=False
            ),
            ]),
               html.Div(id='dd-output-container'),
                  
        ], width=6),
        
        dbc.Col([
            
            html.Div([
                
               html.Div(id='dd-output-container@1'),

    ],className='row'),
            
            
        ], width=6)
        ]),
        
    
    dbc.Row([
        dbc.Col([
            
            
            html.Div([
                 html.Div([
            html.Label('Payment Type'),
                     html.Br(),
            dcc.Dropdown(id='linedropdown01',                 # crating filter of dropdown for sales type                  
                options=[
                         {'label': 'TOTAL BUYING VALUE', 'value':'TOTAL BUYING VALUE'},
                         {'label': 'TOTAL SELLING VALUE','value':'TOTAL SELLING VALUE'}
                ],
                value='TOTAL BUYING VALUE',
                multi=False,
                clearable=False
            ),
            ],className='six columns'),
               html.Div(id='dd-output-container01'),

    ],className='row'), 
            
            
            
        ], width=4),
        dbc.Col([
            
            html.Div([
                 html.Div([
            html.Label('Day Statistics'),
                     html.Br(),                                 
            dcc.Dropdown(id='linedropdown@9',             # crating filter of dropdown for Day Statistics using sales type
                options=[
                         {'label': 'TOTAL BUYING VALUE', 'value': 'TOTAL BUYING VALUE'},
                         {'label': 'TOTAL SELLING VALUE', 'value': 'TOTAL SELLING VALUE'}
                ],
                value='TOTAL BUYING VALUE',
                multi=False,
                clearable=False
            ),
            ],className='six columns'),
               html.Div(id='dd-output-container@9'),

    ],className='row'),
            
            
        ], width=4),
        
        dbc.Col([
            html.Label('Different Categories'),                      # creating Mosaic Plot to the dashboard
            dcc.Graph(
        id='PAYMENT MODE',
        figure=fig3),
        ], width=4)
    ])
])

# callback is used to create app interactivity
#@callback()
@app.callback(
    Output('dd-output-container', 'children'),                 #call backs for common filters, connecting the year radio button an month dropdown into it
    Input('linedropdown', 'value'),
    Input('linedropdown@1', 'value'),
    Input('linedropdown@2', 'value')
)
def  update_table(input_value,a,b):
    df1=df.loc[df['YEAR']==a]
    df2=df1.loc[df['MONTH']==b]
    
    return dcc.Graph(figure=px.pie(df2, values=input_value, names='SALE TYPE',hole=.3))   
            
                
@app.callback(
    Output('dd-output-container01', 'children'),
    Input('linedropdown01', 'value'),                      #call back for pie chart for payment mode
    Input('linedropdown@1', 'value'),
    Input('linedropdown@2', 'value')
)
def  update_table(input_value,a,b):
    df1=df.loc[df['YEAR']==a]
    df2=df1.loc[df['MONTH']==b]
    
    return dcc.Graph(figure=px.pie(df2, values=input_value, names='PAYMENT MODE',hole=.3)) 


@app.callback(
    Output('dd-output-container@1', 'children'),
    Input('linedropdown@1', 'value'),                         #call back for bar graph for products
    Input('linedropdown@2', 'value')
)
def building(a,b):
    df1=df.loc[df['YEAR']==a]
    df2=df1.loc[df['MONTH']==b]
    return dcc.Graph(figure=px.bar(df2, x="TOTAL SELLING VALUE", y="PRODUCT", orientation='h'))
    #return df2
    
@app.callback(
    Output('dd-output-container@9', 'children'),
    Input('linedropdown@9', 'value'),
    Input('linedropdown@1', 'value'),                   #call dask for day statistics using area plot
    Input('linedropdown@2', 'value')
)
def  update_table(input_value,a,b):
    df1=df.loc[df['YEAR']==a]
    df2=df1.loc[df['MONTH']==b]
    return dcc.Graph(figure=px.area(df2, x='DAY', y=input_value)) 
    


# Run the App
if __name__ == '__main__':
    app.run_server(port=8501)


# In[ ]:




