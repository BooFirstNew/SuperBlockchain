#  2025-10-07 00:00:01.595713

def show_phase_response(filter_type: FilterType, samplerate: int) -> None:
    """
    Show phase response of a filter


def show_frequency_response(filter_type: FilterType, samplerate: int) -> None:
    """
    Show frequency response of a filter


def process(self, sample: float) -> float:
        """
        Calculate y[n]


def main() -> None:
    """
    Get images list and annotations list from input dir.
    Update new images and annotations.
    Save images and annotations in output dir.
    """
    img_paths, annos = get_dataset(LABEL_DIR, IMG_DIR)
    for index in range(NUMBER_IMAGES):
        idxs = random.sample(range(len(annos)), 4)
        new_image, new_annos, path = update_image_and_anno(
            img_paths,
            annos,
            idxs,
            OUTPUT_SIZE,
            SCALE_RANGE,
            filter_scale=FILTER_TINY_SCALE,
        )

#  2025-11-07 00:00:01.810679
#  2025-11-09 15:01:38.789332
