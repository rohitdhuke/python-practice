from idlelib import query

import snowflake.connector
import getpass
import pandas as pd
user=input('Enter your username: ')
password=input('Enter your password: ')
conn=snowflake.connector.connect(

    user=user,
    password=password,
    account='HKGMPDN-XO17713',
    warehouse='COMPUTE_WH',
    database='SNOWFLAKE_LEARNING_DB',
    schema='INFORMATION_SCHEMA'
)
cur=conn.cursor()
cur.execute('select * from SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER limit 100')
# for row in cur:
#     print(row)
# cur.close()
# conn.close()
# query ='select * from SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER limit 100'
df = cur.fetch_pandas_all()
print(df.head(10))
cur.close()
conn.close()
