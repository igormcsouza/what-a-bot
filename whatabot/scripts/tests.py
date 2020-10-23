import os

def run_tests():
    os.system('pytest -v --cov=whatabot')

def open_web_coverage():
    os.system('coverage html')
    os.system(f"start {os.path.join('htmlcov', 'index.html')}")