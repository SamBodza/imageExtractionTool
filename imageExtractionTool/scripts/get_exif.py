import os


def get_EXIF(logger, fldr_path, path, suffix=''):
    """scrape EXIf data from moved JPGs
    """
    try:
        command = rf"exiftool {os.path.join(fldr_path, path)} > {os.path.join(fldr_path, 'logs', 'exif', f'exif_out{suffix}.txt')}"
        os.system(command)
    except Exception as err:
        logger.error(f'unable to get EXIF data: {err}')
