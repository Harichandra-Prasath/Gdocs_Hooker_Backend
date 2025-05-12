#!/bin/bash

# Get the directory information
dir=$(dirname "$0")

# Move to the directory
cd "$dir"

# Activate the virutal environment
source .venv/bin/activate

# Get all the env files
env_files=$(ls ./*.env)

i=0
for env_file in $env_files
do
	python3 main.py --env-file "$env_file" >> ~/.gdocks_hooker_"${i}".logs 2>&1 &
	((i++))
done
