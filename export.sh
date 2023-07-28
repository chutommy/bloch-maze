#!/bin/bash

TARGET_NAME="bloch-maze"
TARGET="dist"

declare -a COMPONENTS=("assets" "config.json" "LICENSE" "requirements.txt")

cxfreeze main.py --compress --target-name "${TARGET_NAME}" --target-dir "${TARGET}"

for FILE in "${COMPONENTS[@]}"; do
  cp -r "${FILE}" "${TARGET}"
  echo $FILE
done
