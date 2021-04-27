import json

# person = {"name": "test", "age": 30,
#           "childen": False, "skills": ["python", "php"]}
# person_json = json.dumps(person, indent=4)
# print(person_json)

# # file = open('person.json', 'w')
# json.dump(person, file, indent=4)
# file.close()

# file = open('person.json', 'r')
# json_load = json.loads(person_json)
# print(json_load)
# for i in json_load.items():
#     print(i)

with open("testjson.txt", 'w+') as f:
    f.write("test1test2test3test4test4")
    with open("testjson.txt", 'r') as fr:
        for i in fr:
            print(i, end='')
