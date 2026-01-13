
def maxpooling(arr: np.ndarray, size: int, stride: int) -> np.ndarray:
    """
    This function is used to perform maxpooling on the input array of 2D matrix(image)
    Args:
        arr: numpy array
        size: size of pooling matrix
        stride: the number of pixels shifts over the input matrix
    Returns:
        numpy array of maxpooled matrix
    Sample Input Output:
    >>> maxpooling([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2, 2)
    array([[ 6.,  8.],
           [14., 16.]])
    >>> maxpooling([[147, 180, 122],[241, 76, 32],[126, 13, 157]], 2, 1)
    array([[241., 180.],
           [241., 157.]])
    """
    arr = np.array(arr)
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("The input array is not a square matrix")
    i = 0
    j = 0
    mat_i = 0
    mat_j = 0


def avgpooling(arr: np.ndarray, size: int, stride: int) -> np.ndarray:
    """
    This function is used to perform avgpooling on the input array of 2D matrix(image)
    Args:
        arr: numpy array
        size: size of pooling matrix
        stride: the number of pixels shifts over the input matrix
    Returns:
        numpy array of avgpooled matrix
    Sample Input Output:
    >>> avgpooling([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 2, 2)
    array([[ 3.,  5.],
           [11., 13.]])
    >>> avgpooling([[147, 180, 122],[241, 76, 32],[126, 13, 157]], 2, 1)
    array([[161., 102.],
           [114.,  69.]])
    """
    arr = np.array(arr)
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("The input array is not a square matrix")
    i = 0
    j = 0
    mat_i = 0
    mat_j = 0


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


def random_chars(number_char: int) -> str:
    """
    Automatic generate random 32 characters.
    Get random string code: '7b7ad245cdff75241935e4dd860f3bad'
    >>> len(random_chars(32))
    32
    """
    assert number_char > 1, "The number of character should greater than 1"
    letter_code = ascii_lowercase + digits
    return "".join(random.choice(letter_code) for _ in range(number_char))


def show_frequency_response(filter_type: FilterType, samplerate: int) -> None:
    """
    Show frequency response of a filter

