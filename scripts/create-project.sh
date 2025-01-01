#!/bin/bash

# Help message
show_help() {
  echo "Usage: $(basename "$0" [--help])

This script creates a new Python file in a specified project directory.

Steps:
1. Prompts the user for the project name.
2. Prompts the user for the Python file name.
3. Creates the required directories and the Python file.

Options:
  --help  Display this help message and exit."
}

#check if --help was passed

# Help message
show_help() {
    echo "Usage: $(basename "$0") [--help]
This script creates a new Python file in a specified project directory.

Steps:
1. Prompts the user for the project name.
2. Prompts the user for the Python file name.
3. Creates the required directories and the Python file.

Options:
  --help  Display this help message and exit."
}

# Check if --help was passed
if [[ "$1" == "--help" ]]; then
    show_help
    exit 0
fi




# Prompt user for name of project
read -p "Enter the name of the project: " project_name

# Prompt user for the name of the Python file  name
read -p "Enter the name of the python file name (without .py): " file_name

# Base dir
base_dir="/home/jonas/Development/Projects/100DaysOfCode/src"

#constrcut full path
project_dir="$base_dir/$project_name"
python_file="$project_dir/$file_name.py"

#Create the project dir if not exist
if [ ! -d "$project_dir" ]; then
   mkdir -p "$project_dir"
   echo "Created directory: $project_dir"
fi

# Create the Python file
if [ ! -f "$python_file" ]; then
    touch "$python_file"
    echo "Created Python file: $python_file"
else
    echo "File already exists: $python_file"
fi

