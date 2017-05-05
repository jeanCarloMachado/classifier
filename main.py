import sys
import math
import json
import re
import os

k_distance = int(os.getenv('CUSTOM_K', 2))

target = sys.stdin.readlines()[0].split(',')
target_class = target[-1].split('\n')[0]

file = open("data/iris.data.z1")
swarm = file.read()
swarm = swarm.split('\n')
swarm = filter(lambda x: not re.match(r'^\s*$', x), swarm)
swarm = list(map(lambda entity: entity.split(','), swarm))

entity_distance_list = []
for (i, entity) in enumerate(swarm):
    distance = 0
    label = entity.pop(-1)
    for (j, attribute) in enumerate(entity):
        distance += math.pow(float(attribute) - float(target[j]), 2)
    distance = math.sqrt(distance)
    pair = {}
    pair["data"] = entity
    pair["distance"] = distance
    pair["label"] = label
    entity_distance_list.append(pair)


for i in range(0, len(entity_distance_list)):
    for j in range(0, len(entity_distance_list)):
        if entity_distance_list[i]['distance'] < entity_distance_list[j]['distance']:
            tmp = entity_distance_list[j]
            entity_distance_list[j] = entity_distance_list[i]
            entity_distance_list[i] = tmp



classes = {}
for i in range(0, k_distance):
    if entity_distance_list[i]["label"] in classes:
        classes[entity_distance_list[i]["label"]] = classes[entity_distance_list[i]["label"]]+1
    else:
        classes[entity_distance_list[i]["label"]] = 1

result = (max(classes))
print("Given: " + target_class )
print("Guessed: " + result )
print("Data: " + str(target) )
print("Result:" + str(target_class == result))
