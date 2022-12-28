from collections import Counter
from math import floor
import sys, os, string, random

# Change this variables, if needed
FILES_PATH = 'books'            # the txt files path 
THRESHOLD = 0.000001            # threshold used for Lossy-Count
K = [3, 5, 10]                  


def sort_dict(dic):
    """ Function that sort the dicionary by value and then, by keys """
    return dict(sorted(dic.items(), key = lambda x: (x[1], x[0]), reverse=True))


def calc_prob(counter):
    """ Function that returns value of the probability 1 / 2^k """
    return 1 / ( 2 ** counter )


def exact_counters(content):
    """ Function that returns the exact frequency of each letter"""
    exact_freq = dict(Counter(content))
    return sort_dict(exact_freq)


def decreasing_probability_counter(k):
    """ Function that returns a count implementing decreasing probability counter """
    count = 0
    for _ in range(k):
        # As the counter value increases, it will be incremented with lesser probability
        if random.random() <= calc_prob(count): 
            count += 1

    return count


def estimate_frequent_letters(method, content, k):
    """
    Estimates the k most frequent letters using the Decreasing probability counter with a probability of 1/2^k.
    """
    estimate_freq = {}

    if method == "Decreasing probability counter":
        for letter in content:
            count = decreasing_probability_counter(k)

            if letter in estimate_freq:
                estimate_freq[letter] += count
            else:
                estimate_freq[letter] = count
        
    elif method == "Lossy-Count":
        # It is a probabilistic data structure that allows you to estimate the count of items with a certain error rate (threshold).
        error_bound = 1

        # Iterate through the items
        for letter in content:
            # Increment the count of the item
            if letter in estimate_freq:
                estimate_freq[letter] += 1
            else:
                estimate_freq[letter] = 1

            # Decrease the error bound by threshold
            error_bound -= THRESHOLD

            # If the error bound becomes negative, divide all counts by 2 and reset the error bound to 1
            if error_bound < 0:
                estimate_freq = { letter : floor( estimate_freq[letter] / 2 ) for letter in estimate_freq.keys() }
                error_bound = 1

    else:
        raise Exception(f"Error: the method '{method}' is unknown.")

    estimate_freq = sort_dict(estimate_freq)   # sort the dict by letter estimate frequency
    return { i : estimate_freq[i] for i in list(estimate_freq.keys())[:k] } # returning the top k most frequent letters


def read_and_process():
    """ Read and process the text files from literary works, in different languages: 
            • Remove the Project Gutenberg file headers.
            • Remove all stop-words and punctuation marks. 
            • Convert all letters to uppercase. 
    """
    stop_marks = string.punctuation + '“' + '”' + '’' + '‘' + '—'
    stop_words = []
    with open(f'stopw.txt', 'r') as f:
        stop_words = [ word[:-1] for word in f.readlines() if "####" not in word]

    words = []
    for filename in os.listdir(FILES_PATH):
        # read all books
        with open(f'{FILES_PATH}/{filename}', 'r') as f:
            # remove Project Gutenberg file headers
            while not '*** ' in next(f): pass               # the book only starts after this line: '*** START OF THE PROJECT GUTENBERG EBOOK DON QUIXOTE ***'
            content = f.readlines()

            for line in content:
                if line.startswith("*** "): break           # the book ends at this line: '*** END OF THE PROJECT GUTENBERG EBOOK DON QUIXOTE ***'
                line = line[:-1].split(" ")
                words += [ word.translate(str.maketrans('', '', stop_marks)).upper() for word in line if word.lower() not in stop_words ]    # remove stop words and punctuations marks

    words = list(filter(lambda word: word != '', words))
    return ''.join(words)   # join all words in one string without spaces
     
   
def main():
    """ The main function """
    content = read_and_process()
    
    # Exact counters
    exact_freq = exact_counters(content)

    # Approximate counters: Decreasing probability counter (1 / 2^k)
    prob_counter_freq = { k : estimate_frequent_letters("Decreasing probability counter", content, k) for k in K }

    # Algorithm to identify frequent items in data streams: Lossy-Count
    lossy_count_freq  = { k : estimate_frequent_letters("Lossy-Count", content, k) for k in K }

    # print results
    topten = { i : exact_freq[i] for i in list(exact_freq.keys())[:10] }
    print(">> Exact counters")
    print(f'exact | {topten}')

    print("\n>> Decreasing probability counter (1 / 2^k)")
    for k, count in prob_counter_freq.items():
        print(f'k= {k} | {count}') if k not in [3,5] else print(f'k= {k}  | {count}')

    print(f"\n>> Lossy-Count (threshold={THRESHOLD})")
    for k, count in lossy_count_freq.items():
        print(f'k= {k} | {count}') if k not in [3,5] else print(f'k= {k}  | {count}')


if __name__ == "__main__":
    argv = sys.argv[1:]
    msg = f"""===========================================================================
    python3 main.py -t <threshold: float>\n
        -t | (optional) choose the threshold to use on Lossy-Count algorithm (float)
           | by default, threshold= {THRESHOLD}\n
===========================================================================\n"""

    print(msg)
    for opt in argv:
        if opt == "-t":
            index = argv.index(opt) + 1
            try:
                THRESHOLD = float(argv[index])
            except:
                print("Error: threshold value must be a float.")
                sys.exit()
    main()