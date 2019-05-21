#bpy.data.objects['Armature'].pose.bones['Bone'].bone.select=True
#bpy.ops.tranform.rotate(value=3.142/4,axis=(1,0,0))
#bpy.data.objects['Armature'].pose.bones['Bone'].bone.select=False
 
import pickle
def savep( name ):
    state={}
    for bones in bpy.data.objects['Armature'].pose.bones:
        v=bones.rotation_quaternion
        vector={}
        vector['w']=v[0]
        vector['x']=v[1]
        vector['y']=v[2]
        vector['z']=v[3]
        state[bones.name]=vector
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(state, f, pickle.HIGHEST_PROTOCOL)
 
def loadp(name ):
    state=None
    with open(name + '.pkl', 'rb') as f:
        state= pickle.load(f)
    for i in state:
        bpy.data.objects['Armature'].pose.bones[i].rotation_quaternion[0]=state[i]['w']
        bpy.data.objects['Armature'].pose.bones[i].rotation_quaternion[1]=state[i]['x']
        bpy.data.objects['Armature'].pose.bones[i].rotation_quaternion[2]=state[i]['y']
        bpy.data.objects['Armature'].pose.bones[i].rotation_quaternion[3]=state[i]['z']
