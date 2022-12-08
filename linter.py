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
import sys
from glob import glob

import yaml
from jsonschema import validate
from jsonschema.exceptions import ValidationError

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
)
LOGGER = logging.getLogger(__name__)

UUID_SET = set()


def lint(file_path: str) -> dict:
    """
    Lint YAML file.

    :param file_path: directory path of the file
    :return: dictionary of YAML contents
    """
    with open('ecosystem_schema.yml', 'r') as stream:
        try:
            schema = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            LOGGER.error('Fail to load schema.', e)
    with open(file_path, 'r') as stream:
        try:
            yaml_dict = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            LOGGER.error(f'Fail to load file {yaml_dict}', e)

    validate(yaml_dict, schema)
    return yaml_dict


def check_uuid(yaml_dict: dict) -> None:
    """
    Verifies UUID is unique.

    :param yaml_dict: dictionary of YAML contents
    :return: None
    """
    yaml_id = yaml_dict['id']
    if yaml_id in UUID_SET:
        raise ValueError(f'Duplicate UUID {yaml_id}.')
    UUID_SET.add(yaml_id)


def main():
    files = glob('catalog/**/*.yml', recursive=True) + glob('catalog/**/*.yaml', recursive=True)

    failed = False
    pass_count = 0
    for file_path in files:
        try:
            yaml_dict = lint(file_path)
            check_uuid(yaml_dict)
            pass_count += 1
        except (ValidationError, ValueError) as e:
            LOGGER.error(e)
            failed = True

    LOGGER.info(f'PASS: {pass_count}/{len(files)}')

    if failed:
        LOGGER.info('FAIL')
        sys.exit(1)
    else:
        LOGGER.info('SUCCESS')
        sys.exit()


if __name__ == '__main__':
    main()
