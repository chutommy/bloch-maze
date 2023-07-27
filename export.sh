#!/bin/bash
cxfreeze src/main.py --compress --target-name "bloch-maze" --target-dir "dist" --silent > /dev/null
cp -r assets dist
cp LICENSE dist