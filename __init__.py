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

# Собираем директорию исходных файлов блендера
adress_bl_ui = os.path.join(os.getcwd(), str(bpy.app.version[0])+'.'+str(bpy.app.version[1]), 'scripts', 'startup',  'bl_ui')  

# Собираем адрес директории для резервных копий исходных файлов блендера
adress_dir_backup = os.path.join(os.getcwd(), str(bpy.app.version[0])+'.'+str(bpy.app.version[1]), 'scripts', 'startup', 'bl_ui', 'backup')

# Собираем директорию модифицированых файлов расположеных в папке аддона
dir_modified_files = os.path.join(os.path.dirname(__file__), 'modules', 'modified_files') 


def register():

    # Проверяем на существование директории.
    if os.path.exists(adress_dir_backup):

        print('')
        print('Directory backup exist\n')
        
    else:
    
        print('')
        print('Instail mod\n')
        
        # Если её не оказалось то создаем
        os.makedirs(adress_dir_backup, mode=0o777, exist_ok=False)
        
        print('Create folder: backup')
        print('Directory: '+ adress_bl_ui +'\n')
        
        # Получаем список всех модифицированых файлов
        modified_files = os.listdir(path=dir_modified_files)   
        
        # Проходим по списку извлекая имена
        for name in modified_files:
            
            # Собираем полный адрес исходных файлов расположенных в папке bl_ui блендера
            full_adress_sourse = os.path.join(adress_bl_ui, name)       

            # Делаем копию файла и размещаем в директории backup.
            shutil.copy(full_adress_sourse, adress_dir_backup)
            
            print('Copy file: ' + full_adress_sourse)
            print('Directory: ' + adress_dir_backup + '\n')
            
            # Собираем полный адрес файлов расположенных в папке модифицированых файлов
            full_adress_mod = os.path.join(dir_modified_files, name)
            
            # Делаем копию файла и размещаем в директории bl_ui.
            shutil.copy(full_adress_mod, adress_bl_ui)
            
            print('Replace file: ' + full_adress_sourse)
            print('File: ' + full_adress_mod + '\n')
            

        print('Instail finih\n')
        
    bpy.utils.register_class(RenderPanda3D)

    from bl_ui import ( properties_render, properties_material,)
    properties_render.RENDER_PT_render.COMPAT_ENGINES.add(RenderPanda3D.bl_idname)
    properties_material.MATERIAL_PT_preview.COMPAT_ENGINES.add(RenderPanda3D.bl_idname)

def unregister():

    # Проверяем на существование директории.
    if os.path.exists(adress_dir_backup):
           
        print('')
        
        print('Uninstail mod\n')
    
        # Получаем список всех сохраненых файлов
        list_file_restore = os.listdir(path=adress_dir_backup)
        
        # Проходим по списку извлекая имена
        for name in list_file_restore:

            # Собираем полный адрес файлов расположенных в папке резевного копирования
            full_adress = os.path.join(adress_dir_backup, name)
            
            # Делаем копию файла и размещаем в директории bl_ui.
            shutil.copy(full_adress, adress_bl_ui)
            
            print ('Restore file: ' + full_adress)
            print ('Directory: ' + adress_bl_ui + '\n')
            
        shutil.rmtree(adress_dir_backup)

        print ('Remove directory: ' + adress_dir_backup + '\n')
        print('Uninstail finih\n')
        
    else:
    
        print('No backup directory\n' )

    bpy.utils.unregister_class(RenderPanda3D)

    from bl_ui import ( properties_render, properties_material,)
    properties_render.RENDER_PT_render.COMPAT_ENGINES.remove(RenderPanda3D.bl_idname)
    properties_material.MATERIAL_PT_preview.COMPAT_ENGINES.remove(RenderPanda3D.bl_idname)
    

