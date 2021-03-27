import os
from pathlib import Path

def env_to_str(envvar: str) -> str:
    return os.environ.get(envvar, "")

def env_to_int(envvar: str) -> int:
    pass

def env_is_set(envvar: str) -> bool:
    pass

def env_to_file(envvar: str, filepath: str) -> None:
    # try to get envvar value otherwise set the error into the file
    envvar_value = os.environ.get(envvar, f"INVALID ENVVAR: {envvar}")
    str_to_file(envvar_value, filepath)


def str_to_file(value: str, filepath: str) -> None:
    if value is None:
        value = "INVALID: Nothing provided"

    dest_filepath = Path(filepath).resolve()

    # make sure to create directory
    dest_filepath.parent.mkdir(parents=True, exist_ok=True)

    # create the file
    dest_filepath.write_text(value)
