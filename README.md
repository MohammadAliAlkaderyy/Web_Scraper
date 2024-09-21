# Article Scraper - Data Science

## Overview

ArticleScraper is a Python project designed to scrape articles from a website using sitemap URLs, extract metadata, and save the articles in JSON format and stores them in a MongoDB collection, and provides insightful visualizations and analysis through a Flask-based web application.. The project leverages the `requests` library for making HTTP requests, `BeautifulSoup` for parsing HTML/XML, and Python's `dataclasses` for structured data management.The analysis includes entity recognition and sentiment analysis. The results providing users with different types of visualizations and they  are displayed on a dashboard with multiple pages.

## Features

-Web scraping
-MongoDB integration
-Sentiment Analysis
-Entity Recognition
-Dynamic Visualizations
-Interactive Dashboard

![Uploading Terminal After Scraping 10k Article.png…]()


---


# Project Structure:

## -1 Web Scraping with Python :

#### Objective
Create a Python script to extract articles from the Al Mayadeen website, gather metadata, and save it into JSON files organized by month.

#### Prerequisites
- [Al Mayadeen Sitemap Index](https://www.almayadeen.net/sitemaps/all.xml)
- Basic Python knowledge
- Internet connection
- 
#### Setup
1. **Install Python**: Download and install from [python.org](https://www.python.org/).
2. **Install PyCharm**: Download from [JetBrains](https://www.jetbrains.com/pycharm/download/), install, and configure.
3. **Install Libraries**: Run `pip install requests beautifulsoup4 lxml` in PyCharm terminal.

#### Sitemap Structure
- **Main Sitemap**: [https://www.almayadeen.net/sitemaps/all.xml](https://www.almayadeen.net/sitemaps/all.xml)
- **Monthly Sitemaps**: Pattern `https://www.almayadeen.net/sitemaps/all/sitemap-YYYY-MM.xml`
- **Article URLs**: Found within each monthly sitemap.
- 
#### Tasks
1. **Parse Sitemap**: Retrieve and extract article URLs from monthly sitemaps.
2. **Scrape Articles**: Fetch articles, extract metadata from `<script>` tags, and article text from `<p>` tags.
3. **Store Data**: Save data to JSON files named `articles_YYYY_MM.json`.
    
#### Instructions
1. **Create Script**: `web_scraper.py` for the complete code.
2. **Data Model**: Use a Python dataclass for article metadata and content.
3. **Sitemap Parser**: Retrieve and parse sitemap URLs.
4. **Article Scraper**: Extract metadata and article content.
5. **File Utility**: Save data to JSON files.
6. **Main Function**: Integrate all components and handle errors.

#### Deliverables
- **Python Script**: Upload to GitHub.
- **JSON Files**: Process up to 10,000 articles.

#### Tips
- **Testing**: Validate with a small number of articles first.
- **Error Handling**: Manage network issues and unexpected data formats.
- **Documentation**: Comment code for clarity.


   

---



## 2- Storing Data in MongoDB and Building a Flask API

#### Objective
This task aims to store the data collected in task 1 into MongoDB and build a Flask API for accessing and analyzing the data through various endpoints.
( experience in:
- Storing data in MongoDB.
- Building a Flask API to interact with and analyze the data.)

##### Task Overview
1. **Storing Data in MongoDB**: 
   - Load the scraped JSON data from task 1.
   - Insert the data into a MongoDB collection named `articles` within a database `almayadeen`.

2. **Creating Flask API**: 
   - Build an API to query and analyze the stored data.
   - Create multiple endpoints to access key insights, such as:
     - Top keywords, authors, and article counts.
     - Articles filtered by word count, publication date, or category.

#### Instructions
 1. **Store Data in MongoDB**
- **Script**: `data_storage.py`
- This script reads the JSON files and inserts the data into MongoDB.
 2. **Create Flask API**
- **Script**: `app.py`
- This script defines various API endpoints for querying the data.
- 
#### Example Endpoints:
1. `/top_keywords`: Returns the top 10 most frequent keywords.
2. `/top_authors`: Lists the top 10 authors by article count.
3. `/articles_by_date`: Shows the number of articles published on each date.
4. `/articles_by_word_count`: Groups articles by their word count.
5. `/recent_articles`: Returns the 10 most recently published articles.
6. `/articles_by_keyword/<keyword>`: Returns articles that contain a specific keyword.
    
#### . **Run Flask Application**
- Run `app.py` and access the API via `http://127.0.0.1:5000/`.
- Test endpoints using a browser or Postman.
  
#### Deliverables
- **Python Scripts**: 
  - `data_storage.py`: For storing data in MongoDB.
  - `app.py`: Flask app providing API endpoints.
- **MongoDB Database**: Ensure MongoDB contains the scraped data.
- **Flask API**: API should provide access to key data insights.
- 
#### Tips
- **Testing**: Test each API endpoint using a browser or Postman.
- **Documentation**: Comment your code for clarity.
- **Error Handling**: Ensure the code gracefully handles empty data and network issues.

####  experience in:
- Storing data in MongoDB.
- Building a Flask API to interact with and analyze the data.

---


## 3-Data Visualization with amCharts:

#### Objective:
Creating 30 different visualizations using amCharts to represent insights from the data.
Integrated amCharts library to create various visualizations.
Implemented charts for different data insights.
Visualizations:Line charts, bar charts, pie charts, etc.



## 4- Advanced Data Analysis and Insights:

#### Objective
Apply advanced data analysis techniques, including sentiment analysis, entity recognition, and trend analysis. Enhance your Flask API to provide these insights and create an interactive dashboard.

#### Prerequisites
- **Basic NLP Knowledge**: Understanding of sentiment analysis and entity recognition.
- **Python Libraries**: Familiarity with libraries like NLTK, spaCy, or TextBlob.

#### Setup
1. **Install NLP Libraries**
   
#### Overview
 1. Sentiment Analysis
- **Task**: Analyze article sentiment (positive, negative, neutral).
- **Store Results**: Add a `sentiment` field in MongoDB for each article.
- **API Extension**: Create `/articles_by_sentiment/<sentiment>` endpoint to query by sentiment.

 2. Entity Recognition
- **Task**: Extract named entities (people, places, organizations) from articles.
- **Store Results**: Add an `entities` field in MongoDB.
- **API Extension**: Create `/articles_by_entity/<entity>` endpoint for entity-based queries.

 3. Trend Analysis
- **Task**: Analyze trends in sentiment, keywords, or entities over time.
- **Visualize**: Use charts to display trends.
- **API Extension**: Create endpoints like `/sentiment_trends` or `/keyword_trends`.

 4. Enhancing the API
- **Most Positive/Negative Articles**: `/most_positive_articles` and `/most_negative_articles`.
- **Articles by Entity**: `/articles_by_entity/<entity>`.
- **Trend Data**: `/trends/<keyword>` or `/trends/<entity>`.

 5. Creating a Dashboard
- **Combine Insights**: Develop an interactive dashboard with visualizations.
- **User Interaction**: Allow filtering by sentiment, entities, and date ranges.

 6.Deliverables
- **Enhanced Flask API**: New endpoints for sentiment, entity, and trend analysis.
- **MongoDB Updates**: Articles enriched with sentiment and entity data.
- **Interactive Dashboard**: An engaging dashboard that integrates all insights and visualizations.

 7.Tips
- **Data Validation**: Ensure accuracy in sentiment and entity processing.
- **Optimization**: Optimize queries for performance.
- **Security**: Protect the API with security measures (e.g., authentication).


  
# Technologies Used
Python: For web scraping, data processing, and API creation.
Flask: To build the server and APIs.
MongoDB: For data storage.
am5charts: For generating visualizations.
TextBlob and Stanza: For sentiment and entity analysis.
Bootstrap: For front-end design and dashboard layout.

