import pandas as pd
from owlready2 import *
dogBread = pd.read_csv('./AKC_Popular_Breeds_2013-2016.csv',encoding='utf-8')['Breed']
onto = get_ontology('dogBreeds.owl')

with onto:
    class Dog(Thing):
        pass
    class Breeds(Thing):
        pass
    class is_breed_of(ObjectProperty):
        domain = [Dog]
        range = [Breeds]

my_dog = Dog("Bobo")

my_dog_breeds = Breeds("黃金獵犬")

my_dog.is_breed_of = [my_dog_breeds]

print(my_dog.is_breed_of)

mix = Breeds("白金獵犬")

my_dog.is_breed_of.append(mix)
print(my_dog.is_breed_of)




