# ArticleScraper

## Overview
**ArticleScraper** is a Python-based project designed to efficiently scrape articles from a website using sitemap URLs. It extracts metadata and saves the articles in JSON format. The project utilizes the `requests` library for HTTP requests, `BeautifulSoup` for HTML/XML parsing, and Python's `dataclasses` for structured data management.

## Features
- **Fetch Sitemap URLs**: Extracts monthly sitemap URLs from a primary sitemap index.
- **Scrape Articles**: Downloads and parses articles, extracting metadata such as title, author, keywords, and full text.
- **Save to JSON**: Organizes and saves scraped articles into JSON files, categorized by the year and month of publication.

## Prerequisites
- **Python**: Version 3.7 or later.
- **Required Libraries**: Install the necessary libraries with the following command:
  ```
  pip install requests beautifulsoup4 lxml
  ```

## Usage
1. **Clone the Repository**
   ```
   git clone https://github.com/MhmdRhayem/Article-Scraper.git
   ```

2. **Run the Scraper**
   ```
   python web_scraper.py
   ```

## Output
Scraped articles are saved in the `./articles` directory, organized by year and month.

## Code Structure
- **`Article`**: A data class representing an article with fields such as `url`, `post_id`, `title`, `keywords`, etc.
- **`fetch_data(url)`**: A function to fetch data from a URL.
- **`save_articles(articles_list)`**: A function to save a list of articles to a JSON file.
- **`SitemapParser`**: A class to parse the main sitemap and retrieve monthly sitemap URLs.
- **`ArticleScraper`**: A class to scrape and parse individual articles from their URLs.
- **`main()`**: The main function controlling the flow of the program.

---

