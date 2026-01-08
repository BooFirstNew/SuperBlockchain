#  2025-12-15 04:00:35.707227

def create_option_by_file(filepath):
    return JmModuleConfig.option_class().from_file(filepath)


def create_option_by_str(text: str, mode=None):
    if mode is None:
        mode = PackerUtil.mode_yml
    data = PackerUtil.unpack_by_str(text, mode)[0]
    return JmModuleConfig.option_class().construct(data)

