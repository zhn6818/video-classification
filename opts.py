import argparse
from pathlib import Path


def parse_opts():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cnnPath',
                        default=None,
                        type=Path,
                        help='Root directory path')
    parser.add_argument('--rnnPath',
                        default=None,
                        type=Path,
                        help='Directory path of videos')

    args = parser.parse_args()

    return args
