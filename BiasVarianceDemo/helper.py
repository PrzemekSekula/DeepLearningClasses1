import matplotlib.pyplot as plt
import numpy as np

def plot_model(model, df, x_column = 'area', y_column = 'price'):
    df.plot.scatter(x_column, y_column, title="Model's behavior")
    new_x = np.arange(min(df[x_column]), max(df[x_column]))
    new_y = model.predict(new_x.reshape(-1, 1))
    plt.plot(new_x, new_y, '-', color='red')
    
    
def plot_models(models, df, x_column = 'area', y_column = 'price'):
    plt.figure(figsize=(10, 4))
    for i, model in enumerate(models):
        plt.subplot(1, len(models), i+1)
        plt.scatter(df[x_column], df[y_column], s=1)
        new_x = np.arange(min(df[x_column]), max(df[x_column]))
        new_y = model.predict(new_x.reshape(-1, 1))
        plt.plot(new_x, new_y, '-', color='red')           