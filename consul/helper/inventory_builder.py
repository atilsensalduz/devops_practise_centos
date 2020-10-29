#!/usr/bin/python3

import sys
import yaml


consulservercount = len(sys.argv) - 1

consulinventory = [] 
position = 1
while (consulservercount >= position):
       #consulnodename = "consul0" + str(position)
       consulinventory.append(sys.argv[position])
       position = position + 1

consulinventoryyaml=yaml.dump(consulinventory, explicit_start=True, default_flow_style=False)


file = open("/workspace/roles/consul/task/host.yaml", "w")
file.write(consulinventoryyaml)
file.close()
