# Smart Diabetes Prediction System

## About the Project
The Smart Diabetes Prediction System is a machine learning-based web application that estimates the likelihood of diabetes using medical parameters. It provides a simple interface for users to enter their health-related details and view a prediction.

## Features
- User-friendly home page
- About and instructions pages
- Login interface
- Diabetes prediction form
- Displays prediction results
- Contact page for queries and feedback

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn
- **Model Storage:** Pickle
- **Dataset:** PIMA Indians Diabetes Dataset

## Project Structure
```text
Diabetes-Prediction-System/
│
├── .dist/
├── static/
├── templates/
├── .hintrc
├── app
└── diabetes_model.pkl
```

- `static/` – Contains static assets such as CSS, JavaScript, and images.
- `templates/` – Contains HTML templates for the web pages.
- `diabetes_model.pkl` – Saved machine learning model.
- `app` – Application entry file.
- `.dist/` – Additional project directory.
- `.hintrc` – Configuration file.

## How It Works
1. Open the web application.
2. Navigate to the Predict page.
3. Enter the required medical parameters, including glucose level, blood pressure, BMI, insulin, and age.
4. Click the **Predict** button.
5. View the prediction result displayed on the page.

## Installation and Setup
1. Install Python on your system.
2. Clone or download this repository.
3. Install the required Python libraries.
4. Run the Flask application using the appropriate entry-file name.
5. Open the local URL displayed in the terminal.

**Note:** The exact run command and dependencies should be confirmed from the project source files.

## Future Improvements
- Improve prediction accuracy.
- Enhance user authentication and data security.
- Improve the user interface and accessibility.
- Add more testing and model evaluation.

## Disclaimer
This project is intended for educational and awareness purposes only. Its predictions are not a medical diagnosis and should not replace professional medical advice or laboratory testing.

## Author
Developed as a machine learning-based web application project.
