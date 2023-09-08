#Using this file to build an ML application and deploy a pipeline
from setuptools import find_packages,setup #find all packages in the directory
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]: 
    # this function will return the list of requirements
    requirements = []
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Abba",
    author_email="aaliconcern@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
    # install_requires=['pandas', 'numpy', 'seaborn']
)

