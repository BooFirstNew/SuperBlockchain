
def create_option_by_str(text: str, mode=None):
    if mode is None:
        mode = PackerUtil.mode_yml
    data = PackerUtil.unpack_by_str(text, mode)[0]
    return JmModuleConfig.option_class().construct(data)


def create_option_by_file(filepath):
    return JmModuleConfig.option_class().from_file(filepath)

#  2025-10-24 00:00:01.477674
#  2025-11-18 03:30:42.726360
#  2025-12-02 05:46:08.079556
