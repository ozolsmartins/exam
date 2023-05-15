lloyd = {
  "name": "Lloyd",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}


dic={}
all=[lloyd,alice,tyler]


for i in all:
    dic[i["name"]]={}
    for key in i:
        if key=="name":
            continue
        dic[i["name"]][key]=i[key] # dic['Alice']['homework'] = alice['homework']
print(dic)

n={'Lloyd': {'homework': [90.0, 97.0, 75.0, 92.0], 'quizzes': [88.0, 40.0, 94.0], 'tests': [75.0, 90.0]}, 'Alice': {'homework': [100.0, 92.0, 98.0, 100.0], 'quizzes': [82.0, 83.0, 91.0], 'tests': [89.0, 97.0]}, 'Tyler': {'homework': [0.0, 87.0, 75.0, 22.0], 'quizzes': [0.0, 75.0, 78.0], 'tests': [100.0, 100.0]}}
weights=[0.2,0.3,0.5]

for key in n:
  atzime=0
  for reskey, weight in zip(n[key], weights):
    atzime+=sum(n[key][reskey])/len(n[key][reskey])*weight
  print(key, round(atzime,0))