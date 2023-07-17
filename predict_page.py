import streamlit as st
import pickle
import numpy as np


# def load_model():
#     with open('model.pkl', 'rb') as file:
#         data = pickle.load(file)
#     return data

# data = load_model()

# regressor = pickle.load(open('model1.pkl','rb'))
le_country = pickle.load(open('le_country.pkl','rb'))
le_education = pickle.load(open('le_education.pkl','rb'))

def show_predict_page():
    st.markdown("<h1 style='text-align: center; color: white;'>Software Developer Salary Prediction</h1>", unsafe_allow_html=True)

    st.write("""### We need some information to predict the salary""")

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    st.write(f"{type(le_country)}

    # country = st.selectbox("Country", countries)
    # education = st.selectbox("Education Level", education)

    # expericence = st.slider("Years of Experience", 0, 50, 10)

    # ok = st.button("Calculate Salary")
    # if ok:
    #     X = np.array([[country, education, expericence ]])
    #     X[:, 0] = le_country.transform(X[:,0])
    #     X[:, 1] = le_education.transform(X[:,1])
    #     X = X.astype(float)

    #     salary = regressor.predict(X)
    #     st.subheader(f"The estimated salary is ${salary[0]:.2f}")
