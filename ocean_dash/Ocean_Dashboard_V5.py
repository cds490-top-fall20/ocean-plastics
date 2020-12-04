import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go
import plotly.figure_factory as ff

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import numpy as np

app = dash.Dash(__name__)

# ------------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)

df2 = pd.read_csv("earth_challenge.csv")
df2 = df2[df2["COUNTRY"]== 'United States']
df2 = df2.groupby(['ISO_SUB', 'Year'])[['SUM_Hard_PlasticBeverageBottle','SUM_Hard_OtherPlasticBottle','SUM_HardOrSoft_PlasticBottleCap',
                                        'SUM_PlasticOrFoamFoodContainer','SUM_Hard_BucketOrCrate','SUM_Hard_Lighter','SUM_OtherHardPlastic',
                                        'SUM_PlasticOrFoamPlatesBowlsCup','SUM_HardSoft_PersonalCareProduc','SUM_HardSoftLollipopStick_EarBu',
                                        'SUM_Soft_Bag','SUM_Soft_WrapperOrLabel','SUM_Soft_Straw','SUM_Soft_OtherPlastic','SUM_Soft_CigaretteButts',
                                       'SUM_Soft_StringRingRibbon','Fishing_Net','SUM_FishingLineLureRope','Fishing_BuoysAndFloats','SUM_Foam_OtherPlasticDebris',
                                       'SUM_OtherPlasticDebris','Totalltems_EventRecord']].sum()

df2.reset_index(inplace=True)

# ------------------------------------------------------------------------------

#Radio Items label
DEBRIS_TYPE = dict(
    HPBB ="Hard Plastic Beverage Bottle",
    HOPB = "Hard Other Plastic Bottle",
    HOSPBC = "Plastic Bottle Cap",
    POFFC = "Plastic Or Foam Food Container",
    HBOC = "Bucket Or Crate",
    HL = "Lighter",
    OHP = "Other Hard Plastic",
    POFPBC = "Plastic Or Foam Plates Bowls Cup",
    HSPCP = "Personal Care Product",
    HSLSE = "LollipopStick EarBud",
    SB = "Plastic Bags",
    SWOL = "Wrapper Or Label",
    SS = "Straw",
    SOP = "Soft Other Plastic",
    SCB = "Cigarette Butts",
    SSRR = "String Ring Ribbon",
    FN = "Fishing Net",
    FLLR = "Fishing Line Lure Rope",
    FBAF = "Fishing Buoys And Floats",
    SFOPD = "Foam Other Plastic Debris",
    SOPD = "Other Plastic Debris",
)

DEBRIS_TYPE_name = dict(
    HPBB ="SUM_Hard_PlasticBeverageBottle",
    HOPB = "SUM_Hard_OtherPlasticBottle",
    HOSPBC = "SUM_HardOrSoft_PlasticBottleCap",
    POFFC = "SUM_PlasticOrFoamFoodContainer",
    HBOC = "SUM_Hard_BucketOrCrate",
    HL = "SUM_Hard_Lighter",
    OHP = "SUM_OtherHardPlastic",
    POFPBC = "SUM_PlasticOrFoamPlatesBowlsCup",
    HSPCP = "SUM_HardSoft_PersonalCareProduc",
    HSLSE = "SUM_HardSoftLollipopStick_EarBu",
    SB = "SUM_Soft_Bag",
    SWOL = "SUM_Soft_WrapperOrLabel",
    SS = "SUM_Soft_Straw",
    SOP = "SUM_Soft_OtherPlastic",
    SCB = "SUM_Soft_CigaretteButts",
    SSRR = "SUM_Soft_StringRingRibbon",
    FN = "Fishing_Net",
    FLLR = "SUM_FishingLineLureRope",
    FBAF = "Fishing_BuoysAndFloats",
    SFOPD = "SUM_Foam_OtherPlasticDebris",
    SOPD = "SUM_OtherPlasticDebris",
)

debris_type_options = [
    {"label": str(DEBRIS_TYPE[debris_type]), "value": str(debris_type)}
    for debris_type in DEBRIS_TYPE
]

