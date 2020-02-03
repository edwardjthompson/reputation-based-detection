#! /bin/bash

curl https://gitlab.cs.wwu.edu/tsikerm/assignment-files/raw/master/ip.txt -o ip.txt

cat ip.txt

# sed '$d' mdl.csv
# pwd
# ls -R ../../
# rm mdl.csv

# rm mdl.list

# pip3 install requests

python3 update-mdl.py

# ls