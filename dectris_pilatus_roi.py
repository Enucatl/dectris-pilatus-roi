import click
import numpy as np

@click.command()
@click.argument("file", type=click.Path(exists=True, writable=True))
@click.option("--roi", "roi",
              type=int,
              nargs=4,
              default=(0, 0, 619, 487),
              help="tuple (min_x, min_y, max_x, max_y)")
def crop(file, roi):
    """Crop the image in the raw file file_name to the roi and save it back

    :file_name: string
    :roi: tuple (min_x, min_y, max_x, max_y)

    """
    input_array = np.fromfile(file, dtype=np.int32).reshape((619, 487))
    input_array[roi[0]:roi[2], roi[1]:roi[3]].tofile(file)
