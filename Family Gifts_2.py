import random

family=[]
used_list=set()

def dfs(lst,couples):
    global family,used_list
    if len(lst)==len(family):
		if {lst[-1],lst[0]} not in couples and (lst[-1],lst[0]) not in used_list:
			for i in range(len(lst)):
				used_list.add((lst[i],lst[(i+1)%len(lst)]))
			return lst
    else:
		family2=family
		random.shuffle(family2)
		for e in family2:
			if e not in lst and {lst[-1],e} not in couples and (lst[-1],e) not in used_list:
				x=dfs(lst+[e],couples)
				if x:return x
    return []

def perform(couples):
	global family,used_list
	used_list=set()
	ret=[]
	for e in family:
		#if any(e in f for f in couples):
			while True:
				x=dfs([e],couples)
				if not x:break
				ret.append(x)
	return ret

def find_chains(_family, couples):
	global family,used_list
	'''
	n={
		(3,1):0,
		(4,2):2,
		(6,2):4,
		(5,2):2,
		(6,3):4,
		(9,3):6,
		(10,5):8,
		(9,0):8,
		(9,1):7,
		(10,2):7,
		(17,5):14,
	}[(len(_family),len(couples))]
	'''
	family=list(_family)
	ret=[]
	for i in range(10):
		r=perform(couples)
		if len(r)>len(ret):
			ret=r
	return ret