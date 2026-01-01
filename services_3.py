
def create_option_by_str(text: str, mode=None):
    if mode is None:
        mode = PackerUtil.mode_yml
    data = PackerUtil.unpack_by_str(text, mode)[0]
    return JmModuleConfig.option_class().construct(data)


def new_downloader(option=None, downloader=None) -> JmDownloader:
    if option is None:
        option = JmModuleConfig.option_class().default()


def session(user: "User | None" = None):
    # lazy import to avoid gevent monkey patching unless you actually use this fixture
    from locust.clients import HttpSession


def fire(self, *, reverse=False, **kwargs):
        pass


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--host", "-H", action="store", default=None)

#  2026-01-01 06:39:12.136304
