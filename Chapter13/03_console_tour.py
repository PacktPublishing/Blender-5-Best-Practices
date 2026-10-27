# Chapter 13: Finding your way around the scripting tools, and
# How the Python API is organized
#
# These are single lines meant for the Python Console, typed one at a time
# with an object selected. They are gathered here for reference. Running the
# whole file from the Text Editor works too, with the default Cube present,
# and prints the results to the system console.

import bpy

# bpy.context is the current situation
print(bpy.context.active_object.name)       # the active object's name
print(bpy.context.active_object.location)   # its position
print(len(bpy.data.objects))                # every object in the file

# bpy.data is the document
bpy.data.objects          # every object in the file
bpy.data.objects["Cube"]  # one object, by name
bpy.data.materials        # every material
bpy.data.collections      # every collection

# bpy.context is the current situation
bpy.context.active_object     # the object you last clicked
bpy.context.selected_objects  # everything currently selected
bpy.context.scene             # the current scene

# Two routes to the same list of materials
print(bpy.data.objects["Cube"].data.materials.values())
print(bpy.data.meshes["Cube"].materials.values())

# Two ways to move an object up by one meter

# The operator way. This depends on what is selected and which area is active
bpy.ops.transform.translate(value=(0, 0, 1))

# The data way. Direct, and it does not care about context
obj = bpy.data.objects["Cube"]
obj.location.z += 1

# Looping and filtering: print the name of every mesh in the file
for obj in bpy.data.objects:
    if obj.type == 'MESH':
        print(obj.name)
