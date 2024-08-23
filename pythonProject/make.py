import PyInstaller.__main__

PyInstaller.__main__.run([
    'dot.py',
    '--onefile',
    '--windowed',
    '--add-data "Fox Sprite Sheet(1).png"'
])