POLICY_TYPE = dict(
    CA2014 = "California 2014 SB 270",
    DC2010 = "District of Columbia 2010 B 150",
    NC2010 = "North Carolina 2010 SB 1018",
    NC2017 = "North Carolina 2017 HB 56",
    NY2008 = "New York 2008 AB 11725",
    DC2014 = "District of Columbia 2014 B20-0573"
)

policy_type_options = [
    {"label": str(POLICY_TYPE[policy_type]), "value": str(policy_type)}
    for policy_type in POLICY_TYPE
]

STATE_SELECT = dict(
    AL = "Alabama", AK = "Alaska", AZ = "Arizona",  AR = "Arkansas", CA = "California", CO = "Colorado",
    CT = "Connecticut", DE = "Delaware", FL = "Florida", GA = "Georgia", HI = "Hawaii",
    ID = "Idaho", IL = "Illinois", IN = "Indiana", IA = "Iowa", KS = "Kansas",
    KY = "Kentucky", LA = "Louisiana", ME = "Maine", MD = "Maryland", MA = "Massachusetts",
    MI = "Michigan", MN = "Minnesota", MS = "Mississippi", MO = "Missouri", MT = "Montana",
    NE = "Nebraska", NV = "Nevada", NH = "New Hampshire", NJ = "New Jersey", NM = "New Mexico",
    NY = "New York", NC = "North Carolina", ND = "North Dakota", OH = "Ohio", OK = "Oklahoma",
    OR = "Oregon", PA = "Pennsylvania", RI = "Rhode Island", SC = "South Carolina", SD = "South Dakota",
    TN = "Tennessee", TX = "Texas", UT = "Utah", VT = "Vermont", VA = "Virginia",
    WA = "Washington", WV = "West Virginia", WI = "Wisconsin", WY = "Wyoming", DC = "District of Columbia"
)

state_options = [
    {"label": str(STATE_SELECT[state_select]), "value": str(state_select)}
    for state_select in STATE_SELECT
]

# ------------------------------------------------------------------------------
# App layout
# ------------------------------------------------------------------------------

app.layout = html.Div([
    
    html.H1("Ocean Plastic Dashboard", style={'text-align': 'center'}),
    
    #first row
    html.Div([
        #first column
        html.Div([
            
            html.H3("Filter by EC Challenge 2020 Dates:"),
            
            dcc.Slider(id="slct_year",
               min = 2015,
               max = 2018,
               step  =None,
               marks = {
                   2015: "2015",
                   2016: "2016",
                   2017: "2017",
                   2018: "2018",
               },
                 value=2015
                 ),
            
            html.H3("Filter by Debris Type:"),
            
            dcc.RadioItems(id = "debris_type_selector",
                options=[
                    {'label': 'All', 'value': 'All'}, #will have to change values to fix layout later
                    {'label': 'Hard Plastics', 'value': 'Hard Plastics'},#all the plastic values
                    {'label': 'Soft Plastics', 'value': 'Soft Plastics'},
                    {'label': 'Hard/Soft Plastics', 'value': 'Hard/Soft Plastics'},
                    {'label': 'Foam Plastics', 'value': 'Foam Plastics'},
                    {'label': 'Fishing Plastics', 'value': 'Fishing Plastics'},
                    {'label': 'Other Plastics', 'value': 'Other Plastics'}
                ],
                labelStyle={'display': 'inline-block'},
                className = 'dcc_control'), 
            
            dcc.Dropdown(
                id = "debris_type",
                options = debris_type_options,
                multi = True,
                placeholder = "Select Debris Type",
                className = 'dcc_control',
            ),
            
            html.H3("Filter By State:"),
            dcc.Dropdown(
                id = "slct_the_state",
                options = state_options,
                placeholder = "Select State",
                className = 'dcc_control',
                value = 'CA'
            ),
            
            html.H3("Filter by State for Policy Enactment:"),
            dcc.Dropdown(
                id = "slct_state",
                options = policy_type_options,
                placeholder = "Select Policy Enactment",
                className = 'dcc_control',
                value = 'CA2014'
            ),
            
            dcc.Markdown(id = "policy",
                children = [])
            
        ], className = 'column 1', style={'display': 'inline-block', 'width': '35%', 'vertical-align': 'top','margin-left': 'auto' ,'margin-right':'auto' }),
        
        #second column
        html.Div([
                html.H2("Map of Debris by Selected Dates", style={'text-align': 'center'}),
                dcc.Graph(
                id='bar_graph',
                figure={}),   
        ], className = 'column 1', style={'display': 'inline-block', 'width':'45%', 'vertical-align': 'top', 'margin-left':'auto', 'margin-right' : 'auto'})
        
    ], className = 'firstRow'),
    
    #Second Row
    html.Div([
           html.H3("Percent of Debris in State by Year", style={'text-align': 'center'}),
           dcc.Graph(
            id = 'debris_map',
            figure = {})  
        ], className = 'SecondRow', style={'display': 'block', 'width': '100%'})    
])  

