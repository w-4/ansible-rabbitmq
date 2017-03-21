#!/usr/bin/python

import ast
import commands

out = commands.getstatusoutput("rabbitmqctl cluster_status")
begin = out[1].index('running_nodes')
end = out[1].index('cluster_name')

data = out[1][begin:end].strip("running_nodes,")

nodes = ast.literal_eval(data[:-5])

print len(nodes)
