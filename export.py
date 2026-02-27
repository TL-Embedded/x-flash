import py2exe

py2exe.freeze(console=[
    {
        "script": "./src/main.py"
    }
])
