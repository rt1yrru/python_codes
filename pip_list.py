from pip._internal.utils.misc import get_installed_distributions as _base
def display():
 	for _i in _base:
 		print('project_name : {} , version : {} , Path : {}'.format(_i.project_name,_i.version,_i.location))
