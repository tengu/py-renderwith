all:

clean:
	rm -fr *.egg-info dist build *.egg
scrub: clean
	rm -fr $(ve)
push:
	python setup.py register sdist upload

#ve_opt=--system-site-packages
ve=$(PWD)/ve
python=$(ve)/bin/python
ve: $(ve)
$(ve):
	virtualenv $(ve_opt) $@

install: $(ve)
	$(python) setup.py install
test: $(ve)
	$(python) setup.py test
develop:
	$(python) setup.py develop

####
t:
	$(python) test.py 

