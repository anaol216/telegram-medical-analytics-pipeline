

---

# 10 Academy: Data Engineering Mastery

Kara Solutions – Telegram Medical Analytics Platform – INTERIM REPORT – Week 7 Challenge
**Name:** Anaol Atinafu
**Email:** [atinafuanaol@gmail.com](mailto:atinafuanaol@gmail.com)
**Project:** Shipping a Data Product: From Raw Telegram Data to an Analytical API
**Organization:** Kara Solutions / 10 Academy
**Date:** July 13, 2025

---

## Introduction

This project focuses on building a modern data platform to analyze Ethiopian medical businesses using unstructured data collected from public Telegram channels. The objective is to build an end-to-end ELT pipeline that transforms raw Telegram messages into structured analytical datasets.

---

## Task 0: Project Setup & Environment Management 

### Activities Completed

* 🔹 **Git Repository Initialized**: Set up a version-controlled repository.
* 🔹 **Project Structure Organized**:

  * Created `src/` folder with submodules (`scraper/`, `models/`, etc.)
  * Added necessary `__init__.py` files for Python package structure.
* 🔹 **Dependency Management**:

  * Created `requirements.txt` for Python packages.
  * Installed required packages inside both virtual environment and Docker environment.
* 🔹 **Dockerization**:

  * Developed `Dockerfile` to containerize the Python application.
  * Configured `docker-compose.yml` to orchestrate both the Python service and PostgreSQL database.
* 🔹 **Environment Variables**:

  * Created a `.env` file to securely manage sensitive credentials:

    * `TELEGRAM_API_ID`
    * `TELEGRAM_API_HASH`
    * Database credentials
  * Updated `.gitignore` to exclude `.env` and `venv/` folders.
* 🔹 **dotenv Integration**:

  * Used `python-dotenv` to load secrets within the application.

---

## Task 1: Data Scraping and Collection (Extract & Load) 

### Progress Summary

* 🔹 **Telegram API Access**:

  * Registered and obtained `TELEGRAM_API_ID` and `TELEGRAM_API_HASH`.
  * Established API connection using the `Telethon` library.
* 🔹 **Scraping Script Developed**:

  * Created initial Telegram scraping script inside `src/scraper/telegram_scraper.py`.
  * Extracts:

    * Message text
    * Posting date
    * Sender/channel metadata
    * Images (where available)
* 🔹 **Data Lake Structure Setup**:

  * Raw data stored as JSON files under:

    * `data/raw/telegram_messages/YYYY-MM-DD/channel_name.json`
* 🔹 **Logging & Monitoring**:

  * Integrated basic logging to track scraping sessions and handle errors.
* 🔹 **Channels Scraped**:

  * Chemed Telegram Channel
  * Lobelia Cosmetics: [https://t.me/lobelia4cosmetics](https://t.me/lobelia4cosmetics)
  * Tikvah Pharma: [https://t.me/tikvahpharma](https://t.me/tikvahpharma)
* 🔹 **Image Collection**:

  * Image files collected alongside message data for future YOLO processing.

---

## Challenges Faced

| Challenge                             | Solution                                                         |
| ------------------------------------- | ---------------------------------------------------------------- |
| Import errors (`ModuleNotFoundError`) | Resolved using proper package structure with `__init__.py` files |
| Environment conflicts                 | Standardized using Docker Compose and `.env` files               |
| Telegram API handling                 | Implemented error handling and logging                           |

---

## Next Steps

* Finish structured loading into PostgreSQL.
* Begin data modeling with dbt.
* Set up YOLOv8 environment for image enrichment.
* Develop the FastAPI layer to expose analytical endpoints.

---

## Conclusion

Task 0 and Task 1 have been successfully implemented. The system now reliably scrapes raw Telegram data and organizes it in a structured data lake, ready for transformation and analysis in subsequent tasks.

---
