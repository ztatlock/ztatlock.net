#!/usr/bin/env bash

# determine physical directory of this script
src="${BASH_SOURCE[0]}"
while [ -L "$src" ]; do
  dir="$(cd -P "$(dirname "$src")" && pwd)"
  src="$(readlink "$src")"
  [[ $src != /* ]] && src="$dir/$src"
done
MYDIR="$(cd -P "$(dirname "$src")" && pwd)"

cd "$MYDIR"

# header
cat <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
EOF

pref='https://ztatlock.net'
function page {
  cat <<EOF
  <url>
    <loc>$pref/$(basename "$1" .md).html</loc>
    <lastmod>$(date -r "$1" "+%Y-%m-%d")</lastmod>
  </url>
EOF
}

for p in *.md; do
  page "$p"
done

# footer
cat <<EOF
</urlset>
EOF
