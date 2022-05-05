import papermill as pm

#log_date = '2020-08-26'
log_date = '2020-09-02'
#log_date = '2020-09-09'
#log_date = '2020-09-16'

ch = 'off'

pm.execute_notebook(
   './same_buy.ipynb',
   f'./output_samebuy_{log_date}.ipynb',
   parameters = dict(log_date = log_date)
)

