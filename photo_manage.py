import os
import shutil
from datetime import datetime
from abc import abstractmethod


in_folder = r'D:\Pictures\2016 to 2017'
out_folder_photos_root = r'D:\Pictures\test'
out_folder_photos = 'photos_{}'
out_folder_videos_root = r'D:\Pictures\test_v'
out_folder_videos = 'videos_{}'

EXTENSIONS_IMAGES = ('jpeg', 'jpg', 'png', 'gif')
EXTENSIONS_VIDEOS = ('mp4', 'mpeg4')

OUTPUT_SPECS = {EXTENSIONS_IMAGES: [out_folder_photos_root, out_folder_photos],
                EXTENSIONS_VIDEOS: [out_folder_videos_root, out_folder_videos]}


class ManagePhotos:

    def __init__(self, root_input, output_exts,
                 extensions_photos=('jpeg', 'jpg', 'png', 'gif'),
                 extension_videos=('mp4', 'mpeg4')):
        self._root_input = root_input
        self._output_exts = output_exts
        self._exts_images = extensions_photos
        self._exts_images = extension_videos

    @staticmethod
    def retrieve_images(folder, extensions):
        """ Retrieve images from a given folder  """
        return [f for f in os.listdir(folder)
                if f.lower().endswith(extensions)]

    def copy_images(self):




def retrieve_images(folder, extensions):
    """ Retrieve images from a given folder  """
    base_images = [f for f in os.listdir(folder)
                   if f.lower().endswith(extensions)]
    return base_images


def get_folder_output(namedate, construct):
    for k, v in construct.items():
        if namedate[0].lower().endswith(k):
            return os.path.join(v[0], v[1].format(namedate[2]), namedate[0])
    else:
        raise RuntimeError("Object is of unsupported extension")


def write_file(infile, outfile, mkdir=True):
    out_dir = os.path.split(outfile)[0]
    print(out_dir)
    if mkdir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)
    elif not os.path.exists(out_dir):
        raise FileNotFoundError(f"Output directory {out_dir} does not exist")
    #shutil.copy(infile, outfile)


imgs = retrieve_images(in_folder, EXTENSIONS_IMAGES + EXTENSIONS_VIDEOS)
imgs_input = map(lambda x: os.path.join(in_folder, x), imgs)
imgs_dates = list(map(lambda x: datetime.fromtimestamp(os.path.getmtime(
    os.path.join(in_folder, x))), imgs))
img_yrs = [str(yr.year) for yr in imgs_dates]
imgs_namedate = list(zip(imgs,
                         imgs_dates,
                         img_yrs))
imgs_output = [get_folder_output(x, OUTPUT_SPECS) for x in imgs_namedate]

imgs_final = list(zip(imgs, imgs_input, imgs_output))


tmp = [x[0] for x in imgs_final if x[0].endswith('mp4')]

for img in imgs_final:
    write_file(img[1], img[2])





class RemoveDuplicates(ManagePhotos):
    pass


class TagPhotos(ManagePhotos):
    pass

