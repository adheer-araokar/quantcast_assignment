from pathlib import Path
import pytest


@pytest.fixture
def get_source_dir():
    return Path(__file__).parent / "data/source/"


@pytest.fixture
def get_file_path(get_source_dir):
    def _create(filename: str):
        return str(get_source_dir / filename)

    return _create
