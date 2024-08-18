import requests
from bs4 import BeautifulSoup
from typing import Optional, List, Dict
from dataclasses import dataclass
import json
import os
from dataclasses import asdict


@dataclass
class Article:
    url: str
    postid: Optional[int]
    title: Optional[str]
    keywords: Optional[List[str]]
    thumbnail: Optional[str]
    publication_date: Optional[str]
    last_updated_date: Optional[str]
    author: Optional[str]
    content: Optional[str]
    type: Optional[str]
    word_count: Optional[str]
    lang: Optional[str]
    description: Optional[str]
    classes: Optional[List[Dict[str, str]]]
    video_duration: Optional[str]
    html: Optional[str]
    lite_url: Optional[str]


class SitemapParser:
    def __init__(self, sitemap_index_url: str):
        self.sitemap_index_url = sitemap_index_url

    def get_monthly_sitemap_urls(self):
        try:
            response = requests.get(self.sitemap_index_url)
            xml_content = response.text
            if xml_content:
                soup = BeautifulSoup(xml_content, "lxml")
                sitemaps = soup.find_all("loc")
                sitemap_urls = [sitemap.string for sitemap in sitemaps]
                return sitemap_urls
            return []
        except Exception as e:
            print(f"Failed to parse sitemaps: {e}")
            return []

    def extract_article_urls(self, monthly_sitemap_url: str) -> List[str]:
        response = requests.get(monthly_sitemap_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'xml')
        article_urls = [loc.string for loc in soup.find_all('loc')]
        return article_urls


class ArticleScraper:

    def __init__(self):
        self.session = requests.Session()

    def scrape_article(self, url: str) -> Article:
        response = self.session.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract metadata from <script> tag with type="text/tawsiyat"
        metadata_script = soup.find('script', type='text/tawsiyat')
        metadata = json.loads(metadata_script.string) if metadata_script else {}

        article = Article(
            url=url,
            postid=metadata.get('postid', ''),
            title=metadata.get('title', ''),
            keywords=metadata.get('keywords', '').split(','),
            thumbnail=metadata.get('thumbnail', ''),
            publication_date=metadata.get('published_time', ''),
            last_updated_date=metadata.get('last_updated', ''),
            author=metadata.get('author', ''),
            content=' '.join(p.get_text() for p in soup.find_all('p')),
            type=metadata.get('type', ''),
            word_count=metadata.get('word_count', ''),
            lang=metadata.get('lang', ''),
            description=metadata.get('description', ''),
            classes=metadata.get('classes', []),
            video_duration=metadata.get('video_duration', ''),
            html=metadata.get('html', ''),
            lite_url=metadata.get('lite_url', '')
        )
        return article


class FileUtility:
    def __init__(self, output_directory: str):
        self.output_directory = output_directory
        os.makedirs(output_directory, exist_ok=True)

    def save_to_json(self, articles: List[Article], year: str, month: str):
        filename = f'articles_{year}_{month}.json'
        file_path = os.path.join(self.output_directory, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump([asdict(article) for article in articles], f, ensure_ascii=False, indent=4)


def main():
    # Define the sitemap index URL
    sitemap_index_url = "https://www.almayadeen.net/sitemaps/all.xml"  # Replace with the correct sitemap index URL

    # Initialize the classes
    sitemap_parser = SitemapParser(sitemap_index_url)
    article_scraper = ArticleScraper()
    file_utility = FileUtility(output_directory='output')

    # Retrieve the monthly sitemaps
    monthly_sitemaps = sitemap_parser.get_monthly_sitemap_urls()

    if not monthly_sitemaps:
        print("No monthly sitemaps found.")
        return

    # Initialize article count
    total_articles_scraped = 0
    max_articles = 10000  # Maximum number of articles to scrape

    # Loop through each monthly sitemap
    for monthly_sitemap in monthly_sitemaps:
        if total_articles_scraped >= max_articles:
            break  # Stop if we have reached the limit

        print(f"Processing sitemap: {monthly_sitemap}")

        # Extract article URLs from the monthly sitemap
        article_urls = sitemap_parser.extract_article_urls(monthly_sitemap)

        # Scrape each article and store the data
        articles = []
        for url in article_urls:
            if total_articles_scraped >= max_articles:
                break  # Stop if we have reached the limit

            try:
                article = article_scraper.scrape_article(url)
                articles.append(article)
                total_articles_scraped += 1
                print(f"Scraped article: {article.title} (Total: {total_articles_scraped})")
            except Exception as e:
                print(f"Failed to scrape {url}: {e}")

        # Extract year and month from the sitemap URL
        year_month = monthly_sitemap.split('-')[-2:]  # Extract 'YYYY-MM' from the URL
        year = year_month[0]
        month = year_month[1].replace('.xml', '')

        # Save articles to JSON
        file_utility.save_to_json(articles, year, month)

    print(f"Completed scraping {total_articles_scraped} articles.")


main()
