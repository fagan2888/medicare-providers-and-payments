"""
cleans up the payments files. Removes
unnecessary fields (address, name) and rounds float numbers.
"""



import argparse
from csvkit import DictReader, DictWriter
from loggy import loggy
from sys import stdout

LOGGY = loggy('clean_payments')

CLEANED_PAYMENT_HEADERS = ["npi",
    "place_of_service",
    "hcpcs_code",
    "hcpcs_description",
    "hcpcs_drug_indicator",
    "line_item_service_count",
    "beneficiary_unique_count",
    "unique_beneficiary_per_day_services_count",
    "avg_medicare_allowed_amount",
    "avg_submitted_charge_amount",
    "avg_medicare_payment_amount",
    "avg_medicare_standardized_amount",]


CLEANED_PAYMENT_HEADER_MAP = {
    'average_medicare_standard_amt' : 'avg_medicare_standardized_amount',
    'average_medicare_payment_amt' : 'avg_medicare_payment_amount',
    "average_submitted_chrg_amt" : 'avg_submitted_charge_amount',
    "average_medicare_allowed_amt" : "avg_medicare_allowed_amount",
    "line_srvc_cnt" : "line_item_service_count",
    "bene_unique_cnt" : "beneficiary_unique_count",
    'bene_day_srvc_cnt' : "unique_beneficiary_per_day_services_count",
}



if __name__ == '__main__':
    parser = argparse.ArgumentParser("Normalizes payments data")
    parser.add_argument('infile', type=argparse.FileType('r'))
    args = parser.parse_args()
    infile = args.infile
    LOGGY.info("Reading: %s" % infile.name)

    rawheaders = infile.readline().strip().split('\t')
    newheaders = [h.lower() for h in rawheaders]
    for i, h in enumerate(newheaders):
        if CLEANED_PAYMENT_HEADER_MAP.get(h):
            newheaders[i] = CLEANED_PAYMENT_HEADER_MAP[h]


    csvin = DictReader(infile, delimiter='\t', fieldnames=newheaders)
    csvout = DictWriter(stdout, fieldnames=CLEANED_PAYMENT_HEADERS)

    for row in csvin:
        d = {}
        for h in CLEANED_PAYMENT_HEADERS:
            if 'amount' in h:
                d[h] = round(float(row[h]), 2) if row.get(h) else None
            else:
                d[h] = row[h]

        csvout.writerow(d)




