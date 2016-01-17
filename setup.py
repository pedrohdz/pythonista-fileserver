from setuptools import setup

setup(
    name='pythonista-file-server',
    # Please read the following for setting the version number:
    #    - https://pythonhosted.org/setuptools/setuptools.html#specifying-your-project-s-version  # noqa
    version='0.0.0-dev',
    author='Pedro H <pedro@digitalrounin.com>',
    author_email='pedro@digitalrounin.com',
    install_requires=[],
    # TODO - entry_points might be better
    scripts=[
        'HttpFileServer.py'
        ]
    )
