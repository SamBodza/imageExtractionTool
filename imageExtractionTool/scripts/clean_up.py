import os
import shutil

from config_parser import get_config


def clean_up(logger, fldr_path, csv):
    """clean up input files
    """
    config = get_config()
    csv_path = os.path.join(config['PATHS']['csv_input'], csv)
    new_csv_path = os.path.join(fldr_path, 'csv', csv)
    try:
        shutil.move(csv_path, new_csv_path)
    except Exception as e:
        logger.warning(f'failed at cleaning up')
