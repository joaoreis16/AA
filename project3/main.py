from collections import Counter
import sys, os, string, random, time, unidecode, json

# Change this default variables, if needed
FILES_PATH = 'books'            # the txt files path 
THRESHOLD = 0.0001              # threshold used for Lossy-Count
REPETITIONS = 10                # number of repetitions used for approximate counters
K = [3, 5, 10]                  # K values to use on data stream algorithm (Lossy-Count)


def sort(dic):
    """ Function that sort the dicionary by value and then, by keys """
    return dict(sorted(dic.items(), key = lambda x: (x[1], x[0]), reverse=True))


def exact_counters(content):
    """ Function that returns the exact frequency of each letter"""
    exact_freq = dict(Counter(content))
    return sort(exact_freq)


def calc_prob(counter):
    """ Function that returns value of the probability 1 / 2^k """
    return 1 / ( 2 ** counter )


def decreasing_probability_counter(current_count):
    """ Function that returns a count implementing decreasing probability counter """
    count = 0

    # As the counter value increases, it will be incremented with lesser probability
    if random.random() <= calc_prob(current_count): 
        count += 1

    return count


def estimate_frequent_letters(method, content, k=None):
    """
    Estimates the most frequent letters using one of the following methods: Decreasing probability counter with a probability of 1/2^k and Lossy-Count.
    """
    estimate_freq = {}

    if method == "Approximate Counter":
        # Decreasing probability counter (1 / 2^k)
        for letter in content:
            counter = 0

            if letter in estimate_freq.keys():
                counter = estimate_freq[letter]

            increment = decreasing_probability_counter( counter )

            counter += increment
            estimate_freq[letter] = counter

        
    elif method == "Lossy-Count":
        # Algorithm to identify frequent items in data streams: Lossy-Count
        error = 1

        # Iterate through the content
        for letter in content:
            # Increment the count of the letter
            if letter in estimate_freq:
                estimate_freq[letter] += 1
            else:
                estimate_freq[letter] = 1

            # Decrease the error bound by threshold
            error -= THRESHOLD

            # If the error bound becomes negative, divide all counts by 2 and reset the error bound to 1
            if error < 0:
                estimate_freq = { letter : estimate_freq[letter] - 1 for letter in estimate_freq.keys() }
                error = 1

    else:
        raise Exception(f"Error: the method '{method}' is unknown.")

    estimate_freq = sort(estimate_freq)   # sort the dict by letter estimate frequency
    if k: estimate_freq = { i : estimate_freq[i] for i in list(estimate_freq.keys())[:k] } # returning the top k most frequent letters
    return estimate_freq


def error_stats(language_freq, method):
    """ Function that retuns all absolute and relative errors """
    f = open(f"errors/{method}.txt", 'w')

    for language in language_freq.keys():
        f.write(f">> {language}\n")

        exact_values = language_freq[language]["exact"]
        if method == "prob_counter": prob_counter_values = language_freq[language][method]
        else: prob_counter_values = language_freq[language][method][10]

        info = {}

        for letter in prob_counter_values.keys():
        
            ### Decreasing probability counter
            abs_error = abs(exact_values[letter] - prob_counter_values[letter])         # Calculate absolute error
            rel_error = abs_error / exact_values[letter]                                # Calculate relative error

            info.update( { letter : { "absolute_error": abs_error, "relative_error": rel_error }} )


        f.write(json.dumps(info))
        f.write('\n')      


def read_and_process():
    """ Read and process the text files from literary works, in different languages: 
            • Remove the Project Gutenberg file headers.
            • Remove all stop-words and punctuation marks. 
            • Convert all letters to uppercase. 
    """
    stop_marks = string.punctuation + '“' + '”' + '’' + '‘' + '»' + '«' + '¿' + '—'
    stop_words = []
    with open(f'stopw.txt', 'r') as f:
        stop_words = [ word[:-1] for word in f.readlines() if "####" not in word]

    language_content = {}   # key: language | value: content
    for filename in os.listdir(FILES_PATH):
        # read all books
        with open(f'{FILES_PATH}/{filename}', 'r') as f:
            # remove Project Gutenberg file headers
            while not '*** ' in next(f): pass               # the book only starts after this line: '*** START OF THE PROJECT GUTENBERG EBOOK <book's name> ***'
            content = f.readlines()

            words = []
            for line in content:
                if line.startswith("*** "): break           # the book ends at this line: '*** END OF THE PROJECT GUTENBERG EBOOK <book's name> ***'
                line = line[:-1].split(" ")
                words += [ word.translate(str.maketrans('', '', stop_marks)).upper() for word in line if word.lower() not in stop_words and word.isalpha() ]    # remove stop words, punctuations marks and numbers

            words = ''.join(list(filter(lambda word: word != '', words)))     # remove '' char and join all words in one string without spaces
            language = os.path.splitext(f.name)[0].split("/")[1]
            language_content[language] = ''.join([ unidecode.unidecode(letter)  for letter in words ])  # remove all accents, À, Á, Â, Ã = A

    return language_content
     
   
