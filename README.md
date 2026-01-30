<img width="1659" height="480" alt="image" src="https://github.com/user-attachments/assets/04120d44-38af-4be1-8d2e-9b264bed7d01" />

---

## 🚦 Traffic Accident Risk Prediction Dashboard

An **interactive machine learning dashboard** built using **Streamlit, Plotly, and custom HTML/CSS** to predict the **risk of traffic accidents** based on real-world driving and environmental factors.

This project combines **ML prediction**, **data preprocessing**, and a **modern UI** for real-time accident risk analysis.

---

## ✨ Features

* 🧠 **Machine Learning Prediction**

  * Logistic Regression model
  * Scaler + Imputer preprocessing pipeline

* 🎨 **Premium UI**

  * Custom HTML & CSS (glassmorphism style)
  * KPI cards with risk indicators
  * Clean and modern dashboard layout

* 📊 **Interactive Visualizations (Plotly)**

  * Accident Risk Gauge
  * Probability Bar Chart
  * Hover, zoom, and animations

* 🎯 **User-Friendly Inputs**

  * Dropdowns for categorical data
  * Sliders for numeric ranges
  * Sidebar-based controls

---

## 🛠️ Tech Stack

* **Frontend / Dashboard**: Streamlit, HTML, CSS
* **Visualization**: Plotly
* **Machine Learning**: Scikit-learn
* **Model Storage**: Joblib
* **Language**: Python 3.8+

---
<img width="1874" height="907" alt="image" src="https://github.com/user-attachments/assets/e3ae13ad-f5de-4515-a582-042c7fea8638" />
<img width="1884" height="898" alt="image" src="https://github.com/user-attachments/assets/16326ee7-d9e5-41ee-b426-733cceff944f" />


## 📂 Project Structure

```
├── app.py                 # Main Streamlit application
├── logistic_model.pkl     # Trained ML model
├── scaler.pkl             # Feature scaler
├── imputer.pkl            # Missing value imputer
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/traffic-accident-dashboard.git
cd traffic-accident-dashboard
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 📊 Model Workflow

1. User enters input values
2. Data is **imputed** (missing values handled)
3. Features are **scaled**
4. ML model predicts:

   * Accident Risk (High / Low)
   * Probability score
5. Results are visualized via **interactive charts**

---

## 🚨 Important Note

⚠️ **Accident Severity** should only be used as an input **if it was part of the training features**.
If it was the **target variable**, remove it to avoid **data leakage**.

---

## 📈 Future Enhancements

* 🧠 SHAP-based explainability
* 🎚️ Risk threshold slider
* 📍 Accident heatmap (geo-visualization)
* ☁️ Cloud deployment (Streamlit Cloud / AWS)
* 🌗 Dark / Light mode toggle

---
<img width="1659" height="480" alt="image" src="https://github.com/user-attachments/assets/9040511e-099e-4464-916f-b6ddbeb6c3db" />


## 👨‍💻 Author

Built with ❤️ using **Python, ML, and modern UI design**
Perfect for:

* Final year projects
* ML portfolios
* Data science demos

---

#
---

