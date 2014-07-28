#!/usr/bin/env python

import sys
import yaml
import json
import subprocess
import os

def read_parts_from_mlabns():
    # Download the JSON list of slivers.
    MLAB_NS_QUERY_URL = "http://localhost:8585/ooni?match=all"
    DEVNULL = open(os.devnull, "w")
    wget = subprocess.Popen(["wget", MLAB_NS_QUERY_URL, "-O", "-"], stdout=subprocess.PIPE, stderr=DEVNULL)
    json_list = wget.communicate()[0]
    exit_status = wget.returncode
    if exit_status != 0:
        print "wget could not download the JSON list."
        exit(1)

    # Parse the JSON list, and map it into a list of the tool_extra fields.
    sliver_list = json.loads(json_list)
    part_list = []
    for sliver in sliver_list:
        part_list.append(sliver['tool_extra'])
    return part_list

def assemble_bouncer_config(parts):
    merged_parts = { }
    for part in parts:
        merged_parts.update(part)
    bouncer_config = { 'collector': merged_parts }
    return yaml.safe_dump(bouncer_config)

def write_bouncer_config(path, bouncer_config_contents):
    try:
        f = open(path, 'w')
        f.write(bouncer_config_contents)
        f.close()
    except IOError:
        print "Couldn't write to bouncer config file."
        exit(1)


bouncer_config_path = '/home/mlab_ooni/data/bouncer.yaml'
if len(sys.argv) >= 2:
    bouncer_config_path = sys.argv[1]

# FIXME: Read from the mlab-ns simulator.
parts = read_parts_from_mlabns()
bouncer_config = assemble_bouncer_config(parts)
write_bouncer_config(bouncer_config_path, bouncer_config)
