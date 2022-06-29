import os
import re
import pandas as pd
from typing import List

from config_parser import get_config


def get_file_names(logger, csv: str) -> List[str]:
    """read in input CSV & get file names
    """
    path_config = get_config()['PATHS']
    csv_path = os.path.join(path_config['csv_input'], csv)
    try:
        df = pd.read_csv(csv_path, header=None, names=['file_name'])
        logger.debug(f'read in csv')
    except Exception as e:
        logger.critical(f'could not read {csv_path} : {e}')
        raise

    if re.match('^filestorage://retinal', df['file_name'][1]):
        try:
            df['file_name'] = df['file_name'].map(lambda x: f"{x.split('/')[-1].split('?')[0]}_Full.jpg")
            logger.debug(f"example row {df['file_name'][0]}")
            return df['file_name']
        except Exception as e:
            logger.critical(f'could not convert file names: {e}')
            raise

    elif re.match('Img_[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12}_Full.jpg',
                  df['file_name'][1]):
        logger.debug(f"example row {df['file_name'][0]}")
        return df['file_name']

    elif re.match('Img_[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12}',
                  df['file_name'][1]):
        df['file_name'] = df['file_name'].map(lambda x: str(x) + '_Full.jpg')
        logger.debug(f"example row {df['file_name'][0]}")
        return df['file_name']

    elif re.match('[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12}', df['file_name'][1]):
        df['file_name'] = df['file_name'].map(lambda x: 'Img_' + str(x) + '_Full.jpg')
        logger.debug(f"example row {df['file_name'][0]}")
        return df['file_name']

    else:
        err = 'CSV file_names not in suitable format'
        logger.error(err)
        raise ValueError(err)
