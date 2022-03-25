import papermill as pm

#train_start_date = '2020-08-26'
#train_start_date = '2020-09-02'
train_start_date = '2020-09-09'
#train_start_date = '2020-09-16'

pm.execute_notebook(
   './h-m-training-data.ipynb',
   f'./output_{train_start_date}.ipynb',
   parameters = dict(train_start_date = train_start_date, negative_num=100)
)

