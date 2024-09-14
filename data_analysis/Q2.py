import pandas as pd

ex = {'math':[90, 80, 98], 'eng':[70, 100, 87], 'python':[100, 80, 80]}
df = pd.DataFrame(ex)
df.to_excel('Q2.xlsx')