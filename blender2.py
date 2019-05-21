#bpy.data.objects['Armature'].pose.bones['Bone'].bone.select=True
#bpy.ops.tranform.rotate(value=3.142/4,axis=(1,0,0))
#bpy.data.objects['Armature'].pose.bones['Bone'].bone.select=False

import numpy as np
import math as m

def angles(x,y,z):
    x_ang=np.degrees(m.acos(x/(np.sqrt(x*x+y*y+z*z))))
    y_ang=np.degrees(m.acos(y/(np.sqrt(x*x+y*y+z*z))))
    z_ang=np.degrees(m.acos(z/(np.sqrt(x*x+y*y+z*z))))
    return (x_ang , y_ang , z_ang)

