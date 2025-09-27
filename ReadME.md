## **Backend Installation Steps**

* Install Python 3.10+
* Create & activate virtual environment
* Install dependencies: `pip3 install -r backend_requirements.txt`
* Create FastAPI file: `main.py`
* Create `.env` file in the project root with database values
* Run FastAPI app: `uvicorn main:app --reload`
* Access API at http://127.0.0.1:8000/
* Add venv/ to .gitignore to avoid committing virtual environment