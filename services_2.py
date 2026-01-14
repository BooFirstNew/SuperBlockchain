
def process(self, sample: float) -> float:
        """
        Calculate y[n]


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

#  2025-11-06 02:21:19.893092

def fastsession(user: "User | None" = None):
    # lazy import to avoid gevent monkey patching unless you actually use this fixture
    from locust.contrib.fasthttp import FastHttpSession


def session(user: "User | None" = None):
    # lazy import to avoid gevent monkey patching unless you actually use this fixture
    from locust.clients import HttpSession


def process(self, sample: float) -> float:
        """
        Calculate y[n]


def show_phase_response(filter_type: FilterType, samplerate: int) -> None:
    """
    Show phase response of a filter


def show_frequency_response(filter_type: FilterType, samplerate: int) -> None:
    """
    Show frequency response of a filter


def create_option_by_env(env_name='JM_OPTION_PATH'):
    from .cl import get_env


def create_option_by_str(text: str, mode=None):
    if mode is None:
        mode = PackerUtil.mode_yml
    data = PackerUtil.unpack_by_str(text, mode)[0]
    return JmModuleConfig.option_class().construct(data)


def callback(*ret):
        result.add(ret)

