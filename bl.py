import pickle
import numpy as np

# 'Bone.003'
# 'Bone.002'

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
    


class bonedata():
    
    def __init__(self):    
        self.state=[]
            
    def euler_to_quaternion(self,r):
        (yaw, pitch, roll) = (r[0], r[1], r[2])
        qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
        qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
        qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
        qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
        return [qx, qy, qz, qw]

    def add(self,id,x,y,z,f):
        vector={}
        v=self.euler_to_quaternion((x,y,z))

        vector['x']=v[0]
        vector['y']=v[1]
        vector['z']=v[2]
        vector['w']=v[3]
        vector["frame"]=frame
        vector["bone"]=bone
        self.state.append(vector)
        
    def save(self,name="bonedata.sv"):
        with open(name + '.pkl', 'wb') as f:
            pickle.dump(state, f, pickle.HIGHEST_PROTOCOL)

            
class loadbonedata():

    def __init__(self,name="bonedata.sv"): 
        with open(name) as f:
            self.state= pickle.load(f)

    def load(self):
        for i in state:
            bpy.context.scene.frame_current = [i]["frame"]
            bpy.data.objects['Armature'].pose.bones[i["bone"]].rotation_quaternion[0]=i['w']
            bpy.data.objects['Armature'].pose.bones[i["bone"]].rotation_quaternion[1]=i['x']
            bpy.data.objects['Armature'].pose.bones[i["bone"]].rotation_quaternion[2]=i['y']
            bpy.data.objects['Armature'].pose.bones[i["bone"]].rotation_quaternion[3]=i['z']
