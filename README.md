![docs](https://user-images.githubusercontent.com/8619106/56056146-02264800-5d79-11e9-8483-1c891c3c49f4.png)

# Skycoin Docs Website Documentation

![](https://user-images.githubusercontent.com/26845312/32426705-d95cb988-c281-11e7-9463-a3fce8076a72.png)

[![Build Status](https://travis-ci.org/skycoin/docs.svg?branch=master)](https://travis-ci.org/skycoin/docs)

The documentation in this repo is uploaded to https://www.skycoin.net/docs/.

This documentation is not comprehensive, please see the Github wikis of other Skycoin code repositories for more information.
For example, the [Skycoin wiki](https://github.com/skycoin/skycoin/wiki) and the [Skywire wiki](https://github.com/skycoin/skywire/wiki).
There is also more information in the [Skycoin blog](https://www.skycoin.net/blog/).

## Content

There are two types of documentation:

1. User guides, tutorials, layman explanations (`user-guides` folder)
2. Technical documentation (`docs` folder)

Additionally, there is a glossary.

In this repository [hugo](https://gohugo.io/) is used to generate a static website from markdown files.

Refer to [hugo documentation](https://gohugo.io) to [get started](https://gohugo.io/getting-started/quick-start/).

### Create or Amend Posts

Look in the `content/` folder.  Articles are written in markdown.

Locally, the web site can be previewed with:

```sh
make run
```

The web site will be available at `http://localhost:1313/docs/` immediately after. Notice that the port may be different if another service is bound to `1313`.

To get started make sure that your posts compile without error. Check the formatting.

Then, commit the changes and push.

If there are no problems, then your pages at `http://localhost:1313/docs/` will automatically updated in a few minutes.

### Glossary

Glossary definitions are in the `data/glossary/` folder. Follow the existing format to add a new definition and it will
appear on the glossary page.

## Themes: Layout and Styling

The Skycoin Documentation website uses a custom hugo theme with styling produced using SCSS.
When editing any styles you **must** edit the `.scss` files only.
If any changes are made to the SCSS partials within `static/css/scss/`,
you must re-compile with the following commands.

Move into the theme directory:

```sh
cd themes/skycoin/
```

Install the dependencies such as `node-sass`:

```sh
yarn
# or
npm install
```

Compile and build the SCSS:

```sh
yarn build:css
```
