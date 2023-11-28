# Libraries
import re

import browser


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

    def extract_characters_raw_data(self, main_page_url):
        characters_hrefs_list = self._extract_html_from_character_list_tag()
        character_urls_list = ["{}{}".format(main_page_url, href)
                               for href in characters_hrefs_list]

        character_raw_data_list = list()
        [character_raw_data_list.append(self._extract_character_raw_data(url))
         for url in character_urls_list]
        character_raw_data_list = [
            character_raw_data
            for character_raw_data in character_raw_data_list
            if character_raw_data is not None]

        return character_raw_data_list

    def _extract_html_from_character_list_tag(self):
        pattern = '<div class="character-list">.*?</a></div>.*?</main>'
        match_results = re.search(pattern, self._raw_html, re.IGNORECASE)
        match_results_grouped = match_results.group()

        pattern = '<a href=".*?">'
        match_results_list = re.findall(
            pattern, match_results_grouped, re.IGNORECASE)
        character_hrefs_list = [re.sub('<a href="', '', line)
                                for line in match_results_list]
        character_hrefs_list = [re.sub('" .*?>', '', line)
                                for line in character_hrefs_list]

        return character_hrefs_list

    def _extract_character_raw_data(self, character_url):
        character_browser = browser.Browser(character_url)
        character_raw_html = character_browser.get_html_from_url()

        # Rarity
        pattern = '<img class="character-portrait .*?"'
        match_results = re.search(pattern, character_raw_html, re.IGNORECASE)
        match_results_grouped = match_results.group()
        rarity = re.sub('<.*? rarity-', '', match_results_grouped)
        rarity = re.sub('"', '', rarity)

        # Name
        pattern = '<img class="character-portrait .*? alt=".*?">'
        match_results = re.search(pattern, character_raw_html, re.IGNORECASE)
        match_results_grouped = match_results.group()
        name = re.sub('<.*? alt="', '', match_results_grouped)
        name = re.sub('">', '', name)
        name = name.replace("'", "''")

        # Element
        pattern = '<img class="character-element" .*?</div>'
        match_results = re.search(pattern, character_raw_html, re.IGNORECASE)
        match_results_grouped = match_results.group()
        element = re.sub('<.*? alt="', '', match_results_grouped)
        element = re.sub('"></div>', '', element)
        element = element.replace("'", "''")

        # Weapon
        pattern = '<img class="character-path-icon" .*?>.*?</div>'
        match_results = re.search(pattern, character_raw_html, re.IGNORECASE)
        match_results_grouped = match_results.group()
        weapon = re.sub('<.*?>', '', match_results_grouped)
        weapon = re.sub('</div>', '', weapon)
        weapon = weapon.replace("'", "''")

        # Artifacts
        pattern = ('<h2 class="character-build-section-title">.*?</div>'
                   '</div></div></div>')
        match_results_titles_list = re.findall(
            pattern, character_raw_html, re.IGNORECASE)
        match_results_titles_weapons_and_artifacts_list = [
            title for title in match_results_titles_list
            if title.find("Artifacts") != -1]
        artifacts_dict = dict()

        if len(match_results_titles_weapons_and_artifacts_list) == 0:
            return None

        all_artifacts = re.sub(
            '.*?<div class="character-build-section">', '',
            match_results_titles_weapons_and_artifacts_list[0])

        # Title
        pattern = "<h2 .*?>.*?</h2>"
        match_results = re.search(pattern, all_artifacts, re.IGNORECASE)
        match_results_grouped = match_results.group()
        artifact_title = re.sub('<h2 .*?>', '', match_results_grouped)
        artifact_title = re.sub('</h2>', '', artifact_title)
        artifact_title = artifact_title.split(" ")[-1].lower()
        artifacts_list = list()

        pattern = ('<div class="character-build-weapon-rank">.*?</div>'
                   '</div></div>')
        match_results_artifacts_list = re.findall(
            pattern, all_artifacts, re.IGNORECASE)

        for single_artifact in match_results_artifacts_list:
            # Name & Quantity
            pattern = ('<div class="character-build-weapon-name">.*?</div>'
                       '</div>')
            match_results_list = re.findall(
                pattern, single_artifact, re.IGNORECASE)
            names_and_quantities_list = [
                re.sub('<div class=".*?">', '', line)
                for line in match_results_list]
            names_and_quantities_list = [
                re.sub('</div></div>', '', line)
                for line in names_and_quantities_list]
            names_and_quantities_list = [
                re.sub('</div>', ';', name_and_quantity)
                for name_and_quantity in names_and_quantities_list]
            artifacts_list.append(names_and_quantities_list)
        artifacts_dict[artifact_title] = artifacts_list

        if len(artifacts_dict[artifact_title][0]) == 0:
            return None

        # Stats & Substats
        pattern = '<h2 class="character-stats-title">.*?</div></div>'
        match_results_titles_list = re.findall(
            pattern, character_raw_html, re.IGNORECASE)
        match_results_titles_stats_and_substats_list = [
            title for title in match_results_titles_list
            if title.find("stats") != -1]
        stats_and_substats_dict = {"stats": list(), "substats": list()}

        if len(match_results_titles_stats_and_substats_list) == 0:
            return None

        all_stats_and_substats = re.findall(
            '<b>.*?</b>.*?</div>',
            match_results_titles_stats_and_substats_list[0], re.IGNORECASE)
        all_stats_and_substats = [re.sub('<b>', '', line)
                                  for line in all_stats_and_substats]
        all_stats_and_substats = [re.sub('</b> ', '', line)
                                  for line in all_stats_and_substats]
        all_stats_and_substats = [re.sub('</div>', '', line)
                                  for line in all_stats_and_substats]

        for single_stat_or_substats in all_stats_and_substats:
            if single_stat_or_substats.find(">") == -1:
                slot_and_stat = single_stat_or_substats.replace(":", ";")
                stats_and_substats_dict["stats"].append(slot_and_stat)
            else:
                substats = single_stat_or_substats.replace("Substats:", "")
                substats = substats.split(" > ")
                stats_and_substats_dict["substats"] = substats

        if (len(stats_and_substats_dict["stats"][0]) == 0
                or len(stats_and_substats_dict["substats"][0]) == 0):
            return None

        artifacts_dict_keys = [
            key for key in artifacts_dict.keys()]
        stats_and_substats_dict_keys = [
            key for key in stats_and_substats_dict.keys()]

        character_data = {
            "name": name,
            "rarity": rarity,
            "element": element,
            "weapon": weapon,
            artifacts_dict_keys[0]: artifacts_dict[artifacts_dict_keys[0]],
            stats_and_substats_dict_keys[0]: stats_and_substats_dict[
                stats_and_substats_dict_keys[0]],
            stats_and_substats_dict_keys[1]: stats_and_substats_dict[
                stats_and_substats_dict_keys[1]]
        }

        return character_data
