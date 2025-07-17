

```
# Telegram Medical Analytics Pipeline

## Overview

This project builds a data pipeline to analyze Telegram channels focusing on medical and marketing content in Ethiopia. It processes text messages and images, extracts valuable insights, and exposes analytical endpoints via a REST API. Object detection is applied on media content using the YOLOv8 model, enriching the data warehouse with visual information.

The pipeline is orchestrated using Dagster for robust, schedulable, and observable workflows.

---

## Features

- **Telegram Data Scraping:** Collects messages and media from Telegram channels.
- **Data Storage:** Raw and transformed data stored in PostgreSQL.
- **Image Object Detection:** Detects objects in Telegram images using YOLOv8.
- **Analytical API:** FastAPI endpoints for querying top products, channel activity, and message search.
- **Pipeline Orchestration:** Dagster jobs to automate and monitor the ETL and analysis process.

---

## Project Structure

```

telegram-medical-analytics-pipeline/
│
├── src/                      # Python scripts for scraping, detection, and ETL
│   └── image\_processing/     # YOLOv8 detection module
│
├── api/                      # FastAPI backend source code
│   ├── main.py
│   ├── schemas.py
│   ├── crud.py
│   └── database.py
│
├── dbt/telegram\_dbt/         # dbt models for data transformations
│
├── pipeline/                 # Dagster pipeline and job definitions
│
├── data/                     # Raw data and images
│
├── workspace.yaml            # Dagster workspace config
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── .env                      # Environment variables (API keys, DB credentials)

````

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/anaol216/telegram-medical-analytics-pipeline.git
cd telegram-medical-analytics-pipeline
````

### 2. Create and activate a Python virtual environment

```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows PowerShell
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add:

```
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=telegramdb
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

### 5. Run database migrations and dbt models

Make sure your PostgreSQL is running and accessible. Run dbt models to create your data warehouse tables:

```bash
dbt run --project-dir dbt/telegram_dbt
```

### 6. Run YOLOv8 image detection

```bash
python src/image_processing/detect_objects.py
```

### 7. Start the FastAPI backend

```bash
uvicorn api.main:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore API endpoints.

### 8. Launch Dagster UI (optional)

```bash
dagster dev
```

Use Dagster to orchestrate and monitor your ETL pipeline.

---

## API Endpoints

* **GET /api/reports/top-products?limit=10**
  Returns the top detected product classes.

* **GET /api/channels/{channel\_name}/activity**
  Returns posting activity for a specific Telegram channel.

* **GET /api/search/messages?query=keyword**
  Searches messages containing the specified keyword.

---

## Future Enhancements

* Integrate sentiment analysis on messages.
* Add multi-channel and date range filters.
* Deploy API and pipeline in a containerized environment.
* Build a Streamlit dashboard for visualization.

---

## License

This project is licensed under the MIT License.

---

## Contact

Anaol Atinafu
Email: [atinafuanaol@gmail.com](mailto:atinafuanaol@gmail.com)
GitHub: [https://github.com/anaol216](https://github.com/anaol216)

```
