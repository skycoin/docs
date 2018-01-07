#! /usr/bin/python

"""
Synchronize Bitcoin.org -> Skycoin.net doc link references

Skycoin docs structure is inspired on Bitcoin.org structure.
Both are crypto currency systems powered by block chains.
Therefore there are a lot of intersections. Similarities are
particularly evident in the glossary of terms, but not limited 
to that.

This is a script implementing the following workflow:

    - Recursively parse .md files in _data/ and its subfolders
      looking for link references
    - If the reference is already included in _includes/references.md
      then continue ...
    - ... else if the reference exists in Bitcoin.org docs then
      import it from there and tag it as TODO: REVIEW
    - ... else create a new entry in _includes/references.md
      and tag it as TODO: EMPTY

This is necessary to limit references to the scope of Skycoin
boundaries , keep docs in sync, and discover dangling references
in the documentation.
"""

import argparse
import itertools
import os
import re
import sys

skc_base_path = os.path.join(os.path.dirname(sys.argv[0]), '..')
skc_refs_path = os.path.join(skc_base_path, '_includes', 'references.md')

parser = argparse.ArgumentParser(
        description="Synchronize Bitcoin.org -> Skycoin.net doc link references")

parser.add_argument('path', metavar='PATH', nargs=1,
                    help='Path to Bitcoin.org source folder')

args = parser.parse_args()

btc_refs_path = os.path.join(args.path[0], '_includes', 'references.md')

btc_refs = {}
skc_refs = {}

refs = [{
            'key': 'in',
            'path': btc_refs_path,
            'msg': 'Bitcoin.org references file',
            'map': btc_refs},
        {
            'key': 'out',
            'path': skc_refs_path,
            'msg': 'Skycoin.net references file',
            'map': skc_refs}
        ]

RE_MDLINK = re.compile(r'\[([^\[\]]*)\]\[([^\[\]]*)\]')

for fileref in refs:
    try:
        with open(fileref['path'], 'r') as frefs:
            refs = fileref['map']
            for l in frefs:
                if l[0] != '[':
                    continue
                bracket_index = l.index(']:')
                if bracket_index < 0:
                    continue
                key = l[1:bracket_index]
                # TODO : Log key value found in DEBUG mode
                text = l[bracket_index + 2:]
                refs[key] = text
            # TODO : Log number of key / values retrieved
    except IOError:
        sys.exit('Error opening ' + fileref['msg'])

for dirpath, subdirs, subfiles, dir_fd in os.fwalk(skc_base_path, '_data'):
    for filename in subfiles:
        if not filename.endswith('.md'):
            continue
        with(os.open(filename, 'r', dir_fd=dir_fd)) as mdfile:
            for l in mdfile:
                for match in RE_MDLINK.finditer(l):
                    key, value = match.group(0, 1)
                    if key in skc_refs:
                        continue
                    else:
                        skc_refs[key] = value + ' # TODO : REVIEW' \
                                if key in btc_refs else 'TODO: EMPTY'

for key in sorted(skc_refs.keys()):
    print('[{key}]: {value}'.format(key=key, value=skc_refs[key]))

