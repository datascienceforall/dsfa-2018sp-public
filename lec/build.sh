#!/bin/bash

for f in *.ipynb; do
	jupyter nbconvert --execute --allow-errors --ExecutePreprocessor.timeout=None --to notebook --inplace $f
done
