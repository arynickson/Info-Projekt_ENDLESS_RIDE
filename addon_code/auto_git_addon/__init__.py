bl_info = {
    "name": "Screenshot-Tool",
    "blender": (4, 0, 0),
    "category": "Import-Export",
}

import bpy

class MyProp(bpy.types.PropertyGroup):
# filepath custom property
    filepath : bpy.props.StringProperty(name="Filepath", default="//output.png", description="Where to save Screenshots", subtype="FILE_PATH") 


class screenshot_nodes(bpy.types.Operator):
# custom screenshot operator
    bl_idname = "screen.screenshot_nodes"
    bl_label = "Screenshot Nodetree"

    def execute(self, context):
        for area in bpy.context.screen.areas:
            if area.type == 'NODE_EDITOR':
                

                if context.scene.my_tool.filepath is not None:
                    filepath = context.scene.my_tool.filepath

                
                bpy.ops.wm.context_toggle(data_path='space_data.show_region_ui')
                bpy.ops.screen.screenshot_area(filepath=filepath, hide_props_region=True)
        
        bpy.ops.wm.context_toggle(data_path='space_data.show_region_ui')
        return {'FINISHED'}


class Screenshot_Panel(bpy.types.Panel):
# UI für das addon
    bl_label = "Screenshot-Tool"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Screenshot-Tool"


    @classmethod
    def poll(cls, context):
        return (context.object is not None)
    
    def execute(self, context):
        pass

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene.my_tool, "filepath")
        layout.operator("screen.screenshot", text="Save Screenshot")
        for area in bpy.context.screen.areas:
            if area.type == 'NODE_EDITOR':
                layout.operator(screenshot_nodes.bl_idname, text="Save Nodetree")



bpy.utils.register_class(Screenshot_Panel)
bpy.utils.register_class(screenshot_nodes)
bpy.utils.register_class(MyProp)


def register():
    print("Hello World")
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=MyProp)

def unregister():
    print("Tschau")

if __name__ == "__main__":
    register()