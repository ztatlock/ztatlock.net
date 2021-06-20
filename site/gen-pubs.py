#!/usr/bin/env python3

import json
import os.path

PUBS_JSON = '../pubs.json'
TEMPLATE = 'publications.template'
PUBS_MD = 'publications.md'

def toggle_link(txt, tgt):
    elts = [ f"[{txt}](#{tgt}){{"
           , f"aria-controls='{tgt}' "
           , f"data-toggle='collapse' "
           , f"role='button' "
           , f"aria-expanded='false'"
           , f"}}" ]
    return ''.join(elts)

def pub_entry(pub):
    # format authors
    authors = ', '.join(['[' + x + ']' for x in pub['authors']])

    # format links
    elts = []
    for k in pub['links']:
        if k == 'abstract':
            elts.append(toggle_link(k, "abs-" + pub['id']))
        elif k == 'bib':
            elts.append(toggle_link(k, "bib-" + pub['id']))
        else:
            elts.append(f"[{k}]({pub['links'][k]})")
    links = ' &nbsp;\n  '.join(elts)

    # add award if any
    if 'award' in pub:
        links += f"\n  <br> [{pub['award']}]{{.pub-award}}"

    return f'''
<!-- {pub['date']} -->

::: {{#pub-{pub['id']} .anchor}}
::: {{.pub-entry}}
  **{pub['title']}** \\
  {authors} \\
  {pub['venue']} {pub['year']} \\
  {links}
:::
:::
'''

def abs_card(pub):
    card = ''
    if 'abstract' in pub['links']:
        path = os.path.join('stage', pub['links']['abstract'])
        with open(path, 'r') as f:
            abstract = f.read()
        card = f'''
::: {{#abs-{pub['id']} .collapse}}
::: {{.card .card-body .abs-card}}

{abstract}
:::
:::
'''
    return card

def bib_card(pub):
    card = ''
    if 'bib' in pub['links']:
        path = os.path.join('stage', pub['links']['bib'])
        with open(path, 'r') as f:
            bib = f.read()
        card = f'''
::: {{#bib-{pub['id']} .collapse}}
::: {{.card .card-body .bib-card}}
```

{bib}
```
:::
:::
'''
    return card

def md_pub(pub):
    elts = [ pub_entry(pub)
           , abs_card(pub)
           , bib_card(pub) ]
    elts = [ e.strip() for e in elts if e != '' ]
    return '\n'.join(elts)

def main():
    with open(PUBS_JSON, 'r') as f:
        pubs = json.load(f)

    entries = '\n\n'.join([md_pub(p) for p in pubs])

    with open(TEMPLATE, 'r') as f:
        template = f.read()

    with open(PUBS_MD, 'w') as f:
        f.write(template.replace('PUB_ENTRIES', entries))

main()
