import os
import pandas as pd
from datetime import datetime
from typing import List
from concurrent.futures import ProcessPoolExecutor
import subprocess
from uuid import uuid1

from scripts.config_parser import get_config


def save_tmp_file(df):
    id = str(uuid1())
    if not os.path.exists(f'./tmp_{id}.csv'):
        df.to_csv(f'/tmp/tmp_{id}.csv')

        return f'/tmp/tmp_{id}.csv'
    else:
        save_tmp_file(df)


def copy_files(paths, dst_path, src_path):
    try:
        src_p = [os.path.join(src_path, path) for path in paths]
        dst_p = [os.path.join(dst_path, 'images', path.split('/')[-1]) for path in paths if
                 not os.path.exists(os.path.join(dst_path, 'images', path.split('/')[-1]))]
        df = pd.DataFrame(list(zip(src_p, dst_p)))
        csv_path = save_tmp_file(df)

        subprocess.Popen(f'/home/curator/Dev/toolsProd/csvcopier < {csv_path}', stdout=subprocess.PIPE, stderr=subprocess.PIPE).read()
    except Exception as e:
        print(e)


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
            _ = exe.submit(copy_files, filenames, fldr_path, src_path)

    time_taken = datetime.now() - init_time
    logger.info(f'finished at {time_taken}')
