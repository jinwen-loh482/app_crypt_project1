import numpy as np
import random
import difflib

p1 = "cabooses meltdowns bigmouth makework flippest neutralizers " + \
               "gipped mule antithetical imperials carom masochism stair retsina " + \
               "dullness adeste corsage saraband promenaders gestational mansuetude fig redress " +\
               "pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs " + \
               "ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith " + \
               "constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch"

p2 = "biorhythmic personalizing abjure greets " +\
              "rewashed thruput kashmir chores fiendishly combatting alliums " +\
              "lolly milder postpaid larry annuli codgers apostatizing scrim carillon "+\
              "rust grimly lignifying lycanthrope samisen founds millimeters pentagon "+\
              "humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable "+\
              "acidy duellist potent recyclability capture memorized psalmed meters decline deduced "+\
              "after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago"

p3 = "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci"
p4 = "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s"
p5 = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"

dict2 = [
    "awesomeness",
    "hearkened",
    "aloneness",
    "beheld",
    "courtship",
    "swoops",
    "memphis",
    "attentional",
    "pintsized",
    "rustics",
    "hermeneutics",
    "dismissive",
    "delimiting",
    "proposes",
    "between",
    "postilion",
    "repress",
    "racecourse",
    "matures",
    "directions",
    "pressed",
    "miserabilia",
    "indelicacy",
    "faultlessly",
    "chuted",
    "shorelines",
    "irony",
    "intuitiveness",
    "cadgy",
    "ferries",
    "catcher",
    "wobbly",
    "protruded",
    "combusting",
    "unconvertible",
    "successors",
    "footfalls",
    "bursary",
    "myrtle",
    "photocompose"
]

test_list = [p1, p2, p3, p4, p5]

def build_plaintext(target_length=500, mydict2=dict2):
    p = ""
    while True:
        word = random.randint(0, len(mydict2)-1)
        p = p + mydict2[word] + " "
        if len(p) >= target_length:
            return p[:target_length]

def translate(t):
    if t == " ":
        return 0
    else:
        return ord(t.lower()) - 96

def reverse_translate(n):
    if n == 0:
        return " "
    else:
        return chr(n + 96).lower()

def shift(shift, character):
   temp = translate(character)
   result = (temp + shift) % 27
   return reverse_translate(result)

def encrypt(p):
    keyword = "oh get your money"
    t = len(keyword)
    c = ""
    j =0
    for i in range(0, len(p)):
        k = translate(keyword[j])
        c = c + shift(k, p[i])
        j = (i + 1) % t
    return c

def decrypt(ciphertext, key):
    pt = ""
    j = 0
    for i in range(0, len(ciphertext)):
        k = translate(key[j])
        pt = pt + shift(-k, ciphertext[i])
        j = (i + 1) % len(key)
    return pt

def to_numpy_mat(cipher):
    return np.array([0 if char == " " else ord(char) - 96 for char in cipher.lower()])

def reshape_cipher(cipher, n):
    n_elements = cipher.shape[0]
    rows = n_elements // n
    return cipher[:(rows*n)].reshape((rows, n))

# calculate the index of coincidence of a language given a frequency dictionary
def calc_ic(freq_dict):
    mySum = 0
    n = 0
    c = 27
    for letter in freq_dict.keys():
        n += freq_dict[letter]
        mySum += freq_dict[letter]*(freq_dict[letter]- 1)
    ic = mySum / ((n * (n-1))/c)
    return ic

# calculates the average ic of a cipher transformed into a n*t matrix, where t is the tested key length
def calc_cipher_ic(cipher):
    ic_list = []
    ic_bar = 0

    for col in range(0, cipher.shape[1]):
        current = cipher[:, col]
        unique, counts = np.unique(current, return_counts = True)
        ic_list.append(dict(zip(unique, counts)))
    for i in ic_list:
        ic_bar += calc_ic(i)
    ic_bar /= len(ic_list)
    return ic_bar

