# Assignment 3 — Crypto & Sentiment Data Pipeline

This project completes **Assignment 3: Data Pipeline for Statistical Analysis** using **Pack A — Crypto & Sentiment** for a **365-day window**.

## Project Goal
The goal of this pipeline is to combine:
1. **Binance Market Data API** for daily Bitcoin OHLCV data
2. **Alternative.me Fear & Greed API** for daily crypto sentiment data

The final Gold dataset is designed to support Part 2 statistical analysis such as:
- one-sample t-tests,
- two-sample t-tests,
- and proportion z-tests.

---

## APIs Used
### 1. Binance Market Data
- Pulls daily BTC/USDT candlestick data
- Used for close price, volume, and daily return

### 2. Alternative.me Fear & Greed Index
- Pulls daily sentiment values and labels
- Used for grouping days by Fear, Neutral, and Greed sentiment

---

## Medallion Architecture
```text
Public APIs
   ↓
Ingest Scripts
   ↓
data/bronze/   -> raw API snapshots
   ↓
Transform Scripts
   ↓
data/silver/   -> cleaned source tables
   ↓
Join + Feature Engineering
   ↓
data/gold/     -> final analysis-ready dataset
```

---

## Folder Structure
```text
crypto_assignment_project/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── analysis_preview.md
├── data/
│   ├── bronze/
│   │   ├── binance/
│   │   └── fear_greed/
│   ├── silver/
│   └── gold/
├── ingest/
│   ├── ingest_binance.py
│   ├── ingest_fear_greed.py
│   └── run_ingestion.py
├── transform/
│   ├── bronze_to_silver.py
│   └── silver_to_gold.py
└── notebooks/
    └── .gitkeep
```

---

## How to Run the Project

## 1. Create and activate a virtual environment
### Windows PowerShell
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Mac/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Install dependencies
```bash
pip install -r requirements.txt
```

## 3. Run ingestion twice
```bash
python ingest/run_ingestion.py
python ingest/run_ingestion.py
```
This creates multiple Bronze snapshots, as required by the assignment.

## 4. Transform Bronze to Silver
```bash
python transform/bronze_to_silver.py
```

## 5. Build the Gold dataset
```bash
python transform/silver_to_gold.py
```

---

## Silver Layer
The Silver layer contains one clean file per source:
- `data/silver/btc_daily_clean.csv`
- `data/silver/fear_greed_clean.csv`

### Cleaning decisions
- Converted API timestamps to proper dates
- Cast numeric columns to the correct types
- Renamed columns clearly
- Dropped duplicates by date using the latest Bronze snapshot
- Standardized sentiment labels into a simple grouping variable

---

## Gold Layer
The Gold dataset is stored at:
- `data/gold/crypto_sentiment_daily.csv`

### Gold columns
- `date`
- `btc_close`
- `btc_volume`
- `btc_daily_return`
- `fear_greed_value`
- `fear_greed_label`
- `fear_greed_label_group`
- `positive_return`
- `is_weekend`

### Why this Gold dataset works for Part 2
This dataset supports later statistical analysis because it contains:
- a **continuous numeric variable**: `btc_daily_return`
- a **grouping variable**: `fear_greed_label_group`
- a **binary variable**: `positive_return`

That means it can support:
- **one-sample t-test**: Is mean BTC daily return different from 0?
- **two-sample t-test**: Are returns different on Fear vs Greed days?
- **proportion z-test**: Is the proportion of positive-return days higher on Greed days?

---

## Join Strategy
The Silver datasets are joined on the `date` column.

Because the two APIs may not always have perfectly matching dates, the Gold build uses an **inner join** so that only dates available in both cleaned datasets are included. This creates a smaller but analysis-ready dataset with no missing join values.

---

## Missing Values Strategy
- Missing or invalid numeric values are converted to `NaN`
- Dates with no overlap between sources are excluded in Gold through the inner join
- The first row of `btc_daily_return` is naturally missing because there is no previous day for comparison
- `positive_return` is left blank only when daily return is missing

---

## Example Statistical Question
Do average daily Bitcoin returns differ between **Fear** days and **Greed** days?

- Outcome variable: `btc_daily_return`
- Grouping variable: `fear_greed_label_group`
- Binary variable: `positive_return`
- Suggested test: **two-sample t-test**

---

## AI Usage
I used ChatGPT to help generate starter code structure for the ingestion and transformation scripts, explain the medallion architecture, and draft the README.

One thing I still had to verify myself was the timestamp handling. I had to make sure Binance timestamps were in milliseconds while the Fear & Greed API timestamps were in Unix seconds, otherwise the join by date would have been wrong.

---

## Notes
This project includes full 365-day example output files so the repo has a complete structure. The ingestion scripts are already configured with a 365-day limit, so rerunning the pipeline will recreate Bronze, Silver, and Gold data for the latest 365 days.
