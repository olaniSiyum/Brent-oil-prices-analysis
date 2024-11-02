# helpers.py
import matplotlib.pyplot as plt

def configure_plots():
    plt.style.use('seaborn-darkgrid')
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 12
