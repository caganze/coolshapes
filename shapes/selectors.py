#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:06:57 2017

@author: caganze
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Selector(object):
	"""
	A selecting tool for different shapes
	"""
	def __init__(self):
		self._logic=None
		self._data=None
		self._shapes=None
		self.logic=None
		
	def __repr__(self):
		return 'Selector with data len {}'.format(len(self))
	
	def __len__(self):
		if self._data is None:
			return 0
		else:
			return len(self.data)
        
	def __add__(self, other_selector):
		
		"allows the creation of a larger selector"
		if len(self)==0 or len(other_selector)==0 :
			return Selector()
		else:
			shapes=self.shapes+other_selector.shapes
			#data=functools.reduce(lambda left,right: pd.merge(left,right), [self.data,	 other_selector.data])
			data=pd.concat([self.data,	other_selector.data])
			New=Selector()
			New.data=data
			New.shapes=shapes
	
			if (self._logic is None) or	 (other_selector.logic is None):
				New.logic=None
	
			if (self._logic == 'and') and  (other_selector.logic =='and'):
				New.logic='and'
	
			if (self._logic == 'or') or	 (other_selector.logic =='or'):
				New.logic='or'
	
			ids=None
			if New.logic=='and':
				ids=set.intersection(*map(set,[list(self.data.index),	 list(other_selector.data.index)]))
		
			if New.logic=='or':
				ids=set().union(*[list(self.data.index),	 list(other_selector.data.index)])
			
			New.data=data.ix[ids]
			return New
	
	@property 
	def data(self):
		"""
		data
		"""
		return self._data
		
	@data.setter
	def data(self, new_data):
		self._data=new_data
	
	@property 
	def logic(self):
		"""
		logic
		"""
		return self._logic
		
	@logic.setter
	def logic(self, new_logic):
		self._logic=new_logic
	
	@property
	def shapes(self):
		return self._shapes
	
	@shapes.setter
	def shapes(self, new_shapes):
		self._shapes=new_shapes
		
	def select(self, **kwargs):
		"""
		shapes is a dictionary
		kwargs: pandas dataframe
		"""
		shapes=kwargs.get('shapes', self.shapes)
		_logic=kwargs.get('logic', self._logic)

		print ('concatenating ....')
		data=kwargs.get('data', pd.concat([s.data for s in shapes]).reset_index(drop=True))
		
		if not isinstance(_logic, str) or _logic not in ['and', 'or']:
			raise ValueError(""" Logic must 'and' or 'or' """)
		
		print ('creating points ....')
		
		#points=list(data.apply(tuple, axis=1))
    
		selected=[]
		#print(data)
		print ('selecting ....')
		
		for s in shapes:
			selected.append(list(s.select(data).index))
		
		result=None
		result_index=None
		
		#print(selected)
		if _logic =='and':
			result_index=set.intersection(*map(set,selected))
		if _logic=='or':
			result_index=set().union(*selected)
		
		result=data.ix[result_index].drop_duplicates()
		
		self._data=result
		self._shapes=shapes
	
		return result
		
		