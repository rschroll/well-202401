import altair as alt
from vega_datasets import data

def make_map(df):

    # US states background
    states = alt.topo_feature(data.us_10m.url, feature='states')
    background = alt.Chart(states).mark_geoshape(
        fill='lightgray',
        stroke='white',
        tooltip=None
    ).properties(
        width=500,
        height=300
    ).project('albersUsa')
    
    df = df.dropna()
    
    points = (alt.Chart(df).mark_point()
          .encode(latitude=alt.Latitude('latitude'), longitude='longitude', 
                  color=alt.Color('gradient').scale(scheme='darkred', reverse=True),
                 tooltip=[alt.Tooltip('depth', title='Depth (m)'), 
                          alt.Tooltip('gradient', title='Gradient (°C/m)', format='.3f')])
          .properties(title='Well locations')
         )
    
    return background + points