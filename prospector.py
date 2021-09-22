#!/usr/bin/env python3
"""
    Prospector
    ~~~~~~~~~~

    Reads a CSV file (generated by Facebook ads) and loads it on Novoleads API.

    :copyright: (c) 2019 by Novoleads.
    :author: Leandro E. Colombo Viña <colomboleandro at bitson.group>.
    :license: AGPL, see LICENSE for more details.

    Usage:
        prospector.py (--crm-id=<crm_id> | CRMID) (--token=<token> | TOKEN) (--car-model=<car_model> | CARMODEL) [--car-brand=<car_brand>] [--loglevel=LOGLEVEL] [--filename=<path>] [--url=<url>]
        prospector.py (-h | --help | -v | --version)
    
    Arguments:
        CRMID           The "crm_id" loaded on Novoleads
        TOKEN           Returned "token" from Novoleads API when campaign was created
        CARMODEL        The "car_model" for this CSV

    Options:
        -v, --version               Prints software version
        -h, --help                  This message help and exit
        --filename=<path>           Filename path [default: vw.csv]
        --loglevel=LOGLEVEL         Sets the log level [default: INFO]
        --car-brand=<car_brand>     The "car_brand" for this CSV
        --url=<url>                 Novoleads API URL
"""
import logging
import time
from docopt import docopt
from pandas import read_csv
import requests
import re

__version__ = '0.0.3'

logger = logging.getLogger("Prospector")
logger.setLevel(logging.DEBUG)

# Adds Logging Console Handler
log_format = "".join(["[%(asctime)s] %(levelname)s: %(message)s"])

formatter = logging.Formatter(fmt=log_format)
# Format UTC Time
formatter.converter = time.gmtime
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)


if __name__ == '__main__':
    args = docopt(__doc__, version=__version__)

    debug = False
    if args['--loglevel']:
        ch.setLevel(level=args['--loglevel'])
        if args['--loglevel'] == 'DEBUG':
            debug = True

    CRMID = args['CRMID'] or args['--crm-id']
    URL = f"https://api.automotoresonline.com/iz/campaign/{CRMID}/prospects/" if args["--url"] is None else args["--url"]
    TOKEN = args['TOKEN'] or args['--token']
    FILENAME = args['--filename'] if args['--filename'] else 'vw.csv'
    CARMODEL = args["CARMODEL"] or args['--car-model']
    CARBRAND = args.get('--car-brand')
    logger.debug("CRMID: %s, TOKEN: %s, FILENAME: %s, URL: %s, CARMODEL: %s",CRMID, TOKEN, FILENAME, URL, CARMODEL)

    data = read_csv(FILENAME,
        encoding='UTF-16',
        index_col=False,
        sep='\t',
        squeeze=True,
        usecols=['full_name', 'phone_number', 'email'],
        header=0,
        )
    data.phone_number = data.phone_number.str.replace('\+549?', '', regex=True)
    for index, row in data.iterrows():
        headers = {
            "Authorization": TOKEN
        }
        payload = {
            "name": row["full_name"],
            "email": row["email"],
            "phone": row["phone_number"],
            "car_model": CARMODEL,
        }
        if CARBRAND:
            payload['car_brand'] = CARBRAND
        logger.debug("=== Processing record [%s]: %s", index, payload)
        response = requests.post(URL, json=payload, headers=headers)

        if response.status_code == 201:
            logger.info("Posted %s", payload)
        else:
            logger.error("Something went wrong with %s", payload)
            logger.debug("\t %s %s", response.status_code, response.text)
