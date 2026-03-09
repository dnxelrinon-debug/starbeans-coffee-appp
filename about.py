import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ", layout="wide")

st.title(" About Starbeans Coffee App")

st.image("https://images.unsplash.com/photo-1509042239860-f550ce710b93", width=600)

st.markdown("""
### ☕ What does this app do?

This application simulates a **coffee ordering system**.

Users can:
- choose their coffee
- customize size and sweetness
- add toppings
- simulate payment
- view a sales dashboard
- send feedback
""")

st.divider()

st.markdown("### 🎯 Target Users")

st.write("""
This system is designed for **coffee shop customers**
who want a **simple and interactive digital ordering experience**.
""")

st.divider()

st.markdown("### ⚙ System Inputs")

st.write("""
- Customer Name  
- Coffee Type  
- Drink Size  
- Add-ons (Milk, Sugar, Whipped Cream)  
- Quantity  
- Payment Method  
""")

st.divider()

st.markdown("### 📊 System Outputs")

st.write("""
- Order Summary  
- Total Price  
- Coffee Sales Dashboard  
- Customer Feedback  
""")

st.success("Thank you for using Starbeans Coffee ☕")