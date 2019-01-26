# this file is intended to get a list of computers from a specific ou in sctive directory

import pyad.adquery
import myconstants


def get_computers_ad_ou(input_dn: str):
    q = pyad.adquery.ADQuery()

    q.execute_query(
        attributes=["distinguishedName"],
        where_clause="objectClass = '*'",
        base_dn=input_dn
    )
    return q


def get_pcs():
    pcs = []
    for i in get_computers_ad_ou(myconstants.input_dn).get_results():
        pc = i.get('distinguishedName').split(',')[0][3:]
        myconstants.parse_pc(pc, pcs)
    return pcs


if __name__ == '__main__':
    y = get_pcs()
    print(y)
