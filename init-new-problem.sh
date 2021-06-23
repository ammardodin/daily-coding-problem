#!/bin/bash

set -e

DIR="$(date +%Y-%m-%d)"	
mkdir $DIR
touch "$DIR/problem.md"
touch "$DIR/solution.py"
