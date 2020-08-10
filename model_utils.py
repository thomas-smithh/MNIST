import matplotlib.pyplot as plt

def plot_history(data):
    epochs = len(data['val_loss'])
    val_accuracy = data['val_acc']
    val_loss = data['val_loss']
    accuracy = data['acc']
    loss = data['loss']
    
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(14, 3.5))
    
    ax[0].plot(accuracy, label='Train Accuracy', linewidth=2, marker='x')
    ax[0].plot(val_accuracy, label='Validation Accuracy', linewidth=2, marker='o', linestyle='--')
    ax[1].plot(loss, label='Train Loss', linewidth=2, marker='x')
    ax[1].plot(val_loss, label='Validation Loss', linewidth=2, marker='o', linestyle='--')
    ax[0].grid()
    ax[1].grid()
    ax[0].legend()
    ax[1].legend()
    ax[0].set_title('Accuracy')
    ax[1].set_title('Loss')
    plt.show()