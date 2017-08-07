Parse Mozilla's bonus letter PDF.  Split each page into a separate file, named by the recipient.  Optionally, encrypt each output file.

## Setup

```
pip install PyPDF2
```

## Running

```
python split.py -s SECRET PDFfile
```