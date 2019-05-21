Python 3.5.6 |Anaconda, Inc.| (default, Aug 26 2018, 16:05:27) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
==================== RESTART: E:\workspace\blender\bl.py ====================
Traceback (most recent call last):
  File "E:\workspace\blender\bl.py", line 1, in <module>
    bpy.data.objects['Armature'].pose.bones['Bone'].bone.select=True
NameError: name 'bpy' is not defined
>>> import math as m
>>> import numpy as np
>>> m.asin(3.142/2)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    m.asin(3.142/2)
ValueError: math domain error
>>> m.asin(90)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    m.asin(90)
ValueError: math domain error
>>> m.asin(3.142)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    m.asin(3.142)
ValueError: math domain error
>>> m.acos(3.142)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    m.acos(3.142)
ValueError: math domain error
>>> m.acos(1)
0.0
>>> m.acos(0.5)
1.0471975511965979
>>> np.degrees(m.acos(0.5))
60.00000000000001
>>> np.degrees(m.asin(0.5))
30.000000000000004
>>> bone': [Vector((0.08089639246463776, 0.5640865564346313, 0.9844207763671875)), Vector((0.02505994588136673, -0.2973966598510742, 1.097610592842102))]}
SyntaxError: EOL while scanning string literal
>>> vec1=[0.08089639246463776, 0.5640865564346313, 0.9844207763671875]
>>> vec2=[0.02505994588136673, -0.2973966598510742, 1.097610592842102]
>>> x=np.degrees(m.asin(np.sqrt((0.08089639246463776*0.08089639246463776+0.5640865564346313*0.5640865564346313+0.9844207763671875*0.9844207763671875)/0.08089639246463776)))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x=np.degrees(m.asin(np.sqrt((0.08089639246463776*0.08089639246463776+0.5640865564346313*0.5640865564346313+0.9844207763671875*0.9844207763671875)/0.08089639246463776)))
ValueError: math domain error
>>> x=np.degrees(m.asin(np.sqrt((0.08089639246463776*0.08089639246463776+0.5640865564346313*0.5640865564346313+0.9844207763671875*0.9844207763671875))/0.08089639246463776))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x=np.degrees(m.asin(np.sqrt((0.08089639246463776*0.08089639246463776+0.5640865564346313*0.5640865564346313+0.9844207763671875*0.9844207763671875))/0.08089639246463776))
ValueError: math domain error
>>> np.sqrt((0.08089639246463776*0.08089639246463776+0.5640865564346313*0.5640865564346313+0.9844207763671875*0.9844207763671875))/0.08089639246463776
14.060738567661781
>>> np.sqrt((0.08089639246463776*0.08089639246463776+0.5640865564346313*0.5640865564346313+0.9844207763671875*0.9844207763671875))
1.137463025512236
>>> x=np.degrees(m.acos(np.sqrt(0.08089639246463776/(0.08089639246463776*0.08089639246463776+0.5640865564346313*0.5640865564346313+0.9844207763671875*0.9844207763671875))))
>>> x
75.51951439482215
>>> m.acos(np.sqrt(0.08089639246463776/(0.08089639246463776*0.08089639246463776+0.5640865564346313*0.5640865564346313+0.9844207763671875*0.9844207763671875)))
1.3180641756968994
>>> 0.02505994588136673, -0.2973966598510742, 1.097610592842102
(0.02505994588136673, -0.2973966598510742, 1.097610592842102)
>>> m.acos(np.sqrt(0.08089639246463776/(0.08089639246463776*0.08089639246463776+0.5640865564346313*0.5640865564346313+0.9844207763671875*0.9844207763671875)))
1.3180641756968994
>>> m.acos(np.sqrt(0.02505994588136673/(0.02505994588136673*0.02505994588136673+-0.2973966598510742*-0.2973966598510742+1.097610592842102*1.097610592842102)))
1.4311707858660794
>>> np.degrees(m.acos(np.sqrt(0.02505994588136673/(0.02505994588136673*0.02505994588136673+-0.2973966598510742*-0.2973966598510742+1.097610592842102*1.097610592842102))))
82.00004579254764
>>> 82.00004579254764-75.51951439482215
6.4805313977254855
>>> 
==================== RESTART: E:\workspace\blender\bl.py ====================
Traceback (most recent call last):
  File "E:\workspace\blender\bl.py", line 1, in <module>
    bpy.data.objects['Armature'].pose.bones['Bone'].bone.select=True
