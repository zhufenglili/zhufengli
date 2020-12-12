import yaml

# print(yaml.safe_load(open("data.yaml")))
# a = yaml.safe_load(open('data2.yaml'))
# print(a)
# print(a['li'])
# print(a['li'] ['lii'])
a =["yy:aa",'oo:ooo',["aa"]]
print(yaml.dump(a))