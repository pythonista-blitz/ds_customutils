from setuptools import find_packages, setup


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="datascience_utils",
    version='1.0',
    description="utility scrits for datascience",
    author="Ippei Kurose",
    author_email="black.jupiter.0102@gmail.com",
    url="https://github.com/pythonista-blitz/ds_customutils",
    packages=find_packages(),
    package_dir={"": "src"},
    install_requires=_requires_from_file("requirements.txt"),
    include_package_data=True,
    zip_safe=False,
)
