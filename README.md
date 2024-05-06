
---

# Heart Disease Prediction Streamlit App

This is a simple Streamlit web application that allows users to predict the likelihood of heart disease based on input features. The prediction is made using a machine learning model that has been trained on heart disease data.

![dog and cat image](data/image/hd.png)

[Live Website](https://heart-disease-checking.streamlit.app/)

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Input Features](#input-features)
- [Output](#output)

## Getting Started

### Prerequisites

To run this application, you need:

- Python (3.6 or later)
- Streamlit
- pandas
- pickle

### Installation

1. Clone this repository:

```bash
git clone https://github.com/Prem07a/Heart-Disease.git
```

2. Navigate to the project directory:

```bash
cd Heart-Disease
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app by executing the following command in your terminal:

```bash
streamlit run ./code/website/app.py
```

The web application will open in your default web browser. You can then interact with the app by inputting various features and clicking the "Predict" button to get the predicted outcome.

## Input Features

The following input features can be adjusted in the app:

- Age
- Sex (Male/Female)
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar (> 120 mg/dl)
- Resting Electrocardiographic Results
- Maximum Heart Rate Achieved
- Exercise Induced Angina
- ST Depression Induced by Exercise Relative to Rest
- Slope of the Peak Exercise ST Segment
- Number of Major Vessels Colored by Fluoroscopy
- Thalassemia

## Output

After adjusting the input features and clicking "Predict," the app will display the predicted outcome, indicating whether the prediction suggests a positive or negative likelihood of heart disease.

## Thanks

I would like to thank <a href = "https://github.com/Akshat-Projects">Akshat</a> for reporting a bug in streamlit app.

---
