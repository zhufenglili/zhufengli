import yaml

with open('a.yaml') as f:
   name= yaml.safe_load(f)['dd']
   print(name)