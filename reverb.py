import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def debugg(fstring):
    pass

# prints var outputs
def find_target_frequency(freqs):
    for x in freqs:
        if x > 1000:
            break
        return x

def frequency_check(freqs, spectrum):

    debugg(f'freqs {freqs[:10]}')
    target_frequency = find_target_frequency(freqs)
    debugg(f'target_frequency {target_frequency}')
    index_of_frequency = np.where(freqs == target_frequency)[0][0]
    debugg(f'index_of_frequency {index_of_frequency}')

    data_for_frequency = spectrum[index_of_frequency]
    debugg(f'data_for_frquency {data_for_frequency[:10]}')

    # change a digital signal for a values in decibels

    data_in_db_fun = 10 * np.log10(data_for_frequency)
    return data_in_db_fun


# find a nearest value
def find_nearest_value(array, value):
    array= np.asarray(array)
    debugg(f'array {array[:10]}')
    idx = (np.abs(array - value)).argmin()
    debugg(f'idx {idx}')
    debugg(f'array[idx] {array[idx]}')
    return array[idx]

def analyse(filename):
    sample_rate, data = wavfile.read(filename)
    spectrum, freqs, t, im = plt.specgram(data, Fs=sample_rate, NFFT=1024, cmap=plt.get_cmap('autumn_r'))
    
    data_in_db = frequency_check(freqs, spectrum)
    plt.figure()
    # plot reverb time on grid
    plt.plot(t, data_in_db, linewidth=1, alpha=0.7, color='#004bc6')
    plt.xlabel('Time (s)')
    plt.ylabel('Power (dB)')

    # find an index of a  max value
    index_of_max = np.argmax(data_in_db)

    value_of_max = data_in_db[index_of_max]

    plt.plot(t[index_of_max], data_in_db[index_of_max], 'go')

    # slice array from a max value
    sliced_array = data_in_db[index_of_max:]

    value_of_max_less_5 = value_of_max - 5
    value_of_max_less_5 = find_nearest_value(sliced_array, value_of_max_less_5)

    index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)

    plt.plot(t[index_of_max_less_5], data_in_db[index_of_max_less_5], 'yo')

    # slice array from a max -5dB
    value_of_max_less_25 = value_of_max - 25

    value_of_max_less_25 = find_nearest_value(sliced_array, value_of_max_less_25)

    index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)

    plt.plot(t[index_of_max_less_25], data_in_db[index_of_max_less_25], 'ro')
    rt20 = (t[index_of_max_less_5] - t[index_of_max_less_25])[0]

    # extrapolate rt20 to rt60
    rt60 = 3*rt20

    # optional set limits on plot
    plt.grid()
    plt.show()

    print(f'The RT60 reverb time is {round(abs(rt60), 2)} seconds')
