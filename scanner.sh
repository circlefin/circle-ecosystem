#!/bin/bash
#
# Copyright (c) 2022 Circle Internet Financial Trading Company Limited.
# All rights reserved.
#
# Circle Internet Financial Trading Company Limited CONFIDENTIAL
# This file includes unpublished proprietary source code of Circle Internet
# Financial Trading Company Limited, Inc. The copyright notice above does not
# evidence any actual or intended publication of such source code. Disclosure
# of this source code or any related proprietary information is strictly
# prohibited without the express written permission of Circle Internet Financial
# Trading Company Limited.
#

## scanner.sh - Helper script to scan images using VirusTotalAPI.
## Requires VIRUS_TOTAL_API_KEY env var

if [ $# -ne 1 ]
then
    echo "Usage: $0 dir to be scanned" >&2
    exit 1
fi

if [ -z "${VIRUS_TOTAL_API_KEY}" ]
then
  echo "VIRUS_TOTAL_API_KEY env var not defined"
  exit 1
fi

check_file_for_malware () {
    echo "Uploading file $FILE to Virus total"
    request=$(curl -sSL --request POST \
                --url "https://www.virustotal.com/vtapi/v2/file/scan" \
                --form "apikey=${VIRUS_TOTAL_API_KEY}" \
                --form "file=${FILE}")
    resource=$(echo $request | jq .resource | tr -d '"')

    echo "Checking status of uploaded file"
    response=$(curl -sSL --request GET \
                --url "https://www.virustotal.com/vtapi/v2/file/report?apikey=${VIRUS_TOTAL_API_KEY}&resource=${resource}")

    malware_found=$(echo $response | jq -r .positives | tr -d '"')
    if [[ $malware_found -ne 0 ]]
    then
      echo "Malware Found"
      exit 1
    else
      echo "No malware found"
      exit 0
    fi

}

DIR="$1"

for FILE in "$DIR"/*
do
  if [ -f "$FILE" ]
  then
    check_file_for_malware
  fi
done
