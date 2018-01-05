
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

