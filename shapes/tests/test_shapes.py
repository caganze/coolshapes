import numpy as np
from wisps import Box, Selector,RotatedBox
import numpy as np
import pandas as pd
import pytest

x=np.random.random(100)
y=np.random.random(100)

df=pd.DataFrame([x, y]).transpose()
df.columns=['x', 'y']

b1=Box()
b2=RotatedBox()

def test_box():
	b1.data=df
	b2.data=df
	assert b1.area >0.0
	assert len(b1.select(df)) >0.0
	

def test_selector():
	s=Selector()
	assert len(s) == 0
	s.shapes=[b1, b2]
	s.logic='and'
	s.select()
	assert len(s) >1.0
    