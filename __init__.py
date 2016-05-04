# -*- coding: utf-8 -*-
bl_info = {"name": "Tools", 
           "description": "Utilities to work with the engine Panda3D", 
           "author": "serg-kkz", 
           "version": (0, 1, 0), 
           "blender": (2, 7, 6),
           "location": "3D view > Hatcher", 
           "warning": "", 
           "wiki_url": "", 
           "tracker_url": "",
           "category": "Panda3D"}
           
import bpy
import sys
import os
import shutil

from .modules.panda3d_render import RenderPanda3D

# Директория исходных файлов блендера
adress_bl_ui = os.path.join(os.getcwd(), str(bpy.app.version[0])+'.'+str(bpy.app.version[1]), 'scripts', 'startup',  'bl_ui')  

# Собираем адрес директории для резервных копий исходных файлов блендера
adress_dir_backup = os.path.join(os.getcwd(), str(bpy.app.version[0])+'.'+str(bpy.app.version[1]), 'scripts', 'startup', 'bl_ui', 'backup')

# Aдрес файла исходника блендера properties_world.py
properties_world = os.path.join(os.getcwd(), str(bpy.app.version[0])+'.'+str(bpy.app.version[1]), 'scripts', 'startup',  'bl_ui', 'properties_world.py')    

def register():

    # Проверяем на существование директории.
    if os.path.exists(adress_dir_backup):
    
        print('Directory backup exist')
        
    else:

        # Если её не оказалось то создаем
        os.makedirs(adress_dir_backup, mode=0o777, exist_ok=False)
        print('Create a directory backup')
        
        # Делаем копию файла properties_world.py и размещаем в директории резевного копирования.
        shutil.copy(properties_world, adress_dir_backup)
        print('properties_world.py copied to the backup directory')

        # Собираем адрес файла расположеного в папке аддона которым подменим  файл блендера properties_world.py
        properties_world_mod = os.path.join(os.path.dirname(__file__), 'modules', 'properties_world.py')   
        
        # Копируем properties_world.py и из папки адонна в блендер.
        shutil.copy(properties_world_mod, adress_bl_ui)
        print('Copy properties_world.py to the blender directory')

    bpy.utils.register_class(RenderPanda3D)

    from bl_ui import ( properties_render, properties_material,)
    properties_render.RENDER_PT_render.COMPAT_ENGINES.add(RenderPanda3D.bl_idname)
    properties_material.MATERIAL_PT_preview.COMPAT_ENGINES.add(RenderPanda3D.bl_idname)

def unregister():

    # Проверяем на существование директории.
    if os.path.exists(adress_dir_backup):
    
        # Получаем список всех сохраненых файлов
        list_file_restore = os.listdir(path=adress_dir_backup)
        
        # Проходим по списку извлекая имена
        for name in list_file_restore:

            # Собираем полный адрес файлов расположенных в папке резевного копирования
            full_adress = os.path.join(adress_dir_backup, name)
            
            # Делаем копию файла и размещаем в директории bl_ui.
            shutil.copy(full_adress, adress_bl_ui)
            #print (list_file_restore[name]))
            
        shutil.rmtree(adress_dir_backup)
        print ('Remove directory' + adress_bl_ui)
        
    else:
    
        print('No backup directory')

    bpy.utils.unregister_class(RenderPanda3D)

    from bl_ui import ( properties_render, properties_material,)
    properties_render.RENDER_PT_render.COMPAT_ENGINES.remove(RenderPanda3D.bl_idname)
    properties_material.MATERIAL_PT_preview.COMPAT_ENGINES.remove(RenderPanda3D.bl_idname)
    

