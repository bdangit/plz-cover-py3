import os
from pathlib import Path

import pyfakefs
import pytest

from envutil.envutil import envutil


@pytest.fixture()
def setup_envvar_WOOF():
    # setup
    os.environ["WOOF"] = "this is how I bark"

    yield os.environ["WOOF"]

    # teardown
    del os.environ["WOOF"]


def test_create_file_with_existing_envvar(fs, setup_envvar_WOOF):
    envvar = "WOOF"
    filepath = "some/place/file"

    envutil.env_to_file(envvar, filepath)
    assert Path(filepath).read_text() == "this is how I bark"


def test_create_file_with_nonexisting_envvar(fs):
    envvar = "WOOF"
    filepath = "some/place/file"

    envutil.env_to_file(envvar, filepath)
    assert Path(filepath).read_text() == "INVALID ENVVAR: WOOF"


def test_create_file_at_root(fs, setup_envvar_WOOF):
    envvar = "WOOF"
    filepath = "/this/is/root"

    envutil.env_to_file(envvar, filepath)
    assert Path(filepath).read_text() == "this is how I bark"


def test_create_file_with_existing_parent_dirs(fs, setup_envvar_WOOF):
    envvar = "WOOF"
    filepath = "/this/dir/exists"

    # create up to `/this/dir`
    fs.create_dir(os.path.dirname(filepath))
    assert Path(filepath).parent.exists()

    envutil.env_to_file(envvar, filepath)
    assert Path(filepath).read_text() == "this is how I bark"


def test_create_file_with_existing_dest_filepath(fs, setup_envvar_WOOF):
    envvar = "WOOF"
    filepath = "/this/file/exists"

    # create everything include file
    fs.create_file(filepath, contents="it exists")
    assert Path(filepath).read_text() == "it exists"

    envutil.env_to_file(envvar, filepath)
    assert Path(filepath).read_text() == "this is how I bark"
