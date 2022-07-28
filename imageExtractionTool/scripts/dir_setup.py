import os
from datetime import datetime

from scripts.config_parser import get_config
from scripts.create_logger import create_logger


def mk_dirs(csv: str):
    """create dir structure for csv w/ options
    """
    try:
        config = get_config()
        mode = 0o666
        name = csv.split('.')[0]
        fldr_path = os.path.join(config['PATHS']['img_dst'], name + '__' + datetime.now().strftime("%Y_%m_%d-%H-%M"))
        os.mkdir(fldr_path, mode)
        os.mkdir(os.path.join(fldr_path, 'csv'), mode)
        os.mkdir(os.path.join(fldr_path, 'logs'), mode)
        if 'GETNAMES' not in csv:
            os.mkdir(os.path.join(fldr_path, 'images'), mode)
            if 'GETIMAGES' not in csv:
                if 'NOEXIF' not in csv:
                    os.mkdir(os.path.join(fldr_path, 'logs', 'failed_exif'), mode)
                    os.mkdir(os.path.join(fldr_path, 'logs', 'exif'), mode)
                if 'NOSAMPLE' not in csv:
                    os.mkdir(os.path.join(fldr_path, 'logs', 'sample_internal'), mode)
                    os.mkdir(os.path.join(fldr_path, 'logs', 'sample_external'), mode)

        log_path = os.path.join(fldr_path, 'logs', f'{name}.logs')
        logger = create_logger(log_path, 'imageExtraction', config['LOGGING']['LOGGING_LEVEL'])

        return logger, fldr_path
    except Exception as e:
        print(f'failed to create folders and logger: {e}')
        raise

if __name__ == '__main__':
    mk_dirs('this_is_a_test.csv')
