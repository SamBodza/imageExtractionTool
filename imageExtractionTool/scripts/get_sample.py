# takes sample of images from a directory
import os
import shutil
import random
from alive_progress import alive_bar


def move_image_to_sample(logger, fldr_path, f):
    old_path = os.path.join(fldr_path, 'images', f)
    new_path_1 = os.path.join(fldr_path, 'logs', 'sample_internal', f)
    new_path_2 = os.path.join(fldr_path, 'logs', 'sample_external', f)

    if not os.path.exists(new_path_1):
        shutil.copy(old_path, new_path_1)
        logger.debug(f'copied file {f} into internal sample')
    else:
        logger.debug(f'file {f} already exists')
        pass

    if not os.path.exists(new_path_2):
        shutil.copy(old_path, new_path_2)
        logger.debug(f'copied file {f} into external sample')
    else:
        logger.debug(f'file {f} already exists')
        pass


def get_samples(logger, fldr_path, sample_size=1450):
    """get samples for ML validation
    """
    files = os.listdir(os.path.join(fldr_path, 'images'))
    if len(files) < sample_size:
        sample_size = len(files)
    random_files = random.choices(files, k=sample_size)
    tot = len(random_files)
    with alive_bar(tot, title='Choosing Samples Progress') as bar:
        for f in random_files:
            try:
                move_image_to_sample(logger, fldr_path, f)
            except Exception as e:
                logger.warning(f'failed to copy file {f}')
                pass
            finally:
                bar()
    logger.info(f"copied {len(os.listdir(os.path.join(fldr_path, 'logs', 'sample_internal')))} files into samples")
    logger.info(f"copied {len(os.listdir(os.path.join(fldr_path, 'logs', 'sample_external')))} files into samples")
