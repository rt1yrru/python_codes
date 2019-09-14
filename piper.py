import pip._internal
def a_pip(cmd):
	return pip._internal.main([cmd])
