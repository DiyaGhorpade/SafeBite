# SafeBite Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Stack & Architecture](#stack--architecture)
3. [Repository Structure](#repository-structure)
4. [Setup & Installation](#setup--installation)
5. [Usage Guide](#usage-guide)
6. [Core Models](#core-models)
7. [API Reference](#api-reference)
8. [Contributing](#contributing)

---

## Project Overview

**SafeBite** is an AI-powered food safety detection system designed to identify contamination and adulteration in perishable food items. The project leverages machine learning models to analyze food samples and predict:

- **Food Contamination Levels**: Detects the presence and quantity of harmful contaminants (heavy metals, pesticides, aflatoxins, etc.)
- **Food Adulteration**: Identifies adulterants in food products (unauthorized additives, synthetic substances, etc.)
- **Safety Classification**: Classifies food safety into Low, Medium, or High risk categories

### Problem Solved
SafeBite addresses the critical public health issue of food contamination and adulteration by providing an accessible, technology-driven solution that helps consumers and food safety inspectors detect unsafe food items before consumption.

### Target Users
- Food safety inspectors and regulatory agencies
- Food manufacturers and quality control labs
- Consumers concerned about food safety
- Restaurant and retail food businesses

---

## Stack & Architecture

### Languages & Frameworks
- **Primary**: Python (Machine Learning & Backend)
- **Data Science**: Jupyter Notebooks (91.8% of repository)
- **Frontend**: 
  - React + Vite (TypeScript/JavaScript)
  - Next.js (Alternative modern frontend)
  - Streamlit (Rapid prototyping UI)
  - Tailwind CSS (Styling)

### Key Technologies
- **ML Framework**: scikit-learn
- **Model Serialization**: joblib
- **Data Processing**: pandas, numpy
- **Web Framework**: Streamlit
- **Preprocessing**: OneHotEncoder, StandardScaler, ColumnTransformer
- **Algorithms**: 
  - Logistic Regression (Adulteration prediction)
  - Random Forest & Decision Tree Regressors (Contamination prediction)
  - K-Means Clustering (Safety classification)

### Notable Libraries
- scikit-learn: Machine learning pipeline and model development
- pandas: Data manipulation and feature engineering
- joblib: Model persistence and serialization
- Streamlit: Interactive web UI for predictions
- React/Next.js: Production-grade frontend applications
- Pillow (PIL): Image handling for food samples

---

## Repository Structure

```
SafeBite/
├── Contamination-ML Models & Preprocessed Code/
│   └── food contamination.ipynb          # Notebook for contamination preprocessing
│
├── Datasets/
│   ├── realistic_food_adulteration_samples.csv
│   └── food-contamination-data-cleaned-2.csv
│
├── Training-Modeling/
│   ├── LogisticRegressionModel.py        # Adulteration prediction model
│   ├── Food_adulteration.ipynb           # Adulteration training & tuning
│   ├── food-adulteration-model.ipynb     # Random Forest adulteration classifier
│   ├── contaminant-prediction.ipynb      # Linear regression contamination model
│   ├── contamination-prediction-decision-tree.ipynb
│   ├── contamination-prediction-random-forest.ipynb
│   └── contamination-classification-kmeans.ipynb  # K-Means safety classifier
│
├── Deployment/
│   └── app.py                            # Main Streamlit application
│
├── UI/
│   ├── safebiteui.py                     # Alternative Streamlit UI
│   ├── tomato.jpg, burger.jpg, scientist.png
│
├── front_end/
│   ├── SafeBiteProject/                  # React + Vite frontend
│   │   ├── src/
│   │   │   ├── App.jsx, App.css
│   │   │   ├── main.jsx, index.css
│   │   │   └── components
│   │   ├── vite.config.js
│   │   ├── eslint.config.js
│   │   └── index.html
│   │
│   ├── tailwind.config.js
│   └── SafeBiteProject/newsafebite/website/
│       └── Next.js application with TypeScript
│
├── .devcontainer/                        # Development container configuration
├── kmeans_contamination.ipynb            # K-Means model development
├── kmeans_contamination.joblib           # Serialized K-Means model
├── safebiteui.py                         # Root-level Streamlit UI
├── LICENSE                               # MIT License
└── README.md                             # Project README
```

### How It Fits Together

The system follows a **three-tier architecture**:

1. **Data & Training Layer** (`Training-Modeling/`)
   - Raw food data is loaded and preprocessed
   - Features are engineered and encoded (categorical → numerical)
   - Three separate ML models are trained:
     - **Adulteration Predictor**: Logistic Regression on food type + adulterant + level
     - **Contamination Predictor**: Decision Tree/Random Forest regression on country, food group, contaminant
     - **Safety Classifier**: K-Means clustering for risk level classification

2. **Model Deployment Layer** (`Deployment/app.py`)
   - Pre-trained models are loaded via `joblib` from `.joblib` files
   - Encoders and scalers are loaded to preprocess user input
   - Models expose prediction endpoints for:
     - Adulteration severity
     - Contaminant quantity levels
     - Safety classification (Low/Medium/High)

3. **User Interface Layer**
   - **Streamlit UI** (`Deployment/app.py`, `UI/safebiteui.py`): Quick, interactive web interface with tabbed predictions
   - **React Frontend** (`front_end/SafeBiteProject/`): Production-grade SPA with Tailwind styling
   - **Next.js Frontend**: Modern SSR option with TypeScript support

**Data Flow**:
```
User Input → Streamlit/React UI
    ↓
Preprocessing (OneHotEncoder, StandardScaler)
    ↓
Load Pre-trained Model (joblib)
    ↓
Prediction (Adulteration/Contamination/Safety)
    ↓
Display Result with Classification
```

---

## Setup & Installation

### Prerequisites
- Python 3.8+
- Node.js 16+ (for frontend)
- Git

### Backend Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DiyaGhorpade/SafeBite.git
   cd SafeBite
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   Required packages:
   ```
   streamlit
   scikit-learn
   pandas
   numpy
   joblib
   pillow
   ```

4. **Run the Streamlit application**:
   ```bash
   streamlit run Deployment/app.py
   ```
   
   The app will be accessible at `http://localhost:8501`

### Frontend Setup (React + Vite)

1. **Navigate to frontend directory**:
   ```bash
   cd front_end/SafeBiteProject
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Run development server**:
   ```bash
   npm run dev
   ```

4. **Build for production**:
   ```bash
   npm run build
   ```

### Frontend Setup (Next.js)

1. **Navigate to Next.js directory**:
   ```bash
   cd front_end/SafeBiteProject/newsafebite/website
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Run development server**:
   ```bash
   npm run dev
   ```

4. **Build for production**:
   ```bash
   npm run build
   npm start
   ```

---

## Usage Guide

### Using the Streamlit Application

The main application (`Deployment/app.py`) provides three tabs:

#### Tab 1: Adulteration Prediction

**Purpose**: Predict if a food sample is adulterated

**Inputs**:
- **Adulterant**: Water, Detergent, Starch, Urea, Soapstone, Chalk Powder, Sugar Syrup, Jaggery Syrup, Brick Powder, Salt Powder, Metanil Yellow, None
- **Food Type**: Milk, Wheat, Honey, Chili Powder, Turmeric
- **Adulteration Level**: Numeric value (0-100)

**Output**: Binary prediction (Adulterated/Clean)

**Example**:
```python
# Input: Milk + Water + 5.5
# Output: "Adulteration Prediction: 1" (Adulterated)
```

#### Tab 2: Contaminant Level Prediction

**Purpose**: Predict the concentration level of a specific contaminant

**Inputs**:
- **Country Name**: Hong Kong SAR, Japan, China, Singapore, Thailand, India, Republic of Korea, Indonesia
- **Food Group**: Legumes, Fish, Vegetables, Starchy Roots, Milk & Dairy, Meat, Fruits, Eggs
- **Food Name**: Free text input
- **Contaminant**: Ethyl carbamate, Lead, Cadmium, Aflatoxin B1, Mercury, Arsenic, etc.

**Output**: Predicted concentration level (numeric)

#### Tab 3: Safety Classification

**Purpose**: Classify overall food safety risk

**Inputs**:
- **Food Group**: (Same as Tab 2)
- **Contaminant**: (Same list)
- **Quantity**: Numeric contaminant quantity

**Output**: Safety level (Low/Medium/High)

---

## Core Models

### 1. Adulteration Prediction Model

**File**: `Training-Modeling/LogisticRegressionModel.py`

**Algorithm**: Logistic Regression with preprocessing pipeline

**Features**:
- food_type (categorical) → OneHotEncoded
- adulterant (categorical) → OneHotEncoded
- adulteration_level (numeric) → StandardScaled

**Target**: is_adulterated (binary: 0=clean, 1=adulterated)

**Serialized Model**: `adulteration-prediction-model.joblib`

**Training Data**: `Datasets/realistic_food_adulteration_samples.csv`

### 2. Contamination Level Prediction Model

**Files**: 
- `Training-Modeling/contamination-prediction-decision-tree.ipynb`
- `Training-Modeling/contamination-prediction-random-forest.ipynb`

**Algorithms**: 
- Decision Tree Regressor
- Random Forest Regressor

**Features**:
- CountryName (categorical)
- FoodGroupName (categorical)
- GEMSFoodName (categorical)
- ContaminantName (categorical)

**Target**: ResultValue (numeric log-transformed)

**Preprocessing**:
- Log transformation: `y_train = np.log1p(y_train)`
- OneHotEncoding for categorical features
- Inverse transformation for output: `np.expm1(prediction_log)`

**Serialized Models**: 
- `contamination-prediction-model.joblib`
- Encoders: `contaminant_encoder.joblib`, `foodgroup_encoder.joblib`

**Training Data**: `Datasets/food-contamination-data-cleaned-2.csv`

### 3. Safety Classification Model

**File**: `Training-Modeling/contamination-classification-kmeans.ipynb`

**Algorithm**: K-Means Clustering (k=3)

**Features** (engineered):
- ContaminantEncoded (label-encoded)
- ScaledLogResult (log-transformed & standardscaled contamination level)
- FoodGroupEncoded (label-encoded)

**Clusters**: 
- Cluster 0 → Low Risk
- Cluster 1 → Medium Risk
- Cluster 2 → High Risk

**Serialized Models**:
- `safety-classification-kmeans.joblib`
- Encoders: `contaminant_encoder.joblib`, `foodgroup_encoder.joblib`
- Scaler: `result_scaler.joblib`

**Training Data**: `Datasets/food contamination data_cleaned2.csv`

---

## API Reference

### Streamlit Application Endpoints

#### Adulteration Prediction
```python
# Endpoint: "Predict Adulteration" button in Tab 1
# Request body (implicit via Streamlit form):
{
    "Adulterant": str,        # From selectbox
    "FoodType": str,          # From selectbox
    "AdulterationLevel": float # From number_input
}

# Response:
"Adulteration Prediction: {0 or 1}"
```

#### Contamination Level Prediction
```python
# Endpoint: "Predict Contaminant Level" button in Tab 2
# Request body:
{
    "CountryName": str,
    "FoodGroupName": str,
    "GEMSFoodName": str,
    "ContaminantName": str
}

# Response:
"Contaminant Level: {numeric_value}"
```

#### Safety Classification
```python
# Endpoint: "Predict Safety" button in Tab 3
# Request body:
{
    "FoodGroup": str,              # Selected from dropdown
    "Contaminant": str,            # Selected from dropdown
    "Quantity": float              # Numeric contaminant quantity
}

# Response:
"Safety Prediction: Low | Medium | High"
```

### Model Loading (Internal)

```python
from joblib import load

# Load trained models
adulteration = load("adulteration-prediction-model.joblib")
contamination = load("contamination-prediction-model.joblib")
safety = load("safety-classification-kmeans.joblib")

# Load preprocessing artifacts
contaminant_encoder = load("contaminant_encoder.joblib")
foodgroup_encoder = load("foodgroup_encoder.joblib")
result_scaler = load("result_scaler.joblib")
```

### Making Predictions Programmatically

```python
import pandas as pd
import numpy as np
from joblib import load

# Load models
model = load("contamination-prediction-model.joblib")

# Prepare input
user_input = pd.DataFrame({
    'CountryName': ['India'],
    'FoodGroupName': ['Milk and dairy products'],
    'GEMSFoodName': ['Pasteurized milk'],
    'ContaminantName': ['Lead']
})

# Preprocess and predict
preprocessed = model.named_steps['preprocessor'].transform(user_input)
prediction_log = model.predict(user_input)
prediction_original = np.expm1(prediction_log)[0]

print(f"Predicted Contaminant Level: {prediction_original}")
```

---

## Dataset Information

### Food Adulteration Dataset
- **File**: `Datasets/realistic_food_adulteration_samples.csv`
- **Features**: food_type, adulterant, adulteration_level
- **Target**: is_adulterated (binary)
- **Common Food Types**: Milk, Wheat, Honey, Chili Powder, Turmeric
- **Common Adulterants**: Water, Detergent, Starch, Urea, Soapstone, Chalk Powder

### Food Contamination Dataset
- **File**: `Datasets/food-contamination-data-cleaned-2.csv`
- **Features**: CountryName, FoodGroupName, GEMSFoodName, ContaminantName, Year
- **Target**: ResultValue (contamination quantity)
- **Common Contaminants**: Lead, Cadmium, Aflatoxins, Mercury, Arsenic, Pesticides
- **Food Groups**: Legumes, Fish, Vegetables, Fruits, Dairy, Meat, Eggs, Starchy Roots

---

## Model Performance & Metrics

### Adulteration Model
- **Algorithm**: Logistic Regression
- **Test Split**: 80-20
- **Metrics**: Classification Report (Precision, Recall, F1-Score)

### Contamination Models
- **Algorithm**: Decision Tree / Random Forest Regressor
- **Test Split**: 80-20
- **Metrics**: Mean Squared Error (MSE), R² Score
- **Preprocessing**: Log transformation to handle skewed distributions

### Safety Classification
- **Algorithm**: K-Means (k=3)
- **Silhouette Score**: Used for cluster validation
- **Risk Levels**: Low (Cluster 0), Medium (Cluster 1), High (Cluster 2)

---

## Contributing

### Setting Up Development Environment

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

### Adding New Models

1. Create a new Jupyter notebook in `Training-Modeling/`
2. Load data from `Datasets/`
3. Preprocess, train, and evaluate
4. Save model with joblib: `dump(model, 'model-name.joblib')`
5. Update `Deployment/app.py` to load and use the model

### Frontend Contributions

- **React**: Modify components in `front_end/SafeBiteProject/src/`
- **Next.js**: Modify pages in `front_end/SafeBiteProject/newsafebite/website/app/`
- Follow Tailwind CSS conventions for styling

### Testing Models

```bash
# Run predictions on test data
python Training-Modeling/test_models.py

# Run Streamlit app in test mode
streamlit run Deployment/app.py --logger.level=debug
```

---

## Troubleshooting

### Model Not Found Error
```
FileNotFoundError: File 'model-name.joblib' not found
```

**Solution**: Ensure all `.joblib` files are in the correct directory structure. The app searches recursively from the working directory.

### Missing Contaminant Encoder
```
FileNotFoundError: File 'contaminant_encoder.joblib' not found
```

**Solution**: Regenerate encoders from training notebooks or ensure they're in the same directory as other models.

### Streamlit Session Issues
```bash
# Clear Streamlit cache
streamlit cache clear

# Run with fresh session
streamlit run Deployment/app.py --server.runOnSave false
```

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## Contact & Support

For questions or issues, please:
- Open a GitHub Issue
- Contact the repository maintainer: [@DiyaGhorpade](https://github.com/DiyaGhorpade)

---

## Future Enhancements

- [ ] Multi-sample batch predictions
- [ ] Real-time data integration from food regulatory agencies
- [ ] Mobile app for field inspectors
- [ ] API server (Flask/FastAPI) for integration
- [ ] Advanced visualization dashboards
- [ ] Historical trend analysis
- [ ] Export reports in PDF format
