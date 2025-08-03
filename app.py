import streamlit as st
import pandas as pd

def evaluate_conditions(gender, params):
    missing_params = {}
    conditions = []
    suggestions = {}

    # Check required parameters and log missing ones
    required_params = {
        "Iron Deficiency Anemia": ["RBC", "Hb", "MCV", "Ferritin"],
        "Vitamin B12/Folate Deficiency Anemia": ["RBC", "Hb", "Vitamin B12", "Folate"],
        "Microcytic Anemia": ["RBC", "MCV"],
        "Macrocytic Anemia": ["RBC", "MCV"],
        "Anemia of Chronic Disease": ["RBC", "Hb", "MCV", "Iron"],
        "Acute Infection": ["WBC", "RBC", "Hb", "CRP"],
        "Chronic Infection": ["WBC", "RBC", "Hb", "Lymphocyte Count", "ESR", "CRP"],
        "Leukemia": ["WBC", "RBC", "Hb", "LDH"],
        "Thrombocytopenia": ["RBC", "Hb", "PLT"],
        "Thrombocytosis": ["RBC", "Hb", "PLT"],
        "Dehydration": ["HCT", "Urea", "Creat"],
        "Hodgkin Lymphoma": ["RBC", "WBC", "PLT", "LDH", "ESR", "CRP"],
        "Follicular Lymphoma": ["RBC", "WBC", "PLT", "LDH", "ESR"],
        "Non-follicular Lymphoma": ["RBC", "WBC", "PLT", "LDH", "ESR"],
        "Mature T/NK-cell Lymphoma": ["RBC", "WBC", "PLT", "LDH", "ESR", "Calcium"],
        "Other Non-Hodgkin Lymphoma": ["RBC", "WBC", "PLT", "LDH", "ESR", "CRP"],
        "Other T/NK-cell Lymphoma": ["RBC", "WBC", "PLT", "LDH", "ESR", "Calcium"],
        "B-cell Lymphoma": ["RBC", "WBC", "PLT", "LDH", "ESR", "CRP"],
        "Multiple Myeloma": ["RBC", "WBC", "PLT", "Calcium", "LDH", "ESR"],
        "Lymphoid Leukemia": ["RBC", "WBC", "PLT", "LDH", "ESR", "CRP", "Neutrophil Absolute Number", "Monocyte Absolute Number"],
        "Myeloid Leukemia": ["RBC", "WBC", "PLT", "LDH", "ESR", "CRP", "Neutrophil Absolute Number", "Monocyte Absolute Number"],
        "Nutritional Anemia": ["RBC", "WBC", "PLT", "IRON", "Hb"],
        "Hemolytic Anemia": ["RBC", "WBC", "PLT", "Total Bilirubin"],
        "Aplastic Anemia": ["RBC", "WBC", "PLT", "FERRITIN"],
        "Coagulation Defects and Other Hemorrhagic Conditions": ["PLT", "RBC", "WBC", "Albumin"],
        "Other Diseases of Blood and Blood-Forming Organs": ["RBC", "WBC", "PLT"]
    }

    condition_suggestions = {
        "Iron Deficiency Anemia": {
            "suggestion": "Blood morphology to confirm Iron Deficiency. \n Consider Bone Marrow Biopsy if no improvement with iron supplementation"
        },
        "Vitamin B12/Folate Deficiency Anemia": {
            "suggestion": "Consider Serum Methylmalonic Acid (MMA) test for B12 deficiency.\n Blood morphology for futher confirmation"
        },
        "Microcytic Anemia": {
            "suggestion": "Serum Iron levels, TIBC, Serum Ferritin, Blood morphology for further confirmation for microcytic anemia. \n After confirmation Bone Marrow Biopsy BM Biopsy for microcytic anemia."
        },
        "Macrocytic Anemia": {
            "suggestion": "B12, Homocysteine, Blood smear, MMA, Serum Folate for further confirmation for macrocytic anemia. \n Consider Serum Methylmalonic Acid (MMA) test for B12 deficiency, Blood morphology for futher confirmation for macrocytic anemia"
        },
        "Anemia of Chronic Disease": {
            "suggestion": "Reticulocyte and Morphology for anemia of chronic disease. \n Consider Erythropoietin Level and Bone Marrow Biopsy if indicated for anemia of chronic disease."
        },
        "Acute Infection": {
            "suggestion": "Consider Blood Cultures and specific pathogen testing for Acute Infection.\n "
        },
        "Chronic Infection": {
            "suggestion": "Consider PCR Testing for specific pathogens for Chronic Infections."
        },
        "Leukemia": {
            "suggestion": " Blood morphology, Immunophenotyping, Cytogenic and Molecular testing for Leukemia. \n Bone Marrow Biopsy for confirmation and flow cytometry or Leukemia."
        },
        "Thrombocytopenia": {
            "suggestion": "Coagulation screen, Blood morphology to confirm Thrombocytopenia. \n	Consider Bone Marrow Biopsy if etiology is unclear for Thrombocytopenia"
        },
        "Thrombocytosis": {
            "suggestion": "Coagulation screen, Blood morphology to confirm Thrombocytosis . \n	Consider Bone Marrow Biopsy if secondary causes are suspected for Thrombocytosis"
        },
        "Dehydration": {
            "suggestion": " Serum Electrolytes, Serum and plasma osmolality, to confirm Dehydration. \n	Consider Urinalysis to assess hydration status to further confirm Dehydration"
        },
        "Hodgkin Lymphoma": {
        "suggestion": "Blood morphology to confirm Hodgkin Lymphoma\nLymph Node Biopsy for confirmation diagnosis of Hodgkin Lymphoma"
    },
    "Follicular Lymphoma": {
        "suggestion": "Blood morphology to confirm Follicular Lymphoma\nLymph Node Biopsy and Immunophenotyping for further confirmation of Follicular Lymphoma"
    },
    "Non-follicular Lymphoma": {
        "suggestion": "Blood morphology to confirm Non-follicular Lymphoma\nLymph Node Biopsy and Immunophenotyping for further confirmation of Non-follicular Lymphoma"
    },
    "Mature T/NK-cell Lymphoma": {
        "suggestion": "Blood morphology to confirm Mature T/NK-cell Lymphoma\nLymph Node Biopsy and Flow Cytometry to further confirm Mature T/NK-cell Lymphoma"
    },
    "Other Non-Hodgkin Lymphoma": {
        "suggestion": "Blood morphology to confirm Other Non-Hodgkin Lymphoma\nLymph Node Biopsy for confirmation of Other Non-Hodgkin Lymphoma"
    },
    "Other T/NK-cell Lymphoma": {
        "suggestion": "Blood morphology for confirmation of Other T/NK-cell Lymphoma\nLymph Node Biopsy for confirmation of Other T/NK-cell Lymphoma"
    },
    "B-cell Lymphoma": {
        "suggestion": "Blood morphology, Immunophenotyping to confirm B-cell Lymphoma\nLymph Node Biopsy and Flow Cytometry for further confirmation of B-cell Lymphoma"
    },
    "Multiple Myeloma": {
        "suggestion": "Serum Protein Electrophoresis to confirm Multiple Myeloma\nBone Marrow Biopsy to further confirm Multiple Myeloma"
    },
    "Lymphoid Leukemia": {
        "suggestion": "Immunohistochemistry for confirmation of Lymphoid Leukemia\nBone Marrow Biopsy for confirmation and flow cytometry to further confirm Lymphoid Leukemia"
    },
    "Myeloid Leukemia": {
        "suggestion": "Blood Morphology, Immunophenotyping, Cytogenetic and Molecular Testing to confirm Myeloid Leukemia\nBone Marrow Biopsy and additional tests based on clinical suspicion to further confirm Myeloid Leukemia"
    },
    "Nutritional Anemia": {
        "suggestion": "Consider Dietary Assessment and Supplementation to further confirm Nutritional Anemia"
    },
    "Hemolytic Anemia": {
        "suggestion": "Reticulocyte count, Consider Direct Coombs Test to confirm Hemolytic Anemia\nBone Marrow Biopsy for confirmation of Hemolytic Anemia"
    },
    "Aplastic Anemia": {
        "suggestion": "Reticulocyte count to confirm Aplastic Anemia\nBone Marrow Biopsy for further confirmation of Aplastic Anemia"
    },
    "Coagulation Defects and Other Hemorrhagic Conditions": {
        "suggestion": "Consider Specific Coagulation Factor Testing to confirm Coagulation Defects and Other Hemorrhagic Conditions"
    },
    "Other Diseases of Blood and Blood-Forming Organs": {
        "suggestion": "Additional testing based on clinical suspicion to further confirm Other Diseases of Blood and Blood-Forming Organs as RBCs, WBCs, and Platelets are too low."
    }

    }

    for condition, required in required_params.items():
        missing = [param for param in required if param not in params or params[param] is None]
        if missing:
            missing_params[condition] = missing
        else: 
            if condition == "Iron Deficiency Anemia" and params['RBC'] < 4.5 and params['Hb'] < (13 if gender == 'M' else 12) and params['MCV'] < 80 and params['Ferritin'] < 30:
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Vitamin B12/Folate Deficiency Anemia" and params['RBC'] < 4.5 and params['Hb'] < (13 if gender == 'M' else 12) and (params['Vitamin B12'] < 200 or params['Folate'] < 3):
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Microcytic Anemia" and params['RBC'] < 4.5 and params['MCV'] < 80:
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Macrocytic Anemia" and params['RBC'] < 4.5 and params['MCV'] > 100:
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Anemia of Chronic Disease" and params['RBC'] < 4.5 and params['Hb'] < (13 if gender == 'M' else 12) and 80 <= params['MCV'] <= 100 and params['Iron'] >= 30:
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Acute Infection" and params['WBC'] > 11 and params['RBC'] < 4.5 and params['Hb'] < (13 if gender == 'M' else 12) and params['CRP'] > 5:
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Chronic Infection" and params['WBC'] > 11 and params['RBC'] < 4.5 and params['Hb'] < (13 if gender == 'M' else 12) and params['Lymphocyte Count'] > 20 and params['ESR'] > 20 and params['CRP'] > 5:
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Leukemia" and params['WBC'] > 11 and params['RBC'] < 4.5 and params['Hb'] < (13 if gender == 'M' else 12) and params['LDH'] > 300:
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Thrombocytopenia" and params['RBC'] < 4.5 and params['Hb'] < (13 if gender == 'M' else 12) and params['PLT'] < 150:
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Thrombocytosis" and params['RBC'] < 4.5 and params['Hb'] < (13 if gender == 'M' else 12) and params['PLT'] > 450:
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Dehydration" and params['HCT'] > (0.52 if gender == 'M' else 0.47) and params['Urea'] > 20 and params['Creat'] > (110 if gender == 'M' else 97):
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Hodgkin Lymphoma" and gender == "M" and params['RBC'] < 4.5 and params['WBC'] > 11 and params['PLT'] > 150 and params['LDH'] > 300 and params['ESR'] > 20:
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Non-Hodgkin Lymphoma" and gender == "M" and params['RBC'] < 4.5 and params['WBC'] > 11 and params['PLT'] > 150 and params['LDH'] > 300 and params['ESR'] > 20 and params['Lymphocyte Count'] < 20:
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Multiple Myeloma" and params['RBC'] < 4.5 and params['Hb'] < (13 if gender == 'M' else 12) and params['PLT'] < 150 and params['Calcium'] > 11 and params['CRP'] > 5 and params['LDH'] > 300:
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Polycythemia Vera" and params['RBC'] > 6 and params['Hb'] > (18.5 if gender == 'M' else 16.5) and params['HCT'] > (0.52 if gender == 'M' else 0.48) and params['PLT'] > 450 and params['WBC'] > 10:
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Sickle Cell Anemia" and params['RBC'] < 4.5 and params['Hb'] < (13 if gender == 'M' else 12) and params['MCV'] < 80 and params['Reticulocyte Count'] > 2.5 and params['LDH'] > 300:
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Thalassemia" and params['RBC'] > 5 and params['MCV'] < 75 and params['Hb'] < (13 if gender == 'M' else 12) and params['RDW'] < 14:
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Aplastic Anemia" and params['RBC'] < 4.5 and params['Hb'] < (13 if gender == 'M' else 12) and params['WBC'] < 4 and params['PLT'] < 150:
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Coagulation Defects and Other Hemorrhagic Conditions" and ((gender == "M" and params['PLT'] < 150 and params['RBC'] >= 4.5 and params['WBC'] >= 4 and params['Albumin'] > 1.1) or (gender == "F" and params['PLT'] < 150 and params['RBC'] >= 4 and params['WBC'] >= 4 and params['Albumin'] > 1.1)):
                conditions.append(condition)
                suggestions[condition] = condition_suggestions[condition]["suggestion"]                           
            elif condition == "Other Diseases of Blood and Blood-Forming Organs" and ((gender == "M" and params['RBC'] >= 4.5 and params['WBC'] >= 4 and params['PLT'] >= 150) or (gender == "F" and params['RBC'] >= 4 and params['WBC'] >= 4 and params['PLT'] >= 150)):
                conditions.append(condition)
            
    return conditions, missing_params, suggestions

