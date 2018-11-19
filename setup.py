from setuptools import setup

setup(
    name = 'snapshotaalyzer-2018',
    version ='0.1',
    author ="Mark Dawkins",
    author_email="mark.dawkins@gmail.com",
    description="SnapshotAlyzer 2018 is a tool to manage AWS ec2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/markdawkins/snapshotanalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
       [console_scripts]
       shotty=shotty.shotty:cli
   ''',
)