# ------------------------------------------------------------------------------
 # Connect the Plotly graphs with Dash Components

@app.callback(
    Output("debris_type_selector","value"),Input("slct_state","value"))

def display_status(slct_state):
    
    if slct_state is None:
        return None
    else:
        return "Soft Plastics"
    
@app.callback(
    Output("debris_type","value"),
    [Input("debris_type_selector","value"),
     Input("slct_state","value")])

def display_status(debris_type_selector,slct_state):
    
    if debris_type_selector is None:
        return None
    elif slct_state == 'DC2014':
        return ["POFFC", "SS", "POFPBC"]
    elif debris_type_selector == "All":
        return list(DEBRIS_TYPE.keys())
    elif debris_type_selector == "Hard Plastics":
        return ["HPBB","HOSPBC","HBOC","HL","HOPB","OHP"]
    elif debris_type_selector == "Soft Plastics" and slct_state is None:
        return ["SB","SWOL","SS","SOP","SCB","SSRR"]
    elif debris_type_selector == "Soft Plastics" and slct_state != None:
        return ["SB"]
    elif debris_type_selector == "Hard/Soft Plastics":
        return ["HSPCP", "HSLSE"]
    elif debris_type_selector == "Foam Plastics":
        return ["POFFC","POFPBC","SFOPD"]
    elif debris_type_selector == 'Fishing Plastics':
        return ["FN","FLLR","FBAF"]
    elif debris_type_selector == "Other Plastics":
        return ["HOPB","OHP","SFOPD","SOPD"] 

@app.callback(
    [Output(component_id='bar_graph', component_property='figure'),
     Output(component_id='debris_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value'),
     Input(component_id='debris_type', component_property='value'),
     Input(component_id='slct_state',component_property='value'),
     Input(component_id='slct_the_state',component_property='value')]
)

