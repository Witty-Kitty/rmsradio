#!/bin/bash
for i in bahari chamgei egesa inooro mulembe musyi muuga ramogi sulwe vuuka wimwaro 
do
   python3 url_parser.py $i
   python3 url_deduplicate.py $i
   python3 content_extraction.py $i
done