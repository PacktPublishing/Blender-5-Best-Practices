# Chapter 13: Building your own toolkit
# One add-on holding several tools, with a button for each in a "My Toolkit"
# panel in the 3D Viewport sidebar (N) under the Toolkit tab.
#
# To add a tool of your own: write an Operator class, add it to the classes
# tuple, and add one layout.operator("toolkit.your_tool") line to draw.

import bpy


class TOOLKIT_OT_prefix_names(bpy.types.Operator):
    bl_idname = "toolkit.prefix_names"
    bl_label = "Prefix Selected with Asset_"

    def execute(self, context):
        for obj in context.selected_objects:
            obj.name = "Asset_" + obj.name
        return {'FINISHED'}


class TOOLKIT_OT_snap_to_grid(bpy.types.Operator):
    bl_idname = "toolkit.snap_to_grid"
    bl_label = "Snap Selected to Grid"

    def execute(self, context):
        for obj in context.selected_objects:
            obj.location.x = round(obj.location.x)
            obj.location.y = round(obj.location.y)
            obj.location.z = round(obj.location.z)
        return {'FINISHED'}


class TOOLKIT_OT_clean_orphans(bpy.types.Operator):
    bl_idname = "toolkit.clean_orphans"
    bl_label = "Clean Orphan Data"

    def execute(self, context):
        bpy.ops.outliner.orphans_purge(do_recursive=True)
        self.report({'INFO'}, "Purged unused data")
        return {'FINISHED'}


class VIEW3D_PT_toolkit(bpy.types.Panel):
    bl_label = "My Toolkit"
    bl_idname = "VIEW3D_PT_toolkit"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Toolkit"

    def draw(self, context):
        layout = self.layout
        layout.operator("toolkit.prefix_names")
        layout.operator("toolkit.snap_to_grid")
        layout.operator("toolkit.clean_orphans")


classes = (
    TOOLKIT_OT_prefix_names,
    TOOLKIT_OT_snap_to_grid,
    TOOLKIT_OT_clean_orphans,
    VIEW3D_PT_toolkit,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
