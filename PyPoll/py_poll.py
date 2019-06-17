import os
from tqdm import tqdm
from collections import Counter
import csv

all_candidates = []

file_path = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("Resources","election_summary.txt")

with open(file_path, "r") as f:
    reader = csv.reader(f)
    next(reader) # skip the header
    for row in tqdm(reader):
        candidate = row[2]
        all_candidates.append(candidate)

c = Counter(all_candidates)

for cand, votes in c.most_common(4):
    print(cand,votes  / sum(list(c.values())))
    print(cand,votes = sum(list(c.values))

sum(list(c.values()))

sorted(all_candidates.items(), key = lambda x: x[1], reverse=True)