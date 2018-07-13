import matplotlib.pyplot

import seaborn

import pandas

pandas_data = pandas.read_csv("ks-projects-201801.csv", index_col=0)
# print(pandas_data[4:])

# print(pandas_data.loc[:, 'main_category'])

# Shows number of KS by main_category
seaborn.countplot(x=pandas_data.loc[:, 'main_category'], data=pandas_data)

# Shows number of KS by current state
# seaborn.countplot(x=pandas_data.loc[:, 'state'], data=pandas_data)

# seaborn.countplot(x=pandas_data.loc[:, 'main_category'], hue=pandas_data.loc[:, 'state'], data=pandas_data)

# seaborn.countplot(data=pandas_data)

# print(matplotlib.pyplot.get_backend())
# mng = matplotlib.pyplot.get_current_fig_manager()
#print(mng.window.size((1920, 1080)))
# mng.resize(1920, 1080)

matplotlib.pyplot.get_current_fig_manager().resize(1920, 1080)

matplotlib.pyplot.show()