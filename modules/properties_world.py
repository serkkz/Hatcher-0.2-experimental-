import bpy
from bpy.types import Panel
from rna_prop_ui import PropertyPanel


class WorldButtonsPanel:
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'

    @classmethod
    def poll(cls, context):
        return context.world and (context.scene.render.engine in cls.COMPAT_ENGINES)


class MATERIAL(WorldButtonsPanel, Panel):
    bl_label = "Materials and textures"
    COMPAT_ENGINES = {'Panda3D:Hatcher'}

    def draw(self, context):
    
        if hasattr(bpy.context.active_object.active_material, 'name'):
            self.layout.template_preview(context.active_object.active_material)
        
        
if __name__ == "__main__":
    bpy.utils.register_module(__name__)
