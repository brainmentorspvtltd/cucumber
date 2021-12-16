# Run the build process by running the command
# 'python setup.py build'

import sys
from cx_Freeze import setup, Executable

options = {
    'build_exe': {
        'include_files': [
            'assets/image1.png',
            'assets/image2.png',
            'assets/image3.png',
            'assets/image6.gif',
            'assets/sound1.wav'
        ],
        'path': sys.path + ['modules']
    }
}

executables = [
    Executable('BikeRider.py')
]

setup(name='Bike Rider',
      version='0.1',
      description='Python Bike Rider',
      options=options,
      executables=executables
      )
