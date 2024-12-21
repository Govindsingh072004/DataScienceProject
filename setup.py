from setuptools import setup,find_packages
from typing import List
HYPER_E_DOT="-e ."

def automate_requirements(file_path:str)->List[str]:
    """Automate the process of reading the requirements.txt file and returning a list of packages."""
    requirements=[]
    with open(file_path,'r') as file_object:
        requirements=file_object.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPER_E_DOT in requirements:
            requirements.remove(HYPER_E_DOT)
    return requirements    





setup(
    name="DataScienceProject",
    version="0.0.1",
    author="Govind Singh",
    author_email="singhg81484@gmail.com",
    description="This is The End To End Industries Ready Data Science Project",
    packages=find_packages(),
    install_requires=automate_requirements("requirements.txt")

)