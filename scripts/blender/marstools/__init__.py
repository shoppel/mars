'''
MARS Blender Tools - a Blender Add-On to work with MARS robot models

File __init__.py

Created on 6 Jan 2014

@author: kavonszadkowski

Copy this add-on to your Blender add-on folder and activate it
in your preferences to gain instant (virtual) world domination.
'''


bl_info = {
    "name": "MARS Blender Tools",
    "description": "A set of tools to enable editing of MARS robot models in Blender.",
    "author": "Kai von Szadkowski, Malte Langosz",
    "version": (0, 3),
    "blender": (2, 62, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "category": "3D View"
    }

if "bpy" in locals():
    import imp
    #imp.reload(mtmaterials)
    #imp.reload(mtcreateprops)
    #imp.reload(mt_importexport)
    #imp.reload(mt_oldexport)
    imp.reload(mtcontrollers)
    imp.reload(mtexport)
    imp.reload(mtimport)
    imp.reload(mtgui)
    imp.reload(mtimport)
    imp.reload(mtjoints)
    imp.reload(mtmisctools)
    imp.reload(mtsensors)
    imp.reload(mtutility)
    print("Reloading MARS Blender Tools.")
else:
    from . import mtcontrollers, mtexport, mtgui, mtimport, mtjoints, mtmisctools, mtsensors, mtutility
    print("Importing MARS Blender Tools modules.")

import bpy
#import sys
#sys.path.append('/usr/lib/python3/dist-packages/') #TODO: make this work on any system!!!
#import yaml

def register():
    mtcontrollers.register()
    mtexport.register()
    mtgui.register()
    mtimport.register()
    mtjoints.register()
    mtmisctools.register()
    mtsensors.register()
    mtutility.register()
    bpy.utils.register_module(__name__)

def unregister():
    mtcontrollers.unregister()
    mtexport.unregister()
    mtgui.unregister()
    mtimport.unregister()
    mtjoints.unregister()
    mtmisctools.unregister()
    mtsensors.unregister()
    mtutility.unregister()
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
