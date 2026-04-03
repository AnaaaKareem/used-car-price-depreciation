# User Car Price Detector

This guide provides instructions on how to set up and run the FastAPI Backend and the Streamlit Dashboard for real-time car valuations.

## Prerequisites

Before starting, ensure you have the following installed:
- Python 3.10 or higher
- pip (Python Package Installer)

## Environment Setup

It is strongly recommended to use a virtual environment to isolate project dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# .\venv\Scripts\activate
```

### Install Dependencies
Execute the following command to install the required libraries for both the backend and frontend:

```bash
pip install fastapi uvicorn streamlit pandas numpy joblib scikit-learn category_encoders requests pydantic
```

## Executing the Application

To use the full valuation system, you must run the Backend and the Frontend simultaneously in separate terminal windows.

### Initialize the FastAPI Backend
The backend engine handles the machine learning inference, data normalization, and live currency exchange (USD ↔ GBP).

```bash
# Ensure you are in the project root directory
uvicorn src.app:app --reload
```
- Local Endpoint: http://localhost:8000
- Interactive API Docs: http://localhost:8000/docs (Swagger UI)

### Launch the Streamlit Dashboard
The dashboard provides a premium UI for users to input vehicle parameters and receive instant market valuations.

```bash
# Open a NEW terminal tab (Keep the backend running!)
# Remember to activate your virtual environment (source venv/bin/activate)
streamlit run src/dashboard.py
```
- Local Dashboard: http://localhost:8501 (Should open automatically)

## System Architecture Note

- Backend (src/app.py): Acts as the "Brain". It validates input using Pydantic, fetches live FX rates, and executes the Random Forest pipeline.
- Frontend (src/dashboard.py): Acts as the "Face". It collects user input and communicates with the backend via REST API.
- Model Check (models/model.pkl): The system requires this serialized bundle. If it is missing, ensure you have ran python src/train.py after data processing.

## Troubleshooting

- "Connection Failed: Backend server not reachable": verify that your uvicorn command is still active in its terminal tab.
- "ModuleNotFoundError": You likely forgot to activate the virtual environment or run the pip install command.
- "Model not found": Ensure the models/ directory contains model.pkl.
