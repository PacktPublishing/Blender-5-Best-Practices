# Chapter 13: Your first automations
# Rename a batch of objects, version 1.
#
# This walks every object in the file. The counter counts every object, not
# just the meshes, so the first mesh may not be Prop_000 (see Figure 13.8).
# See 04b_rename_batch_collection.py for the fix.

import bpy

for index, obj in enumerate(list(bpy.data.objects)):
    if obj.type == 'MESH':
        obj.name = f"Prop_{index:03d}"
