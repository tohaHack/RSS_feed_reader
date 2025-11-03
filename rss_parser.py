"""RSS Feed Reader"""

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
import urllib.request
import urllib.error
from pathlib import Path
from typing import Optional


URLS_FILE: Path = Path("saved_urls.txt")
FEED_SUFFIX: str = "/feed"

def load_urls() -> list[str]:
    try:
        return [line.strip() for line in URLS_FILE.read_text(encoding="utf-8").splitlines() if line.strip()]
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error occurred: {e}")
        return []
    

def save_url(url: str) -> bool:
    try:
        URLS_FILE.write_text(
            URLS_FILE.read_text(encoding='utf-8', errors='ignore') + url + '\n' # Append new URL
        )
        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

def fetch_feed(url: str) -> Optional[dict]:
    try:
        response: urllib.request._UrlopenRet = urllib.request.urlopen(url=url)
        xml_bytes: str = response.read()
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}")
        return None
    except urllib.error.URLError as e:
        print(f"Connection Lost: {e.reason}")
        return None
    
    try:
        root: Element = ET.fromstring(xml_bytes)
    except ET.ParseError:
        print("Invalid XML/Feed")
        return None

    articles: dict = {}
    for item in root.findall("./channel/item"):
        title: str | None = item.findtext("title")
        link: str | None = item.findtext("link")
        
        if title and link:
            articles[title] = link
            print(f"  • {title}\n    {link}\n")
    return articles if articles else None


def add_news_site(urls: list[str]) -> list[str]:
    new_url: str = input("Enter the RSS feed URL: ")

    if not new_url:
        print("URL cannot be empty!")
        return urls

    new_url += FEED_SUFFIX

    if new_url in urls:
        print("This URL already exists!")
        return urls
    
    if save_url(new_url):
        urls.append(new_url)
        print(f"✓ Added: {new_url}")
    
    return urls


def display_urls(urls: list[str]) -> None:
    if not urls:
        print("No URLs to display.")
        return

    for url in urls:
        print(f"\n📰 Fetching from: {url}")
        articles = fetch_feed(url)
        
        if articles:
            print(f"✓ Successfully fetched {len(articles)} articles\n")
        else:
            print("✗ No articles found\n")


def main() -> None:
    urls: list[str] = load_urls()

    while True:
        choice = input("\nDo you want to add new news site? (y/n): ").lower()

        if choice == 'y':
            urls = add_news_site(urls=urls)
        
        elif choice == 'n':
            if input('Do you want to view saved news sites? (y/n): ').lower() == 'y':
                display_urls(urls=urls)
            break

        else:
            print("Please enter 'y' or 'n'")


if __name__ == "__main__":
    main()