#! /bin/bash

# curl https://gitlab.cs.wwu.edu/tsikerm/assignment-files/raw/master/mdl.csv -o mdl.csv

# sed '$d' mdl.csv

rm mdl.csv

# rm mdl.list

pip3 install requests

python3 update-mdl.py