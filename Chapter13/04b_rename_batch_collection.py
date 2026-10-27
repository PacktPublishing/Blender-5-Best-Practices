# Chapter 13: Your first automations
# Rename a batch of objects, version 2.
#
# Move the objects you do not want to rename out of the collection, then loop
# over that collection only. The meshes are now numbered from Prop_000
# (see Figure 13.9). The mesh check is kept but is optional.

import bpy

for index, obj in enumerate(bpy.data.collections["Collection"].objects):
    if obj.type == 'MESH':
        obj.name = f"Prop_{index:03d}"
