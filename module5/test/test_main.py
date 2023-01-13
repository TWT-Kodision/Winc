from main import get_none, flatten_dict

def test_get_none():
    assert get_none() == None, "dit is een test"


def test_output_is_list(output):
   assert type(output) is list, 'output is not a list'
   print ('output is list')

def test_simple_dict(output):
    for number in output:
        print (number)
        assert type(number) is int or type(number) is float, 'output is not a simpel list'

def test_complex_list(output):
    for item in output:
        print (item)
        assert type(item) is int or type(item) is dict or type(item) is float, 'output is not a simpel or complex list'


print (flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}}))
print(test_output_is_list(flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})))
#print(test_simple_dict(flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}))) 
print(test_complex_list(flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})))
  

