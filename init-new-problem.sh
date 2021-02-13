#!/bin/bash

set -eiop

DIR="$(date +%d-%m-%Y)"	
mkdir $DIR
touch "$DIR/problem.md"
touch "$DIR/solution.py"