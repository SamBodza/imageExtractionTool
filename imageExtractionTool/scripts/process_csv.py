from scripts.dir_setup import mk_dirs
from scripts.get_file_names import get_file_names
from scripts.get_file_paths import get_file_paths
from scripts.image_paths_to_csv import image_paths_to_csv
from scripts.move_files_multithreaded2 import move_files
from scripts.get_sample import get_samples
from scripts.find_failed_exif import find_failed_exif
from scripts.clean_known_exif import exif_second_pass
from scripts.clean_up import clean_up


def get_names_only(csv: str):
    """get paths to images from csv"""
    logger, fldr_path = mk_dirs(csv)
    logger.info('create directories and logger')
    names = get_file_names(logger, csv)
    logger.info('got file names from CSV')
    paths = get_file_paths(logger, names)
    logger.info('got file paths from CSV')
    image_paths_to_csv(logger, paths)
    logger.info('paths written to CSV')

    return logger, fldr_path, paths


def get_images_only(csv: str):
    """pull copy of images from csv"""
    logger, fldr_path, paths = get_names_only(csv)
    logger.info('moving files')
    move_files(logger, fldr_path, paths)

    return logger, fldr_path


def get_sample_only(csv: str):
    """Gets copy of images and takes sample without parsing exif"""
    logger, fldr_path = get_images_only(csv)
    logger.info('taking sample')
    get_samples(logger, fldr_path)

    return logger, fldr_path


def get_exif_only(csv: str):
    """Gets copy of images and parses exif without taking sample"""
    logger, fldr_path = get_images_only(csv)
    logger.info('finding failed exif')
    find_failed_exif(logger, fldr_path)
    logger.info('exif_second_path')
    exif_second_pass(logger, fldr_path)

    return logger, fldr_path


def full_process(csv: str):
    logger, fldr_path = get_exif_only(csv)
    logger.info('getting samples')
    get_samples(logger, fldr_path)
    logger.info('cleaning up')
    clean_up(logger, fldr_path, csv)


def process(csv: str):
    """Process CSV"""
    if 'GETNAMES' in csv:
        logger, fldr_path = get_names_only(csv)
        clean_up(logger, fldr_path, csv)
    elif 'GETIMAGES' in csv:
        logger, fldr_path = get_images_only(csv)
        clean_up(logger, fldr_path, csv)
    elif 'GETEXIF' in csv:
        logger, fldr_path = get_exif_only(csv)
        clean_up(logger, fldr_path, csv)
    elif 'GETSAMPLE' in csv:
        logger, fldr_path = get_sample_only(csv)
        clean_up(logger, fldr_path, csv)
    else:
        full_process(csv)
