# Al Mayadeen Web Scraper

## Overview

This project is a web scraper designed to collect and store articles from the Al Mayadeen website. The scraper utilizes the sitemap provided by Al Mayadeen to gather URLs of articles and then extracts metadata and content from each article. The extracted data is saved in JSON files, organized by year and month.

## Project Structure

The project consists of the following main components:


Parse the sitemap index at https://www.almayadeen.net/sitemaps/all.xml.
Retrieve URLs of monthly sitemaps.
Extract and scrape each article's metadata and content from the specified <script> tag with type text/tawsiyat.
Save the scraped articles into JSON files, organized by year and month.

1. **Article Dataclass**:
   
url: The URL of the article.
postid: The ID of the post.
title: The title of the article.
keywords: A list of keywords related to the article.
thumbnail: The URL of the article's thumbnail image.
publication_date: The original publication date of the article.
last_updated_date: The last updated date of the article.
author: The author of the article.
content: The main content of the article.
type: The type of the content (e.g., "article").
word_count: The word count of the article.
lang: The language of the article.
description: A brief description of the article.
classes: A list of classes associated with the article, each containing:
key: The class identifier.
mapping: The mapping type of the class.
value: The value of the class.
video_duration: The duration of any video included in the article.
html: The HTML content of the article (if any).
lite_url: A lighter version of the article's URL (if available).
Output Files:

3. **SitemapParser Class**:
    Handles the retrieval and parsing of sitemap URLs. This class extracts URLs from the sitemap index and the monthly sitemaps to identify individual articles.

5. **ArticleScraper Class**:
    Responsible for fetching and parsing the content of individual articles. It extracts the metadata from the `<script>` tag with `type="text/tawsiyat"` and the main content of the article.

7. **FileUtility Class**:
    Manages the saving of scraped articles to JSON files. The files are stored in an output directory, organized by year and month.

9. **Main Function**:
     Orchestrates the scraping process. It:
   - Fetches monthly sitemaps from the sitemap index.
   - Iterates over the article URLs within each monthly sitemap.
   - Scrapes the content and metadata of each article.
   - Saves the scraped articles to JSON files.

JSON files are generated and saved in the output/ directory, named in the format articles_YYYY_MM.json.

# Notes
The maximum number of articles scraped is capped at 10,000 to prevent excessive data load.
Ensure that your internet connection is stable during scraping to avoid interruptions.
License

# Contributing
Feel free to open issues or submit pull requests if you have any improvements or bug fixes!

# Acknowledgements
BeautifulSoup
Requests
Al Mayadeen for providing accessible sitemaps.
