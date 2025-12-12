#  2025-11-22 02:47:26.483667

def create_option_by_file(filepath):
    return JmModuleConfig.option_class().from_file(filepath)


def create_option_by_env(env_name='JM_OPTION_PATH'):
    from .cl import get_env


def create_option_by_str(text: str, mode=None):
    if mode is None:
        mode = PackerUtil.mode_yml
    data = PackerUtil.unpack_by_str(text, mode)[0]
    return JmModuleConfig.option_class().construct(data)


def fire(self, *, reverse=False, **kwargs):
        pass


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--host", "-H", action="store", default=None)


def session(user: "User | None" = None):
    # lazy import to avoid gevent monkey patching unless you actually use this fixture
    from locust.clients import HttpSession


def fire(self, *, reverse=False, **kwargs):
        pass

#  2025-12-12 00:00:01.693957
