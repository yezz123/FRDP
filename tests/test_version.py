from app import __version__


def test_version() -> None:
    assert __version__ == "2.0.0"
