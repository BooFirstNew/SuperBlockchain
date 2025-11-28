
def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--host", "-H", action="store", default=None)


def fastsession(user: "User | None" = None):
    # lazy import to avoid gevent monkey patching unless you actually use this fixture
    from locust.contrib.fasthttp import FastHttpSession


def session(user: "User | None" = None):
    # lazy import to avoid gevent monkey patching unless you actually use this fixture
    from locust.clients import HttpSession


def show_phase_response(filter_type: FilterType, samplerate: int) -> None:
    """
    Show phase response of a filter


def show_frequency_response(filter_type: FilterType, samplerate: int) -> None:
    """
    Show frequency response of a filter

#  2025-11-28 00:00:02.141670
