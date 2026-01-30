import streamlit as st
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px

# ===============================
# Page Config
# ===============================
st.set_page_config(
    page_title="Traffic Accident Risk Dashboard",
    page_icon="🚦",
    layout="wide"
)

# ===============================
# Custom CSS
# ===============================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

.main-title {
    font-size: 42px;
    font-weight: 800;
    color: white;
}

.sub-title {
    color: #d1d5db;
    margin-bottom: 30px;
}

.card {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    color: white;
    text-align: center;
}

.card h2 {
    font-size: 22px;
    color: #e5e7eb;
}

.card h1 {
    font-size: 36px;
    margin: 10px 0;
}

.badge-high {
    background: #ef4444;
    padding: 6px 14px;
    border-radius: 20px;
}

.badge-low {
    background: #22c55e;
    padding: 6px 14px;
    border-radius: 20px;
}

.footer {
    text-align: center;
    color: #9ca3af;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# Header
# ===============================
st.markdown('<div class="main-title">🚦 Traffic Accident Risk Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">AI-powered real-time accident risk analysis</div>', unsafe_allow_html=True)

# ===============================
# Load Model
# ===============================
@st.cache_resource
def load_objects():
    return (
        joblib.load("logistic_model.pkl"),
        joblib.load("scaler.pkl"),
        joblib.load("imputer.pkl")
    )

model, scaler, imputer = load_objects()

# ===============================
# Sidebar Inputs
# ===============================
st.sidebar.header("📝 Input Parameters")

weather = st.sidebar.selectbox("Weather", [0,1,2,3],
    format_func=lambda x: ["Clear","Rainy","Foggy","Stormy"][x])

road_type = st.sidebar.selectbox("Road Type", [0,1,2],
    format_func=lambda x: ["Highway","City","Rural"][x])

time_of_day = st.sidebar.selectbox("Time of Day", [0,1,2,3],
    format_func=lambda x: ["Morning","Afternoon","Evening","Night"][x])

traffic_density = st.sidebar.slider("Traffic Density", 0, 100, 30)
speed_limit = st.sidebar.slider("Speed Limit (km/h)", 20, 120, 60)
num_vehicles = st.sidebar.number_input("Number of Vehicles", 1, step=1)

driver_alcohol = st.sidebar.selectbox("Driver Alcohol", [0,1],
    format_func=lambda x: "Yes" if x else "No")

acc_severity = st.sidebar.selectbox("Accident Severity", [0,1,2],
    format_func=lambda x: ["Low","Medium","High"][x])

road_condition = st.sidebar.selectbox("Road Condition", [0,1,2],
    format_func=lambda x: ["Dry","Wet","Icy"][x])

vehicle_type = st.sidebar.selectbox("Vehicle Type", [0,1,2],
    format_func=lambda x: ["Car","Truck","Bike"][x])

driver_age = st.sidebar.slider("Driver Age", 18, 80, 25)
experience = st.sidebar.slider("Experience (Years)", 0, 40, 2)

light_condition = st.sidebar.selectbox("Light Condition", [0,1,2],
    format_func=lambda x: ["Daylight","Street Light","Dark"][x])

# ===============================
# Input Array
# ===============================
X = np.array([[weather, road_type, time_of_day, traffic_density,
               speed_limit, num_vehicles, driver_alcohol,
               acc_severity, road_condition, vehicle_type,
               driver_age, experience, light_condition]])

# ===============================
# Prediction
# ===============================
if st.sidebar.button("🚀 Predict Risk"):

    X_scaled = scaler.transform(imputer.transform(X))
    pred = model.predict(X_scaled)[0]
    prob = model.predict_proba(X_scaled)[0]
    risk = prob[1] * 100

    # ===============================
    # KPI Cards
    # ===============================
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="card">
            <h2>Accident Risk</h2>
            <h1>{risk:.1f}%</h1>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        badge = "badge-high" if pred else "badge-low"
        label = "High Risk ⚠️" if pred else "Low Risk ✅"
        st.markdown(f"""
        <div class="card">
            <h2>Prediction</h2>
            <span class="{badge}">{label}</span>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="card">
            <h2>Model Confidence</h2>
            <h1>{max(prob)*100:.1f}%</h1>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ===============================
    # Gauge
    # ===============================
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk,
        title={"text": "Accident Risk (%)"},
        gauge={
            "axis": {"range": [0, 100]},
            "steps": [
                {"range": [0, 40], "color": "#22c55e"},
                {"range": [40, 70], "color": "#f59e0b"},
                {"range": [70, 100], "color": "#ef4444"},
            ],
            "bar": {"color": "#ef4444"},
        }
    ))

    st.plotly_chart(gauge, use_container_width=True)

    # ===============================
    # Probability Chart
    # ===============================
    df = {"Risk": ["Low", "High"], "Probability": prob}
    fig = px.bar(df, x="Risk", y="Probability", text_auto=".2f", range_y=[0,1])
    st.plotly_chart(fig, use_container_width=True)

# ===============================
# Footer
# ===============================
st.markdown('<div class="footer">🚦 Designed with HTML, CSS, Plotly & Streamlit</div>',
            unsafe_allow_html=True)
