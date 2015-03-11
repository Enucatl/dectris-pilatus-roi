from setuptools import setup

setup(
    name='dectris_pilatus_roi',
    version='0.1',
    py_modules=['dectris_pilatus_roi'],
    install_requires=[
        'click',
        'numpy',
    ],
    entry_points='''
        [console_scripts]
        dectris_pilatus_roi=dectris_pilatus_roi:crop
    ''',
)
