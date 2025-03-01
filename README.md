# Hacker News ETL with Apache Airflow

This project implements an **ETL (Extract, Transform, Load) pipeline** using **Apache Airflow** to fetch top stories from [Hacker News](https://news.ycombinator.com/) and save them as a CSV file.

## 📌 Project Overview

- **Extract**: Fetches top 50 stories from the Hacker News API.
- **Transform**: Extracts relevant information (title, score, URL, timestamp).
- **Load**: Saves the extracted data into a CSV file (`hackernews_top_stories.csv`).
