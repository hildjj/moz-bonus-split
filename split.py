#!/usr/bin/env python

import argparse
import PyPDF2
import re

parser = argparse.ArgumentParser()
parser.add_argument("PDFfile", help="The file to break down")
parser.add_argument("-s", "--secret", help="Secret with which to encrypt each page")
args = parser.parse_args()

pdf = PyPDF2.PdfFileReader(args.PDFfile)
for page in pdf.pages:
  d = page.getContents().getData()
  # Horrible hack.  Close enough for now and seems to work.
  m = re.search('Tm\n\(([^)]+):\)Tj\n', d)
  if (m):
    out = PyPDF2.PdfFileWriter()
    out.addPage(page)
    if args.secret:
      out.encrypt(args.secret)
    of = open(m.group(1) + ".pdf", "wb")
    out.write(of)
    of.close()