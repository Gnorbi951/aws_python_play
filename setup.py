from setuptools import setup, find_packages


packages = find_packages()

requirements = [
    'pydantic',
]

test_requirements = [
    'pytest',
    'pytest-cov',
    'pylint',
]

setup(
    author='Norbert Gocze',
    author_email='gnorbi951@gmail.com',
    version='0.0.1',
    python_requires='~=3.9',
    description="Short description",
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='aws_python_play',
    name='aws_python_play',
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        'test': test_requirements,
    },
    test_suite='tests',
    tests_require=test_requirements,
)
