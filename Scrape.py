import requests
from bs4 import BeautifulSoup

def scrape_and_save_page(url):
    """Scrapes the given Wikipedia URL and saves it as a text file."""

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the main content paragraphs
        paragraphs = soup.find_all('p')
        text = '\n'.join([paragraph.get_text() for paragraph in paragraphs])

        # Extract the page title from the HTML title tag
        title = soup.title.string

        # Create a filename based on the title, handling special characters
        filename = f"{title.replace('/', '_')}.txt"

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)

        print(f"Page scraped and saved as: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")

if __name__ == '__main__':
    url = input("Enter the Wikipedia URL to scrape: ")
    scrape_and_save_page(url)
