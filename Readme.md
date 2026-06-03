 # Automated Price Scraper
[![Automated Cloud Scraper](https://github.com/Bhanukarthik-220548/automated-price-scraper/actions/workflows/auto_scraper.yml/badge.svg)](https://github.com/Bhanukarthik-220548/automated-price-scraper/actions/workflows/auto_scraper.yml)
 

A Python-based web scraping project that automatically tracks book prices and stores historical data in a CSV file. The scraper runs daily using GitHub Actions and can also be triggered manually.

## Features

* Automated daily scraping
* Manual workflow execution
* CSV-based price history
* Automatic commits via GitHub Actions
* CI/CD pipeline integration

## Tech Stack

* Python
* Requests
* BeautifulSoup4
* GitHub Actions
* Git

## Project Structure

```text
.
├── scraper.py
├── price_history.csv
├── requirements.txt
└── .github
    └── workflows
        └── scraper.yml
```

## How It Works

1. Scrapes book information from the target website.
2. Extracts title and price.
3. Appends data to a CSV file.
4. GitHub Actions runs automatically on schedule.
5. Updated data is committed back to the repository.

## Future Improvements

* Email notifications for price drops
* Multiple product tracking
* Charts and analytics
* Database integration
