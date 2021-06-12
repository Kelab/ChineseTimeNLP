build:
	python -m build
upload:
	python -m twine upload dist/*
