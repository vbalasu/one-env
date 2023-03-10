from databricks import sql
import os
access_token = os.environ.get('DATABRICKS_TOKEN')

connection = sql.connect(
                        server_hostname = "e2-demo-field-eng.cloud.databricks.com",
                        http_path = "/sql/1.0/warehouses/ead10bf07050390f",
                        access_token=access_token)

import pandas as pd
df = pd.read_sql("select * from hive_metastore.demos_dlt_cdc_vijay_balasubramaniam.distinct_names", connection)
df.to_csv('distinct_names.csv', index=False)

connection.close()