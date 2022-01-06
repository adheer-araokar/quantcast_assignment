#!/bin/sh
valid="true"
while getopts d:f: flag
do
    case "${flag}" in
        d) date=${OPTARG};;
        f) filepath=${OPTARG};;
        *)
          echo "Usage: $0 [-d -f]"
          valid="false"
          ;;
    esac
done
if [[ $valid == "true" ]]
then
  python3 -m cookie_log_parser -d "$date" -f "$filepath"
fi
