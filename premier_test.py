""" Fichier: base.py"""

import os, os.path
import sys

# from dotenv import load_dotenv

# load_dotenv()

def main(args=sys.argv[:1]):
    """ Main"""
    print("Usage: %s" % os.path.basename(sys.argv[0]))
    return 0

if __name__ == "__main__":
    sys.exit(main())
else:
    print('STATUS: Reading from stdin')
