# main file for imageExtractionTool
import os

from scripts.process_csv import process
from scripts.config_parser import get_config


if __name__ == '__main__':
    paths_config = get_config()['PATHS']
    csvs = [f for f in os.listdir(paths_config['csv_input']) if '.csv' in f]
    if csvs:
        for csv in csvs:
            process(csv)
