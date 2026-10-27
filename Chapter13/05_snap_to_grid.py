# Chapter 13: Your first automations
# Snap the selected objects to whole-number coordinates.

import bpy

for obj in bpy.context.selected_objects:
    obj.location.x = round(obj.location.x)
    obj.location.y = round(obj.location.y)
    obj.location.z = round(obj.location.z)
