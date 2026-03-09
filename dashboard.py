import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard", page_icon="📊")

st.title("📊 Coffee Shop Dashboard")

data = {
    "Coffee": ["Espresso", "Latte", "Cappuccino", "Americano", "Mocha"],
    "Orders": [20, 45, 30, 25, 18]
}

df = pd.DataFrame(data)

st.subheader("Sales Table")
st.dataframe(df)

st.subheader("Sales Chart")

chart_type = st.selectbox(
    "Select Chart Type",
    ["Bar Chart", "Line Chart", "Area Chart"]
)

if chart_type == "Bar Chart":
    st.bar_chart(df.set_index("Coffee"))

elif chart_type == "Line Chart":
    st.line_chart(df.set_index("Coffee"))

else:
    st.area_chart(df.set_index("Coffee"))