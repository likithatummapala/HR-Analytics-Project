import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="HR Analytics Dashboard",
    layout="wide"
)

st.title("HR Analytics - Employee Attrition Dashboard")

# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------
file_path = "HR_Analytics.csv"

if not os.path.exists(file_path):
    file_path = "HR_Analytics.csv"

try:
    df = pd.read_csv(file_path)

    st.success(
        f"Dataset Loaded: {df.shape[0]} rows, {df.shape[1]} columns"
    )

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # --------------------------------------------------
    # HANDLE MISSING VALUES
    # --------------------------------------------------
    for col in df.columns:
        if df[col].isnull().sum() > 0:

            if df[col].dtype == "object":
                df[col] = df[col].fillna(df[col].mode()[0])
            else:
                df[col] = df[col].fillna(df[col].median())

    # --------------------------------------------------
    # VISUALIZATIONS
    # --------------------------------------------------
    st.subheader("Visualizations - 8 Charts")

    c1, c2 = st.columns(2)

    # 1. Attrition
    with c1:
        fig1, ax1 = plt.subplots(figsize=(5, 3.5))

        df["Attrition"].value_counts().plot(
            kind="pie",
            autopct="%1.1f%%",
            ax=ax1
        )

        ax1.set_title("1. Attrition Count")
        ax1.set_ylabel("")

        st.pyplot(fig1)
        plt.close(fig1)

        # 2. Department vs Attrition
        fig2, ax2 = plt.subplots(figsize=(5, 3.5))

        pd.crosstab(
            df["Department"],
            df["Attrition"]
        ).plot(kind="bar", ax=ax2)

        ax2.set_title("2. Department vs Attrition")
        ax2.set_xlabel("Department")
        ax2.set_ylabel("Employees")

        st.pyplot(fig2)
        plt.close(fig2)

        # 3. Age Distribution
        fig3, ax3 = plt.subplots(figsize=(5, 3.5))

        ax3.hist(df["Age"], bins=20)

        ax3.set_title("3. Age Distribution")
        ax3.set_xlabel("Age")
        ax3.set_ylabel("Employees")

        st.pyplot(fig3)
        plt.close(fig3)

        # 4. OverTime vs Attrition
        fig4, ax4 = plt.subplots(figsize=(5, 3.5))

        pd.crosstab(
            df["OverTime"],
            df["Attrition"]
        ).plot(kind="bar", ax=ax4)

        ax4.set_title("4. OverTime vs Attrition")
        ax4.set_xlabel("OverTime")
        ax4.set_ylabel("Employees")

        st.pyplot(fig4)
        plt.close(fig4)

    # --------------------------------------------------
    # COLUMN 2
    # --------------------------------------------------
    with c2:

        # 5. Monthly Income
        fig5, ax5 = plt.subplots(figsize=(5, 3.5))

        ax5.hist(df["MonthlyIncome"], bins=20)

        ax5.set_title("5. Monthly Income Distribution")
        ax5.set_xlabel("Monthly Income")
        ax5.set_ylabel("Employees")

        st.pyplot(fig5)
        plt.close(fig5)

        # 6. Job Satisfaction
        fig6, ax6 = plt.subplots(figsize=(5, 3.5))

        satisfaction = df["JobSatisfaction"].value_counts().sort_index()

        ax6.bar(
            satisfaction.index,
            satisfaction.values
        )

        ax6.set_title("6. Job Satisfaction Count")
        ax6.set_xlabel("Job Satisfaction")
        ax6.set_ylabel("Employees")

        st.pyplot(fig6)
        plt.close(fig6)

        # 7. Gender vs Attrition
        fig7, ax7 = plt.subplots(figsize=(5, 3.5))

        pd.crosstab(
            df["Gender"],
            df["Attrition"]
        ).plot(kind="bar", ax=ax7)

        ax7.set_title("7. Gender vs Attrition")
        ax7.set_xlabel("Gender")
        ax7.set_ylabel("Employees")

        st.pyplot(fig7)
        plt.close(fig7)

        # 8. Years at Company vs Income
        fig8, ax8 = plt.subplots(figsize=(5, 3.5))

        if "YearsAtCompany" in df.columns:

            colors = df["Attrition"].map({
                "Yes": "red",
                "No": "green"
            })

            ax8.scatter(
                df["YearsAtCompany"],
                df["MonthlyIncome"],
                c=colors,
                alpha=0.5
            )

            ax8.set_title(
                "8. YearsAtCompany vs Income"
            )

            ax8.set_xlabel("Years at Company")
            ax8.set_ylabel("Monthly Income")

            st.pyplot(fig8)

        plt.close(fig8)

    # --------------------------------------------------
    # MACHINE LEARNING
    # --------------------------------------------------
    st.subheader("Attrition Prediction Model")

    df_encoded = df.copy()

    # Encode categorical columns
    for col in df_encoded.select_dtypes(
        include="object"
    ).columns:

        le = LabelEncoder()

        df_encoded[col] = le.fit_transform(
            df_encoded[col].astype(str)
        )

    # Separate features and target
    X = df_encoded.drop(
        "Attrition",
        axis=1,
        errors="ignore"
    )

    y = df_encoded["Attrition"]

    # Remove unnecessary columns
    columns_to_remove = [
        "EmployeeCount",
        "EmployeeNumber",
        "Over18",
        "StandardHours"
    ]

    for col in columns_to_remove:
        if col in X.columns:
            X = X.drop(col, axis=1)

    # Keep numerical columns
    X = X.select_dtypes(
        include=["int64", "float64"]
    )

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Random Forest
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Prediction
    predictions = model.predict(X_test)

    # Accuracy
    acc = accuracy_score(
        y_test,
        predictions
    )

    st.success(
        f"Model Accuracy: {acc * 100:.2f}%"
    )

except Exception as e:

    st.error(f"Error: {e}")

    st.write("Files available in the current folder:")

    st.write(os.listdir("."))