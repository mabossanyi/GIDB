# Libraries
import re


class Extractor:
    # Attributes
    _raw_html = ''

    # Constructors
    def __init__(self, raw_html):
        self._raw_html = raw_html

    # Methods
    def extract_elements(self):
        elements_list = self._extract_html_from_filters_divider_tag("element")

        return elements_list

    def _extract_html_from_filters_divider_tag(self, string_to_find):
        pattern = '<div class="filters-divider"></div>.*?</div></div>'
        match_results = re.search(pattern, self._raw_html, re.IGNORECASE)
        match_results_grouped = match_results.group()

        pattern = '<img alt=".*?" .*?>'
        match_results_list = re.findall(
            pattern, match_results_grouped, re.IGNORECASE)
        results_list = [line
                        for line in match_results_list
                        if line.find(string_to_find) != -1]
        results_list = [re.sub('<.*?"', '', line)
                        for line in results_list]
        results_list = [re.sub('".*?>', '', line)
                        for line in results_list]

        return results_list
