import streamlit as st
import pandas as pd
import database
import wellplot

st.title("Abandoned Wells")

st.text("An interactive map of abandonded wells that can be used for geothermal energy")

depth = st.sidebar.number_input("Minimum Depth (m)", min_value=0, value=500)
gradient = st.sidebar.number_input("Gradient (°C/m)", min_value=0.0, value=0.05, format='%0.4f', step=0.001)

data = database.get_wells(depth, gradient)
df = pd.DataFrame(data)
chart = wellplot.make_map(df)



st.altair_chart(chart)