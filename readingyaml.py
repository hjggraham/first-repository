
import ruamel.yaml
import datetime

# load the configuration
def read_yaml(myfile, verbose=False):
	"""
	read_yaml is to read a yaml file and convert it into python.

	Example
	--------
	>>> read_yaml('mytest')
	# reads 'mytest' and converts it to a dictionary in python.
	"""
	try: 
		with open(myfile, 'r') as file:
			yaml = ruamel.yaml.YAML()    
			my_dict = yaml.load(file)
		return my_dict
	except FileNotFoundError:
		if verbose: print('FileNotFoundError, empty dict')
		my_dict = {}
		return my_dict
	except ruamel.yaml.constructor.DuplicateKeyError:
		my_dict = {}
		return my_dict
	except Exception as e: 
		print(e.__class__)
		return None


def write_yaml(my_dict, myfile):
	"""
	write_yaml is to convert a dictionary into a yaml file.
	
	Examples
	--------

	>>> write_yaml({'green': 'hello'}, ('mytest2.yml'))
	# converts a dictionary into yaml file ('mytest2.yml').
	"""	
	with open(myfile, 'w') as file:  
		yaml = ruamel.yaml.YAML()     
		yaml.dump(my_dict, file)


def append_yaml(my_dict, myfile):
	"""
	append_yaml is to append dictionaries to a yaml file.

	Examples
	--------
	>>> append_yaml({'blue': 'bonjour'}, ('mytest2.yml'))
	# appends the new dictionary to the existing ('mytest2.yml') file.
	"""	
	with open(myfile, 'a') as file:  
		yaml = ruamel.yaml.YAML()    
		yaml.dump(my_dict, file)



def get_last_stage(myfile, verbose=True):
	my_dict=read_yaml(myfile, verbose)
	try:
		return list(my_dict.keys())[-1]+1
	except IndexError:
		if verbose: print('IndexError, I consider 0 as first item')
		return 0
	except Exception as e: 
		print(e.__class__)
		return 0


def tag_it(myfile, mycomment):
	"""
	tag_it is to create timestamps and add them to a yaml file.

	Examples
	--------
	>>> tag_it('myfile', 'hello')
	# creates a time stamp with a comment, "hello", in "myfile"
	"""	
	stage = get_last_stage(myfile)
	with open(myfile, 'a') as file:
		yaml = ruamel.yaml.YAML() 
		my_dict = {stage: {}}
		my_dict[stage]['hr'] = datetime.datetime.now()
		my_dict[stage]['unix'] = datetime.datetime.now().timestamp()        #in seconds
		my_dict[stage]['mycomment'] = mycomment
		yaml.dump(my_dict, file)

