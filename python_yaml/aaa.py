import yaml

with open('./a.yml') as f:
   aa= yaml.safe_load(f)
   ab=aa['a']
   print(ab)
   print(aa['b'])