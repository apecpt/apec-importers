#!/usr/bin/env python

import argparse
import json
import logging
import os
import sys

import requests



def main():
	args = parse_args()
	if args.quiet:
		logLevel = logging.ERROR
	else:
		logLevel = logging.INFO
		logging.basicConfig(level=logLevel)
	logging.info("Starting importer.")


def parse_args():
	parser = argparse.ArgumentParser(description="APEC books json loader")
	parser.add_argument("-q", "--quiet", action="store_true", help="Supress output messages", default=False, dest="quiet")
	return parser.parse_args()

if __name__ == '__main__':
	main()
