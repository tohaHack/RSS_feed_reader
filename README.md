# RSS Feed Reader

A simple and clean Python application for reading RSS feeds from multiple news sources. Add your favorite news sites and fetch the latest articles with ease.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Features

- 📰 **Add Multiple News Sources** - Easily add RSS feed URLs to your collection
- 💾 **Persistent Storage** - URLs are saved to a file for future sessions
- 🔍 **Parse RSS Feeds** - Automatically extracts titles and links from RSS feeds
- ⚠️ **Robust Error Handling** - Gracefully handles network errors, invalid XML, and connection issues
- 🎯 **Simple CLI Interface** - User-friendly command-line interface
- 📊 **Clean Code Architecture** - Well-structured, maintainable, and extensible codebase

## Requirements

- Python 3.9 or higher
- Standard library modules only (no external dependencies)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tohaHack/RSS_feed_reader.git
cd rss_feed_reader
```

2. Create a Python virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. No external dependencies needed! The project uses Python's standard library.

## Usage

Run the application:
```bash
python rss_reader.py
```

### Interactive Menu

```
Do you want to add new news site? (y/n): y
Enter RSS feed URL: https://example.com/news
✓ Added: https://example.com/news/feed

Do you want to add new news site? (y/n): n
Do you want to see news from saved URLs? (y/n): y

📰 Fetching from: https://example.com/news/feed
  • Article Title One
    https://example.com/article1

  • Article Title Two
    https://example.com/article2

✓ Successfully fetched 2 articles
```

## Project Structure

```
rss-feed-reader/
├── rss_reader.py          # Main application file
├── saved_urls.txt         # Stored RSS feed URLs (auto-generated)
├── README.md              # This file
└── .gitignore             # Git ignore file
```

### Main Functions

**`load_urls()`**
- Loads saved URLs from `saved_urls.txt`
- Returns a list of URL strings
- Handles file not found gracefully

**`save_url(url: str) -> bool`**
- Saves a new URL to the file
- Returns True on success, False on error

**`fetch_feed(url: str) -> Optional[dict]`**
- Fetches and parses RSS feed from the given URL
- Handles HTTP errors, connection errors, and XML parsing errors
- Returns dictionary with article titles as keys and links as values

**`add_news_site(urls: list[str]) -> list[str]`**
- Prompts user to enter a new RSS feed URL
- Validates input and prevents duplicates
- Returns updated URL list

**`display_news(urls: list[str]) -> None`**
- Fetches and displays articles from all saved URLs
- Shows article count for each source

**`main()`**
- Runs the main application loop
- Handles user interaction and menu navigation

## Configuration

### Modifying Feed Suffix

By default, the application appends `/feed` to URLs. To change this, modify the constant in `rss_reader.py`:

```python
FEED_SUFFIX = "/rss"  # Change to your preferred suffix
```

### Changing Storage File

To use a different filename:

```python
URLS_FILE = Path("my_rss_feeds.txt")
```

## Error Handling

The application gracefully handles:

- **HTTP Errors** (404, 403, 500, etc.) - Displays HTTP error code
- **Connection Errors** - Notifies user when connection is lost
- **Invalid XML** - Handles malformed RSS feeds
- **File I/O Errors** - Manages missing or corrupted URL files
- **Empty Input** - Validates user input and prevents empty URLs

### Example Error Messages

```
HTTP Error 404: https://example.com/invalid/feed
Connection Error: [Errno 11001] getaddrinfo failed
Invalid XML/Feed: https://example.com/feed
```

## Example RSS Feeds

Here are some popular RSS feed URLs you can use:

- BBC News: `https://feeds.bbc.co.uk/news`
- CNN: `https://feeds.cnn.com/rss/cnn_topstories.rss`
- Reuters: `https://www.reutersagency.com/feed`
- TechCrunch: `https://feeds.techcrunch.com/techcrunch`
- The Verge: `https://www.theverge.com/rss`

## Future Enhancements

Potential features for future versions:

- [ ] Search functionality within articles
- [ ] Filter articles by keyword
- [ ] Remove/update stored URLs
- [ ] Async feed fetching for faster performance
- [ ] Article caching to reduce API calls
- [ ] Export articles to CSV/JSON
- [ ] Web-based GUI interface
- [ ] Logging system
- [ ] Configuration file support

## Development

### Code Style

This project follows PEP 8 style guidelines with:
- Type hints for all functions
- Docstrings for all functions
- Clear variable naming
- Single Responsibility Principle

### Running Tests

Currently, no automated tests. To manually test:

```bash
# Test with valid RSS feed
python rss_reader.py

# Test with invalid URL (should handle gracefully)
# Test with empty input (should reject)
# Test duplicate URL entry (should reject)
```

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'urllib'`
- **Solution**: This is part of Python's standard library. Ensure you're using Python 3.x

**Issue**: `FileNotFoundError: saved_urls.txt`
- **Solution**: This is expected on first run. The file will be created when you add your first URL.

**Issue**: RSS feed returns no articles
- **Solution**: Not all RSS feeds have the standard `./channel/item` structure. Some feeds may use different XML paths.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## Author

Created by [k3zu](https://github.com/tohaHack)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is provided as-is for educational purposes. Ensure you have permission to access and parse RSS feeds from any news sources.

---

## Quick Start

```bash
# 1. Run the app
python rss_reader.py

# 2. Add a news source
# Input: y
# URL: https://feeds.bbc.co.uk/news

# 3. View news
# Input: n
# Input: y

# 4. Exit
# Done!
```

For more information, visit the [RSS Specification](https://www.rss-board.org/rss-specification).