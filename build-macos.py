import os
import shutil
import py2app 

from distutils.core import setup

def tree(src):
    first_pass = True
    for root, dirs, files in os.walk(os.path.normpath(src)):
        if first_pass:
            yield ('', [os.path.join(root, f) for f in files])
            first_pass = False
        else:
            relative_root = os.path.relpath(root, src)
            yield (relative_root, [os.path.join(root, f) for f in files])

if os.path.exists('build'):
    shutil.rmtree('build')

if os.path.exists('dist/main.app'):
    shutil.rmtree('dist/main.app')

ENTRY_POINT = ['src/index.py']

DATA_FILES = list(tree('gui'))

# Include additional files here
# DATA_FILES.extend([
#     ('', [])
# ])

OPTIONS = {
    'argv_emulation': False,
    'strip': True,
    'includes': ['WebKit', 'Foundation', 'webview', 'pkg_resources.py2_warn']
}

setup(
    name="App Name",
    app=ENTRY_POINT,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
