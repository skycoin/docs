#! /usr/local/bin/python3

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
    - If an entry is not referenced anywhere in the docs then
      tag it as TODO: NOTUSED

This is necessary to limit references to the scope of Skycoin
boundaries , keep docs in sync, and discover dangling references
in the documentation.
"""

import argparse
import itertools
import os
import re
import sys

sky_base_path = os.path.join(os.path.dirname(sys.argv[0]), '..')

parser = argparse.ArgumentParser(
        description="Synchronize Bitcoin.org -> Skycoin.net doc link references")

parser.add_argument('path', metavar='PATH', nargs=1,
                    help='Path to Bitcoin.org source folder')

args = parser.parse_args()

btc_base_path = args.path[0]

btc_refs = {}
sky_refs = {}

RE_MDLINK = re.compile(r'\[([^\[\]]*)\]\[([^\[\]]*)\]')

REPOS_DATA = [
    {
        'caption': 'Bitcoin.org',
        'refs': btc_refs,
        'path': btc_base_path},
    {
        'caption': 'Skycoin.net',
        'refs': sky_refs,
        'path': sky_base_path}]

doc_folders = [('_includes',)]
paths = [os.path.join(*base_path, filename)
            for base_path in doc_folders
            for filename in os.listdir(os.path.join(btc_base_path, *base_path))
            if filename.endswith('.md')]

for path in paths:
    for repo in REPOS_DATA:
        refs = repo['refs']
        caption = repo['caption']
        base_path = repo['path']
        try:
            filepath = os.path.join(base_path, path)
            with open(filepath, 'r') as frefs:
                for lineno, l in enumerate(frefs):
                    if l[0] != '[':
                        continue
                    bracket_index = l.index(']:')
                    if bracket_index < 0:
                        continue
                    key = l[1:bracket_index].lower()
                    # TODO : Log key value found in DEBUG mode
                    text = l[bracket_index + 2:].strip()
                    refs[key] = [path, lineno, text, 0]
                # TODO : Log number of key / values retrieved in DEBUG mode
        except IOError:
            sys.exit('Error opening ' + filepath)

import pprint

for dirpath, subdirs, subfiles, dir_fd in os.fwalk(sky_base_path, 'content'):
    for filename in subfiles:
        if not filename.endswith('.md'):
            continue
        with(os.fdopen(os.open(filename, os.O_RDONLY, dir_fd=dir_fd))) as mdfile:
            for l in mdfile:
                for match in RE_MDLINK.finditer(l):
                    key, value = match.group(2, 1)
                    if not key:
                        key = value
                    key = key.lower()
                    if key.startswith('/'):
                        pass
                    elif key in sky_refs:
                        # Increment reference count
                        sky_refs[key][3] += 1
                    else:
                        source, lineno, text = (btc_refs.get(key) or (None, None, None))[:3]
                        sky_refs[key] = [source, None, 'REVIEW : ' + text \
                                if key in btc_refs else 'TODO: EMPTY', 1]

print("""
{% comment %}
This file is licensed under the MIT License (MIT) available on
http://opensource.org/licenses/MIT.
{% endcomment %}

""")

for key in sorted(sky_refs.keys()):
    value = sky_refs[key]
    if value[3] == 0:
        value[2] = 'TODO: NOUSE ' + value[2]
    print('[{key}]: {value}'.format(key=key, value=value[2]))

