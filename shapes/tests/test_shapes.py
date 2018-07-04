import numpy as np
import shapes
import numpy as np
import pandas as pd
import pytest
import copy 

x=np.random.random(100)
y=np.random.random(100)

df=pd.DataFrame([x, y]).transpose()
df.columns=['x', 'y']
def test_box():
	b1=shapes.Box()
	b1.data=df
	b2=copy.deepcopy(b1)
	b2.rotate(np.pi/2)
	b3=copy.deepcopy(b1)
	assert len(b3.select(df)) < len(df)
	assert len(b1) == len(b2)
	assert b2.angle != b1.angle
	