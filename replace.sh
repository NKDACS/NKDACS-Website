#!/usr/bin/env bash

# Clone Theme for Editing
if [ ! -d "mkdocs-material" ] ; then
  git clone --depth 1 https://github.com/squidfunk/mkdocs-material.git
fi

# Change Google CDN to loli.net
sed -i 's/fonts.gstatic.com/fonts-gstatic.proxy.ustclug.org/g' mkdocs-material/material/base.html
sed -i 's/fonts.googleapis.com/fonts.proxy.ustclug.org/g' mkdocs-material/material/base.html
sed -i "s/'assets\/fonts\/material-icons.css'/'https:\/\/fonts.proxy.ustclug.org\/icon?family=Material+Icons'/g" mkdocs-material/material/base.html