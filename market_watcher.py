# -*- coding: utf-8 -*-
import pandas as pd
import subprocess


file_path = "data/stock/"
file_name = "stocks.csv"
url = r'"http://k-db.com/stocks/?download=csv"'

cmd1 = r"mkdir -p " + file_path
cmd2 = r"curl -o " + file_path + file_name + " " + url
cmd3 = r"iconv -f SHIFT_JIS -t UTF-8 " + file_path + file_name + " > " + file_path + "utf-8_" + file_name

cmd1_r = subprocess.check_output(cmd1, shell=True)
print(cmd1_r)

cmd2_r = subprocess.Popen(cmd2, shell=True).communicate()
print(cmd2_r)

cmd3_r = subprocess.Popen(cmd3, shell=True).communicate()
print(cmd3_r)

df = pd.read_csv(url)
print(df.values)