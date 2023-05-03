#!/bin/bash
for file in *
do
    mv "$file" "$(date +%Y-%m-%d)-$file"
done