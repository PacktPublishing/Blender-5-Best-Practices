# Chapter 13: The finished tool, up front
# The batch asset exporter. Point it at a collection called "Assets", run it,
# and every object in that collection exports to its own .glb file named
# after the object, inside Documents/Blender exports.

import bpy
from pathlib import Path


def export_assets():
    # A cross-platform folder inside the user's Documents folder
    export_dir = Path.home() / "Documents" / "Blender exports"
    export_dir.mkdir(parents=True, exist_ok=True)

    # The collection to export from
    collection = bpy.data.collections.get("Assets")
    if collection is None:
        print("No collection named 'Assets' was found.")
        return

    for obj in collection.objects:
        # Make this object the only selected and active object
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj

        # Name the file after the object and export it as glTF binary
        filepath = export_dir / (obj.name + ".glb")
        bpy.ops.export_scene.gltf(
            filepath=str(filepath),
            use_selection=True,
            export_format='GLB',
        )


export_assets()
