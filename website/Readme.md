<!-- ![skycoin blog logo](https://user-images.githubusercontent.com/26845312/32426756-27c29fd4-c282-11e7-8c9b-b0aa179a03ab.png) -->

Skycoin DevsDocs
============

<!-- https://www.skycoin.net/blog/ -->

This blog uses [hugo](https://gohugo.io/) to generate a static website from markdown files.

Refer to hugo documentation for full detail.

Translation Bounty Program
==========================

If you are here for the translation bounty program and need help submitting a translation, follow this guide (pdf):

<!-- [Skycoin  Blog Github Translation Instructions](https://github.com/skycoin/blog/files/1469162/github-translation-manual.pdf) -->

Content: Create or Amend Posts
==============================

Look in the `content/` folder.  Posts are written in markdown.

Locally, the blog can be previewed with:

```sh
hugo serve
```

Make sure that your posts compile without error. Check the formatting.

Then, commit the changes and push.

If there are no problems, then (url website) will automatically update in a few minutes.

Translations
============

https://gohugo.io/content-management/multilingual/

If the language is not currently supported by the blog,
add a language config statement to config.toml (see the file for an example).

The blog posts are in a subdirectory in `content/`.
To add a translation of an existing post, change the extension from `.md` to `.$LANG.md`.

For example, to add a German translation of `content/statement/Skycoin Distribution.md`,
name the file `content/statement/Skycoin Distribution.de.md`.

Themes: Layout and Styling
==========================

Skycoin Blog uses a custom hugo theme with styling produced using SCSS, when editing any styles you **must** edit the `.scss` files only. If any changes are made to the SCSS partials within `static/css/scss/`, you must re-compile with the following commands.

Move into the theme directory
```sh
  cd themes/skycoin/
```

Install the dependencies such as `node-sass`
```sh
  yarn
  # or
  npm install
```

Compile and build the SCSS
```sh
  yarn build:css
```
