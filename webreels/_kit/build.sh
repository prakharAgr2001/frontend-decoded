#!/bin/sh
# usage: sh webreels/_kit/build.sh wr12   -> prepends the kit to webreels/wr12/{scenes.src.js,style.src.css}
d=$(dirname "$0"); r=$d/../$1
cat $d/story.js $r/scenes.src.js > $r/scenes.js
cat $d/story.css $r/style.src.css > $r/style.css
