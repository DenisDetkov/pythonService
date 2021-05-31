import sys

sys.path.append("/var/www/webroot/ROOT/")

from __init__ import app as application

if __name__ == "__main__":
    application.run()
