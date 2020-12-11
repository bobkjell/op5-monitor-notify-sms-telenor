#!/usr/bin/env python
#
# Description: Send SMS from OP5 Monitor using Telenor SMS Pro API

# Module import
import requests, argparse, logging
from requests.auth import HTTPBasicAuth

# Logging
logging.basicConfig(filename='/var/log/op5/sms_error.log',
	format='%(asctime)s %(levelname)s %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S',
	encoding='utf-8',
	level=logging.WARNING)

# Argument parsing
parser = argparse.ArgumentParser(description='Send OP5 notifications using Telenor SMS API.')
parser.add_argument("-H", "--hostname", help="Hostname of alerting host", type=str, required=True)
parser.add_argument("-S", "--service", help="Service description of alerting service", type=str, required=False)
parser.add_argument("-P", "--pager", help="Phone number to nofify", type=str, required=True)
parser.add_argument("-ho","--hostoutput", help="Host alarm message", type=str, required=False)
parser.add_argument("-hs","--hoststate", help="Host state", type=str, required=False)
parser.add_argument("-so","--serviceoutput", help="Service alarm message", type=str, required=False)
parser.add_argument("-ss","--servicestate", help="Service state", type=str, required=False)
parser.add_argument("-c","--customerid", help="Telenor API Customerid", type=str, required=True)
parser.add_argument("-u","--username", help="Telenor API Basic Username", type=str, required=True)
parser.add_argument("-px","--passwordxml", help="Telenor API Password", type=str, required=True)
parser.add_argument("-pb","--passwordbasic", help="Telenor API Basic Password", type=str, required=True)
parser.add_argument("-f","--fromsender", help="FROM address", type=str, required=True)
args = parser.parse_args()

# Build service- and host-message
if args.service:
  sms_message = args.service + " on " + args.hostname + " is " + args.servicestate + ". " + args.serviceoutput
else:
  sms_message = args.hostname + " is " + args.hoststate + ". " + args.hostoutput

# Buid message (XML)
xmlbody = ("<?xml version='1.0' encoding='ISO-8859-1'?><mobilectrl_sms>"
"<header>"
"<customer_id>" + args.customerid +  "</customer_id>"
"<password>" +  args.passwordxml + "</password>"
"<from_alphanumeric>" + args.fromsender + "</from_alphanumeric>"
"</header>"
"<payload>"
"<sms account='71700'>"
"<message><![CDATA[" + sms_message + "]]></message>"
"<to_msisdn>" + args.pager + "</to_msisdn>"
"</sms>"
"</payload>"
"</mobilectrl_sms>")

# Send SMS
try:
  headers = {'Content-Type': 'application/xml'}
  response = requests.post("https://sms-pro.net:44343/services/" + args.customerid + "/sendsms", data=xmlbody, headers=headers, auth=HTTPBasicAuth(args.username, args.passwordbasic))
  response.raise_for_status()
except requests.exceptions.HTTPError as error:
  logging.error(error)
  raise SystemExit(error)
