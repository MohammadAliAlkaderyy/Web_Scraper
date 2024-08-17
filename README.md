# Al Mayadeen Web Scraper

## Overview

This project is a web scraper designed to collect and store articles from the Al Mayadeen website. The scraper utilizes the sitemap provided by Al Mayadeen to gather URLs of articles and then extracts metadata and content from each article. The extracted data is saved in JSON files, organized by year and month.

## Project Structure

The project consists of the following main components:

1. **Article Dataclass**: Defines the structure of the data to be extracted from each article, including fields like `url`, `post_id`, `title`, `keywords`, `thumbnail`, `publication_date`, `last_updated_date`, `author`, and `content`.

2. **SitemapParser Class**: Handles the retrieval and parsing of sitemap URLs. This class extracts URLs from the sitemap index and the monthly sitemaps to identify individual articles.

3. **ArticleScraper Class**: Responsible for fetching and parsing the content of individual articles. It extracts the metadata from the `<script>` tag with `type="text/tawsiyat"` and the main content of the article.

4. **FileUtility Class**: Manages the saving of scraped articles to JSON files. The files are stored in an output directory, organized by year and month.

5. **Main Function**: Orchestrates the scraping process. It:
   - Fetches monthly sitemaps from the sitemap index.
   - Iterates over the article URLs within each monthly sitemap.
   - Scrapes the content and metadata of each article.
   - Saves the scraped articles to JSON files.
