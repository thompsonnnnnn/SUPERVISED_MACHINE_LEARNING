# 🌤️ Outdoor Sports Weather Prediction App

## 📌 Project Overview
This project is a **machine learning-based web app** that predicts whether the weather conditions are suitable for outdoor sports.  
It is designed for a **Proven Data Private Limited** whose business revolves around planning outdoor events such as football, tennis, and cricket matches.  
The app allows users to enter current weather conditions, and the model will predict **"Yes"** or **"No"** for playing outdoors.

The prediction is based on weather features:
- **Outlook** (sunny, overcast, rainy)
- **Temperature** (hot, mild, cool)
- **Humidity** (high, normal)
- **Windy** (true, false)

---

## 🎯 Problem Statement
Outdoor sports organizers often face uncertainty in planning events due to unpredictable weather.  
Incorrect decisions can lead to:
- **Financial losses** (venue bookings, staffing costs)
- **Reduced customer satisfaction** (event cancellations)
- **Wasted resources** (equipment setup in bad weather)

Our goal is to **develop a machine learning model** that can assist decision-makers in **real-time** to determine whether it’s advisable to hold outdoor sports events given certain weather conditions.

---

## 🧠 Machine Learning Approach
- **Type of Learning:** Supervised Learning  
- **Model Type:** Classification (Binary: Yes or No)  
- **Algorithms Used:** Logistic Regression, Decision Tree, Random Forest, Support Vector Machine  
- **Best Model Selection:** Based on accuracy score

---

## 🛠️ Project Workflow
1. **Data Loading**
   - CSV file with weather conditions and corresponding `Play` decision.

2. **Data Exploration**
   - Check dataset shape, column types, unique values, and missing data.
   - Identify duplicates and anomalies.

3. **Data Cleaning**
   - Remove duplicates.
   - Handle missing values (fill with mode for categorical features).
   - Standardize text (lowercase, remove spaces).
   - Fix misspellings (e.g., `sunyy` → `sunny`, `Rainny` → `rainy`).

4. **Encoding & Feature Scaling**
   - Encode categorical variables using OneHotEncoder.
   - Apply scaling for numerical stability.

5. **Train-Test Split**
   - Split data into training (80%) and testing (20%) sets.

6. **Model Training**
   - Train **4 separate models** without pipelines for simplicity.
   - Compare model performance.

7. **Model Evaluation**
   - Accuracy score calculation.
   - Confusion matrix visualization.

8. **Model Saving**
   - Save the best model as `best_weather_model.pkl`.
   - Save metadata for dropdown options in Streamlit.

9. **Streamlit Web App**
   - User inputs weather conditions via dropdowns and checkboxes.
   - Model predicts if it’s good weather for outdoor sports.


---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/thompsonnnnnn/SUPERVISED_MACHINE_LEARNING.git
```
```bash
cd SUPERVISED_MACHINE_LEARNING
```
2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
3️⃣ Run the Streamlit app
```bash
streamlit run app.py
```

💡 Technologies Used
* Python (pandas, numpy, matplotlib, scikit-learn, joblib)

* Streamlit (web interface)

* GitHub (version control & deployment)

👤 Author
Developed by Thompson – Data Science & Machine Learning Enthusiast
* 📧 Email: ekwums@yahoo.com
* 🔗 LinkedIn: Your LinkedIn Profile
* 🐙 GitHub: https://github.com/thompsonnnnnn/


---