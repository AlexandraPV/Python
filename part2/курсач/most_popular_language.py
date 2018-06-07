from db import *
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt



PLOT_LABEL_FONT_SIZE = 8

def getColors(n):
    COLORS = []
    cm = plt.cm.get_cmap('hsv', n)
    for i in np.arange(n):
        COLORS.append(cm(i))
    return COLORS

def dict_sort(my_dict):
    keys = []
    values = []
    my_dict = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)
    for k, v in my_dict:
        keys.append(k)
        values.append(v)
    return (keys,values)

def most_popular_language():
    conn = connect_db()
    df = pd.read_sql("SELECT  SUM(assembly) AS assembly, SUM(c) AS c, SUM(c_plus_plus) AS c_plus_plus, SUM(c_sharp) AS c_sharp, SUM(html) AS html, SUM(css) AS css, SUM(javascript) AS javascript, SUM(php) AS php, SUM(python) AS python, SUM(angular2) AS angular2, SUM(vue) AS vue, SUM(java) AS java, SUM(scala) AS scala FROM public.git",conn)
    dict = {}
    values = df.values[0].tolist()
    keys = df.keys()
    for i in range(len(values)):
        dict[keys[i]] = values[i]
    dict_keys, dict_values = dict_sort(dict)
    top_keys = len(dict_keys)
    plt.title('Популярність мов програмування', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=0, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.xlabel('Мова програмування', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('Процентне відношення', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.show()

if __name__ == '__main__':
    most_popular_language()