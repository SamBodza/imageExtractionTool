import os
import shutil
from alive_progress import alive_bar


def get_EXIF(logger, fldr_path):
    """scrape EXIf data from moved JPGs
    """
    try:
        command = rf"exiftool {os.path.join(fldr_path, 'images')} > {os.path.join(fldr_path, 'logs', 'exif', 'exif_out.txt')}"
        os.system(command)
    except Exception as err:
        logger.error(f'unable to get EXIF data: {err}')


def find_failed_exif(logger, fldr_path):
    """parse scraped EXIF data
    """
    try:
        get_EXIF(logger, fldr_path)
        with open(os.path.join(fldr_path, 'logs', 'exif', 'exif_out.txt')) as f:
            contents = f.read()

        files = contents.split('========')
        tot = len(files)
        with alive_bar(tot, title='Parse Progress') as bar:
            for file in files[1:-1]:
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
        try:
            _ = files[-1]
            data = file.splitlines()
            if len(data) != 24:
                logger.error(f'EXIF error found in {data[0][1:]}, had {len(data)} tags')
                new_path = os.path.join(fldr_path, 'logs', 'failed_exif', data[0][1:].split('/')[-1])
                shutil.move(data[0][1:], new_path)
                logger.debug(f'moved {data[0][1:]} to {new_path}')
        except Exception as e:
            logger.error(f'EXIF error found in {data[0][1:]} : {e}')

    except Exception as err:
        logger.error(f'unable to parse exif: {err}')
