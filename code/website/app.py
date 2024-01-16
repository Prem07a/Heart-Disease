import streamlit as st
import pandas as pd
import pickle

model_filename = '/workspaces/Heart-Disease/model/model.pkl'

with open(model_filename, 'rb') as file:
    model = pickle.load(file)

def main():
    st.title('WQD 7003 Group 17 - Heart Disease Risk Prediction')
    age = st.slider('Age', 18, 100, 50)
    sex_options = ["Male", "Female"]
    sex = st.selectbox('Sex', sex_options)
    sex_num = 1 if sex == 'Male' else 0 
    cp_options = ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic']
    cp = st.selectbox('Chest Pain Type', cp_options)
    cp_num = cp_options.index(cp)
    trestbps = st.slider('Resting Blood Pressure', 90, 200, 120)
    chol = st.slider('Cholesterol', 100, 600, 250)
    fbs_options = ["Yes", "No"]
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', fbs_options)
    fbs_num = fbs_options.index(fbs)
    restecg_options = ['Normal', 'ST-T Abnormality', 'Left Ventricular Hypertrophy']
    restecg = st.selectbox('Resting Electrocardiographic Results', restecg_options)
    restecg_num = restecg_options.index(restecg)
    thalach = st.slider('Maximum Heart Rate Achieved', 70, 220, 150)
    exang_options = ['No', 'Yes']
    exang = st.selectbox('Exercise Induced Angina', exang_options)
    exang_num = exang_options.index(exang)
    oldpeak = st.slider('ST Depression Induced by Exercise Relative to Rest', 0.0, 6.2, 1.0)
    slope_options = ['Upsloping', 'Flat', 'Downsloping']
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', slope_options)
    slope_num = slope_options.index(slope)
    ca = st.slider('Number of Major Vessels Colored by Fluoroscopy', 0, 4, 1)
    thal_options = ['Normal', 'Fixed Defect', 'Reversible Defect']
    thal = st.selectbox('Thalassemia', thal_options)
    thal_num = thal_options.index(thal)

    if st.button('Predict'):
        user_input = pd.DataFrame(data={
            'age': [age],
            'sex': [sex_num],  
            'cp': [cp_num],
            'trestbps': [trestbps],
            'chol': [chol],
            'fbs': [fbs_num],
            'restecg': [restecg_num],
            'thalach': [thalach],
            'exang': [exang_num],
            'oldpeak': [oldpeak],
            'slope': [slope_num],
            'ca': [ca],  
            'thal_num': [thal_num],  
        })
        
        prediction = model.predict(user_input)
        prediction_proba = model.predict_proba(user_input)

        if prediction[0] == 1:
            bg_color = 'red'
            prediction_result = 'Oh no, get an appointment with a heart specialist soon to keep living. Unfortunately, you have a high risk of getting heart disease!'
        else:
            bg_color = 'green'
            prediction_result = 'Congratulations, keep up the good work in maintaining a healthy heart. You have a low risk of getting heart disease ;)'
        
        confidence = prediction_proba[0][1] if prediction[0] == 1 else prediction_proba[0][0]

        result_message = f"<h5>Prediction:</h5> <h1 style='font-weight:bold;'>{prediction_result}</h1> <h5>Confidence:</h5> <h2>{((confidence*10000)//1)/100}%</h2>"

        st.markdown(
            f"<p style='background-color:{bg_color}; color:white; padding:10px;'>{result_message}</p>", 
                unsafe_allow_html=True
        )

if __name__ == '__main__':
    main()
