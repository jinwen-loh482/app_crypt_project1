import random
import numpy as np
import statistics

def translate(t):
    # get characters as numbers 1-27
    if t == " ":
        return 27
    else:
        return ord(t.lower()) - 96

def reverse_translate(n):
    # get numbers 1-27 from characters where ' ' is 27
    if n == 27:
        return " "
    else:
        return chr(n + 96).lower()

def shift(shift, character):
    # get character as number
    temp = translate(character) - 1
    # apply shift
    result = (temp + shift) % 27 + 1
    # translate number back to character
    return reverse_translate(result)
   
def encrypt(p):
    t = 0
    c = ""
    # cyclic shift encryption (test for when cycle is length t)
    for i in range(0, 500):
        t = (t % 22) + 1
        c = c + shift(t, p[i])
    return c

def random_encrypt(p):
    t = 0
    c = ""
    # compute random key with possible duplicates
    key = np.random.choice(27, 24, replace=True)
    # apply one of 24 random shifts in the key for each iteration
    # 'random' shift encryption
    for i in range(0, 500):
        t = random.randint(0, 23)
        c = c + shift(key[t], p[i])
    return c

def calculate_shift(t1, t2):
    # return how much it takes t1 to get to t2 by shift
    if t1 >= t2:
        return (t1 - t2)*-1 + 27
    else:
        return t2 - t1

def compute_unique_shifts(text1, text2):
    # set prevents duplicate shift insertion
    s = set()
    for i in range(0,500):
        t1 = translate(text1[i])
        t2 = translate(text2[i])
        # add shift to the set
        s.add(calculate_shift(t1, t2))
    # return number of unique shifts
    return len(s)

def compute_unique_shifts_with_insertion(ciphertext, text):
    # get number of insertions as r
    insertions = len(ciphertext) - 500

    if not insertions:
        return compute_unique_shifts(ciphertext, text)

    # create 10 blocks of 2*r + 1 sets
    # 1 set is the 'no insertion' set
    # r sets are 'insertion sets' 1-r
    # r sets are 'linear step insertion sets' 1-r
    list_of_sets = list([[set() for j in range(0, insertions + insertions + 1)] for i in range(0, 6)])

    # k is used to calculate whether to increment the 'linear step insertion sets' in each block
    k = 0
    for i in range(0,500):
        t1 = translate(text[i])

        # for every average number of characters per insertion, increment k, the step
        if insertions and i % (500/insertions) == 0:
            k = k + 1

        c = translate(ciphertext[i])
        list_of_sets[int(i/84) % 6][0].add(calculate_shift(t1, c))
        
        for j in range(1, insertions + 1):
            c = translate(ciphertext[i + j])

            # add shift to set in block i/50 (blocks 1-10), set j (sets 1-r)
            list_of_sets[int(i/84) % 6][j].add(calculate_shift(t1, c))

            # check bound errors for j + k
            if (j + k) > insertions:
                c = translate(ciphertext[i + insertions])
            else:
                c = translate(ciphertext[i + j + k])

            # add shift to r sets after 'insertion sets'
            list_of_sets[int(i/84) % 6][insertions + j].add(calculate_shift(t1, c))
            
    # compute the minimum number of unique shifts per block
    setlengths = [[len(_s) for _s in s] for s in list_of_sets]
    medsetlengths = [min(length) for length in setlengths]

    # compute weighted average with weights higher at smaller unique shifts
    medsetlengths.sort(reverse=True)
    numerator = sum([(i+1)*medsetlengths[i] for i in range(len(medsetlengths))])
    denominator = sum([(i + 1) for i in range(len(medsetlengths))])
    return numerator/denominator

def unique_shift_attack(message_pp, ciphertext):
    message_1 = "cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch"
    message_2 = "biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago"
    message_3 = "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci"
    message_4 = "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s"
    message_5 = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"
    messages = [message_1, message_2, message_3, message_4, message_5, message_pp]
    return min([(plaintext, compute_unique_shifts_with_insertion(ciphertext, plaintext)) for plaintext in messages], key = lambda x: x[1])[0]


