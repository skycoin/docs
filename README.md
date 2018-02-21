Skycoin DevsDocs
============

# Docs

There are three types of documentation:

1. User guides, tutorials, layman explanations (`user-guides` folder)
2. Documentation of existing infrastructure and components (`docs` folder)
3. RFCs, documentation and specifications for future infrastructure and components (`future` folder)

#Blog

This blog uses [hugo](https://gohugo.io/) to generate a static website from markdown files.

Refer to hugo documentation for full detail.

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
