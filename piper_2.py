def pip_auto_install(_package):
    """
    Automatically installs all requirements if pip is installed.
    """
    try:
        from pip._internal import main as pip_main
        pip_main(['install', _package])
    except ImportError:
        print("Failed to import pip. Please ensure that pip is installed.")
        print("For further instructions see "
              "https://pip.pypa.io/en/stable/installing/")
        sys.exit(-1)
    except Exception as err:
        print("Failed to install pip requirements: " + err.message)
        sys.exit(-1)
