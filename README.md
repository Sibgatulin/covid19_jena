# covid19_jena

Repo contains

1. a simple python script which retrieves the page of Jena public service and in a very ad hoc way extracts the number of cases *based on how they are currently formatted on the site*.
2. a shell script which compares the current value with the last entry in a CSV file and updates it if needed, triggering a commit

To satisfy python requirements simply run ``pip install -r requirements.txt``, then swap the shebang for the path to the version of python you used (or for ``#!/usr/bin/env pyhton``).

Furthermore the script can be registered with ``crontab`` as, for example,
``15 9,21 * * * renat /path/to/covid19_jena_scraper.sh``