# Streamlit App
def main():
    st.set_page_config(
        page_title="Blood Test Analysis",
        page_icon="🩸",
        layout="wide"
    )
    
    st.title("🩸 Blood Test Analysis System")
    st.markdown("---")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", ["Input Form", "About"])
    
    if page == "Input Form":
        show_input_form()
    elif page == "About":
        show_about_page()

def show_input_form():
    st.header("Enter Your Blood Test Parameters")
    
    # Create form
    with st.form("blood_test_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Patient Information")
            gender = st.selectbox("Gender", ["M", "F"], help="Select M for Male, F for Female")
            
            st.subheader("Basic Blood Parameters")
            rbc = st.number_input("RBC (Red Blood Cell count)", min_value=0.0, step=0.01, help="× 10¹² cells/L")
            mcv = st.number_input("MCV (Mean Corpuscular Volume)", min_value=0.0, step=0.01, help="fL")
            hb = st.number_input("Hemoglobin (Hb)", min_value=0.0, step=0.01, help="g/dL")
            iron = st.number_input("Iron", min_value=0.0, step=0.01, help="μg/dL")
            wbc = st.number_input("WBC (White Blood Cell count)", min_value=0.0, step=0.01, help="× 10⁹ cells/L")
            crp = st.number_input("CRP (C-reactive protein)", min_value=0.0, step=0.01, help="mg/L")
            lymphocyte_count = st.number_input("Lymphocyte Count", min_value=0.0, step=0.01, help="× 10⁹ cells/L")
            esr = st.number_input("ESR (Erythrocyte Sedimentation Rate)", min_value=0.0, step=0.01, help="mm/hr")
            ldh = st.number_input("LDH (Lactate Dehydrogenase)", min_value=0.0, step=0.01, help="U/L")
            plt = st.number_input("PLT (Platelet count)", min_value=0.0, step=0.01, help="× 10⁹ cells/L")
            
        with col2:
            st.subheader("Additional Parameters")
            hct = st.number_input("HCT (Hematocrit)", min_value=0.0, step=0.01, help="%")
            urea = st.number_input("Urea", min_value=0.0, step=0.01, help="mg/dL")
            creat = st.number_input("Creatinine (Creat)", min_value=0.0, step=0.01, help="μmol/L")
            calcium = st.number_input("Calcium", min_value=0.0, step=0.01, help="mg/dL")
            neutrophil_abs = st.number_input("Neutrophil Absolute Number", min_value=0.0, step=0.01, help="× 10⁹ cells/L")
            monocyte_abs = st.number_input("Monocyte Absolute Number", min_value=0.0, step=0.01, help="× 10⁹ cells/L")
            bilirubin = st.number_input("Total Bilirubin", min_value=0.0, step=0.01, help="mg/dL")
            ferritin = st.number_input("Ferritin", min_value=0.0, step=0.01, help="ng/mL")
            albumin = st.number_input("Albumin", min_value=0.0, step=0.01, help="g/dL")
            vit_b12 = st.number_input("Vitamin B12", min_value=0.0, step=0.01, help="pg/mL")
            folate = st.number_input("Folate", min_value=0.0, step=0.01, help="ng/mL")
        
        submitted = st.form_submit_button("Analyze Results", type="primary")
        
        if submitted:
            # Prepare parameters dictionary
            params = {
                'RBC': rbc,
                'MCV': mcv,
                'Hb': hb,
                'Iron': iron,
                'WBC': wbc,
                'CRP': crp,
                'Lymphocyte Count': lymphocyte_count,
                'ESR': esr,
                'LDH': ldh,
                'PLT': plt,
                'HCT': hct,
                'Urea': urea,
                'Creat': creat,
                'Calcium': calcium,
                'Neutrophil Absolute Number': neutrophil_abs,
                'Monocyte Absolute Number': monocyte_abs,
                'Total Bilirubin': bilirubin,
                'Ferritin': ferritin,
                'Albumin': albumin,
                'Vitamin B12': vit_b12,
                'Folate': folate
            }
            
            # Evaluate conditions
            conditions, missing_params, suggestions = evaluate_conditions(gender, params)
            
            # Display results
            st.markdown("---")
            st.header("📊 Analysis Results")
            
            if conditions:
                st.success(f"✅ {len(conditions)} condition(s) detected")
                
                # Create a DataFrame for better display
                results_data = []
                for condition in conditions:
                    results_data.append({
                        "Condition": condition,
                        "Suggestion": suggestions.get(condition, "No specific suggestion available")
                    })
                
                df = pd.DataFrame(results_data)
                st.dataframe(df, use_container_width=True)
                
                # Show detailed suggestions
                st.subheader("🔍 Detailed Recommendations")
                for condition in conditions:
                    with st.expander(f"📋 {condition}"):
                        st.write(suggestions.get(condition, "No specific suggestion available"))
            else:
                st.info("ℹ️ No conditions detected based on the provided parameters.")
                st.write("This could mean:")
                st.write("• All parameters are within normal ranges")
                st.write("• Insufficient data to make a diagnosis")
                st.write("• Parameters don't match any known condition patterns")
            
            # Show missing parameters if any
            if missing_params:
                st.warning("⚠️ Some conditions could not be evaluated due to missing parameters")
                with st.expander("Missing Parameters"):
                    for condition, missing in missing_params.items():
                        st.write(f"**{condition}**: Missing {', '.join(missing)}")

