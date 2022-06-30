import os
import shutil
from alive_progress import alive_bar
from get_exif import get_EXIF


def find_failed_exif(logger, fldr_path):
    """parse scraped EXIF data for images
    with more or less than 24 lines"""
    try:
        get_EXIF(logger, fldr_path, 'images')
        with open(os.path.join(fldr_path, 'logs', 'exif', 'exif_out.txt')) as f:
            contents = f.read()

        files = contents.split('========')
        tot = len(files)
        with alive_bar(tot, title='Parse Progress') as bar:
            for file in files[1:]:
                try:
                    data = file.splitlines()
                    if len(data) != 24:
                        logger.error(f'EXIF error found in {data[0][1:]}, had {len(data)} tags')
                        new_path = os.path.join(fldr_path, 'logs', 'failed_exif', data[0][1:].split('/')[-1])
                        shutil.move(data[0][1:], new_path)
                except Exception as e:
                    logger.error(f'failed to get EXIF: {e}')
                finally:
                    bar()
    except Exception as err:
        logger.error(f'unable to parse exif: {err}')
