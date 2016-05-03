# -*- coding: utf-8 -*-
bl_info = {"name": "ToolsR", 
           "description": "ToolsR", 
           "author": "serg-kkz", 
           "version": (0, 1), 
           "blender": (2, 7, 6),
           "location": "3D view > Hatcher", 
           "warning": "", 
           "wiki_url": "", 
           "tracker_url": "",
           "category": "Panda3DR"}
import bpy


class CustomRenderEngine(bpy.types.RenderEngine):

    bl_idname = "Panda3D:Hatcher"
    bl_label = "Panda3D:Hatcher"
    bl_use_preview = True


    def render(self, scene):
        scale = scene.render.resolution_percentage / 100.0
        self.size_x = int(scene.render.resolution_x * scale)
        self.size_y = int(scene.render.resolution_y * scale)

        if self.is_preview:
            self.render_preview(scene)
        else:
            self.render_scene(scene)

    def render_preview(self, scene):
    
        pixel_count = self.size_x * self.size_y
        green_rect = [[0.0, 1.0, 0.0, 1.0]] * pixel_count
        result = self.begin_result(0, 0, self.size_x, self.size_y)
        layer = result.layers[0].passes["Combined"]
        layer.rect = green_rect
        self.end_result(result)


    def render_scene(self, scene):
    
        pixel_count = self.size_x * self.size_y
        blue_rect = [[0.0, 0.0, 1.0, 1.0]] * pixel_count
        result = self.begin_result(0, 0, self.size_x, self.size_y)
        layer = result.layers[0].passes["Combined"]
        layer.rect = blue_rect
        self.end_result(result)


def register():
    bpy.utils.register_class(CustomRenderEngine)

    from bl_ui import ( properties_render, properties_material,)
    properties_render.RENDER_PT_render.COMPAT_ENGINES.add(CustomRenderEngine.bl_idname)
    properties_material.MATERIAL_PT_preview.COMPAT_ENGINES.add(CustomRenderEngine.bl_idname)


def unregister():
    bpy.utils.unregister_class(CustomRenderEngine)

    from bl_ui import ( properties_render, properties_material,)
    properties_render.RENDER_PT_render.COMPAT_ENGINES.remove(CustomRenderEngine.bl_idname)
    properties_material.MATERIAL_PT_preview.COMPAT_ENGINES.remove(CustomRenderEngine.bl_idname)
