import streamlit as st
import pandas as pd
import pickle

model_filename = '../../model/model.pkl'

with open(model_filename, 'rb') as file:
    model = pickle.load(file)

def main():
    st.title('Heart Disease Prediction')
    age = st.slider('Age', 18, 100, 50)
    sex = st.selectbox('Sex', [0, 1])
    cp = st.slider('Chest Pain Type', 0, 3, 1)
    trestbps = st.slider('Resting Blood Pressure', 90, 200, 120)
    chol = st.slider('Cholesterol', 100, 600, 250)
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])
    restecg = st.selectbox('Resting Electrocardiographic Results', [0, 1, 2])
    thalach = st.slider('Maximum Heart Rate Achieved', 70, 220, 150)
    exang = st.selectbox('Exercise Induced Angina', [0, 1])
    oldpeak = st.slider('ST Depression Induced by Exercise Relative to Rest', 0.0, 6.2, 1.0)
    slope = st.slider('Slope of the Peak Exercise ST Segment', 0, 2, 1)
    ca = st.slider('Number of Major Vessels Colored by Fluoroscopy', 0, 4, 1)
    thal = st.slider('Thalassemia', 0, 3, 1)

    if st.button('Predict'):
        user_input = pd.DataFrame(data={
            'age': [age],
            'sex': [sex],
            'cp': [cp],
            'trestbps': [trestbps],
            'chol': [chol],
            'fbs': [fbs],
            'restecg': [restecg],
            'thalach': [thalach],
            'exang': [exang],
            'oldpeak': [oldpeak],
            'slope': [slope],
            'ca': [ca],
            'thal': [thal]
        })
        prediction = model.predict(user_input)
        st.write(f"Prediction: {'Positive' if prediction[0] == 1 else 'Negative'}")

if __name__ == '__main__':
    main()
