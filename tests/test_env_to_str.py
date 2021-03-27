import os
import pytest

from envutil.envutil import envutil

@pytest.fixture()
def setup_envvar_WOOF():
    # setup
    os.environ["WOOF"] = "this is how I bark"

    yield os.environ["WOOF"]

    # teardown
    del os.environ["WOOF"]


def test_valid_str(setup_envvar_WOOF):
    envvar = "WOOF"
    assert envutil.env_to_str(envvar) == "this is how I bark"


def test_nonexisting_envvar():
    envvar = "WOOF"
    assert envutil.env_to_str(envvar) == ""