#!/bin/bash

./xlsx/importer.py $1/*.xlsx | ./tools/files.py $1 | ./tools/summary.py
