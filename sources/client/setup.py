from cx_Freeze import setup, Executable
from DocAccounting.settings import getVersion
# base = "Win32GUI"
base = None
executables = [Executable("main.py", target_name='DocAccounting_v' + getVersion().replace('.', '_') + '.exe', base=base, icon="icon.ico")]
packages = ['queue', 'sqlalchemy']
options = {
    'build_exe': {
        'packages': packages,
        'include_msvcr': True,
        'build_exe': 'build_windows',
        'include_files': ['C:/Python_368_32bit/Lib/site-packages/qt_material']
    },
    'bdist_msi': {
    }
}

setup(
    name='DocAccounting',
    options=options,
    version=getVersion(),
    description='Accounting documents in the organization',
    executables=executables
)