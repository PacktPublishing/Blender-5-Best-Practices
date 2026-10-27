# Chapter 13: From script to tool: Operators, panels, and extensions
# The batch exporter as a small add-on. Run it from the Text Editor and an
# "Asset Export" panel appears in the 3D Viewport sidebar (N) under the
# Export tab. Zip this folder together with blender_manifest.toml to install
# it as an extension via Edit | Preferences | Get Extensions | Install from Disk.

import bpy
from pathlib import Path


class ASSET_OT_batch_export(bpy.types.Operator):
    bl_idname = "asset.batch_export"
    bl_label = "Batch Export Assets"

    def execute(self, context):
        export_dir = Path.home() / "Documents" / "Blender exports"
        export_dir.mkdir(parents=True, exist_ok=True)

        collection = bpy.data.collections.get("Assets")
        if collection is None:
            self.report({'WARNING'}, "No collection named 'Assets' found")
            return {'CANCELLED'}

        for obj in collection.objects:
            bpy.ops.object.select_all(action='DESELECT')
            obj.select_set(True)
            context.view_layer.objects.active = obj
            filepath = export_dir / (obj.name + ".glb")
            bpy.ops.export_scene.gltf(
                filepath=str(filepath),
                use_selection=True,
                export_format='GLB',
            )

        self.report({'INFO'}, f"Exported {len(collection.objects)} assets")
        return {'FINISHED'}


class VIEW3D_PT_batch_export(bpy.types.Panel):
    bl_label = "Asset Export"
    bl_idname = "VIEW3D_PT_batch_export"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Export"

    def draw(self, context):
        self.layout.operator("asset.batch_export")


def register():
    bpy.utils.register_class(ASSET_OT_batch_export)
    bpy.utils.register_class(VIEW3D_PT_batch_export)


def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_batch_export)
    bpy.utils.unregister_class(ASSET_OT_batch_export)


if __name__ == "__main__":
    register()
