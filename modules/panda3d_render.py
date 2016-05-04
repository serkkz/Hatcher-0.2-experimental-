import bpy

class RenderPanda3D(bpy.types.RenderEngine):
    bl_idname = "Panda3D"
    bl_label = "Panda3D"
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