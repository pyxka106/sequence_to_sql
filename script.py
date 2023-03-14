import fnmatch
import glob
import os
import pandas as pd

os.chdir('E:/Document/TERI_baseline_normalized_2')
# Transfer multiple .tsv files to one single Dataframe
data_files = glob.glob("*.tsv")

df = pd.DataFrame()

for data_file in data_files:
    if fnmatch.fnmatch(data_file, '*_CD8*.tsv'):
        df_new = pd.read_csv(data_file, sep='\t')
        file_name = data_file[:data_file.index(".")].split("_")
        subject_id = file_name[0]
        df_new['subject_id'] = subject_id
        df = df.append(df_new, ignore_index=False)

df.to_csv('./cd8_2.csv', index=False)
