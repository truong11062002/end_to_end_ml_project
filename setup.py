from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(filename: str) -> List[str]:
    ''' 
    This function will return the list of requirements
    '''
    requirements = []
    with open(filename) as f:
        requirements = f.read().splitlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name='end_to_end_ml_project',
    version='0.0.1',
    author='truongnn',
    author_email='truong11062002@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)