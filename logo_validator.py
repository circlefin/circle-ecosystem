# Copyright (c) 2022 Circle Internet Financial Trading Company Limited.
# All rights reserved.
#
# Circle Internet Financial Trading Company Limited CONFIDENTIAL
# This file includes unpublished proprietary source code of Circle Internet
# Financial Trading Company Limited, Inc. The copyright notice above does not
# evidence any actual or intended publication of such source code. Disclosure
# of this source code or any related proprietary information is strictly
# prohibited without the express written permission of Circle Internet
# Financial Trading Company Limited.

import logging
import os
import sys
from glob import glob

from PIL import Image
from svgpathtools import svg2paths2

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
)
LOGGER = logging.getLogger(__name__)

ACCEPTABLE_FILE_EXTENSIONS = ['.jpg', '.png', '.svg']
IMAGE_SIZE = 5 * 1024 * 1024


class ValidationError(Exception):
    """Exception raised for invalid logos."""
    pass


def validate_logo(logo_path: str) -> None:
    """
    Validate a logo to ensure it follows the following requirements:
        1. Acceptable File Types: .jpg, .png, .svg
        2. Max File Size: 5 MB
        2. Image Size: 200 x 200 pixels
        3. Aspect Ratio: 1:1 (square)

    :param logo_path: path of the logo
    :return: boolean whether the logo passes requirements
    """

    # 1. Check the file type
    file_ext_index = logo_path.rfind('.')
    file_ext = logo_path[file_ext_index:]
    if file_ext not in ACCEPTABLE_FILE_EXTENSIONS:
        raise ValidationError(f'Invalid file type {file_ext} for {logo_path}.')

    # 2. Check the file size
    size = os.path.getsize(logo_path)
    if size > IMAGE_SIZE:
        raise ValidationError(f'Invalid file size {(size / (1024 * 1024)):.2f} MB for {logo_path}.')

    # 3. Check the image size and ratio
    if file_ext == '.svg':
        _, __, svg_attributes = svg2paths2(logo_path)
        width, height = int(svg_attributes['width']), int(svg_attributes['height'])
    else:
        im = Image.open(logo_path)
        width, height = im.size

    if width != 200 or height != 200:
        raise ValidationError(f'Invalid image size {width}x{height} for {logo_path}.')


def main():
    logos = glob('catalog/**/logos/*', recursive=True)

    failed = False
    pass_count = 0
    for logo_path in logos:
        try:
            validate_logo(logo_path)
            pass_count += 1
        except ValidationError as e:
            LOGGER.error(e)
            failed = True

    LOGGER.info(f'PASS: {pass_count}/{len(logos)}')

    if failed:
        LOGGER.info('FAIL')
        sys.exit(1)
    else:
        LOGGER.info('SUCCESS')
        sys.exit()


if __name__ == '__main__':
    main()
