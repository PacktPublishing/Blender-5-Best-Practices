# Chapter 13: A basic script
# Run from the Python Console or the Text Editor (Alt + P).
# Select a few objects first. Every selected object gains an "Asset_" prefix.

import bpy

for obj in bpy.context.selected_objects:
    obj.name = "Asset_" + obj.name
