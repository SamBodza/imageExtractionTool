import os

from config_parser import get_config
from get_exif import get_EXIF


def remove_custom_EXIF(logger, fldr_path):
    try:
        config = get_config()['EXIF']['config']
        command = rf"exiftool -config {config} -all= {os.path.join(fldr_path, 'logs', 'failed_exif')}"
        os.system(command)
        logger.debug(f'removed EXIF data for {fldr_path}')
    except Exception as e:
        logger.error(f"couldn't use custom exif config to remove data: {e}")


def get_tags(logger, fldr_path):
    try:
        with open(os.path.join(fldr_path, 'logs', 'exif_out2.txt')) as f:
            contents = f.read()
        set_tags = []
        files = contents.split('========')
        tot = len(files)
        with alive_bar(tot, title='Get Tags Progress') as bar:
            for file in files[1:-1]:
                try:
                    data = file.splitlines()
                    if len(data) != 24:
                        for d in data:
                            tags = d.split(':')
                            tag = tags[0]
                            if tag not in set_tags:
                                set_tags.append(tag)
                except Exception as e:
                    logger.warning(f'failed on file {data[0]}: {e}')
                finally:
                    bar()
    except Exception as err:
        logger.critical(f'unable to parse exif: {err}')

    try:
        with open(os.path.join(fldr_path, 'logs', 'exif_to_check.txt'), 'w') as f:
            tot = len(set_tags)
            with alive_bar(tot, title='Write tags Progress') as bar:
                for item in set_tags:
                    if fldr_path not in item:
                        f.write("%s\n" % item)
                    bar()
    except Exception as e:
        logger.critical(f'unable to write tags to file: {e}')


def exif_second_pass(logger, fldr_path):
    remove_custom_EXIF(logger, fldr_path)
    get_EXIF(logger, fldr_path, os.path.join('logs', 'failed_exif'), '2')
    get_tags(logger, fldr_path)
