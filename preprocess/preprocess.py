import json
import os


def preprocess():
    data_key = ['test', 'train', 'val']
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, './data')

