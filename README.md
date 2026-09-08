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


## Screenshots
<img width="1728" height="1117" alt="image" src="https://github.com/user-attachments/assets/56eea19e-15db-4128-84d0-583e9eb9a9ac" />

<img width="1728" height="1117" alt="image" src="https://github.com/user-attachments/assets/0b7136ab-a86d-42b4-8d02-008be2340e5f" />

<img width="1725" height="1114" alt="image" src="https://github.com/user-attachments/assets/88f35c40-4457-4a63-b17b-7421dff6b741" />

<img width="1728" height="1117" alt="image" src="https://github.com/user-attachments/assets/57c74123-5e0e-4324-872e-7bed078d58dc" />

<img width="1718" height="1117" alt="image" src="https://github.com/user-attachments/assets/b2aeac08-3fc2-4843-8484-7764fb20e3b6" />



