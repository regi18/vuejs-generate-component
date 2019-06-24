"""
Easily create new components in a vue project
Just execute the script with create-component.py <component name> 
to create a new component (it will be added in the components folder
and imported in App.vue).
For faster use, for example, you could rename the script to something shorter, 
like vue-c.py

Created by: regi18
Version: 1.2.0
Github: https://github.com/regi18/
"""

import argparse
import os
import re

parser = argparse.ArgumentParser()
parser.add_argument("name", help="The component's name (please pass it with PascalCase)", nargs="?", type=str)
args = parser.parse_args()


# Converts the name to kebab-case for the tag's name
def pacal_case2kebab_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower()

kebab_case_component_name = pacal_case2kebab_case(args.name)

# How the component will be created
component_template = """<template>
</template>

<script>
export default {{
  name: '{}'
}}
</script>

<style scoped>
</style>
""".format(kebab_case_component_name)


# Create the new component
if os.path.isdir(".\\src\\components\\"):
  with open(".\\src\\components\\{}.vue".format(args.name), "x") as f:
    f.write(component_template)
else:
  print('[!] Components folder not found (.\\src\\components\\)')
  quit()

import_string = "import " + args.name + " from './components/" + args.name + ".vue';\n"

# Imports and adds the newly created component to the App.vue file
with open(".\\src\\App.vue","r") as f:
    file = f.readlines()
    for i,line in enumerate(file):
        if "<script>" in line:
            file.insert(i+1,import_string)
        if "components: {" in line:
            file.insert(i+1,"    " + args.name + ",\n")
            
    with open(".\\src\\App.vue","w") as w:
        w.writelines(file)
