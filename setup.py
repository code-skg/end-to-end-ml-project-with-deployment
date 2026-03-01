from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Return a list of dependencies from requirements.txt"""

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()

    requirements = [
        req.strip()
        for req in requirements
        if req.strip() and req.strip() != "-e ."
    ]

    return requirements

setup(
    name="end_to_end_ml_project",
    version="0.1.0",
    author="Satyam",
    description="End-to-end ML project with deployment",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")
) 

