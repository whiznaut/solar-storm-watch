# 🌌 Solar Storm Watch  

Solar Storm Watch is a local ETL (Extract → Transform → Load) pipeline that ingests real-time **space weather data** from public NOAA APIs, transforms and cleans the raw records, stores them in a local **SQLite database**, and generates summaries for analysis.  

This project is designed as a **portfolio-quality data engineering project** showcasing best practices in:  
- Modular Python ETL design  
- Database integration with SQLite  
- Data validation and testing with `pytest`  
- CI/CD automation with GitHub Actions  
- Optional containerization with Docker  

---

## ⚙️ Features  

- **Ingest**: Fetches real-time space weather alerts, events, and forecasts from [NOAA SWPC APIs](https://services.swpc.noaa.gov/).  
- **Transform**: Cleans JSON → tabular data, validates fields, handles missing values.  
- **Load**: Inserts processed records into a structured SQLite database with deduplication.  
- **Storage**: Saves both raw JSON and processed CSVs locally for reproducibility.  
- **Querying**: Easily extract subsets of data from SQLite for analysis.  
- **Testing**: Full unit tests for each pipeline step.  
- **Automation**: CI/CD with GitHub Actions ensures tests run on every push.  
- **Containerization**: Docker support for reproducible environments.  

---

## 🚀 Getting Started  

### 1. Clone the repository  
```bash
git clone https://github.com/yourusername/solar-storm-watch.git
cd solar-storm-watch
```

### 2. Create and activate a virtual environment 
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies 
```bash
pip install -r requirements.txt
```

### 4. Run the pipeline
```bash
python src/main.py
```

This will:
- Fetch the latest space weather data from NOAA
- Save raw JSON files to data/raw/
- Transform and store processed CSVs in data/processed/
- Insert cleaned records into data/solar_data.db


## Running Tests

### Unit tests are located in the tests/ directory. Run them with:
```bash
pytest -v
```

## Running with Docker (optional)

### 1. Build the container:
```bash 
docker build -t solar-storm-watch .
```

### 2. Run the pipeline inside Docker:
```bash 
docker run --rm -v $(pwd)/data:/app/data solar-storm-watch
```

## Technologies Used 

- Python 3.10+
- Pandas (data transformation)
- SQLite3 (lightweight database)
- Pytest (testing framework)
- Requests (API ingestion)
- GitHub Actions (CI/CD)
- Docker (optional containerization)


## Why This Project?

This project demonstrates practical data engineering skills:
- Working with real-world APIs
- Handling data pipelines end-to-end
- Implementing clean code & modularity
- Testing & CI/CD for reliability
- Deployable with Docker


## Future Improvements

- Add scheduling with Apache Airflow or Prefect
- Support additional NOAA datasets (e.g., solar wind, geomagnetic indices)
- Build a simple dashboard with Streamlit or Dash
- Migrate from SQLite → PostgreSQL for scalability