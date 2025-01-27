bl_info = {
    "name": "Pixel-Texture-Scaling-Calc",
    "blender": (4, 0, 0),
    "category": "Object",
}

import bpy
import subprocess

def auto_copy(txt):
    cmd='echo '+str(txt).strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

class PixelScalingCalc(bpy.types.Panel):

    bl_label = "Pixel-Scaling-Calc"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Pixel-Scaling-Calc"

    @classmethod
    def poll(cls, context):
        return (context.object is not None)
    
    def draw(self, context):
        layout = self.layout
        scene = bpy.context.scene
        ### liste aller 3druler längen
        seitenlaengen = list((s.points[0].co - s.points[-1].co).length for s in bpy.data.grease_pencils["Annotations"].layers["RulerData3D"].frames[0].strokes)

        ### loop durch bereich layout um grid scale zu finden
        for area in bpy.data.screens["Layout"].areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        grid_scaling_var = space.overlay.grid_scale
                        break
        
        ### einfach seitenlänge vom 3druler durch die grid size für seitenlänge in pixeln
        if len(seitenlaengen) != 0:
            calc_pixel_scaling = round(seitenlaengen[-1] // grid_scaling_var)
        else:
            calc_pixel_scaling = 0
        box = layout.box()
        ### text set
        box.label(text="Measured length in px: "+str(calc_pixel_scaling))
        
        ### berechneten scaling wert zu clipboard automatisch kopieren
        auto_copy(calc_pixel_scaling)
        scene = bpy.context.scene
 


bpy.utils.register_class(PixelScalingCalc)


def register():
    print("Hello World")

def unregister():
    print("Tschau")

if __name__ == "__main__":
    register()
