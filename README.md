# load sequences data to sql

**script.py** Transfer multiple .tsv files to one single Dataframe\
**script_1.py** Establish SQL Server & Load data to target table\

# extract and export target information from sql to .csv files

```
SELECT subject_id, j_gene, j_deletions, count(j_deletions)
from teri_baseline.cd4_all
where frame_type = 'In' and v_gene is not null and j_gene is not null
group by subject_id,  j_gene, j_deletions
order by subject_id,  j_gene, j_deletions
into outfile 'E:/Document/08_03/cd4_j_del.csv'
```
