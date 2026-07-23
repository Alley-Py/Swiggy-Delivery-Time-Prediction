import streamlit as st
import pandas as pd
import pickle
from datetime import datetime
from PIL import Image

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Swiggy ETA Predictor",
    page_icon="🚚",
    layout="wide"
)

# ==========================================================
# LOAD MODEL
# ==========================================================

with open(
        "PL_Swiggy_delivery_time_prediction.pkl",
        "rb"
) as f:

    model = pickle.load(f)

# ==========================================================
# DARK THEME CSS
# ==========================================================

st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

section[data-testid="stSidebar"]{
    background-color:#161A23;
}

.main-title{
    font-size:42px;
    font-weight:bold;
    color:#FC8019;
}

.subtitle{
    font-size:18px;
    color:#C9D1D9;
}

.prediction-card{

    background:linear-gradient(
        135deg,
        #FC8019,
        #FF9F43
    );

    padding:35px;

    border-radius:25px;

    text-align:center;

    color:white;

    box-shadow:
        0px 8px 20px rgba(0,0,0,0.4);
}

div.stButton > button:first-child{

    background-color:#FC8019;

    color:white;

    height:60px;

    width:100%;

    border-radius:15px;

    border:none;

    font-size:20px;

    font-weight:bold;
}

</style>
""",
unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

col1, col2 = st.columns(
    [1,4]
)

with col1:

    st.image(
        "swiggy_logo.png",
        width=120
    )

with col2:

    st.markdown(
    """
    <div class='main-title'>

    🚚 Swiggy ETA Prediction System

    </div>

    <div class='subtitle'>

    Predict food delivery times using
    Machine Learning and LightGBM

    </div>
    """,

    unsafe_allow_html=True
    )

# ==========================================================
# MODEL PERFORMANCE
# ==========================================================

c1, c2, c3 = st.columns(3)

c1.metric(
    "MAE",
    "3.18 mins"
)

c2.metric(
    "RMSE",
    "3.99"
)

c3.metric(
    "R² Score",
    "81.9%"
)

st.markdown("---")

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.header(
    "📝 Delivery Details"
)

age = st.sidebar.slider(
    "Rider Age",
    18,
    60,
    30
)

ratings = st.sidebar.slider(
    "Rider Rating",
    1.0,
    5.0,
    4.5
)

weather = st.sidebar.selectbox(
    "Weather",
    ['sunny', 'stormy', 'sandstorms', 'cloudy', 'fog', 'windy']
)

traffic = st.sidebar.selectbox(
    "Traffic",
    [
        "low",
        "medium",
        "high",
        "jam"
    ]
)

vehicle_condition = st.sidebar.selectbox(
    "Vehicle Condition",
    [0, 1, 2]
)

type_of_order = st.sidebar.selectbox(
    "Type of Order",
    [
        "meal",
        "snack",
        "drinks",
        "buffet"
    ]
)

type_of_vehicle = st.sidebar.selectbox(
    "Vehicle Type",
    [
        "motorcycle",
        "scooter",
        "electric_scooter"
    ]
)

multiple_deliveries = st.sidebar.slider(
    "Multiple Deliveries",
    0,
    3,
    0
)

festival = st.sidebar.selectbox(
    "Festival",
    [
        "no",
        "yes"
    ]
)

city_type = st.sidebar.selectbox(
    "City Type",
    [
        "semi-urban",
        "urban",
        "metropolitian"
    ]
)

city_name = st.sidebar.selectbox(
    "City Name",
    [
        "BANG",
        "CHEN",
        "HYD",
        "JAP",
        "KNP",
        "KOC",
        "KOL",
        "MUM",
        "PUNE",
        "RANCHI",
        "SURAT"
    ]
)

pickup_time_minutes = st.sidebar.slider(
    "Pickup Time (Minutes)",
    0,
    60,
    15
)

distance = st.sidebar.slider(
    "Distance (KM)",
    0.0,
    30.0,
    5.0
)

# ==========================================================
# AUTO GENERATED FEATURES
# ==========================================================

now = datetime.now()

order_day = now.day

order_month = now.month

day_map = {

    0: "monday",
    1: "tuesday",
    2: "wednesday",
    3: "thursday",
    4: "friday",
    5: "saturday",
    6: "sunday"
}

order_day_of_week = day_map[
    now.weekday()
]

is_weekend = int(
    now.weekday() >= 5
)

order_time_hour = now.hour

# ----------------------------------------------------------

if 5 <= order_time_hour < 12:

    order_time_of_day = "morning"

elif 12 <= order_time_hour < 17:

    order_time_of_day = "afternoon"

elif 17 <= order_time_hour < 22:

    order_time_of_day = "evening"

elif 22 <= order_time_hour <= 23:

    order_time_of_day = "night"

else:

    order_time_of_day = "after_midnight"

# ----------------------------------------------------------

peak_hours = [12, 13, 19, 20, 21]

is_peak_hour = int(
    order_time_hour in peak_hours
)

# ==========================================================
# CURRENT ORDER INFORMATION
# ==========================================================

st.subheader(
    "📊 Current Order Information"
)

a, b, c = st.columns(3)

a.info(
    f"🕒 Hour : {order_time_hour}"
)

b.info(
    f"📅 Day : {order_day_of_week.title()}"
)

c.info(
    f"🔥 Peak Hour : {'Yes' if is_peak_hour else 'No'}"
)

st.markdown("---")

# ==========================================================
# PREDICTION
# ==========================================================

if st.button(
        "🚀 Predict Delivery Time"
):

    input_df = pd.DataFrame({

        "age": [age],
        "ratings": [ratings],
        "weather": [weather],
        "traffic": [traffic],
        "vehicle_condition": [vehicle_condition],
        "type_of_order": [type_of_order],
        "type_of_vehicle": [type_of_vehicle],
        "multiple_deliveries": [multiple_deliveries],
        "festival": [festival],
        "city_type": [city_type],
        "city_name": [city_name],
        "order_day": [order_day],
        "order_month": [order_month],
        "order_day_of_week": [order_day_of_week],
        "is_weekend": [is_weekend],
        "pickup_time_minutes": [pickup_time_minutes],
        "order_time_hour": [order_time_hour],
        "order_time_of_day": [order_time_of_day],
        "distance": [distance],
        "is_peak_hour": [is_peak_hour]

    })

    prediction = model.predict(
        input_df
    )[0]

    # ======================================================
    # RESULT CARD
    # ======================================================

    st.markdown(
        f"""
        <div class='prediction-card'>

        <h2>

        Estimated Delivery Time

        </h2>

        <h1>

        {prediction:.2f} Minutes

        </h1>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    # ======================================================
    # DELIVERY STATUS
    # ======================================================

    if prediction <= 20:

        st.success(
            "🚀 Fast Delivery Expected"
        )

    elif prediction <= 35:

        st.warning(
            "⏳ Moderate Delivery Time"
        )

    else:

        st.error(
            "🚨 Delivery Delay Possible"
        )

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption(
"""
Developed Using:

✅ LightGBM  
✅ CRISP-ML(Q) Methodology  
✅ Streamlit Deployment  

Final Model Performance:

MAE : 3.18 Minutes  
RMSE : 3.99  
R² : 81.9%
"""
)