def show_about_page():
    st.header("About This Application")
    st.write("""
    This is a medical diagnostic tool that analyzes blood test parameters to identify potential 
    hematological conditions and provide clinical recommendations.
    
    **Features:**
    - Analyzes 25+ different blood-related conditions
    - Provides specific clinical recommendations
    - Handles missing parameters gracefully
    - Gender-specific reference ranges
    
    **Disclaimer:**
    This tool is for educational and screening purposes only. All results should be reviewed 
    by qualified healthcare professionals before making any clinical decisions.
    """)
    
    st.subheader("Supported Conditions")
    conditions_list = [
        "Iron Deficiency Anemia",
        "Vitamin B12/Folate Deficiency Anemia", 
        "Microcytic Anemia",
        "Macrocytic Anemia",
        "Anemia of Chronic Disease",
        "Acute Infection",
        "Chronic Infection",
        "Leukemia",
        "Thrombocytopenia",
        "Thrombocytosis",
        "Dehydration",
        "Hodgkin Lymphoma",
        "Follicular Lymphoma",
        "Non-follicular Lymphoma",
        "Mature T/NK-cell Lymphoma",
        "Other Non-Hodgkin Lymphoma",
        "Other T/NK-cell Lymphoma",
        "B-cell Lymphoma",
        "Multiple Myeloma",
        "Lymphoid Leukemia",
        "Myeloid Leukemia",
        "Nutritional Anemia",
        "Hemolytic Anemia",
        "Aplastic Anemia",
        "Coagulation Defects and Other Hemorrhagic Conditions",
        "Other Diseases of Blood and Blood-Forming Organs"
    ]
    
    for condition in conditions_list:
        st.write(f"• {condition}")

if __name__ == "__main__":
    main() 
