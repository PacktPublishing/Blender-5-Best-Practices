# Chapter 13: Blender Automation and Advanced Tips with Python Scripting

Every code listing from the chapter, in the order it appears. The chapter explains each one line by line; the files here are so you can run them without retyping.

## How to run a script

1. Open the **Scripting** workspace from the tabs along the top of Blender.
2. In the Text Editor, choose **Text | Open** and pick a `.py` file from this folder, or paste the contents into a new text block.
3. Press **Run Script** or `Alt + P`.

Printed output goes to the system console. On Windows, open it with **Window | Toggle System Console**. On macOS and Linux, start Blender from a terminal to see it.

Scripts act on the whole file instantly and some changes cannot be undone. Try them on a test file first, or save before you run.

## The scripts

| File | Chapter section | What it does |
| --- | --- | --- |
| `01_rename_selected.py` | A basic script | Prefixes every selected object's name with `Asset_` |
| `02_batch_exporter.py` | The finished tool, up front | Exports each object in a collection named `Assets` to its own `.glb` file in `Documents/Blender exports` |
| `03_console_tour.py` | Finding your way around the scripting tools; How the Python API is organized | The single-line console examples, gathered for reference: `bpy.context`, `bpy.data`, `bpy.ops`, operator versus data, loop and filter |
| `04_rename_batch.py` | Your first automations | Renames every mesh to `Prop_000`, `Prop_001` and so on, counting across every object in the file (Figure 13.8) |
| `04b_rename_batch_collection.py` | Your first automations | The same renamer, counting only the objects in a collection named `Collection` (Figure 13.9) |
| `05_snap_to_grid.py` | Your first automations | Rounds the location of every selected object to whole-number coordinates |
| `06_clean_orphans.py` | Your first automations | Purges unused data, the same command as **File | Clean Up** |
| `07_batch_exporter_skip_wip.py` | When Python beats the button | The batch exporter with one extra rule: objects whose names start with `_` are skipped |

## The add-ons

Two folders hold the chapter's add-ons as Blender extensions. Each contains an `__init__.py` with the code and a `blender_manifest.toml` that describes it.

| Folder | Chapter section | What it adds |
| --- | --- | --- |
| `batch_asset_exporter/` | From script to tool: Operators, panels, and extensions | An **Asset Export** panel in the 3D Viewport sidebar (`N`), under an **Export** tab, with one button that runs the batch exporter |
| `my_toolkit/` | Building your own toolkit | A **My Toolkit** panel under a **Toolkit** tab with three buttons: prefix names, snap to grid, clean orphan data |

To try an add-on without installing it, open its `__init__.py` in the Text Editor and press **Run Script**. The panel appears in the sidebar for the rest of the session.

To install it as an extension so it survives between sessions:

1. Open `blender_manifest.toml` and put your own name and email in the `maintainer` line.
2. Zip the folder so that `__init__.py` and `blender_manifest.toml` sit at the top level of the zip. Blender can do this for you from a terminal:

   ```
   blender --command extension build --source-dir batch_asset_exporter --output-dir .
   ```

3. In Blender, choose **Edit | Preferences | Get Extensions**, open the drop-down arrow at the top right, and choose **Install from Disk**. Pick the zip.

## Before you trust an export

Always run an export script on a small test collection first and open one of the resulting files to confirm it contains what you expect. An export that is subtly wrong is still wrong two hundred times.

## A note on Blender versions

Blender's Python API evolves between releases. These scripts were written for Blender 5.1 and tested on Blender 5.2. If a later release changes an operator or property, the Info log and **Copy Python Command** (right-click any button) will show you the current spelling.
