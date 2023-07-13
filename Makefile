SOURCE_FOLDER=./threads

get-project-version:
	@cat .project-version

install-requirements:
	pip3 install \
	    -r requirements/project.txt \
	    -r requirements/dev.txt \
	    -r requirements/ops.txt

check-code-quality:
	isort $(SOURCE_FOLDER) --diff --check-only
	flake8 $(SOURCE_FOLDER)
	black --check $(SOURCE_FOLDER)

check-yaml-standards:
	yamllint .

format:
	isort $(SOURCE_FOLDER)
	autoflake --recursive --in-place --remove-unused-variables $(SOURCE_FOLDER)
	autopep8 --exclude migrations --recursive --in-place -a -a $(SOURCE_FOLDER)
	black $(SOURCE_FOLDER)
