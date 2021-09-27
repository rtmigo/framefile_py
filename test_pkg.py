from chkpkg import Package

if __name__ == "__main__":
    with Package() as pkg:
        # running console_scripts defined in setup.py
        pkg.run_python_code('import hashdigits')
    print("\nPackage is OK!")
