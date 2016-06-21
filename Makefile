init:
	pip install -r requirements.txt

test:
	python -m unittest discover -v tests

clean:
	rm -f `find shingles -name '*.pyc'`
	rm -f `find shingles -name '*.pyo'`
	rm -f `find . -name '*~'`
	rm -rf build iso dist api text_shingles-$(VERSION) text_shingles.egg-info
