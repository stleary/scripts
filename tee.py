#!/usr/bin/env python

class tee():
    '''A file-like class that can optionally send output to a log file.
       Inspired by
http://www.redmountainsw.com/wordpress/archives/python-subclassing-file-types
       and with help from KirkMcDonald.
    '''
    def __init__(self, _fd1, _fd2):
        self.fd1 = _fd1
        self.fd2 = _fd2

    def __del__(self):
        if self.fd1 != sys.stdout and self.fd1 != sys.stderr:
            self.fd1.close()
        if self.fd2 != sys.stdout and self.fd2 != sys.stderr:
            self.fd2.close()

    def write(self, text):
        if isinstance(text, unicode):
            text = text.encode('utf-8')
        self.fd1.write(text)
        self.fd2.write(text)

    def flush(self):
        self.fd1.flush()
        self.fd2.flush()

if __name__ == '__main__':
    import sys

    # Set up a tee to the log file, and redirect stderr there:
    logfilename = sys.argv[1]
    print "teeing output to", logfilename
    stderrsav = sys.stderr
    outputlog = open(logfilename, "w", buffering=1)
    sys.stderr = tee(stderrsav, outputlog)

