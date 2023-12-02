# Libraries
import browser
import extractor
import processor
from storage import Storage
from writer import Writer


# Methods
def main():
    # Header of the program
    version = "TODO"

    # Get the class "Extractor" for the main page using the URL
    # to extract the HTML
    main_page_url = "https://genshin.gg/"
    main_page_extractor = get_page_extractor_from_url(main_page_url)

    # Get the class "Storage"
    storage = Storage()

    # Extract and store the elements
    extract_and_store_elements(main_page_extractor, storage)

    # Extract and store the weapons
    extract_and_store_weapons(main_page_extractor, storage)

    # Get the class "Extractor" for the artifacts page using the URL
    # to extract the HTML
    artifacts_page_url = "https://genshin.gg/artifacts/"
    artifacts_page_extractor = get_page_extractor_from_url(artifacts_page_url)

    # Extract and store the items (i.e. the artifact names)
    extract_and_store_items(artifacts_page_extractor, storage)

    # Extract and store the items sets (i.e. the artifact sets description)
    extract_and_store_items_sets(artifacts_page_extractor, storage)

    # Extract and store the characters data for each character on the main page
    extract_and_store_characters_data(
        main_page_url, main_page_extractor, storage)

    # Get the class "Processor" from the characters raw data
    data_processor = processor.Processor(storage.get_characters_raw_data())

    # Preprocess and store the stats from the characters raw data
    preprocess_and_store_stats(data_processor, storage)

    # Preprocess and store the slots from the characters raw data
    preprocess_and_store_slots(data_processor, storage)

    # Preprocess and store the characters from the characters raw data
    preprocess_and_store_characters(data_processor, storage)

    # Preprocess and store the characters stats from the characters raw data
    preprocess_and_store_characters_stats(data_processor, storage)

    # Preprocess and store the characters items from the characters raw data
    preprocess_and_store_characters_items(data_processor, storage)

    # Write the "INSERT.sql" file
    file_name = "INSERT.sql"
    write_insert_sql_file(file_name, version, storage)


def get_page_extractor_from_url(url):
    page_browser = browser.Browser(url)
    raw_html = page_browser.get_html_from_url()
    page_extractor = extractor.Extractor(raw_html)

    return page_extractor


def extract_and_store_elements(page_extractor, storage):
    elements = page_extractor.extract_elements()
    storage.store_elements(elements)


def extract_and_store_weapons(page_extractor, storage):
    weapons = page_extractor.extract_weapons()
    storage.store_weapons(weapons)


def extract_and_store_items(artifacts_extractor, storage):
    items_names = artifacts_extractor.extract_artifacts_name()
    storage.store_items(items_names)


def extract_and_store_items_sets(artifacts_extractor, storage):
    items_sets = artifacts_extractor.extract_artifacts_description()
    storage.store_items_sets(items_sets)


def extract_and_store_characters_data(url, page_extractor, storage):
    characters_raw_data = page_extractor.extract_characters_raw_data(url)
    storage.store_characters_raw_data(characters_raw_data)


def preprocess_and_store_stats(data_processor, storage):
    stats = data_processor.preprocess_characters_raw_data_for_stat()
    storage.store_stats(stats)


def preprocess_and_store_slots(data_processor, storage):
    slots = data_processor.preprocess_characters_raw_data_for_slot()
    storage.store_slots(slots)


def preprocess_and_store_characters(data_processor, storage):
    characters = data_processor.preprocess_characters_raw_data_for_character()
    storage.store_characters(characters)


def preprocess_and_store_characters_stats(data_processor, storage):
    characters_stats = (
        data_processor.preprocess_characters_raw_data_for_characters_stat())
    storage.store_characters_stats(characters_stats)


def preprocess_and_store_characters_items(data_processor, storage):
    characters_items = (
        data_processor.preprocess_characters_raw_data_for_characters_items())
    storage.store_characters_items(characters_items)


def write_insert_sql_file(file_name, version, storage):
    file_writer = Writer()
    file_writer.write_insert_sql_file(file_name, version, storage)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
