import setuptools

setuptools.setup(
    name='my_awesome_cli',
    version='0.2',
    description='My Awesome CLI',
    packages=setuptools.find_packages(),
    # I fool `pip` by specifying the version number which
    # is greater than the one released in PyPi and force
    # it to look at the dependency_links where i wrongly specify
    # that i have a version which is greater than 0.1.2
    install_requires='fire>0.1.2',
    dependency_links=[
        'git+https://github.com/google/python-fire.git@9bff9d01ce16589201f57ffef27ea84744951c11#egg=fire-0.1.2.1',
    ],
    entry_points={
        'console_scripts': [
            'my-awesome-cli=my_awesome_cli.main:main'
        ],
    }
)
