# Libraries
import browser
import extractor
import processor
from storage import Storage
from writer import Writer


# Methods
def main():
    # Header of the program
    version = "4.3 (Phase 2)"
    print("Running the Genshin Impact Database (GIDB) script using "
          "the version '{}'\n".format(version))

    # Get the class "Extractor" for the main page using the URL
    # to extract the HTML
    main_page_url = "https://genshin.gg/"
    main_page_extractor = get_page_extractor_from_url(main_page_url)

    # Get the class "Storage"
    storage = Storage()

    # Extract and store the elements
    print("Extracting and storing the elements...")
    extract_and_store_elements(main_page_extractor, storage)

    # Extract and store the weapons
    print("Extracting and storing the weapons...")
    extract_and_store_weapons(main_page_extractor, storage)

    # Get the class "Extractor" for the artifacts page using the URL
    # to extract the HTML
    artifacts_page_url = "https://genshin.gg/artifacts/"
    artifacts_page_extractor = get_page_extractor_from_url(artifacts_page_url)

    # Extract and store the items (i.e. the artifact names)
    print("Extracting and storing the items (artifacts)...")
    extract_and_store_items(artifacts_page_extractor, storage)

    # Extract and store the item sets (i.e. the artifact sets description)
    print("Extracting and storing the items sets...")
    extract_and_store_item_sets(artifacts_page_extractor, storage)

    # Extract and store the characters data for each character on the main page
    print("Extracting and storing the characters data for each character...")
    extract_and_store_characters_data(
        main_page_url, main_page_extractor, storage)

    # Get the class "Processor" from the characters raw data
    data_processor = processor.Processor(storage.get_characters_raw_data())

    # Preprocess and store the stats from the characters raw data
    print("Preprocessing and storing the stats...")
    preprocess_and_store_stats(data_processor, storage)

    # Preprocess and store the slots from the characters raw data
    print("Preprocessing and storing the slots...")
    preprocess_and_store_slots(data_processor, storage)

    # Preprocess and store the characters from the characters raw data
    print("Preprocessing and storing the characters...")
    preprocess_and_store_characters(data_processor, storage)

    # Preprocess and store the character stats from the characters raw data
    print("Preprocessing and storing the characters-stats...")
    preprocess_and_store_character_stats(data_processor, storage)

    # Preprocess and store the character items from the characters raw data
    print("Preprocessing and storing the characters-items...")
    preprocess_and_store_character_items(data_processor, storage)

    # Write the "INSERT.sql" file
    file_name = "INSERT.sql"
    print("Writing the 'INSERT.sql' file...")
    write_insert_sql_file(file_name, version, storage)


def get_page_extractor_from_url(url):
    page_browser = browser.Browser(url)
    raw_html = page_browser.get_html_from_url()
    page_extractor = extractor.Extractor(raw_html)

    return page_extractor


def extract_and_store_elements(page_extractor, storage):
    elements = page_extractor.extract_elements()
    storage.store_elements(elements)
    _print_verbosity_from_data(elements)
    print(" Completed.\n\t --> Total of {} element(s)\n".format(len(elements)))


def extract_and_store_weapons(page_extractor, storage):
    weapons = page_extractor.extract_weapons()
    storage.store_weapons(weapons)
    _print_verbosity_from_data(weapons)
    print(" Completed.\n\t --> Total of {} weapon(s)\n".format(len(weapons)))


def extract_and_store_items(artifacts_extractor, storage):
    item_names = artifacts_extractor.extract_artifacts_name()
    storage.store_items(item_names)
    _print_verbosity_from_data(item_names, title="Artifacts")
    print(" Completed.\n\t --> Total of {} item(s)\n".format(len(item_names)))


def extract_and_store_item_sets(artifacts_extractor, storage):
    item_sets = artifacts_extractor.extract_artifacts_description()
    storage.store_item_sets(item_sets)
    print(" Completed.\n\t --> Total of {} items set(s)\n".format(
        len(item_sets)))


def extract_and_store_characters_data(url, page_extractor, storage):
    characters_raw_data = page_extractor.extract_characters_raw_data(url)
    storage.store_characters_raw_data(characters_raw_data)
    print(" Completed.\n\t --> Total of {} character(s) data\n".format(
        len(characters_raw_data)))


def preprocess_and_store_stats(data_processor, storage):
    stats = data_processor.preprocess_characters_raw_data_for_stats()
    storage.store_stats(stats)
    _print_verbosity_from_data(stats)
    print(" Completed.\n\t --> Total of {} stat(s)\n".format(len(stats)))


def preprocess_and_store_slots(data_processor, storage):
    slots = data_processor.preprocess_characters_raw_data_for_slots()
    storage.store_slots(slots)
    _print_verbosity_from_data(slots)
    print(" Completed.\n\t --> Total of {} slot(s)\n".format(len(slots)))


def preprocess_and_store_characters(data_processor, storage):
    characters = data_processor.preprocess_characters_raw_data_for_characters()
    storage.store_characters(characters)
    print(" Completed.\n\t --> Total of {} character(s)\n".format(
        len(characters)))


def preprocess_and_store_character_stats(data_processor, storage):
    character_stats = (
        data_processor.preprocess_characters_raw_data_for_character_stats())
    storage.store_character_stats(character_stats)
    print(" Completed.\n\t --> Total of {} characters-stat(s)\n".format(
        len(character_stats)))


def preprocess_and_store_character_items(data_processor, storage):
    character_items = (
        data_processor.preprocess_characters_raw_data_for_character_items())
    storage.store_character_items(character_items)
    print(" Completed.\n\t --> Total of {} characters-item(s)\n".format(
        len(character_items)))


def write_insert_sql_file(file_name, version, storage):
    file_writer = Writer()
    file_writer.write_insert_sql_file(file_name, version, storage)
    print(" Completed.")


def _print_verbosity_from_data(data_list, title=""):
    if title != "":
        print("  {}:".format(title))

    [print("\t> {}".format(data)) for data in data_list]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
