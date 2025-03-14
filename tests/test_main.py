from pathlib import Path

import pytest
from decrippter2_data.main import SchemaManager, main


@pytest.fixture
def sm() -> SchemaManager:
    return SchemaManager()


@pytest.fixture
def example() -> Path:
    return Path(__file__).parent.parent.joinpath("tests/examples/valid.json")


@pytest.fixture
def example_invalid() -> Path:
    return Path(__file__).parent.parent.joinpath("tests/examples/invalid.json")


def test_init_sm(sm):
    assert isinstance(sm, SchemaManager)


def test_read_json(sm, example):
    assert isinstance(sm.read_json(example), dict)


def test_validate_schema(sm, example):
    assert sm.validate_schema(example) is None


def test_main_valid(example):
    with pytest.raises(SystemExit) as e:
        main([example])
    assert e.type == SystemExit
    assert e.value.code == 0


def test_main_invalid(example_invalid):
    with pytest.raises(SystemExit) as e:
        main([example_invalid])
    assert e.type == SystemExit
    assert e.value.code == 1
