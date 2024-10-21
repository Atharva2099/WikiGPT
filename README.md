# WikiGPT

wikiGPT is a Streamlit-based web application that allows users to scrape Wikipedia pages and process the content using the Mistral language model. The app provides an interface to input Wikipedia URLs, scrape their content, and ask questions about the scraped text using natural language processing.

## Features

    - Scrape content from Wikipedia pages
    - Save scraped content as text files
    - Process scraped content using the Mistral language model
    - Interactive web interface built with Streamlit

## Installation

1. Clone this repository:

git clone https://github.com/yourusername/wikiGPT.git
cd wikiGPT

2. Install the required dependencies:

pip install -r requirements.txt

3. Install Ollama following the instructions at [Ollama](https://ollama.com/)

## Usage

1. Run the Streamlit app:

   streamlit run app.py

2. Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8000).
   
3. Use the app interface to:

        - Enter a Wikipedia URL to scrape
        - Upload a scraped text file
        - Enter a prompt to process the text with Mistral

  ## File Structure
  
    - app.py: Main Streamlit application file
    - scrape.py: Contains the web scraping functionality
    - requirements.txt: List of Python dependencies
      
  ## Dependencies

    - streamlit
    - langchain
    - requests
    - beautifulsoup4
    - ollama (system-level installation)
