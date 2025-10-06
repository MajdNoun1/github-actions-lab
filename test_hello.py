def test_sample(): 
assert 2 + 2 == 4
name: Set up Python 
uses: actions/setup-python@v4
with: 
python-version: '3.x' - name: Install pytest 
run: pip install pytest - name: Run tests 
run: pytest
