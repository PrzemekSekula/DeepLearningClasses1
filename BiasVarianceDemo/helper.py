import matplotlib.pyplot as plt
import numpy as np

def plot_model(model, df, x_column = 'area', y_column = 'price'):
    df.plot.scatter(x_column, y_column, title="Model's behavior")
    new_x = np.arange(min(df[x_column]), max(df[x_column]))
    new_y = model.predict(new_x.reshape(-1, 1))
    plt.plot(new_x, new_y, '-', color='red')