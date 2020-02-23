import os
import pickle
from subprocess import run
import pandas as pd
import neural_net
import sound_recorder


def analyser_func (mode, root, tk, output_text_area) :
    if mode == 'train':
        neural_net.run(root, tk, output_text_area)
    elif mode == 'analyse':
        if not os.path.isfile('trained_neural_net'):  # check if neural_net file exists
            output_text_area.delete(1.0, tk.END)
            output_text_area.insert(1.0, 'Neural net not trained. First train the neural net.\n')
            root.update_idletasks()
        else:
            sound_recorder.run(root, tk, output_text_area)

            output_text_area.insert(9.0, 'Extracting data from recorded voice...\n\n')
            root.update_idletasks()
            run(['C:/Program Files/R/R-3.6.2/bin/Rscript', 'getAttributes.r',
                 os.getcwd()])  # running R script for extracting data from recorded voice

            output_text_area.insert(11.0, 'Preprocessing extracted data...\n\n')
            root.update_idletasks()
            data = pd.read_csv('output/voiceDetails.csv')
            del data['peakf'], data['sound.files'], data['selec'], data['duration']
            dataset = pd.read_csv('voice.csv')
            dataset = dataset.iloc[:, :-1]
            data = (data - dataset.mean()) / (dataset.max() - dataset.min())  # scale

            trained_neural_net = pickle.load(open('trained_neural_net', 'rb'))  # load trained neural net from file

            output_text_area.insert(13.0, 'Prediction: ')
            output_text_area.insert(13.14, 'Speaker is a female' if trained_neural_net.predict(data)[0] == 0 else 'Speaker is a male')
            root.update_idletasks()
    else:
        print('\nInvalid option. Please try again...')