NameError: name 'bpy' is not defined
>>> angles(0.02505994588136673, -0.2973966598510742, 1.097610592842102)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    angles(0.02505994588136673, -0.2973966598510742, 1.097610592842102)
NameError: name 'angles' is not defined
>>> 
==================== RESTART: E:\workspace\blender\bl.py ====================
>>> angles(0.02505994588136673, -0.2973966598510742, 1.097610592842102)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    angles(0.02505994588136673, -0.2973966598510742, 1.097610592842102)
  File "E:\workspace\blender\bl.py", line 9, in angles
    x_ang=np.degrees(m.mcos(x/(np.sqrt(x*x+y*y+z*z))))
AttributeError: module 'math' has no attribute 'mcos'
>>> 
==================== RESTART: E:\workspace\blender\bl.py ====================
>>> angles(0.02505994588136673, -0.2973966598510742, 1.097610592842102)
(0.02505994588136673, -0.2973966598510742, 1.097610592842102)
>>> 
==================== RESTART: E:\workspace\blender\bl.py ====================
>>> angles(0.02505994588136673, -0.2973966598510742, 1.097610592842102)
(88.73758928928957, 105.15648229230935, 15.211492466311858)
>>> angles(0.02505994588136673, -0.2973966598510742, 1.097610592842102)
(88.73758928928957, 105.15648229230935, 15.211492466311858)
>>> angles(0.02505994588136673, -0.2973966598510742, 1.097610592842102)
(88.73758928928957, 105.15648229230935, 15.211492466311858)
>>> angles(0.08089639246463776, 0.5640865564346313, 0.9844207763671875)
(85.92168004574144, 60.26980375446668, 30.06552890564543)
>>> a=np.array(88.73758928928957, 105.15648229230935, 15.211492466311858)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a=np.array(88.73758928928957, 105.15648229230935, 15.211492466311858)
ValueError: only 2 non-keyword arguments accepted
>>> a=np.array([88.73758928928957, 105.15648229230935, 15.211492466311858])
>>> b=np.array([85.92168004574144, 60.26980375446668, 30.06552890564543])
>>> a-b
array([  2.81590924,  44.88667854, -14.85403644])
>>> np.radians(2.815)
0.04913101844364037
>>> angles(0,1,0.5)
(90.0, 26.565051177077994, 63.43494882292201)
>>> 0/5
0.0
>>> from np import *
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    from np import *
ImportError: No module named 'np'
>>> from numpy import *
>>> cos(90)
-0.4480736161291701
>>> cos(radians(45))
0.7071067811865476
>>> angles(0,1,0.7)
(90.0, 34.99202019855866, 55.00797980144134)
>>> angles(0,0.7,0.7)
(90.0, 45.0, 45.0)
>>> angles(0,0,0.7)
(90.0, 90.0, 0.0)
>>> angles(0,0,0)

Warning (from warnings module):
  File "E:\workspace\blender\bl.py", line 9
    x_ang=np.degrees(m.acos(x/(np.sqrt(x*x+y*y+z*z))))
RuntimeWarning: invalid value encountered in double_scalars

Warning (from warnings module):
  File "E:\workspace\blender\bl.py", line 10
    y_ang=np.degrees(m.acos(y/(np.sqrt(x*x+y*y+z*z))))
RuntimeWarning: invalid value encountered in double_scalars

Warning (from warnings module):
  File "E:\workspace\blender\bl.py", line 11
    z_ang=np.degrees(m.acos(z/(np.sqrt(x*x+y*y+z*z))))
