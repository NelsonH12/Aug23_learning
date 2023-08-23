import camelot
tables = camelot.read_pdf('foo.pdf')
print (tables)

#this is a known issue in replit.  OpenCV fails when not operating in the root.  The
#existing workaround is to create a fork and then work from the root there.