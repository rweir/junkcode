"""Converts nginx-style redirects to s3 xml magic redirects

example input:
rewrite ^/docs/foo.html http://example.org/docs/foo/ permanent;
rewrite ^/docs/bar.html http://ertius.org/docs/bar/ permanent;
"""

import sys
import xml.etree.ElementTree as ET

if len(sys.argv) != 3:
    print("Usage: gen-redirects.py map baseurl")

filename = sys.argv[1]
baseurl = sys.argv[2]

root = ET.Element("RoutingRules")

with open(filename) as f:
    for line in f:
        if not line.strip().startswith("rewrite"):
            continue
        bits = line.split()
        src = bits[1][2:]
        dst = bits[2][len(baseurl) :]
        rule = ET.SubElement(root, "RoutingRule")

        cond = ET.SubElement(rule, "Condition")
        prefix = ET.SubElement(cond, "KeyPrefixEquals")
        prefix.text = src

        redirect = ET.SubElement(rule, "Redirect")
        replace = ET.SubElement(redirect, "ReplaceKeyWith")
        replace.text = dst

print(ET.tostring(root))
