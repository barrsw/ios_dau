# Databricks notebook source
# MAGIC %run Repos/apps/ios-dau/utils/parallel_notebook_runner

# COMMAND ----------

Notebook.runner(notebook_name = './main',
                arguments={"envs": "h2b_train_inverted"},
                start_date=date(2023,3,1), 
                end_date=date(2023,4,1),
                timeout=3600*5,
                parallel_runs=2)

# COMMAND ----------

