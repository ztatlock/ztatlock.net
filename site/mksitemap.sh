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
SITE='https://ztatlock.net'

# header
cat <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>$SITE/</loc>
    <lastmod>$(date -r "index.md" "+%Y-%m-%d")</lastmod>
  </url>
EOF

function page {
  cat <<EOF
  <url>
    <loc>$SITE/$(basename "$1" .md).html</loc>
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