def update_graph(slct_year,debris_type,slct_state,slct_the_state):
    
    if debris_type is None:
        debris = ['SUM_Soft_Bag']
    else:
        debris = [DEBRIS_TYPE_name[x] for x in debris_type]
    
    dff = df2.copy()
    dff = dff.assign(Percent = dff[debris].sum(axis=1) / dff.iloc[:,23])
    dff = dff[dff["Year"] == slct_year]
    
    if slct_the_state != None:
        slct_state = slct_the_state
        dff2 = dff.copy()
        dff2 = dff2[dff2["ISO_SUB"] == slct_state]
    elif slct_state is None:
        dff2 = dff.copy()
        slct_the_state = None
    else:
        slct_state = slct_state[:-4]
        dff2 = dff.copy()
        dff2 = dff2[dff2["ISO_SUB"] == slct_state]
    
    # Plotly Express
    fig = px.choropleth(
        data_frame= dff2,
        locationmode='USA-states',
        locations= 'ISO_SUB',
        scope="usa",
        color='Percent',
        hover_data=['ISO_SUB', 'Percent'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Percent': 'Percent Debris'},
        template='plotly_dark',
        range_color = [0,1]
    )
    
    if slct_state is None:
        pass
    else:
        fig.update_geos(fitbounds="locations", visible=False)
    
    df3 = df2.copy()
    #df3 = df3.assign(Percent = df3[debris].sum(axis=1) / df3.iloc[:,23])
    
    #this code creates the dataframe of the selected debris
    deb_names = []
    for x in debris:
        name = 'Percent' + str(x)
        deb_names.append(name)
        #print(name)
        #print(df3[str(x)].sum()/df3.iloc[:,23])
        df3.insert(loc = len(df3.columns), column = name, value = df3[str(x)]/ df3.iloc[:,23])
        
    df3 = df3[df3["ISO_SUB"] == slct_state]
    
    print(df3)
    
    fig2 = px.line(
        data_frame = df3,
        x = 'Year',
        y = deb_names
    )
      
    return fig, fig2

@app.callback(
    [Output(component_id = 'policy', component_property = 'children')],
    [Input(component_id='slct_state',component_property='value')]
)

# all the code to update the text for the policy enactment
def update_text(slct_state):
    text = ['']
    if slct_state == 'CA2014':
        text = ['''
        ** California 2014 SB 270 **
        
        This Policy Enactment was passed in 2014, limiting single use carryout plastic bags, and went into effect July 2015
        
        [More info on this policy here](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=201320140SB270)
        
        [Info on all State Plastic Bag legislation here](https://www.ncsl.org/research/environment-and-natural-resources/plastic-bag-legislation.aspx)
        ''']
    elif slct_state == 'DC2010':
        text = ['''
        ** District of Columbia 2010 B 150 **
        
        bans the use of disposable non-recyclable plastic carryout bags, establishes a fee on all other disposable carryout bags
        
        [More info on this policy here](https://doee.dc.gov/sites/default/files/dc/sites/ddoe/publication/attachments/Anacostia%20Clean%20Up%20and%20Protection%20Act%20of%202009_3.20.15.pdf)
        
        [Info on all State Plastic Bag legislation here](https://www.ncsl.org/research/environment-and-natural-resources/plastic-bag-legislation.aspx)
        ''']
    elif slct_state == 'NC2010':
        text = ['''
        ** North Carolina 2010 SB 1018 **
        
        Reduces plastic and non-recycled paper bag use on North Carolina's Outer Banks
        
        [More info on this policy here](https://www.ncleg.net/Sessions/2009/Bills/Senate/PDF/S1018v6.pdf)
        
        [Info on all State Plastic Bag legislation here](https://www.ncsl.org/research/environment-and-natural-resources/plastic-bag-legislation.aspx)
        ''']
    elif slct_state == 'NC2017':
        text = ['''
        ** North Carolina 2017 HB 56 **
        
        Repeals the eight-year ban on the use of plastic bags by retailers on the Outer Banks.
        
        [More info on this policy here](https://www.ncleg.gov/Sessions/2017/Bills/House/PDF/H56v7.pdf)
        
        [Info on all State Plastic Bag legislation here](https://www.ncsl.org/research/environment-and-natural-resources/plastic-bag-legislation.aspx)
        ''']
    elif slct_state == 'NY2008':
        text = ['''
        ** New York 2008 AB 11725 **
        
        Plastic Bag Reduction, Reuse and Recycling Act
        
        [More info on this policy here](https://nyassembly.gov/leg/?bn=A.11725&term=2007)
        
        [Info on all State Plastic Bag legislation here](https://www.ncsl.org/research/environment-and-natural-resources/plastic-bag-legislation.aspx)
        ''']
    elif slct_state == 'DC2014':
        text = ['''
        ** District of Columbia 2014 B20-0573 **
        
        Bans on foam and plastic straws
        
        [More info on this policy here](https://doee.dc.gov/foodserviceware)
        
        [Info on all State Plastic Bag legislation here](https://www.ncsl.org/research/environment-and-natural-resources/plastic-bag-legislation.aspx)
        ''']
    
    
    return text
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True, host = '0.0.0.0')