# Generates the average distribution of letters of the dictionary and test1 plaintexts,
def statistical_test(L, test1_list, dict2):
    target_length = L;
    freq_list = [0] * 27
    freq_dict = {}
    n = 0;
    for i in range(0, len(test1_list)):
        pt = build_plaintext(target_length, dict2)
        n += target_length
        temp = reshape_cipher(to_numpy_mat(pt), 1)
        for col in range(0, temp.shape[1]):
            current = temp[:, col]
            unique, counts = np.unique(current, return_counts=True)
            freq_dict = dict(zip(unique, counts))
        for letter in freq_dict.keys():
            freq_list[int(letter)] += freq_dict[letter]
    # get freq for test1 pt
    for i in test1_list:
        n += len(i)
        temp = reshape_cipher(to_numpy_mat(i), 1)
        for col in range(0, temp.shape[1]):
            current = temp[:, col]
            unique, counts = np.unique(current, return_counts=True)
            freq_dict = dict(zip(unique, counts))
        for letter in freq_dict.keys():
            freq_list[int(letter)] += freq_dict[letter]
    letter_dist = freq_list
    letter_dist[:] = [round(i / n, 6) for i in letter_dist]
    return letter_dist


# Generates the distribution of letters of the dictionary and test1 plaintexts, and average the distribution
# by iters, where iters is usually 1000
def generate_big_distribution(iters, L, dict2, test1_list):
    average_dist = [0]*27
    for i in range(0, iters):
        temp = statistical_test(L, test1_list, dict2)
        average_dist[:] = [i + j for i, j in zip(average_dist, temp)]
    average_dist[:] = [round(i / iters, 6) for i in average_dist]
    return average_dist

def get_key_length(ic_list):
    key_length = 0
    max_ic = 0
    for i in range(1, 25):
        if ic_list[i-1] > max_ic:
            max_ic = ic_list[i-1]
            key_length = i
    return key_length

# Performs sum(f_i * n_i)
# Where f_i is the probability of encountering letter_i in English,
# and n_i is the probability of encountering letter_i in the plaintext
def chi_val(cipher_list, letter_dist):
    n = len(cipher_list)
    freq_list = [0] * 27
    unique, counts = np.unique(cipher_list, return_counts = True)
    freq_dict = dict(zip(unique, counts))
    for letter in freq_dict.keys():
        freq_list[int(letter)] += freq_dict[letter]
    my_dist = freq_list
    my_dist[:] = [round(i / n, 6) for i in my_dist]
    chi = sum([i * j for i, j in zip(letter_dist, my_dist)])
    return chi

# Most likely key value is the shift that maximizes sum(f_i * n_i) (the chi value)
# Where f_i is the probability of encountering letter_i in English,
# and n_i is the probability of encountering letter_i in the plaintext
def find_key(cipher_numpy, letter_dist, key_length):
    key = [0] * key_length
    cipher_cols = reshape_cipher(cipher_numpy, key_length)
    for col in range(0, cipher_cols.shape[1]):
        most_likely_k = 0
        max_chi = 0
        for shift in range(0, 27):
            current = cipher_cols[:, col]
            current = [(row - shift) % 27 for row in current]
            temp_chi = chi_val(current, letter_dist)
            max_chi = max(temp_chi, max_chi)
            if temp_chi == max_chi:
                most_likely_k = shift
        key[col] = most_likely_k
    return key

def error_num(m, m_prime):
    count = 0
    for i in range(0, len(m)):
        if m[i] != m_prime[i]:
            count += 1
    return count

def match_in_dictionary(words, i, test2_dict):
    change = False
    max_dict_word = max([len(word) for word in test2_dict])
    min_dict_word = min([len(word) for word in test2_dict])

    if len(words[i]) < min_dict_word:
        # add with next word
        words[i] = words[i] + 'x' + words[i + 1]
        del words[i + 1]
        change = True
    elif len(words[i]) > max_dict_word:
        # split word with space
        words[i + 1] = words[i][max_dict_word:] + words[i + 1]
        words[i] = words[i][:max_dict_word]
        change = True
    else:
        cwords = difflib.get_close_matches(words[i], test2_dict)
        if not cwords:
            half_word = words[i][:int(len(words[i])/2)]
            cwords = difflib.get_close_matches(half_word, test2_dict)
        if cwords:
            lenw = len(words[i])
            lenc = len(cwords[0])
            if lenc > lenw:
                # include next word
                words[i] = words[i] + 'x' + words[i + 1]
                del words[i + 1]
                change = True
            elif lenc < lenw:
                # push rest to next word
                words[i + 1] = words[i][lenc:] + words[i + 1]
                words[i] = cwords[0]
                change = True
            else:
                words[i] = cwords[0]
        # if no words match after trying to split the word, move on

    return words, change

