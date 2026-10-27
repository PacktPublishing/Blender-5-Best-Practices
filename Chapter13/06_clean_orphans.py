# Chapter 13: Your first automations
# Clean up the leftovers. The same command as File | Clean Up.
# do_recursive=True keeps going until nothing unused remains.

import bpy

bpy.ops.outliner.orphans_purge(do_recursive=True)
