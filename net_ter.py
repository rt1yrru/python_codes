import netifaces

def display():
    for _i in netifaces.interfaces():
	      return (netifaces.ifaddresses(_i))