def fix_last_word(word, test2_dict):
    cwords = difflib.get_close_matches(word, test2_dict)
    if cwords:
        return cwords[0]
    else:
        return word


def fit_to_dictionary(m_prime, L, test2_dict):
    bad = True
    change = False
    words = m_prime.split(' ')
    while bad:
        for i in range(len(words)):
            if (i + 1) == len(words):
                words[i] = fix_last_word(words[i], test2_dict)
                bad = False
            elif words[i] not in dict2:
                words, change = match_in_dictionary(words, i, test2_dict)
                if change:
                    words = ' '.join(words).split(' ')
                    change = False
                    break
    m_prime_prime = ' '.join(words)[:L]
    m_prime_prime_length = len(m_prime_prime)
    if m_prime_prime_length < L:
        m_prime_prime = m_prime_prime + m_prime[m_prime_prime_length - L:]
    return m_prime_prime


# given a ciphertext, run an index of coincidence attack to predict the plaintext.
def ic_attack(ciphertext, L=500, test2_dict=dict2, test1_list=test_list):
    letter_dist = generate_big_distribution(1000, L, test2_dict, test1_list)
    cipher = to_numpy_mat(ciphertext)

    ic_list = []
    for i in range(1, 25):
        temp = reshape_cipher(cipher, i)
        ic_list.append(calc_cipher_ic(temp))

    key_length = get_key_length(ic_list)

    key = find_key(cipher, letter_dist, key_length)
    key = [reverse_translate(i) for i in key]
    m_prime = decrypt(ciphertext, key)
    m_prime = fit_to_dictionary(m_prime, L, test2_dict)
    return m_prime

def ic_attack_key(ciphertext, L=500, test2_dict=dict2, test1_list=test_list):
    letter_dist = generate_big_distribution(1000, L, test2_dict, test1_list)
    cipher = to_numpy_mat(ciphertext)

    ic_list = []
    for i in range(1, 25):
        temp = reshape_cipher(cipher, i)
        ic_list.append(calc_cipher_ic(temp))

    key_length = get_key_length(ic_list)

    key = find_key(cipher, letter_dist, key_length)
    key = [reverse_translate(i) for i in key]
    m_prime = decrypt(ciphertext, key)
    m_prime = fit_to_dictionary(m_prime, L, test2_dict)
    print(key)
    return m_prime

def ic_attack_random_insert(ciphertext, L=500, test2_dict=dict2, test1_list=test_list):
    message_pp = ic_attack(ciphertext, L, test2_dict, test1_list)
    ciphertext_pp = ciphertext
    insertions = len(ciphertext) - L
    max_executions = 5
    for insertion in range(min(max_executions, insertions)):
        words = message_pp.split(' ')
        bad_index = -1
        for i in range(len(words)):
            # if a bad word exists, compute bad_index
            if words[i] not in test2_dict and (i + 1) != len(words):
                if words[i + 1] not in test2_dict:
                    bad_index = sum([len(word) for word in words[:i]]) + i
                    break
        if bad_index == -1:
            # if no bad_index, exit
            return message_pp
        else:
            # skip bad index and recompute ic attack
            ciphertext_pp = ciphertext_pp[:bad_index] + ciphertext_pp[bad_index + 1:]
            message_pp = ic_attack(ciphertext_pp, L, test2_dict, test1_list)
    
    # remove remainder insertions and run ic_attack one last time (r > 20)
    insertions_left_over = len(ciphertext_pp) - L
    if insertions_left_over > 0:
        for insertions in range(insertions_left_over):
            ciphertext_pp = ciphertext_pp[:bad_index] + ciphertext_pp[bad_index + 1:]
        message_pp = ic_attack(ciphertext_pp, L, test2_dict, test1_list)

    return message_pp