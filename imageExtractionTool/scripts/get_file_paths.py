import os
import psycopg2
import pandas as pd
from typing import List

from jpgPostgresConfig.conn import SQLconfig
from scripts.config_parser import get_config


def extract_path(logger, row):
    """get paths for file names found
    """
    try:
        path = os.path.join(get_config()['PATHS']['img_dst'], row.split('\\')[-2], row.split('\\')[-1])
        logger.debug(f'got path {path}')
        return path
    except Exception as e:
        logger.warning(f'failed to get path for {row}')
        pass


def connect_single(logger, SQLconfig, sql, get=False):
    """ run single query
    """
    conn = None
    data = None

    try:
        conn = psycopg2.connect(dbname=SQLconfig['dbname'],
                                host=SQLconfig['host'],
                                user=SQLconfig['user'],
                                password=SQLconfig['password'],
                                port=SQLconfig['port']
                                )
        cur = conn.cursor()
        cur.execute(sql)
        if get:
            data = [row for row in cur.fetchall()]

    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(f'failed to connect to db: {error}')
        raise Exception(f'{error}')

    finally:
        if conn:
            cur.close()
            conn.close()
        return data


def get_file_paths_backup(logger, data: List[str]) -> List[str]:
    """failover to CSV for path names
    """
    try:
        db_config = get_config()['DB']
        df = pd.read_csv(db_config['db_backup'], names=['folder_name', 'file_name'], header=None)
        logger.debug(f'read in CSV for failover')
        mask = df['file_name'].isin(list(set(data)))
        logger.debug(f'got set for for failover')
        df = df.loc[mask]
        df.reset_index()
        paths = []
        for row in zip(*df.to_dict('list').values()):
            paths.append(os.path.join(row[0], row[1]))
            logger.debug(f'got row {row} for failover')

        return paths

    except Exception as e:
        logger.critical(f'unable to access backup DB')


def get_file_paths(logger, data: List[str]) -> List[str]:
    """get path names from postgres DB w/ fail over to CSV
    """
    try:
        arg = ",".join(("'%s'" % x for x in data))
        arg_str = f'({arg})'
        sql = f"""
        SELECT full_file_name
            FROM custom.onprem_jpg_stock_edited
        WHERE file_name IN {arg_str}
        """
        # logger.debug(f'query example: {sql}')
        paths = [p for p in connect_single(logger, SQLconfig, sql, get=True)]
        logger.debug(f' example path {paths[0]}')
        if len(paths) > 1:
            return paths
        else:
            raise Exception
    except Exception as e:
        logger.error(f'was unable to get paths: {e}')
        logger.error(f'trying backup DB')
        try:
            paths = get_file_paths_backup(logger, data)
            return list(set(paths))
        except Exception as e:
            logger.critical(f'failed to get backup DB')
            raise
