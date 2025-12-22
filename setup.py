from setuptools import find_packages, setup
from typing import list
HYPEN_E_DOT= '-e.'
def get_requirement(file_path:str)-> list[str]:
    requirement=[]
    with open(file_path) as file_obj:
        requirement= file_obj.readlines()
        requirement=[ req.replace("\n"," ") for req in requirement]
        if HPEN_E_DOT in requirement :
            requirement.remove(HPEN_E_DOT)
    return requirement
     

setup (
    name = 'my first ML project',
    version= '0.0.1',
    author= ' tushar',
    author_email= ' tc3158494@gmail.com',
    packages = find_packages(),
    install_requires= get_requirement('requirement.txt')
)
