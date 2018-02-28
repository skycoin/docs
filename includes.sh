rm -rv content
touch content/.gitkeep
cp -rv _data content/
touch content/.gitkeep

find content/* -type f -name "*.md" -exec sh -c 'cat _includes/references.md >> "{}" ' \;