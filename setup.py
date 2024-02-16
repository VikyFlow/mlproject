# sarà responsabile di creare la mia app di machine learning come pacchetto
# creates our application as a package itself

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(filepath:str)->List[str]: 
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    authot = 'Victoria',
    packages=find_packages(), 
    install_requires= get_requirements('requirements.txt')
)

