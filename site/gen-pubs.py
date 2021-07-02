#!/usr/bin/env python3

import json
import math
import os.path

PUBS_JSON = '../pubs.json'
TEMPLATE = 'publications.template'
PUBS_MD = 'publications.md'

def break_join(elts):
    max_len = 100
    full_txt = ''.join(elts)
    nlines = math.ceil(len(full_txt) / max_len)
    ideal = math.ceil(len(full_txt) / nlines)

    def cands(elts, line, lines):
        if len(elts) == 0:
            return [lines + [line]]
        else:
            e, es = elts[0], elts[1:]
            if len(line + e) < ideal:
                return cands(es, line + e, lines)
            elif max_len < len(line + e):
                return cands(es, e, lines + [line])
            else:
                # in between ideal and max, try both
                a = cands(es, line + e, lines)
                b = cands(es, e, lines + [line])
                return a + b

    def error(lines):
        err = 0
        for i in range(len(lines) - 1):
            err += abs(len(lines[i]) - len(lines[i + 1]))
        return err

    cs = cands(elts, '', [])
    cs = sorted(cs, key=error)
    return "<br class='big-only'>\n  ".join(cs[0])

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
    elts = ['[' + a + '], ' for a in pub['authors']]
    authors = break_join(elts).rstrip(', ')

    # format venue
    if 'series' in pub:
        venue = f"{pub['venue']} ({pub['series']}) {pub['year']}"
    else:
        venue = f"{pub['venue']} {pub['year']}"

    # format links
    elts = []
    for k in pub['links']:
        if k == 'abstract':
            elts.append(toggle_link(k, 'abs-' + pub['id']))
        elif k == 'bib':
            elts.append(toggle_link(k, 'bib-' + pub['id']))
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
  {venue} \\
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
