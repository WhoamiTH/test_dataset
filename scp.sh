#!/bin/bash
set -e



cp drawpic.py test_abalone19
cp drawpic.py test_ecoli1
cp drawpic.py test_glass0
cp drawpic.py test_glass5
cp drawpic.py test_pageblocks1
cp drawpic.py test_pima
cp drawpic.py test_vehicle0
cp drawpic.py test_yeast3
cp drawpic.py test_yeast5
cp drawpic.py test_yeast6

cd ./test_abalone19/
python scan_data_dir.py>result.txt
cd ../

cd ./test_ecoli1/
python scan_data_dir.py>result.txt
cd ../

cd ./test_glass0/
python scan_data_dir.py>result.txt
cd ../

cd ./test_glass5/
python scan_data_dir.py>result.txt
cd ../

cd ./test_pageblocks1/
python scan_data_dir.py>result.txt
cd ../

cd ./test_pima/
python scan_data_dir.py>result.txt
cd ../

cd ./test_vehicle0/
python scan_data_dir.py>result.txt
cd ../

cd ./test_yeast3/
python scan_data_dir.py>result.txt
cd ../

cd ./test_yeast5/
python scan_data_dir.py>result.txt
cd ../

cd ./test_yeast6/
python scan_data_dir.py>result.txt
cd ../



