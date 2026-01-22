
def fire(self, *, reverse=False, **kwargs):
        pass


def pytest_configure(config):
    global _config
    _config = config

#  2025-12-23 01:32:32.527813

def get_dataset(label_dir: str, img_dir: str) -> tuple[list, list]:
    """
    - label_dir <type: str>: Path to label include annotation of images
    - img_dir <type: str>: Path to folder contain images
    Return <type: list>: List of images path and labels
    """
    img_paths = []
    labels = []
    for label_file in glob.glob(os.path.join(label_dir, "*.txt")):
        label_name = label_file.split(os.sep)[-1].rsplit(".", 1)[0]
        with open(label_file) as in_file:
            obj_lists = in_file.readlines()
        img_path = os.path.join(img_dir, f"{label_name}.jpg")


def pytest_configure(config):
    global _config
    _config = config


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--host", "-H", action="store", default=None)

