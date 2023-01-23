import os
from shutil import copy
from datetime import datetime
from alive_progress import alive_bar
from typing import List
from concurrent.futures import ProcessPoolExecutor
import sys
import subprocess

from scripts.config_parser import get_config


def copy_files_old(logger, tot, paths, dst_path, src_path):
    with alive_bar(tot, title='Image Move Progress') as bar:
        for path in paths:
            try:
                src_p = os.path.join(src_path, path)
                dst_p = os.path.join(dst_path, 'images', path.split('/')[-1])
                if not os.path.exists(dst_p):
                    copy(src_p, dst_p)
                else:
                    pass
                logger.debug(f' copied {src_p} to {dst_p}')
            except Exception as e:
                logger.warning(f'could not move file {src_p}')
                pass
            finally:
                bar()


def copy_files(logger, paths, dst_path, src_path):
    for path in paths:
        try:
            src_p = os.path.join(src_path, path)
            dst_p = os.path.join(dst_path, 'images', path.split('/')[-1])
            if not os.path.exists(dst_p):
                subprocess.Popen(['cp', src_p, dst_p], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            logger.debug(f' copied {src_p} to {dst_p}')
        except Exception as e:
            logger.warning(f'could not move file {src_p}')
            pass


def move_files_old(logger, fldr_path, paths: List[str]):
    """move images from source to new folder
    """
    path_config = get_config()['PATHS']
    init_time = datetime.now()
    tot = len(paths)
    logger.info(f'started move at {init_time} with {tot} images')
    with alive_bar(tot, title='Image Move Progress') as bar:
        for path in paths:
            try:
                src_p = os.path.join(path_config['img_src'], path)
                dst_p = os.path.join(fldr_path, 'images', path.split('/')[-1])
                if not os.path.exists(dst_p):
                    copy(src_p, dst_p)
                    logger.debug(f' copied {src_p} to {dst_p}')
            except Exception as e:
                logger.warning(f'could not move file {src_p}')
                pass
            finally:
                bar()
    time_taken = datetime.now() - init_time
    logger.info(f'finished at {time_taken}')


def move_files(logger, fldr_path, paths: List[str]):
    """move images from source to new folder
    """
    path_config = get_config()['PATHS']
    src_path = path_config['img_src']
    init_time = datetime.now()
    tot = len(paths)
    logger.info(f'started move at {init_time} with {tot} images')
    n_workers = 8
    chunksize = round(tot / n_workers)
    with ProcessPoolExecutor(n_workers) as exe:
        # split the copy operations into chunks
        for i in range(0, tot, chunksize):
            # select a chunk of filenames
            filenames = paths[i:(i + chunksize)]

            # submit the batch copy task
            _ = exe.submit(copy_files, logger,filenames, fldr_path, src_path)

    time_taken = datetime.now() - init_time
    logger.info(f'finished at {time_taken}')
