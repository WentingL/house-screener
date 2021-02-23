import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def conf_fig():
    font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

    matplotlib.rc('font', **font)
    plt.grid(color='gray', lw=0.5, alpha=0.5, linestyle='--')
    plt.rc('ytick', labelsize=13)
    plt.rc('xtick', labelsize=13)
    plt.box(False)

class Visualization():

    df = pd.read_csv("proof_of_concept/extracted_data.csv", index_col=0)
    df.astype({'price': 'int32', 'bath': 'int32', 'area': 'int32'})

    conf_fig()

    plt.scatter(df['price'], df['area'])

    plt.xlabel("Price(CAD)"), plt.ylabel("Area(Sqft)")
    # Plot trend line
    z = np.polyfit(df['price'], df['area'], 1)
    p = np.poly1d(z)
    plt.plot(df['price'], p(df['price']), "g--")

    plt.savefig("first-figure.png", dpi=600)
