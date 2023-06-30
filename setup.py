from setuptools import find_packages, setup 
from typing import List

def get_requirements(file_path) -> List[str]:
    """
    The following function will return the list of requirements

    Args:
        file_path (_type_): _description_

    Returns:
        List[str]: _description_
    """
    # Open the requirements.txt file and read the dependencies  
    requirements = []
    with open(file_path) as file_obj: 
        requirements= file_obj.readlines()
        requirements= [req.replace('\n', ' ') for req in requirements]

setup(
    name='mlproject'
    version='0.0.1'
    author='Tahir Muhammad'
    author_email = 'Tahir.muhammad@mail.utoronto.ca'
    packages = find_packages()
    install_requires = get_requirements('requirements.txt')
)