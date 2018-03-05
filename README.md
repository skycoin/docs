Skycoin documentation
=====================

![](https://user-images.githubusercontent.com/26845312/32426705-d95cb988-c281-11e7-9463-a3fce8076a72.png)

[![Build Status](https://travis-ci.org/skycoin/docs.svg?branch=master)](https://travis-ci.org/skycoin/docs)

Skycoin is a next-generation cryptocurrency. Contents in this repository document how Skycoin improves upon Bitcoin and what parts of the OP Redecentralize and OP Darknet Plan it is supposed to address.

There are three types of documentation:

1. User guides, tutorials, layman explanations (`user-guides` folder)
2. Documentation of existing infrastructure and components (`docs` folder)
3. RFCs, documentation and specifications for future infrastructure and components (`future` folder)

In this repository [hugo](https://gohugo.io/) is used to generate a static website from markdown files.

Refer to [hugo documentation](https://gohugo.io) to [get started](https://gohugo.io/getting-started/quick-start/).

Content: Create or Amend Posts
==============================

Look in the `_data/` folder.  Articles are written in markdown.

Locally, the web site can be previewed with:

```sh
make run
```

The web site will be available at `http://localhost:1313/` immediately after. Notice that the port may be different if another service is bound to `1313`.

To get started make sure that your posts compile without error. Check the formatting.

Then, commit the changes and push.

If there are no problems, then your pages at `http://localhost:1313/` will automatically updated in a few minutes.

Themes: Layout and Styling
==========================

Skycoin Documentation web site uses a custom hugo theme with styling produced using SCSS, when editing any styles you **must** edit the `.scss` files only. If any changes are made to the SCSS partials within `static/css/scss/`, you must re-compile with the following commands.

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
