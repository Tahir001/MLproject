from setuptools import find_packages, setup 

setup(
    name='mlproject'
    version='0.0.1'
    author='Tahir Muhammad'
    author_email = 'Tahir.muhammad@mail.utoronto.ca'
    packages = find_packages()
    install_requires = ['pandas', 'numpy', 'seaborn']
)