import streamlit as st
import pandas as pd
import time

# MUST be first Streamlit command
st.set_page_config(page_title="Starbeans Coffee App", page_icon="☕", layout="wide")

# =====================
# STYLE
# =====================
st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}

/* Main title */
h1 {
    text-align: center;
    color: #ffffff;
    font-size: 48px;
}

/* Subtitles */
h2, h3 {
    color: #e8f5e9;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0b3d2e;
    color: white;
}

/* Buttons */
.stButton>button {
    background-color: #00704A;
    color: white;
    border-radius: 12px;
    padding: 10px 20px;
    font-size: 16px;
}

.stButton>button:hover {
    background-color: #00a86b;
    transform: scale(1.05);
}

/* Input boxes */
input, textarea {
    border-radius: 8px !important;
}

/* Card style */
.card {
    padding:20px;
    border-radius:15px;
    background-color: rgba(255,255,255,0.08);
    box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
}

</style>
""", unsafe_allow_html=True)

# =====================
# HEADER
# =====================

st.markdown("## ☕ Coffee Menu")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/924/924514.png", width=120)
    st.subheader("Espresso")
    st.write("Strong and bold coffee.")
    st.write("Price: ₱80")
    if st.button("Select Espresso"):
        st.session_state["coffee"] = "Espresso"

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/924/924501.png", width=120)
    st.subheader("Latte")
    st.write("Smooth coffee with milk.")
    st.write("Price: ₱120")
    if st.button("Select Latte"):
        st.session_state["coffee"] = "Latte"

with col3:
    st.image("https://cdn-icons-png.flaticon.com/512/924/924523.png", width=120)
    st.subheader("Cappuccino")
    st.write("Rich espresso with foam.")
    st.write("Price: ₱130")
    if st.button("Select Cappuccino"):
        st.session_state["coffee"] = "Cappuccino"

# =====================
# SIDEBAR
# =====================

st.sidebar.title("☕ Starbeans Coffee")
dark_mode = st.sidebar.toggle("🌙 Dark Mode")

# =====================
# THEME
# =====================

if dark_mode:
    st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <style>
    .stApp {
        background-color: #f6fff8;
    }
    </style>
    """, unsafe_allow_html=True)

# =====================
# ORDER PAGE
# =====================

st.title("☕ Starbeans Coffee Ordering")

st.header("Customer Info")

name = st.text_input("Customer Name")
age = st.number_input("Age", 10, 100)

date = st.date_input("Order Date")
order_time = st.time_input("Order Time")

st.divider()

st.header("Choose Your Coffee")

size = st.radio(
    "Size",
    ["Small", "Medium", "Large"]
)

coffee = st.selectbox(
    "Coffee Type",
    ["Espresso", "Latte", "Cappuccino", "Americano", "Mocha"],
    index=0 if "coffee" not in st.session_state else
    ["Espresso","Latte","Cappuccino","Americano","Mocha"].index(st.session_state["coffee"])
)


sweetness = st.slider("Sweetness Level", 0, 10)

milk = st.checkbox("Add Milk (+10)")
sugar = st.checkbox("Add Sugar (+5)")
whipped = st.checkbox("Whipped Cream (+15)")

quantity = st.number_input("Quantity", 1, 10)

notes = st.text_area("Extra Notes")

st.subheader("Upload Cup Design (optional)")
design = st.file_uploader("Upload Image")

if st.button("Place Order"):

    prices = {
        "Espresso": 80,
        "Latte": 120,
        "Cappuccino": 130,
        "Americano": 90,
        "Mocha": 140
    }

    price = prices[coffee]

    if size == "Medium":
        price += 20
    elif size == "Large":
        price += 40

    if milk:
        price += 10
    if sugar:
        price += 5
    if whipped:
        price += 15

    total = price * quantity

    st.subheader("Processing Order")

    progress = st.progress(0)
    status = st.empty()

    for i in range(100):
        progress.progress(i + 1)
        status.text(f"Preparing coffee... {i+1}%")
        time.sleep(0.02)

    st.success("☕ Order Ready!")

    st.subheader("Order Summary")

    st.write("Customer:", name)
    st.write("Coffee:", coffee)
    st.write("Size:", size)
    st.write("Quantity:", quantity)
    st.write("Sweetness:", sweetness)

    st.success(f"Total Price: ₱{total}")

    # PAYMENT
    st.subheader("💳 Payment")

    payment_method = st.radio(
        "Payment Method",
        ["Cash", "Credit Card", "GCash"]
    )

    if payment_method == "Credit Card":
        card = st.text_input("Card Number")
        expiry = st.text_input("Expiry Date")
        cvv = st.text_input("CVV")

    if payment_method == "GCash":
        phone = st.text_input("GCash Number")

    if st.button("Confirm Payment"):

        st.success("✅ Payment Successful!")

page = st.sidebar.selectbox(
    "Navigation",
    ["Order Coffee", "Dashboard", "Feedback", "About"]
)
