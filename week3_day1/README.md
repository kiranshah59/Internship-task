Week 3 — MySQL Data Engineering Project

This project demonstrates how to build a complete data pipeline using Python and MySQL, including API integration, database design, data processing, and analytical reporting.

The goal is to simulate real-world backend/data engineering workflows by collecting data from APIs, storing it in relational databases, and performing structured analysis using SQL.

---Project Overview

Across five tasks, this project covers:

Database creation and schema design
API data extraction and transformation
Inserting structured and nested JSON data into MySQL
Writing SQL queries for analysis
Exporting processed data into files (CSV, TXT)
Generating automated summary reports
Task Breakdown


---Task 1 — Library Database System

A structured database for managing books and reviews.

Created library_db
Designed books and reviews tables
Inserted sample book dataset
Performed analytical queries:
Books published after 2000
High-rated Fiction books
Average rating calculation
Genre-wise book count


---Task 2 — API to MySQL Pipeline

A full ETL pipeline using user and post data.

Created app_db
Fetched data from JSONPlaceholder API
Stored:
User details (including nested city & company fields)
Posts for selected users (IDs 1–3)
Implemented SQL analysis:
Alphabetical user sorting
City-wise grouping of users
JOIN between users and posts


---Task 3 — Weather Data Engineering Pipeline

A real-world weather analytics system.

Created weather_db
Fetched 7-day forecasts for:
New York
London
Tokyo
Stored:
Max temperature
Min temperature
Average humidity
SQL analysis:
Hottest city (average)
Single hottest recorded day
Days with high temperature variation (>10°C)
Generated automated report:
summary.txt


---Task 4 — Student Grade Management System

A data processing system for academic records.

Created grades_db
Stored student marks
Implemented:
Grade assignment logic
Grade updates
Pass/fail classification
Deletion of low-performing students
Analytical queries on grade distribution



---Task 5 — News Data Pipeline & Analysis 

Created news_db database and articles table in MySQL
Fetched news data for multiple countries using an API
Stored article details (title, source, country, language, date) in MySQL
Exported data to news_data.csv
Performed SQL analysis:
Articles per country
Top news sources
Latest articles
Language distribution