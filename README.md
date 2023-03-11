# one-env

This application is intended to be run in EC2 in the temp-1-hour instance of aws-field-eng (us-west-2)

Follow these steps to set up the demo:

A. Setup the web server and client

1. Run `~/test/temp-1-hour/run.sh` to start the server
2. Connect to the server using `ssh temp-1-hour`
3. Run `~/github/one-env/run.sh` to start the service on port 5000
4. Confirm that you can access the url [https://deloitte-university.databricks-partners.com/hello](https://deloitte-university.databricks-partners.com/hello)
5. Edit `~/timer.json` to increase the remaining minutes

B. Setup Databricks

1. Open the [dbdemos notebook](https://e2-demo-field-eng.cloud.databricks.com/?o=1444828305810485#notebook/3254325001509350/command/3631133442639536)
2. Start the interactive cluster [dbdemos-dlt-cdc-vijay_balasubramaniam
](https://e2-demo-field-eng.cloud.databricks.com/?o=1444828305810485#setting/clusters/0309-191351-v77c0rzi/apps)
3. Open the notebook [01-Retail_DLT_CDC_SQL](https://e2-demo-field-eng.cloud.databricks.com/?o=1444828305810485#notebook/3631133442640798/command/3631133442640808) and navigate to the diagram
4. Open the DLT notebook [05-Realtime-Customers](https://e2-demo-field-eng.cloud.databricks.com/?o=1444828305810485#notebook/3631133442764049/command/3631133442764051)
5. Open the Realtime dashboard notebook [06-Realtime-Dashboard](https://e2-demo-field-eng.cloud.databricks.com/?o=1444828305810485#notebook/3631133442764114/command/3631133442764215)
6. Start the [DLT Pipeline](https://e2-demo-field-eng.cloud.databricks.com/?o=1444828305810485#joblist/pipelines/9f406290-3739-4fdd-b6c5-d9f0e9502efb/updates/985b1305-0e14-4c0a-a23a-3eae65d05a86) in continuous mode
7. Open Data Explorer to [hive_metastore.demos_dlt_cdc_vijay_balasubramaniam](https://e2-demo-field-eng.cloud.databricks.com/sql/explore/data/hive_metastore/demos_dlt_cdc_vijay_balasubramaniam?o=1444828305810485)
