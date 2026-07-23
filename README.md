# 🚚 Swiggy Delivery Time Prediction using Machine Learning

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![LightGBM](https://img.shields.io/badge/LightGBM-Gradient_Boosting-green?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</p>

---

# 📌 Project Overview

This project develops an **end-to-end Machine Learning solution** to predict **Swiggy food delivery time (ETA)** using the **CRISP-ML(Q)** methodology. The model analyzes rider, order, environmental, geographical, and temporal factors to accurately estimate delivery time. The final solution is deployed as an interactive **Streamlit web application** for real-time ETA prediction.

---

# 🎯 Business Problem

Food delivery platforms like **Swiggy** process millions of orders every day, where accurate **Estimated Time of Arrival (ETA)** plays a vital role in customer satisfaction and operational efficiency. Delivery time is affected by several dynamic factors such as traffic, weather, delivery distance, rider performance, restaurant preparation time, and order demand. Inaccurate ETA predictions can lead to customer dissatisfaction, increased order cancellations, and inefficient resource utilization.

This project aims to build a data-driven machine learning solution capable of providing accurate and reliable delivery time predictions.

---

# 📊 Dataset Information

| Attribute | Details |
|------------|----------|
| Dataset | Swiggy Delivery Time Dataset |
| Dataset Size | **45,502 Rows × 26 Columns** |
| Problem Type | Supervised Machine Learning (Regression) |
| Target Variable | **time_taken** |

---

# 📋 Feature Description

## 📋 Feature Categories

| **Feature Category** | **Columns** | **Purpose** |
|----------------------|-------------|-------------|
| 👤 **Rider Information** | `rider_id`, `age`, `ratings`, `vehicle_condition`, `type_of_vehicle` | Captures rider demographics, vehicle details, and delivery performance characteristics that influence delivery efficiency. |
| 🛒 **Order Information** | `type_of_order`, `pickup_time_minutes`, `multiple_deliveries` | Represents order characteristics, restaurant preparation time, and rider workload during delivery. |
| 🌦 **Environmental Factors** | `weather`, `traffic`, `festival` | Describes external conditions that significantly impact travel time and delivery speed. |
| 📍 **Location Features** | `city_name`, `city_type`, `restaurant_latitude`, `restaurant_longitude`, `delivery_latitude`, `delivery_longitude`, `distance` | Captures geographical information and travel distance between the restaurant and customer, which directly affects ETA. |
| 📅 **Temporal Features** | `order_date`, `order_day`, `order_month`, `order_day_of_week`, `order_time_hour`, `order_time_of_day`, `is_weekend`, `is_peak_hour` | Represents date and time information to capture daily, weekly, monthly, weekend, and peak-hour delivery patterns. |
| 🎯 **Target Variable** | `time_taken` | Actual delivery time (in minutes) used as the target variable for regression. |

---

# 🔄 CRISP-ML(Q) Workflow

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Exploratory Data Analysis (EDA)
5. Feature Engineering
6. Model Building
7. Cross Validation
8. Hyperparameter Tuning
9. Model Evaluation
10. Streamlit Deployment

---

# 🛠 Technology Stack

| Category | Tools & Libraries |
|-----------|-------------------|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib, Plotly |
| Machine Learning | Scikit-learn, LightGBM, XGBoost, CatBoost |
| Deployment | Streamlit |
| Version Control | Git & GitHub |

---

# ⚙️ Data Preprocessing

- Missing Value Imputation
- Feature Engineering
- Feature Encoding
- Feature Scaling
- Dynamic Peak Hour Generation
- Time-Based Feature Creation
- Pipeline Integration

---

# 🤖 Models Evaluated

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor
- CatBoost Regressor
- Support Vector Regressor (SVR)
- **LightGBM Regressor**

| **Feature Category** | **Columns** | **Purpose** |
|----------------------|-------------|-------------|
| 🔄 **Cross Validation** | **5-Fold Cross Validation** | Evaluates model performance across multiple data splits to ensure robustness, minimize overfitting, and improve generalization. |
| ⚙️ **Hyperparameter Tuning** | **Optuna Framework**, `n_trials = 50` | Optimizes LightGBM hyperparameters by performing 50 optimization trials to identify the best-performing model configuration. |

---

# 📈 Model Performance

| Model | MAE | RMSE | R² Score |
|--------|-----|------|----------|
| XGBoost | 3.530 | 4.799 | 0.738 |
| CatBoost | 3.235 | 4.067 | 0.812 |
| ⭐ **LightGBM** | **3.182** | **3.993** | **0.819** |

---

# 🏆 Final Model

**LightGBM Regressor** was selected as the final model because it achieved:

- Lowest Mean Absolute Error (MAE)
- Lowest Root Mean Squared Error (RMSE)
- Highest R² Score
- Faster training and inference
- Excellent generalization capability
- High scalability for real-time deployment

---

# 🚀 Streamlit Deployment

The final preprocessing pipeline and trained LightGBM model were deployed using **Streamlit** to provide real-time ETA predictions. Users can enter rider, order, weather, traffic, and distance information through an interactive interface, while temporal features are generated automatically using Python's `datetime` module. The application preprocesses the input using the saved pipeline and instantly predicts the estimated delivery time.

---

# 📂 Project Structure

```text
Swiggy-Delivery-Time-Prediction
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── model/
│   └── PL_Swiggy_delivery_time_prediction.pkl
│
├── notebook/
│   └── Swiggy_Delivery_Time_Prediction.ipynb
│
├── data/
│   └── swiggy_dataset.csv
│
└── presentation/
    └── Swiggy_Delivery_Time_Prediction.pptx
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YourUsername/Swiggy-Delivery-Time-Prediction.git
```

Navigate to the project directory:

```bash
cd Swiggy-Delivery-Time-Prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

# 📈 Business Impact

- Improved ETA prediction accuracy
- Enhanced customer satisfaction
- Reduced order cancellations
- Better delivery planning
- Improved operational efficiency

---

# 🔮 Future Scope

- Live Traffic API Integration
- Weather API Integration
- Google Maps Route Optimization
- Continuous Model Retraining
- Cloud Deployment (AWS/Azure/GCP)
- Intelligent Rider Allocation
- Prediction Confidence Intervals

---

# 👨‍💻 Author

**Mir Ali**

**Machine Learning & Data Analytics Enthusiast**

- 📧 Email: *Your Email*
- 💼 LinkedIn: *Your LinkedIn Profile*
- 🌐 GitHub: *Your GitHub Profile*

---
# License

This project is open source and available for learning and portfolio purposes.

---
## ⭐ If you found this project useful, consider giving it a Star!
