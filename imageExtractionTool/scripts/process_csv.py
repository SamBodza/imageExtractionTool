from setup import mk_dirs
from get_file_names import get_file_names
from get_file_paths import get_file_paths
from image_paths_to_csv import image_paths_to_csv
from move_files import move_files
from get_sample import get_samples
from find_failed_exif import find_failed_exif
from clean_known_exif import exif_second_pass


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
    move_files(logger, fldr_path, paths)

    return logger, fldr_path


def get_sample_only(csv: str):
    """Gets copy of images and takes sample without parsing exif"""
    logger, fldr_path = get_images_only(csv)
    get_samples(logger, fldr_path)

    return logger, fldr_path


def get_exif_only(csv: str):
    """Gets copy of images and parses exif without taking sample"""
    logger, fldr_path = get_images_only(csv)
    find_failed_exif(logger, fldr_path)
    exif_second_pass(logger, fldr_path)

    return logger, fldr_path


def full_process(csv: str):
    logger, fldr_path = get_exif_only(csv)
    get_samples(logger, fldr_path)


def process(csv: str):
    """Process CSV"""
    if 'GETNAMES' in csv:
        get_names_only(csv)
    elif 'GETIMAGES' in csv:
        get_images_only(csv)
    elif 'GETEXIF' in csv:
        get_exif_only(csv)
    elif 'GETSAMPLE' in csv:
        get_sample_only(csv)
    else:
        full_process(csv)
