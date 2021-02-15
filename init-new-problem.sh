#!/bin/bash

set -e

DIR="$(date +%d-%m-%Y)"	
mkdir $DIR
touch "$DIR/problem.md"
touch "$DIR/solution.py"
