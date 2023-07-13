SOURCE_FOLDER=./threads

get-project-version:
	@cat .project-version

install-requirements:
	pip3 install \
	    -r requirements/project.txt \
	    -r requirements/dev.txt \
	    -r requirements/ops.txt

check-code-quality:
	darglint $(SOURCE_FOLDER)
	ruff check $(SOURCE_FOLDER) --fix
	yamllint .

format:
	ruff check $(SOURCE_FOLDER) --fix
