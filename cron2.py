#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
# vim:set ts=4 sw=4 et:

import sys, json
from pprint import pprint

dataMibs = json.load(sys.stdin)
dataJson = dataMibs['status']
adslInfos = {}
if 'dsl' in dataJson:
    adslInfos = dataJson['dsl']['dsl0']
else:
    adslInfos = dataJson
for song,singer in adslInfos.items():
    print(song, " ", singer)