#!/bin/sh
JC19_DIR=/home/renat/scripts/covid19_jena
pushd $JC19_DIR
git pull

ENTRY_LAST=$(tail -1 $JC19_DIR/jena_covid19_scraped.csv)
ENTRY_NEW=$($JC19_DIR/scrape.py)
if [ "$ENTRY_NEW" != "$ENTRY_LAST" ]; then
    echo $ENTRY_NEW >> $JC19_DIR/jena_covid19_scraped.csv
    git add $JC19_DIR/jena_covid19_scraped.csv
    git commit -m "update from ${ENTRY_NEW%,*}"
    git push
fi
popd
