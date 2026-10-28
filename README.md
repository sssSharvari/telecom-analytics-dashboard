# 📊 Telecom Analytics Dashboard

An interactive **telecom customer analytics dashboard** built with Python and Streamlit to explore customer churn, compare telecom companies, visualize customer behavior, and predict churn using Logistic Regression.

## 🚀 Project Overview

Customer churn is a major challenge for telecom companies. Understanding customer behavior and identifying customers who may leave can help businesses improve retention strategies.

This project provides an interactive dashboard for analyzing customer churn patterns using synthetic telecom customer data. It combines data visualization with a machine learning model to demonstrate how analytics can support customer retention decisions.

## ✨ Features

- **Customer Churn Analysis:** Visualize churn distribution and explore customer characteristics.
- **Company Comparison:** Compare telecom companies using available customer analytics.
- **Interactive Visualizations:** Explore data through interactive charts built with Plotly.
- **Churn Prediction:** Use a Logistic Regression model to predict whether a customer may churn based on selected attributes.
- **Customer Insights:** Analyze factors such as tenure, monthly charges, contract type, internet service, and support services.
- **Interactive Dashboard:** Filter and explore analytics through a Streamlit web interface.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Streamlit** — Interactive web application
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical operations and synthetic data generation
- **Plotly** — Interactive data visualizations
- **Scikit-learn** — Feature scaling, data splitting, and Logistic Regression

## 📂 Project Structure

```text
telecom-analytics-dashboard/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/sssSharvari/telecom-analytics-dashboard.git
```

### 2. Navigate to the project directory

```bash
cd telecom-analytics-dashboard
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install the dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser. If it does not open automatically, use the local URL displayed in the terminal.

## 📈 Machine Learning Approach

The project uses **Logistic Regression**, a supervised classification algorithm, to demonstrate customer churn prediction.

The workflow includes:

1. Generate synthetic telecom customer data.
2. Prepare customer attributes for model input.
3. Split the dataset into training and testing sets.
4. Scale numerical features where appropriate.
5. Train the Logistic Regression model.
6. Use customer attributes to generate churn predictions.
7. Present analysis and predictions through the dashboard.

## 📊 Customer Attributes

The model uses attributes such as:

- Company
- Age
- Customer tenure
- Monthly charges
- Contract type
- Internet service
- Technical support
- Online security
- Payment method

## 🧪 Dataset and Limitations

**Important:** This project generates synthetic customer data for demonstration and learning purposes. It does not use actual telecom company records.

The churn labels are generated using predefined rules, so the model demonstrates a machine learning workflow rather than establishing real-world predictive performance. Results should not be interpreted as validated business predictions.

## 🔮 Future Improvements

- Add model evaluation metrics, including accuracy, precision, recall, F1-score, and a confusion matrix.
- Display calibrated churn probabilities alongside predictions.
- Improve categorical feature encoding and model preprocessing.
- Enhance company-specific filtering and comparison.
- Integrate a real, publicly available telecom churn dataset.
- Add model comparison and feature importance analysis.
- Deploy the dashboard online using Streamlit Community Cloud.

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Exploratory data analysis
- Interactive dashboard development
- Data visualization
- Machine learning classification
- Data preprocessing
- Python application development

## 👩‍💻 Author

**Sharvari Pradeep Sasane**

- GitHub: [@sssSharvari](https://github.com/sssSharvari)

---

*Developed as a learning project to explore telecom analytics, customer churn, and machine learning using Python.*
