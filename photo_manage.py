import os
import shutil
from datetime import datetime


class PhotosCopyYear:
    """Identifies images in a folder and copies them to another based upon
    extension and year created.

    Could be generalised for things other than year etcetera but not too
    important for this use case."""

    def __init__(self,
                 root_input,
                 extensions_photos=('jpeg', 'jpg', 'png', 'gif'),
                 extension_videos=('mp4', 'mpeg4')):
        self._root_input = root_input
        self._exts_images = extensions_photos
        self._exts_videos = extension_videos

    @staticmethod
    def retrieve_images(folder, extensions):
        """ Retrieve images from a given folder  """
        return [f for f in os.listdir(folder)
                if f.lower().endswith(extensions)]

    @staticmethod
    def _get_folder_output(namedate, construct):
        """Get an appropriate location based upon the year and content of the
        file (e.g. file extension)"""

        # This essentially loops through a dictionary where keys are a set of
        # file extensions. If matching, set output folder according to path in
        # value.
        for k, v in construct.items():
            if namedate[0].lower().endswith(k):
                return os.path.join(v[0], v[1].format(namedate[2]),
                                    namedate[0])
        else:
            raise RuntimeError("Object is of unsupported extension")

    @staticmethod
    def _write_file(infile, outfile, mkdir=True):
        """Create the output"""
        out_dir = os.path.split(outfile)[0]
        if mkdir and not os.path.exists(out_dir):
            os.makedirs(out_dir, exist_ok=True)
        elif not os.path.exists(out_dir):
            raise FileNotFoundError(
                f"Output directory {out_dir} does not exist")
        shutil.copy(infile, outfile)

    def copy_images(self, specs):

        # Determine image/video files in the folder
        imgs = self.retrieve_images(self._root_input,
                                    self._exts_images + self._exts_videos)

        # Get input path for each image (make separate list to above)
        imgs_input = map(lambda x: os.path.join(self._root_input, x), imgs)

        # On Windows, use date modified rather than created as copying files
        # resets their date whereas date modified stays the same
        imgs_dates = list(
            map(lambda x: datetime.fromtimestamp(
                os.path.getmtime(x)), imgs_input))

        # Extract year image was taken
        img_yrs = [str(yr.year) for yr in imgs_dates]
        imgs_namedate = list(zip(imgs,
                                 imgs_dates,
                                 img_yrs))

        # Create output path for each image
        imgs_output = [self._get_folder_output(x, specs)
                       for x in imgs_namedate]

        # Get each input and output path
        imgs_final = list(zip(imgs_input, imgs_output))

        # Perform the copying
        for img in imgs_final:
            self._write_file(img[0], img[1])
