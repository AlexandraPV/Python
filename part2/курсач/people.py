from most_popular_language import *
import matplotlib
matplotlib.use("TkAgg")


def people():
    conn = connect_db()
    dict = {}

    df = pd.read_sql("SELECT COUNT(assembly) AS assembly FROM public.git WHERE assembly<>0;",conn)
    dict[df.keys()[0]] = df.values[0][0]

    df = pd.read_sql("SELECT COUNT(c) AS c FROM public.git WHERE c<>0;", conn)
    dict[df.keys()[0]] = df.values[0][0]

    df = pd.read_sql("SELECT COUNT(c_plus_plus) AS c_plus_plus FROM public.git WHERE c_plus_plus<>0;", conn)
    dict[df.keys()[0]] = df.values[0][0]

    df = pd.read_sql("SELECT COUNT(c_sharp) AS c_sharp FROM public.git WHERE c_sharp<>0;", conn)
    dict[df.keys()[0]] = df.values[0][0]

    df = pd.read_sql("SELECT COUNT(html) AS html FROM public.git WHERE html<>0;", conn)
    dict[df.keys()[0]] = df.values[0][0]

    df = pd.read_sql("SELECT COUNT(css) AS css FROM public.git WHERE css<>0;", conn)
    dict[df.keys()[0]] = df.values[0][0]

    df = pd.read_sql("SELECT COUNT(javascript) AS javascript FROM public.git WHERE javascript<>0;", conn)
    dict[df.keys()[0]] = df.values[0][0]

    df = pd.read_sql("SELECT COUNT(php) AS php FROM public.git WHERE php<>0;", conn)
    dict[df.keys()[0]] = df.values[0][0]

    df = pd.read_sql("SELECT COUNT(python) AS python FROM public.git WHERE python<>0;", conn)
    dict[df.keys()[0]] = df.values[0][0]

    df = pd.read_sql("SELECT COUNT(angular2) AS angular2 FROM public.git WHERE angular2<>0;", conn)
    dict[df.keys()[0]] = df.values[0][0]

    df = pd.read_sql("SELECT COUNT(vue) AS vue FROM public.git WHERE vue<>0;", conn)
    dict[df.keys()[0]] = df.values[0][0]

    df = pd.read_sql("SELECT COUNT(java) AS java FROM public.git WHERE java<>0;", conn)
    dict[df.keys()[0]] = df.values[0][0]

    df = pd.read_sql("SELECT COUNT(scala) AS scala FROM public.git WHERE scala<>0;", conn)
    dict[df.keys()[0]] = df.values[0][0]
    values = df.values[0].tolist()
    keys = df.keys()
    for i in range(len(values)):
        dict[keys[i]] = values[i]
    dict_keys, dict_values = dict_sort(dict)
    top_keys = len(dict_keys)
    plt.title('Кількість людей, які пишуть на даній мові програмування', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.bar(np.arange(top_keys), dict_values, color=getColors(top_keys))
    plt.xticks(np.arange(top_keys), dict_keys, rotation=0, fontsize=8)
    plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
    plt.xlabel('Мова програмування', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.ylabel('Кількість людей', fontsize=PLOT_LABEL_FONT_SIZE)
    plt.show()


if __name__ == '__main__':
    people()