RuntimeWarning: invalid value encountered in double_scalars
(nan, nan, nan)
>>> angles(1,1,1)
(54.735610317245346, 54.735610317245346, 54.735610317245346)
>>> angles(0,1,1)angles(0,0,0)
SyntaxError: invalid syntax
>>> angles(0,1,1)
(90.0, 45.00000000000001, 45.00000000000001)
>>> sqrt(1+1)
1.4142135623730951
>>> angles(0,0,1.4)
(90.0, 90.0, 0.0)
>>> x=angles(0.08089639246463776, 0.5640865564346313, 0.9844207763671875)
>>> y=angles(0.02505994588136673, -0.2973966598510742, 1.097610592842102)
>>> x+y
(85.92168004574144, 60.26980375446668, 30.06552890564543, 88.73758928928957, 105.15648229230935, 15.211492466311858)
>>> x
(85.92168004574144, 60.26980375446668, 30.06552890564543)
>>> y
(88.73758928928957, 105.15648229230935, 15.211492466311858)
>>> x=array([x])
>>> x
array([[85.92168005, 60.26980375, 30.06552891]])
>>> y=array([y])
>>> x-y
array([[ -2.81590924, -44.88667854,  14.85403644]])
>>> angle(0.08295748382806778, 0.6117605566978455, 0.9553476572036743)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    angle(0.08295748382806778, 0.6117605566978455, 0.9553476572036743)
TypeError: angle() takes from 1 to 2 positional arguments but 3 were given
>>> angles(0.08295748382806778, 0.6117605566978455, 0.9553476572036743)
(85.81758920231601, 57.46403034909137, 32.87113596786619)
>>> x=angles(0.4720208942890167, -0.8074203133583069, 0.6473721265792847))
SyntaxError: invalid syntax
>>> x=angles(0.4720208942890167, -0.8074203133583069, 0.6473721265792847)
>>> x=array(x)
>>> y=angles(0.08295748382806778, 0.6117605566978455, 0.9553476572036743)
>>> y=array(y)
>>> x+y
array([151.29972486, 192.68618762,  88.18107547])
>>> x-y
array([-20.33545355,  77.75812692,  22.43880353])
>>> degrees(x)
array([3751.85000661, 7747.65890838, 3169.02609841])
>>> radians(x-y)
array([-0.35492062,  1.35713534,  0.391631  ])
>>> x=array((0.0, -0.7071787714958191, 0.7070348262786865))
>>> 
>>> x
array([ 0.        , -0.70717877,  0.70703483])
>>> y=array((0,0,1))
>>> y
array([0, 0, 1])
>>> x=array(angles(0.0, -0.7071787714958191, 0.7070348262786865))
>>> x
array([ 90.        , 135.00583183,  45.00583183])
>>> y=array(angles(0,0,1))
>>> y
array([90., 90.,  0.])
>>> x-y
array([ 0.        , 45.00583183, 45.00583183])
>>> x=array(angles(0.7071787714958191, -0.5000211000442505, 0.49987709522247314)))
SyntaxError: invalid syntax
>>> x=array(angles(0.7071787714958191, -0.5000211000442505, 0.49987709522247314))
>>> x
array([ 44.99416717, 120.00139555,  60.00813141])
>>> x=array(angles((0.5059449672698975, -0.3106348216533661, 0.8046898245811462))
	)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    x=array(angles((0.5059449672698975, -0.3106348216533661, 0.8046898245811462))
TypeError: angles() missing 2 required positional arguments: 'y' and 'z'
>>> x=array(angles(0.5059449672698975, -0.3106348216533661, 0.8046898245811462))

	
>>> x
array([ 59.60589876, 108.0974918 ,  36.41969002])
>>> x=array(angles(0.0, -0.7071787714958191, 0.7070348262786865))
>>> x
array([ 90.        , 135.00583183,  45.00583183])
>>> y=array(angles(0.5, -0.7071787714958191, 0.49989819526672363))
>>> y
array([ 60.00000034, 135.00583297,  60.00673546])
>>> x-y
array([ 2.99999997e+01, -1.14442977e-06, -1.50009036e+01])
>>> x
array([ 90.        , 135.00583183,  45.00583183])
>>> array([ 2.99999997e+01, -1.14442977e-06, -1.50009036e+01]).dtype=float32
>>> a=array([ 2.99999997e+01, -1.14442977e-06, -1.50009036e+01]).dtype=float32
>>> a
<class 'numpy.float32'>
>>> a=array([ 2.99999997e+01, -1.14442977e-06, -1.50009036e+01)
	
SyntaxError: invalid syntax
>>> a=array([ 2.99999997e+01, -1.14442977e-06, -1.50009036e+01])
>>> a.dtype=float32
>>> a
array([-6.4257221e+35,  2.9687498e+00, -1.2071496e+14, -3.5000065e-01,
        1.2434942e+29, -2.7187781e+00], dtype=float32)
>>> loat32'>>>> a=array([ 2.99999997e+01
SyntaxError: EOL while scanning string literal
>>> 2.99999997e+01
29.9999997
>>> x=array(angles(0.0, -6.662610054016113, 6.661253929138184))
>>> x
array([ 90.        , 135.00583166,  45.00583166])
>>> y=array(angles(0.0, -6.662610054016113, 6.661253929138184))
>>> y
array([ 90.        , 135.00583166,  45.00583166])
>>> y=array(angles(0.0, -6.662610054016113, 6.661253929138184))
>>> x=array(angles(0.0, 0.0, 9.421394348144531))
>>> x
array([90., 90.,  0.])
>>> x-y
array([  0.        , -45.00583166, -45.00583166])
>>> y
array([ 90.        , 135.00583166,  45.00583166])
>>> y-x
array([ 0.        , 45.00583166, 45.00583166])
>>> y
array([ 90.        , 135.00583166,  45.00583166])
>>> x
array([90., 90.,  0.])
>>> 
