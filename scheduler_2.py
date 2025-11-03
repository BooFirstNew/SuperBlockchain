
def fire(self, *, reverse=False, **kwargs):
        pass


def session(user: "User | None" = None):
    # lazy import to avoid gevent monkey patching unless you actually use this fixture
    from locust.clients import HttpSession

