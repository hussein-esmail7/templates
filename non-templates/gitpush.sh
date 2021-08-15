#!/bin/bash

# gitpush.sh
# Hussein Esmail
# Created: 2021 04 10
# Updated: 2021 04 10
# Description: This program is used to push files to Github faster.

set -e
path="$(pwd)"
file_to_find=".git"
shift 1
while [[ $path != / ]];
do
    find "$file_to_find" -maxdepth 1 -mindepth 1 "$path"
    # Note: if you want to ignore symlinks, use "$(realpath -s "$path"/..)"
    path="$(readlink -f "$path"/..)"
    echo "$path"
done

exit 0
