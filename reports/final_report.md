# 10 Academy: Data Engineering Mastery  
## Telegram Medical Analytics Pipeline  
### Final Report – Week 7 Challenge  

**Name:** Anaol Atinafu  
**Email:** atinafuanaol@gmail.com  
**Project:** Telegram Analytics with Object Detection and Analytical API  
**Organization:** 10 Academy  
**Date:** July 18, 2025  

---

## Introduction

This project focuses on analyzing marketing and medical-related Telegram channels in Ethiopia using a modern data pipeline. The pipeline processes both text and image content, extracting structured insights such as product mentions, channel activity, and visual object detection from posted media using YOLOv8. The solution supports business teams in monitoring channel trends, understanding visual marketing content, and searching for product mentions through an analytical API.

The project is divided into 5 main tasks:

1. Data Collection via Telegram Scraper  
2. PostgreSQL Data Loading  
3. Object Detection with YOLOv8  
4. Analytical API Development with FastAPI  
5. Pipeline Orchestration with Dagster  

---

## Technical Choices

| Component          | Final Decision                                       |
|--------------------|-----------------------------------------------------|
| Data Source        | Telegram channels (scraped messages and media)      |
| Database           | PostgreSQL (raw and fact tables)                     |
| ETL Framework      | Python scripts organized in modular structure       |
| Object Detection   | YOLOv8n (ultralytics, local model)                   |
| Backend API        | FastAPI + Uvicorn                                    |
| Orchestration      | Dagster (local pipeline orchestration)               |
| Visualization      | Streamlit (optional future step)                      |

---

## System Breakdown

**Task 1: Data Collection**  
- Scraped messages and images from Telegram channels.  
- Stored metadata and image file paths in PostgreSQL (`raw_telegram_messages` table).  

**Task 2: Database Modeling**  
- Structured staging and fact models using dbt:  
    - `raw_telegram_messages`  
    - `fct_messages`  
    - `fct_image_detections`  
    - `dim_channels`  

**Task 3: Object Detection with YOLO**  
- Applied pre-trained YOLOv8n on downloaded Telegram images.  
- Stored detected objects and confidence scores in `fct_image_detections`.  

**Task 4: FastAPI Analytical Endpoints**  
- Built REST API to query insights:  
    - `/api/reports/top-products`  
    - `/api/channels/{channel_name}/activity`  
    - `/api/search/messages?query=product`  
- Exposed structured insights from dbt-transformed tables.

**Task 5: Dagster Orchestration**  
- Converted pipeline steps into Dagster ops and jobs.  
- Enabled local pipeline monitoring and scheduling via Dagster UI.

---

## System Evaluation

| Endpoint                         | Example URL                                         | Purpose                               |
|---------------------------------|-----------------------------------------------------|-------------------------------------|
| `/api/reports/top-products`      | `/api/reports/top-products?limit=10`                | Returns most detected product classes|
| `/api/channels/{channel}/activity` | `/api/channels/lobelia4cosmetics/activity`          | Shows posting frequency for a channel|
| `/api/search/messages`           | `/api/search/messages?query=paracetamol`            | Searches Telegram messages by keyword|

**Database Statistics:**  
- Messages in `fct_messages`: 10,000+  
- Images processed: 134  
- Detections inserted: 178  

---

## User Interface and Monitoring

- API browsable via Swagger Docs (`http://127.0.0.1:8000/docs`).  
- Dagster UI for job execution and monitoring (`dagster dev`).  
- API responses structured using Pydantic schemas.

---

## Challenges and Solutions

| Challenge                          | Solution                                       |
|----------------------------------|------------------------------------------------|
| YOLO detections missing from DB  | Improved filename parsing for message IDs      |
| API returning 500 errors          | Fixed SQL queries and ensured table existence  |
| Dagster not detecting jobs        | Created workspace.yaml and correct pipeline    |
| PostgreSQL schema inconsistencies | Migrated properly using dbt                     |

---

## Key Learnings

- Image content adds unique insights into marketing trends when combined with NLP.  
- Modular API design simplifies querying complex data.  
- Dagster is an effective orchestrator for managing data pipelines.  
- Clear data models (via dbt) improve downstream reporting and API development.

---

## Future Improvements

- Add sentiment analysis of messages.  
- Integrate YOLO image labels directly into message text search.  
- Deploy FastAPI with Docker for production use.  
- Schedule pipeline to run daily using Dagster.  
- Add a Streamlit dashboard for executive-level insights.

---

## Repository Overview

| File / Folder           | Purpose                                |
|------------------------|----------------------------------------|
| `src/`                 | All ETL, YOLO detection scripts        |
| `src/image_processing/`| YOLOv8 image detection module           |
| `api/main.py`          | FastAPI application                     |
| `api/schemas.py`       | Pydantic response models                |
| `api/crud.py`          | SQL queries to PostgreSQL                |
| `dbt/telegram_dbt`     | dbt models for fact/dim tables          |
| `pipeline/pipeline.py` | Dagster pipeline definition             |
| `workspace.yaml`       | Dagster configuration                   |
| `requirements.txt`     | Project dependencies                    |
| `README.md`            | Setup and usage guide                    |

---

## GitHub Link

**Main Branch:**  
https://github.com/anaol216/telegram-medical-analytics-pipeline  

---

## Conclusion

This Telegram Analytics project demonstrates how unstructured text and image data from social media can be structured, analyzed, and exposed as business insights using modern data engineering tools. From YOLO object detection to dbt transformations and FastAPI endpoints, the solution is modular and production-ready. With Dagster orchestration in place, the project is scalable for future daily operations.

---
