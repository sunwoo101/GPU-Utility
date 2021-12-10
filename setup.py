from setuptools import setup
APP = ['gpuutil-gui.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True, 
    'site_packages': True,
    'iconfile': 'appicon.icns',
    'packages': [],
    'plist': {
        'CFBundleName': 'GPU Utility',
    }
}
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)