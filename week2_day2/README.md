
# Global News Data Project

This project is a Python-based data engineering pipeline that collects, stores, cleans, and analyzes real-time news headlines from multiple countries using a public news API.

It demonstrates a full ETL workflow (Extract → Transform → Load) using Python.


# Project Overview

The system is divided into two main components:

1. Data Collection Pipeline

A script that:

* Fetches live news data from an API
* Standardizes and cleans the response
* Stores results in a structured dataset
* Prevents duplicate entries on multiple runs

2. Data Analysis Engine

A script that:

* Reads stored CSV data
* Performs statistical and textual analysis
* Generates insights about news trends across countries


# Countries Covered

* 🇳🇵 Nepal
* 🇮🇳 India
* 🇺🇸 USA
* 🇬🇧 UK
* 🇦🇺 Australia

# 📂 Output Files

| File            | Purpose                                     |
| --------------- | ------------------------------------------- |
| `news_data.csv` | Raw + cleaned combined dataset              |
| `title.csv`     | Headlines filtered by word count (>6 words) |

---

# Key Insights Generated

The analysis answers:

* Which country publishes the most headlines
* Average headline length per country
* Duplicate headlines across countries
* Most active news source globally
* Recent vs older news distribution (6-hour window)
* Data deduplication handling
* Filtering long headlines
* Countries with longest vs shortest headlines



# Technologies Used

* Python 
* Pandas 
* Requests 
* datetime 
* dotenv 
