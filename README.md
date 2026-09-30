# 📊 HR Analytics - Employee Attrition Dashboard

## 📌 Project Overview

The **HR Analytics - Employee Attrition Dashboard** is a data analysis and machine learning project developed using **Python, Pandas, Matplotlib, Scikit-learn, and Streamlit**.

This project analyzes employee data to understand **employee attrition** and identifies patterns related to age, department, overtime, income, job satisfaction, gender, and years at the company.

A **Random Forest Classifier** is also used to predict employee attrition.

---

## 🎯 Objectives

* Analyze employee attrition.
* Understand factors related to employee turnover.
* Explore employee information using data visualization.
* Handle missing values in the dataset.
* Convert categorical data into numerical values.
* Build a machine learning model.
* Predict employee attrition.
* Display the model accuracy.
* Create an interactive Streamlit dashboard.

---

## 📂 Dataset

The project uses the **HR Analytics dataset**.

### Dataset file

```text
HR_Analytics-4.csv
```

The dataset contains employee-related information such as:

* Age
* Department
* Gender
* Monthly Income
* Job Satisfaction
* OverTime
* Years At Company
* Attrition
* Job Role
* Education
* Marital Status
* Work Experience
* And other HR-related attributes

---

# 📊 Data Visualizations

The dashboard contains **8 visualizations**.

### 1. Attrition Count

Displays the percentage of employees who stayed with the company and employees who left.

### 2. Department vs Attrition

Shows employee attrition across different departments.

### 3. Age Distribution

Displays the distribution of employee ages.

### 4. OverTime vs Attrition

Shows the relationship between overtime work and employee attrition.

### 5. Monthly Income Distribution

Displays the distribution of employee monthly income.

### 6. Job Satisfaction Count

Shows the number of employees for each job satisfaction level.

### 7. Gender vs Attrition

Compares employee attrition across genders.

### 8. Years At Company vs Monthly Income

Shows the relationship between years spent at the company and monthly income.

---

# 🤖 Machine Learning

The project uses the **Random Forest Classifier** for employee attrition prediction.

### Machine Learning Workflow

```text
HR Dataset
     ↓
Data Cleaning
     ↓
Missing Value Handling
     ↓
Categorical Data Encoding
     ↓
Feature Selection
     ↓
Train-Test Split
     ↓
Random Forest Classifier
     ↓
Prediction
     ↓
Accuracy Score
```

### Train-Test Split

The dataset is divided into:

* **80% Training Data**
* **20% Testing Data**

The model accuracy is displayed in the Streamlit application.

---

# 🛠️ Technologies Used

| Technology      | Purpose              |
| --------------- | -------------------- |
| Python          | Programming Language |
| Pandas          | Data Processing      |
| Matplotlib      | Data Visualization   |
| Scikit-learn    | Machine Learning     |
| Streamlit       | Web Dashboard        |
| Random Forest   | Classification Model |
| GitHub          | Version Control      |
| Streamlit Cloud | Deployment           |

---

# 📁 Project Structure

```text
HR-Analytics/
│
├── app.py
├── HR_Analytics-4.csv
├── requirements.txt
└── README.md
```

---

# 📦 Installation

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

## 2. Open the Project Folder

```bash
cd HR-Analytics
```

## 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

## 4. Run the Streamlit Application

```bash
streamlit run app.py
```

---

# 📋 Requirements

Create a file named **requirements.txt** in the same folder as `app.py`.

```text
streamlit
pandas
matplotlib
scikit-learn
```

---

# 🚀 Streamlit Cloud Deployment

The application can be deployed using **Streamlit Community Cloud**.

### Steps

1. Upload the project files to GitHub.
2. Make sure `app.py` is in the repository.
3. Make sure `HR_Analytics-4.csv` is in the repository.
4. Make sure `requirements.txt` is in the repository.
5. Connect the GitHub repository to Streamlit Community Cloud.
6. Select `app.py` as the main file.
7. Deploy the application.

### Required files

```text
app.py
HR_Analytics-4.csv
requirements.txt
README.md
```

---

# 🔍 Dashboard Features

The application provides:

* ✅ Dataset preview
* ✅ Employee attrition analysis
* ✅ 8 visualizations
* ✅ Missing-value handling
* ✅ Categorical data encoding
* ✅ Random Forest classification
* ✅ Model accuracy
* ✅ Interactive Streamlit interface
* ✅ CSV dataset support

---

# 📈 Expected Output

After successfully running the application, the dashboard displays:

```text
HR Analytics - Employee Attrition Dashboard

Dataset Loaded: XXXX rows, XX columns

Dataset Preview

Visualizations - 8 Charts

Attrition Prediction Model

Model Accuracy: XX.XX%
```

---

# 💡 Conclusion

The **HR Analytics Employee Attrition Dashboard** demonstrates how data analysis, visualization, and machine learning can be combined to analyze employee attrition.

The Streamlit dashboard provides an interactive way to explore HR data and understand different employee-related factors while using a Random Forest model for attrition prediction.

---

# 👩‍💻 Author

**Likitha Tummapala**

---

## ⭐ Project

If you find this project useful, please give the repository a ⭐ on GitHub.
