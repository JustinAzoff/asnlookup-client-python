# Usage

    echo -e "4.4.2.2\n8.8.8.8" | asnlookup-client | column  -t -s $'\t'
    DEBUG:asnlookup.client:Connecting to asn lookup server
    DEBUG:asnlookup.client:fields=['ip', 'asn', 'prefix', 'owner', 'cc']
    4.4.2.2  3356   4.0.0.0/9   LEVEL3 - Level 3 Communications, Inc.  US
    8.8.8.8  15169  8.8.8.0/24  GOOGLE - Google Inc.                   US
