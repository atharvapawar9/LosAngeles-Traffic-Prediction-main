import streamlit as st

# App title
st.title("Los Angeles Traffic Prediction Map")

# Dropdown to select between different map outputs
map_choice = st.selectbox("Select a traffic map:", [
    "Heatmap Traffic Map",
    "Optimized Traffic Map"
])

# Map file selection
map_files = {
    "Heatmap Traffic Map": "heatmap_traffic_map.html",
    "Optimized Traffic Map": "optimized_traffic_map.html"
}

# Load and display selected HTML map
with open(map_files[map_choice], 'r', encoding='utf-8') as f:
    html_data = f.read()

st.components.v1.html(html_data, height=600, scrolling=True)
