#!/usr/bin/env python

import argparse
import PyPDF2
import re

parser = argparse.ArgumentParser()
parser.add_argument("PDFfile", help="The file to break down")
parser.add_argument("-s", "--secret", help="Secret with which to encrypt each page")
args = parser.parse_args()

pdf = PyPDF2.PdfFileReader(args.PDFfile)
pn = 0
for page in pdf.pages:
  d = page.getContents().getData()
  pn += 1
  # Horrible hack.  Close enough for now and seems to work.
  m = re.findall(b'Tm\n\(([^)]+)\)Tj\n', d)
  try:
    colon = m.index(b':')
    name = m[colon-1]
    out = PyPDF2.PdfFileWriter()
    out.addPage(page)
    if args.secret:
      out.encrypt(args.secret)
    of = open(name + b".pdf", "wb")
    out.write(of)
    of.close()
  except ValueError:
    print("Name not found on page", pn)
