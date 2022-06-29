import os

from config_parser import

def remove_EXIF(logger, fldr_path):
    try:
        command  = rf"exiftool -config {} -all= {os.path.join(fldr_path, 'logs', 'failed_exif')}"
        os.system(command)
        logger.debug(f'removed EXIF data for {fldr_path}')
    except Exception as e:
        pass