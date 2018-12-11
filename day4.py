# this file is intended to get a list of computers from a specific ou in sctive directory

import pyad.adquery


def get_computers_ad_ou(input_dn: str):
    q = pyad.adquery.ADQuery()

    q.execute_query(
        attributes=["distinguishedName"],
        where_clause="objectClass = '*'",
        base_dn=input_dn
    )

    return q


if __name__ == '__main__':
    pass
