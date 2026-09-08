# Web-Scraping-Capstone-Project

# Real-Time Weather Web Scraper & Interactive Dashboard

An end-to-end Python data pipeline that scrapes live weather data from global cities, cleans and processes the dataset using Pandas, stores it persistently in a SQLite database, and presents interactive visualizations using Matplotlib and Plotly in a Jupyter Notebook.


## Tech Stack & Libraries

* **Web Scraping:** `Selenium`, `webdriver-manager`
* **Data Manipulation & Cleaning:** `Pandas`, `NumPy`, `re` (Regex)
* **Database & Storage:** `SQLite3`, `CSV`
* **Data Visualization & Analytics:** `Matplotlib`, `Plotly`
* **Interactive UI:** `ipywidgets` (Jupyter Notebook)


## Features & Workflow

1. **Automated Scraping:** Uses headless Selenium Chrome driver to fetch live city temperatures, local times, and URLs from Timeanddate.
2. **Data Transformation:** Cleans degree symbols, normalizes city names, handles missing values, and calculates temperature conversions ($°F \rightarrow °C$).
3. **Database Integration:** Automatically resets and updates a structured SQLite table (`weather.db`) with cleaned data.
4. **Interactive Dashboard:** 
   * **Distribution Charts:** Bar Graph and Box plot for global temperature spread.
   * **Dynamic Threshold Sliders:** Interactive `ipywidgets` sliders to filter cities above specific temperature thresholds.


## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/Web-Scraping-Capstone-Project.git](https://github.com/your-username/Web-Scraping-Capstone-Project.git)
   cd Web-Scraping-Capstone-Project
2. **Create a branch**
   ```bash
   git checkout -b "scrapingbranch"
3. **Create a folder called "WEB SCRAPING"**
4. **Create a main file called "cities.py"**
