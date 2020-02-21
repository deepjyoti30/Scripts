from pathlib import Path
from sys import argv
import re
from collections import OrderedDict
from os import makedirs
import json
from subprocess import call


class SeriesPlayer():
    """
    Series player class to play a series and keep track of it as
    we go about with it.

    It will use mpv to play the series.
    """
    def __init__(self, path):
        self.path = path
        self._log_dir = Path("~/.cache/series/").expanduser()
        self._path_check()

        # Name of the series
        self._series_name = self.path.name
        self._history_file = self._log_dir.joinpath(Path(
                                    "{}.series".format(self._series_name)
                                ))
        self._current_epi_file = self._log_dir.joinpath(Path(
                                    "{}.current".format(self._series_name)
                                ))
        self._init_checks()
        self._start()

    def _init_checks(self):
        """Make the obvious initial checks."""

        print("[*] Series name is [{}]".format(self._series_name))
        print("[*] Checking if history file exists...")
        # If the file is present in cache, then don't process
        if not self._history_file.exists():
            print("[*] Does not exist. Calling processes to get data.")
            self._parent_list = self._process_parent()
            self._process_children()

            # Dump the data into series file
            self._save_to_file()
            self._save_current()

            self._cached_data = self._parent_list
        else:
            print("[*] Exists! Skipping processes")
            with open(self._history_file, 'r') as RSTREAM:
                self._cached_data = json.load(RSTREAM)
            print("[*] Data extracted from cached file")

    def _path_check(self):
        """Check if the path is okay for working on."""
        print("[*] Doing pre process checks...")

        if not self.path.exists():
            print("Passed path does not exist! Exiting..!")
            exit(-1)

        if not self._log_dir.exists():
            makedirs(self._log_dir)

        self.parent_dir = self.path

    def _serialize_data(self, series_data):
        """Serialize the data."""
        serialized_data = {}

        for season_number, season_data in series_data.items():
            for episode_number in range(0, len(season_data)):
                data_value = season_data[str(episode_number + 1)]
                if len(season_number) < 2:
                    season_number = "0" + season_number
                if episode_number < 9:
                    episode_number = "0" + str(episode_number + 1)
                else:
                    episode_number = str(episode_number + 1)
                data_key = "{}{}".format(season_number, episode_number)
                serialized_data[data_key] = data_value

        return serialized_data

    def _play(self, episode):
        """Play the passed episode."""
        starting_epi = episode

        for it in self._cached_data:
            try:
                if it < starting_epi:
                    continue
                print("[*] Playing {}".format(it))
                self._save_current(it)
                self._mpv(self._cached_data[it])
            except KeyboardInterrupt:
                print("[*] You watched till {}".format(it))
                exit(0)

    def _mpv(self, path):
        """Call MPV and pass the path to play."""
        call([
                'mpv',
                '--really-quiet',
                '--save-position-on-quit',
                '--resume-playback',
                path
            ])

    def _start(self):
        """Start with the execution."""
        self._cached_data = self._serialize_data(self._cached_data)
        current_epi = open(self._current_epi_file, 'r').read().replace("\n", "")

        if current_epi == "None":
            print("[*] Starting series from beginning!")
            current_epi = "0101"
        else:
            print("[*] Resuming series at {}".format(current_epi))

        self._play(current_epi)

    def _get_all_match(self, values, keyword):
        """Get all the possible matches of the keyword passed in the list."""
        matched_list = {}

        for value in values:
            # Try to extract the season number, if it's not present
            # skip the dir
            season_name = value.name.lower()
            result = re.search(
                    '{}({})?[\ \.]?[0-9]?[0-9]'.format(keyword[0], keyword[1:]),
                    season_name
                )
            if result is not None:
                result = result.group(0)
            else:
                continue
            season_number = re.sub(
                                    '{}({})?'.format(keyword[0], keyword[1:]),
                                    '',
                                    result
                                ).replace(" ", "")
            matched_list[int(season_number)] = value.as_posix()

        return matched_list

    def _process_parent(self):
        """Process the parent directory and extract all the Seasons."""
        season_list = []

        for season in self.parent_dir.iterdir():
            if season.is_dir():
                season_list.append(season)

        return OrderedDict(sorted(
                            self._get_all_match(season_list, "season")
                            .items()
                            ))

    def _process_children(self):
        """Process all the episodes."""
        temp_episode_list = []

        for key, season in self._parent_list.items():
            season = Path(season)
            for episode in season.iterdir():
                if re.search('mp4|mkv|avi$', episode.name.lower()):
                    temp_episode_list.append(episode)
            self._parent_list[key] = OrderedDict(sorted(
                self._get_all_match(temp_episode_list, "episode").items()
            ))

    def _save_current(self, current_epi=None):
        """Save the current epi to the file."""
        with open(self._current_epi_file, 'w') as WSTREAM:
            WSTREAM.write(str(current_epi))

    def _save_to_file(self):
        """Save the data to the series file."""
        with open(self._history_file, 'w') as WSTREAM:
            json.dump(self._parent_list, WSTREAM)

        print("[*] Data written to {}".format(self._history_file.parent))


def main():
    if len(argv) <= 1:
        print("Please pass a path for the series to play.!")
        exit(-1)

    passed_path = Path(" ".join(argv[1:])).expanduser()
    series_player = SeriesPlayer(passed_path)


if __name__ == "__main__":
    main()
