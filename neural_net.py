"""Train and validate neural net"""
import pickle
import warnings

from sklearn.neural_network import MLPClassifier

from data_process import *

warnings.filterwarnings("ignore")


def train_neural_net(x_train, y_train, root, tk, output_text_area):
    """
    Train and save neural net.
    :param x_train: Training inputs.
    :param y_train: Training outputs.
    :return: Trained neural_net
    """
    output_text_area.insert(5.0, 'Training neural net...\n\n')
    root.update_idletasks()
    neural_net = MLPClassifier()
    neural_net.fit(x_train, y_train)  # train neural net

    output_text_area.insert(7.0, 'Saving trained neural net to file...\n\n')
    root.update_idletasks()
    pickle.dump(neural_net, open('trained_neural_net', 'wb'))

    # visualize(pd.Series(neural_net.loss_curve_), graph_type='area')  # plot loss curve

    return neural_net


def run(root, tk, output_text_area):
    """
    main.
    :return: None
    """
    voice_data = read(root, tk, output_text_area)  # read data

    x_train, x_test, y_train, y_test = preprocess(voice_data, root, tk, output_text_area)  # preprocess data

    trained_neural_net = train_neural_net(x_train, y_train, root, tk, output_text_area)  # train neural net

    output_text_area.insert(9.0, 'Calculating accuracy...\n')
    get_accuracy(x_train, x_test, y_train, y_test, trained_neural_net, root, tk, output_text_area)  # print results
    root.update_idletasks()


if __name__ == '__main__':
    run()
