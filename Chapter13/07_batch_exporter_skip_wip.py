# Chapter 13: When Python beats the button
# The batch exporter with one rule the button cannot express:
# skip any object whose name starts with an underscore (work in progress).

import bpy
from pathlib import Path


def export_assets():
    export_dir = Path.home() / "Documents" / "Blender exports"
    export_dir.mkdir(parents=True, exist_ok=True)

    collection = bpy.data.collections.get("Assets")
    if collection is None:
        print("No collection named 'Assets' was found.")
        return

    for obj in collection.objects:
        if obj.name.startswith("_"):
            continue  # skip work-in-progress objects

        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        filepath = export_dir / (obj.name + ".glb")
        bpy.ops.export_scene.gltf(
            filepath=str(filepath),
            use_selection=True,
            export_format='GLB',
        )


export_assets()
