
import ruamel.yaml
import datetime
"""
read_yaml is to read a yaml file and convert it into python.
write_yaml is to convert a dictionary into a yaml file.

Examples
--------
>>> read_yaml('mytest')
# reads 'mytest' and converts it to a dictionary in python

>>> write_yaml({'green': 'hello'}, ('mytest2.yml'))
# converts a dictionary into yaml file ('mytest2.yml').

>>> append_yaml({'blue': 'bonjour'}, ('mytest2.yml'))
# appends the new dictionary to the existing ('mytest2.yml') file.

"""
# load the configuration
def read_yaml(myfile):
	with open(myfile, 'r') as file:
		yaml = ruamel.yaml.YAML()    
		cfg = yaml.load(file)
	return cfg


def write_yaml(my_dict, myfile):
	with open(myfile, 'w') as file:  
		yaml = ruamel.yaml.YAML()     
		yaml.dump(my_dict, file)


def append_yaml(my_dict, myfile):
	with open(myfile, 'a') as file:  
		yaml = ruamel.yaml.YAML()    
		yaml.dump(my_dict, file)

def time_yaml(myfile):
	with open(myfile, 'a') as file:
		yaml = ruamel.yaml.YAML() 
		my_dict = {}
		my_dict['hr'] = datetime.datetime.now()
		my_dict['unix'] = datetime.datetime.now().timestamp()        #in seconds
		yaml.dump(my_dict, file)

