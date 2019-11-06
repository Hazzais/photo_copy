"""
Ideas:
- get contents of a directory
- get photos and videos
- get their dates
- copy to folder based on datetime
- find duplicates
"""
import os
import argparse

from photo_manage import PhotosCopyYear


def dir_path(string):
    # See: https://stackoverflow.com/questions/38834378/
    # path-to-a-directory-as-argparse-argument
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


parser = argparse.ArgumentParser()
parser.add_argument('path',
                    type=dir_path,
                    help='The path where images and videos are to be copied '
                         'from')
parser.add_argument('--out-root-images',
                    type=str,
                    default='images/',
                    help='The path where images are to be copied to. Will be '
                         'created if it does not exist.')
parser.add_argument('--out-root-videos',
                    type=str,
                    default='videos/',
                    help='The path where videos are to be copied to. Will be '
                         'created if it does not exist.')

args = parser.parse_args()

EXTENSIONS_IMAGES = ('jpeg', 'jpg', 'png', 'gif')
EXTENSIONS_VIDEOS = ('mp4', 'mpeg4')

OUTPUT_SPECS = {EXTENSIONS_IMAGES: args.out_root_images,
                EXTENSIONS_VIDEOS: args.out_root_videos}

if __name__ == '__main__':
    pc = PhotosCopyYear(args.path)
    pc.copy_images(OUTPUT_SPECS)
