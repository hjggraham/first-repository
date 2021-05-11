
import ruamel.yaml
import datetime
"""
read_yaml is to read a yaml file and convert it into python.
write_yaml is to convert a dictionary into a yaml file.
append_yaml is to append dictionaries to a yaml file.
time_yaml is to create timestamps and add them to a yaml file.

Examples
--------
>>> read_yaml('mytest')
# reads 'mytest' and converts it to a dictionary in python

>>> write_yaml({'green': 'hello'}, ('mytest2.yml'))
# converts a dictionary into yaml file ('mytest2.yml').

>>> append_yaml({'blue': 'bonjour'}, ('mytest2.yml'))
# appends the new dictionary to the existing ('mytest2.yml') file.

>>> time_yaml('myfile', 'hello', 'first stage')
# creates a time stamp with a comment, "hello", under the dictionary "first stage" in "myfile"

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


def time_yaml(myfile, mycomment, stage):
	with open(myfile, 'a') as file:
		yaml = ruamel.yaml.YAML() 
		my_dict = {stage: {}}
		my_dict[stage]['hr'] = datetime.datetime.now()
		my_dict[stage]['unix'] = datetime.datetime.now().timestamp()        #in seconds
		my_dict[stage]['mycomment'] = mycomment
		yaml.dump(my_dict, file)


def get_last_stage(myfile):
	try:
		my_dict=read_yaml(myfile)
		return list(my_dict.keys())[-1]+1
	except:
		return 0


def tag1_it(myfile, mycomment):
	stage = get_last_stage(myfile)
	with open(myfile, 'a') as file:
		yaml = ruamel.yaml.YAML() 
		my_dict = {stage: {}}
		my_dict[stage]['hr'] = datetime.datetime.now()
		my_dict[stage]['unix'] = datetime.datetime.now().timestamp()        #in seconds
		my_dict[stage]['mycomment'] = mycomment
		yaml.dump(my_dict, file)

