import os
from setuptools import find_packages, setup
#
#
#
#
def get_install_requires():
    lib_folder = os.path.dirname(os.path.realpath(__file__))
    requirement_path = f"{lib_folder}/requirements.txt"

    install_requires = []

    if os.path.isfile(requirement_path):
        install_requires = open(requirement_path, "r", encoding="utf-8").read().splitlines()

    return install_requires
#
#
#
#
setup(
		name="PyGraphicUI",
		version="1.0",
		author="oddshellnick",
		author_email="oddshellnick.programming@gmail.com",
		packages=find_packages(),
		install_requires=get_install_requires()
)
