#!/bin/bash
rm toto.txt
python verif_exist_result.py > toto.txt
wc -l toto.txt
echo $nbligne "tests restants"