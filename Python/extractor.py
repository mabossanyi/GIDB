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

    def extract_weapons(self):
        weapons_list = self._extract_html_from_filters_divider_tag("weapon")

        return weapons_list

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

    def extract_artifacts_name(self):
        artifacts_details_list = self._extract_html_from_rt_tr_group_tag()
        names_list = [re.sub('<div class=.*?.png">', '', line)
                      for line in artifacts_details_list]
        names_list = [re.sub('</div>.*?</div></div></div>', '', line)
                      for line in names_list]
        names_list = [name.replace("'", "''") for name in names_list]

        return names_list

    def extract_artifacts_description(self):
        artifacts_details_list = self._extract_html_from_rt_tr_group_tag()
        new_artifacts_details_list = list()

        for line in artifacts_details_list:
            pattern = '<div class="rt-td".*?>.*?</div>'
            match_results_list = re.findall(pattern, line, re.IGNORECASE)

            name = re.sub('<div class=.*?.png">', '', match_results_list[0])
            name = re.sub('</div>', '', name)
            name = name.replace("'", "''")

            new_artifacts_details_list.append(
                self._extract_artifact_description_with_count(
                    "2", match_results_list[-2], name))
            new_artifacts_details_list.append(
                self._extract_artifact_description_with_count(
                    "4", match_results_list[-1], name))

        return new_artifacts_details_list

    def _extract_html_from_rt_tr_group_tag(self):
        pattern = '<div class="rt-tr-group".*?>.*?</div></div></div>'
        match_results_list = re.findall(pattern, self._raw_html, re.IGNORECASE)
        match_results_list = [match_result
                              for match_result in match_results_list
                              if match_result.find("rarity-3") == -1]

        return match_results_list

    def _extract_artifact_description_with_count(self, quantity,
                                                 description_html, name):
        description = re.sub('<div .*?>', '', description_html)
        description = re.sub('</div>', '', description)
        description = description.replace("'", "''")

        return name, quantity, description
