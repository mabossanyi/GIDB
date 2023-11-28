# Libraries
import browser
import extractor
from storage import Storage


# Methods
def main():
    # Get the class "Extractor" for the main page using the URL
    # to extract the HTML
    main_page_url = "https://genshin.gg/"
    main_page_extractor = get_page_extractor_from_url(main_page_url)

    # Get the class "Storage"
    storage = Storage()

    # Extract and store the elements
    extract_and_store_elements(main_page_extractor, storage)


def get_page_extractor_from_url(url):
    page_browser = browser.Browser(url)
    raw_html = page_browser.get_html_from_url()
    page_extractor = extractor.Extractor(raw_html)

    return page_extractor


def extract_and_store_elements(page_extractor, storage):
    elements = page_extractor.extract_elements()
    storage.store_elements(elements)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
