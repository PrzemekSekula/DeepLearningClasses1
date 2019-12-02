from matplotlib import pyplot as plt
import numpy as np

def plot_train_valid_history(history):
    """
    Plots train and validation losses.
    Arguments: history - history of training (result of keras model.fit).
        history.history must be a dictionary that looks as follow:
        {
            'loss' : .....
            'valid_loss' : .....
            'acc' : .... # Optional
            'val_acc' : ..... # Optional
        }
    """
    train = history.history['loss']
    valid = history.history['val_loss']

    epochs = np.arange(len(train)) + 1
    fig = plt.figure(figsize=(8, 4))
    if 'acc' in history.history:
        ax1 = fig.add_subplot(121)
        ax1.plot(epochs, train, c='b', label='Train loss')
        ax1.plot(epochs, valid, c='g', label='Valid loss')
        plt.legend(loc='lower left');
        plt.grid(True)        
        
        ax1 = fig.add_subplot(122)
        ax1.plot(epochs, history.history['acc'], c='b', label='Train acc')
        ax1.plot(epochs, history.history['val_acc'], c='g', label='Valid acc')
        plt.legend(loc='lower right');
        plt.grid(True)        
         
        
    else:
        ax1 = fig.add_subplot(111)
        ax1.plot(epochs, train, c='b', label='Train loss')
        ax1.plot(epochs, valid, c='g', label='Valid loss')
        plt.legend(loc='lower left');
        plt.grid(True)
    plt.show()