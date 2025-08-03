# Blood Test Analysis - Streamlit App

This is a Streamlit version of the Flask blood test analysis application. It provides the same functionality with a modern, interactive web interface.

## Features

- **Interactive Form**: Easy-to-use form for entering blood test parameters
- **Real-time Analysis**: Instant evaluation of blood parameters against medical conditions
- **Comprehensive Coverage**: Analyzes 25+ different hematological conditions
- **Clinical Recommendations**: Provides specific suggestions for each detected condition
- **Gender-specific Analysis**: Uses different reference ranges for males and females
- **Missing Parameter Handling**: Gracefully handles cases where some parameters are missing

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements_streamlit.txt
```

## Running the Application

1. Start the Streamlit app:
```bash
streamlit run streamlit_app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

## How to Use

1. **Enter Patient Information**: Select the patient's gender (M for Male, F for Female)

2. **Input Blood Parameters**: Fill in the blood test values in the form fields. You can leave fields empty if the test wasn't performed.

3. **Submit for Analysis**: Click the "Analyze Results" button to process the data.

4. **Review Results**: The app will display:
   - Detected conditions (if any)
   - Clinical recommendations for each condition
   - Missing parameters that prevented evaluation of certain conditions

## Supported Conditions

The application can detect and provide recommendations for:

- **Anemias**: Iron Deficiency, Vitamin B12/Folate Deficiency, Microcytic, Macrocytic, Chronic Disease, Nutritional, Hemolytic, Aplastic
- **Infections**: Acute and Chronic Infections
- **Blood Cancers**: Various types of Leukemia and Lymphoma
- **Platelet Disorders**: Thrombocytopenia and Thrombocytosis
- **Other Conditions**: Dehydration, Multiple Myeloma, Coagulation Defects

## Important Notes

- **Medical Disclaimer**: This tool is for educational and screening purposes only
- **Professional Review**: All results should be reviewed by qualified healthcare professionals
- **Reference Ranges**: The app uses standard medical reference ranges but may need adjustment for specific populations

## File Structure

```
criteriaFlaskApp/
├── streamlit_app.py          # Main Streamlit application
├── requirements_streamlit.txt # Python dependencies
├── README_streamlit.md       # This file
├── app.py                    # Original Flask application
└── templates/                # Original Flask templates
    ├── input_form.html
    └── results.html
```

## Differences from Flask Version

- **Modern UI**: Streamlit provides a more modern, responsive interface
- **Real-time Updates**: No page refreshes needed
- **Better Data Display**: Uses pandas DataFrames for cleaner results display
- **Sidebar Navigation**: Easy navigation between different sections
- **Expandable Details**: Click to expand detailed recommendations
- **Better Error Handling**: More informative error messages and warnings 