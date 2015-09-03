#!/usr/bin/env python

import argparse
import json
import logging
import os
import sys
import itertools
import codecs

import requests

def import_data(data, url):
	r = requests.post(url + "/import/rawPublications", data=json.dumps(data), headers={'Content-Type' : 'Application/Json'})
	r.raise_for_status()
	logging.info(r.json()['addedPublications'])

def print_status(url):
	r = requests.get(url + "/publications")
	r.raise_for_status()
	l = len(r.json())
	logging.info("Status: %d publications" % l)

def grouper(n, iterable):
    it = iter(iterable)
    while True:
       chunk = tuple(itertools.islice(it, n))
       if not chunk:
           return
       yield chunk

def main():
	args = parse_args()
	if args.quiet:
		logLevel = logging.ERROR
	else:
		logLevel = logging.INFO
		logging.basicConfig(level=logLevel)
	logging.debug("Starting importer.")
	inputFile = codecs.open(args.input_file, "r", "utf-8") if args.input_file != "-" else codecs.getreader("utf-i")(sys.stdin)
	data = json.load(inputFile)
	batches = grouper(args.batch_size, data)
	for b in batches:
		batch = list(b)
		logging.debug("Importing %d publications." % len(batch))
		import_data(batch, args.server_url)
		print_status(args.server_url)



DEFAULT_SERVER_URL = "http://localhost:8081"

def parse_args():
	parser = argparse.ArgumentParser(description="APEC books json loader")
	parser.add_argument("-q", "--quiet", action="store_true", help="Supress output messages", default=False, dest="quiet")
	parser.add_argument("-i", "--input-file", help="file to read input from, default is stdin", default="-")
	parser.add_argument("-b", "--batch-size", help="Group requests in batches, default is 10", default=10, type=int)
	parser.add_argument("--server-url", help="server url", default=DEFAULT_SERVER_URL)
	return parser.parse_args()

if __name__ == '__main__':
	main()
