# Expense Management System

This project is an expense management system that consists of a streamlit frontend application and a FastAPI backend server.

## Project Structure
- **frontend/** : Contains the streamlit application code.
- **backend/** : Contains the FastAPI backend server code.
- **test/** : Contains the test cases for both frontend and backend.
- **requirements/** : Lists the required Python packages.
- **README.md/** : Provides an overview and instructor for the projects

## Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone ```
2. **Install dependencies:**
    ``` commandline
   pip install -r requirements.txt
   ```
3. **Run the FastAPI server:**
    ```commandline
    uvicorn server.server.app --reload
   ```
4. **Run the FastAPI server:**
    ```commandline
    streamlit run frontend/app.py```