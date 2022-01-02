#!/bin/sh
while getopts d:f: flag
do
    case "${flag}" in
        d) date=${OPTARG};;
        f) filepath=${OPTARG};;
    esac
done
python3 -m cookie_log_parser -d $date -f $filepath

