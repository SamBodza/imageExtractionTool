import os
import shutil
from datetime import datetime
from alive_progress import alive_bar
from typing import List

from config_parser import get_config


def move_files(logger, fldr_path, paths: List[str]):
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
                    shutil.copy(src_p, dst_p)
                else:
                    pass
                logger.debug(f' copied {src_p} to {dst_p}')
            except Exception as e:
                logger.warning(f'could not move file {src_p}')
                pass
            finally:
                bar()
    time_taken = datetime.now() - init_time
    logger.info(f'finished at {time_taken}')
