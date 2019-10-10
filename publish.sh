#!/usr/bin/env bash

# determine physical directory of this script
src="${BASH_SOURCE[0]}"
while [ -L "$src" ]; do
  dir="$(cd -P "$(dirname "$src")" && pwd)"
  src="$(readlink "$src")"
  [[ $src != /* ]] && src="$dir/$src"
done
MYDIR="$(cd -P "$(dirname "$src")" && pwd)"

rsync \
  --verbose \
  --recursive \
  --delete \
  --force \
  "$MYDIR/site/" ztatlock@tatlock.net:/var/www/tatlock.net
