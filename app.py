# ----------------------------------------
# TELECOM ANALYTICS DASHBOARD (POWER BI STYLE)
# ----------------------------------------

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# ----------------------------------------
# PAGE CONFIG
# ----------------------------------------

st.set_page_config(page_title="Telecom Analytics", layout="wide")

# ----------------------------------------
# 1. DATASET (5000 USERS)
# ----------------------------------------

np.random.seed(42)
n = 5000

companies = ["Jio", "Airtel", "Vodafone Idea", "BSNL"]

data = {
    "CustomerID": range(1, n+1),
    "Company": np.random.choice(companies, n, p=[0.4, 0.3, 0.2, 0.1]),
    "Age": np.random.randint(18, 70, n),
    "Tenure": np.random.exponential(scale=24, size=n).astype(int).clip(1, 72),
    "MonthlyCharges": np.random.randint(300, 6000, n),
    "ContractType": np.random.choice(["Month-to-Month", "One Year", "Two Year"], n),
    "InternetService": np.random.choice(["DSL", "Fiber", "No"], n),
    "TechSupport": np.random.choice(["Yes", "No"], n),
    "OnlineSecurity": np.random.choice(["Yes", "No"], n),
    "PaymentMethod": np.random.choice(["CreditCard", "DebitCard", "BankTransfer", "Cash"], n),
}

df_display = pd.DataFrame(data)
df = df_display.copy()

# ----------------------------------------
# CHURN LOGIC
# ----------------------------------------

df["Churn"] = (
    ((df["Tenure"] < 12) & (df["MonthlyCharges"] > 4000)) |
    ((df["ContractType"] == "Month-to-Month") & (df["MonthlyCharges"] > 3500)) |
    ((df["TechSupport"] == "No") & (df["OnlineSecurity"] == "No")) |
    ((df["Company"] == "Vodafone Idea") & (df["Tenure"] < 24)) |
    ((df["Company"] == "BSNL") & (df["InternetService"] == "DSL")) |
    ((df["Company"] == "Jio") & (df["MonthlyCharges"] < 800))
).astype(int)

df_display["Churn"] = df["Churn"]

# ----------------------------------------
# ENCODING (FOR MODEL ONLY)
# ----------------------------------------

company_map = {"Jio": 0, "Airtel": 1, "Vodafone Idea": 2, "BSNL": 3}
contract_map = {"Month-to-Month": 0, "One Year": 1, "Two Year": 2}
internet_map = {"DSL": 0, "Fiber": 1, "No": 2}
yes_no_map = {"No": 0, "Yes": 1}
payment_map = {"CreditCard": 0, "DebitCard": 1, "BankTransfer": 2, "Cash": 3}

df["Company"] = df["Company"].map(company_map)
df["ContractType"] = df["ContractType"].map(contract_map)
df["InternetService"] = df["InternetService"].map(internet_map)
df["TechSupport"] = df["TechSupport"].map(yes_no_map)
df["OnlineSecurity"] = df["OnlineSecurity"].map(yes_no_map)
df["PaymentMethod"] = df["PaymentMethod"].map(payment_map)

# ----------------------------------------
# MODEL
# ----------------------------------------

X = df.drop(["Churn", "CustomerID"], axis=1)
y = df["Churn"]

sc = StandardScaler()
X_scaled = sc.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# ----------------------------------------
# SIDEBAR NAVIGATION + FILTER
# ----------------------------------------

st.sidebar.title("📡 Telecom Analytics")

page = st.sidebar.radio("Navigate", [
    "Overview",
    "Company Comparison",
    "Prediction"
])

company_names = ["All", "Jio", "Airtel", "Vodafone Idea", "BSNL"]

selected_company = st.sidebar.selectbox("Select Company", company_names)

if selected_company != "All":
    filtered_display = df_display[df_display["Company"] == selected_company]
else:
    filtered_display = df_display.copy()

st.markdown(f"### 📍 Current View: {selected_company}")

# ----------------------------------------
# OVERVIEW
# ----------------------------------------

if page == "Overview":

    st.title("📊 Telecom Analytics Overview")

    # KPI Cards
    col1, col2, col3 = st.columns(3)

    col1.markdown(f"### 👥 Customers\n## {len(filtered_display)}")
    col2.markdown(f"### 🔁 Churn Rate\n## {round(filtered_display['Churn'].mean()*100, 2)}%")
    col3.markdown(f"### 💰 Avg Charges\n## ₹ {int(filtered_display['MonthlyCharges'].mean())}")

    # Charts
    col1, col2 = st.columns(2)

    with col1:
        fig = px.pie(
            filtered_display,
            names="Churn",
            hole=0.5,
            title="Customer Churn Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.scatter(
            filtered_display,
            x="Tenure",
            y="MonthlyCharges",
            color="Churn",
            hover_data=["Company"],
            title="Customer Behavior"
        )
        st.plotly_chart(fig, use_container_width=True)

    # Distribution
    fig = px.histogram(
        filtered_display,
        x="MonthlyCharges",
        nbins=40,
        title="Monthly Charges Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

# ----------------------------------------
# COMPANY COMPARISON
# ----------------------------------------

elif page == "Company Comparison":

    st.title("📊 Company Comparison")

    if selected_company == "All":

        stats = df_display.groupby("Company").agg({
            "Churn": "mean",
            "MonthlyCharges": "mean",
            "Tenure": "mean"
        }).reset_index()

        stats["Churn Rate (%)"] = stats["Churn"] * 100

        st.dataframe(stats)

        fig = px.bar(
            stats,
            x="Company",
            y="Churn Rate (%)",
            color="Company",
            text="Churn Rate (%)",
            title="Churn Rate by Company"
        )
        fig.update_traces(textposition='outside')

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.info(f"Detailed insights for {selected_company}")

# ----------------------------------------
# PREDICTION
# ----------------------------------------

elif page == "Prediction":

    st.title("🔮 Churn Prediction")

    company = st.selectbox("Company", ["Jio", "Airtel", "Vodafone Idea", "BSNL"])
    age = st.slider("Age", 18, 70)
    tenure = st.slider("Tenure", 1, 72)
    charges = st.slider("Monthly Charges", 300, 6000)

    contract = st.selectbox("Contract", ["Month-to-Month", "One Year", "Two Year"])
    internet = st.selectbox("Internet", ["DSL", "Fiber", "No"])
    tech = st.selectbox("Tech Support", ["Yes", "No"])
    security = st.selectbox("Online Security", ["Yes", "No"])
    payment = st.selectbox("Payment", ["CreditCard", "DebitCard", "BankTransfer", "Cash"])

    input_data = np.array([[
        company_map[company],
        age,
        tenure,
        charges,
        contract_map[contract],
        internet_map[internet],
        yes_no_map[tech],
        yes_no_map[security],
        payment_map[payment]
    ]])

    input_scaled = sc.transform(input_data)

    if st.button("Predict"):
        result = model.predict(input_scaled)[0]

        if result == 1:
            st.error("⚠️ High churn probability")
        else:
            st.success("✅ Customer likely to stay")
