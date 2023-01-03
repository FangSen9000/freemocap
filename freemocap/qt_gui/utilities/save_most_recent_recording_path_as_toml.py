import logging
from pathlib import Path
from typing import Union

import toml

from freemocap.configuration.paths_and_files_names import (
    get_logs_info_and_settings_folder_path,
    MOST_RECENT_RECORDING_TOML_FILENAME,
)

logger = logging.getLogger(__name__)


def save_most_recent_recording_path_as_toml(
    most_recent_recording_path: Union[str, Path]
):
    """Save the most recent recording path to a toml file"""
    output_file_path = (
        Path(get_logs_info_and_settings_folder_path())
        / MOST_RECENT_RECORDING_TOML_FILENAME
    )

    logger.info(
        f"Saving most recent recording path {str(most_recent_recording_path)} to toml file: {str(output_file_path)}"
    )
    toml_dict = {}
    toml_dict["most_recent_recording_path"] = most_recent_recording_path

    with open(str(output_file_path), "w") as toml_file:
        toml.dump(toml_dict, toml_file)