def main():
    """ The main function """
    language_content = read_and_process()
    
    language_time = {}  # { language : { exact : time, prob_counter : time, lossy-count : time } }
    language_freq = {}  # { language : { exact : {letters : count}, prob_counter : {letters : count}, lossy-count : {letters : count} } }

    for language, content in language_content.items():
        language_freq[language] = language_time[language] = {}

        # Exact counters
        start = time.time()
        exact_freq = exact_counters(content)
        exact_count_time = time.time() - start

        # Approximate counters: Decreasing probability counter (1 / 2^k)
        errors = []
        best_prob_counter_freq = {}
        prob_counter_time = 0

        for _ in range(REPETITIONS):
            start = time.time()
            prob_counter_freq = estimate_frequent_letters("Approximate Counter", content)
            end = ( time.time() - start )
            prob_counter_time += end
            
            error = sum( abs(exact_freq[letter] - prob_counter_freq[letter]) / exact_freq[letter]  for letter in exact_freq ) / len(exact_freq)

            if not errors: 
                best_prob_counter_freq = prob_counter_freq

            elif errors and error <= min(errors):
                best_prob_counter_freq = prob_counter_freq

            errors.append(error)
        
        prob_counter_time = prob_counter_time / REPETITIONS    

        # Algorithm to identify frequent items in data streams: Lossy-Count
        start = time.time()
        lossy_count_freq  = { k : estimate_frequent_letters("Lossy-Count", content, k) for k in K }
        lossy_count_time = time.time() - start

        language_freq[language] = { "exact" : exact_freq, "prob_counter": best_prob_counter_freq, "lossy-count": lossy_count_freq }
        language_time[language] = { "exact" : exact_count_time, "prob_counter": prob_counter_time, "lossy-count": lossy_count_time }

    error_stats(language_freq, "prob_counter")
    error_stats(language_freq, "lossy-count")

    # print results per language
    for language, count in language_freq.items():
        exec_times = language_time[language]

        print(f"\n==================================== {language.upper()} ==========================================")
        print(">> Exact counters")
        print(f'      | {count["exact"]}')
        print(f'\n\tExecution time: {exec_times["exact"]}s\n')

        print(f"\n>> Decreasing probability counter (repetitions={REPETITIONS})")
        print(f'      | {count["prob_counter"]}')  
        print(f'\n\tExecution time: {exec_times["prob_counter"]}s\n')

        print(f"\n>> Lossy-Count (threshold={THRESHOLD})")
        for k, count in count["lossy-count"].items():
            print(f'k= {k} | {count}') if k not in [3,5] else print(f'k= {k}  | {count}')
        print(f'\n\tExecution time: {exec_times["lossy-count"]}s\n')


if __name__ == "__main__":
    argv = sys.argv[1:]
    msg = f"""=================================================================================================
    python3 main.py (-t <threshold: float>) (-r <repetitions: int>)\n
        -t | (optional) choose the threshold to use on Lossy-Count algorithm (float)
           | by default, threshold= {THRESHOLD}
           
        -r | (optional) choose the number of repetitions to use on Approximate counters (int)
           | by default, repetitions= {REPETITIONS}\n
=================================================================================================\n"""

    print(msg)
    for opt in argv:
        if opt == "-t":
            index = argv.index(opt) + 1
            try:
                THRESHOLD = float(argv[index])
            except:
                print("Error: threshold value must be a float.")
                sys.exit()

        if opt == "-r":
            index = argv.index(opt) + 1
            try:
                REPETITIONS = int(argv[index])
            except:
                print("Error: repetitions value must be a int.")
                sys.exit()
    main()