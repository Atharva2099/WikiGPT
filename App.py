import streamlit as st

# LLM
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Scraping function
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

        return filename

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching page: {e}")
        return None

# LLM setup
llm = Ollama(
    model="mistral:7b-instruct",
    verbose=True,
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
)

# Streamlit app
st.write("Mistral WebApp")

# Scraping section
scrape_url = st.text_input("Enter Wikipedia URL to scrape:")
if scrape_url:
    filename = scrape_and_save_page(scrape_url)
    if filename:
        st.success(f"Page scraped and saved as: {filename}")

# LLM processing
selected_file = st.file_uploader("Select a text file to process", type=["txt"])
if selected_file:
    file_text = selected_file.read().decode("utf-8")

    prompt = st.text_input("Enter your Prompt:")
    if prompt:
        with st.spinner("Processing with Mistral..."):
            llm_prompt = f"Answer the following question in 100 or so words about the text:\n{file_text}\nQuestion: {prompt}"
            llm_response = llm(llm_prompt)
        st.write(llm_response)
