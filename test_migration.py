import os

MIGRATION_SCRIPTS = "C:/teamfora/server/src/main/resources/sql/mysql/migration"

script_names = os.listdir(MIGRATION_SCRIPTS)
script_map = {}
for s in script_names:
    print(s)
    version = int(s.split('-')[0])
    print(version)
    script_map[version] = s

for x in script_map.items():
    print(x)

print()

versions = list(script_map.keys())
last_version = versions[-1]
print(last_version)
print(versions[3:8])

print("".find("ERROR"))
print("this ERROR 1146 (42S02) at line 1: Table".find("ERROR"))