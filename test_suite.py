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
    keyword = "oh get your money"
    t = len(keyword)
    c = ""
    j =0
    for i in range(0, len(p)):
        k = translate(keyword[j])
        c = c + shift(k, p[i])
        j = (i + 1) % t
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
    # create 10 blocks of r+1 sets
    list_of_sets = list([[set() for j in range(0, insertions + 1)] for i in range(0,10)])
    for i in range(0,500):
        t1 = translate(text[i])
        for j in range(0, insertions + 1):
            # calculate c as if j insertions happened before the current block
            c = translate(ciphertext[i + j])
            # add shift to set in block i/50 (blocks 1-10), set j (sets 1-r)
            list_of_sets[int(i/50)][j].add(calculate_shift(t1, c))

    # get all lengths for each set and return an average of the minimum lengths
    setlengths = [[len(_s) for _s in s] for s in list_of_sets]
    return statistics.mean([min(length) for length in setlengths])

def compute_unique_shifts_with_insertion2(ciphertext, text):
    # get number of insertions as r
    insertions = len(ciphertext) - 500

    # create 10 blocks of 2*r + 1 sets
    # 1 set is the 'no insertion' set
    # r sets are 'insertion sets' 1-r
    # r sets are 'linear step insertion sets' 1-r
    list_of_sets = list([[set() for j in range(0, insertions + insertions + 1 + 1)] for i in range(0,10)])

    # k is used to calculate whether to increment the 'linear step insertion sets' in each block
    k = 0
    for i in range(0,500):
        t1 = translate(text[i])

        # for every average number of characters per insertion, increment k, the step
        if insertions and i % (500/insertions) == 0:
            k = k + 1

        for j in range(0, insertions + 1):
            c = translate(ciphertext[i + j])

            # add shift to set in block i/50 (blocks 1-10), set j (sets 1-r)
            list_of_sets[int(i/50)][j].add(calculate_shift(t1, c))

            # check bound errors for j + k
            if (j + k) > insertions:
                c = translate(ciphertext[i + insertions])
            else:
                c = translate(ciphertext[i + j + k])

            # add shift to r sets after 'insertion sets'
            list_of_sets[int(i/50)][insertions + j + 1].add(calculate_shift(t1, c))
            
    # compute the minimum number of unique shifts per block
    setlengths = [[len(_s) for _s in s] for s in list_of_sets]
    minsetlengths = [min(length) for length in setlengths]

    # compute weighted average with weights higher at smaller unique shifts
    minsetlengths.sort(reverse=True)
    numerator = sum([(i+1)*minsetlengths[i] for i in range(len(minsetlengths))])
    denominator = sum([(i + 1) for i in range(len(minsetlengths))])
    return numerator/denominator


def run_shift_test():
    p1 = "cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch"
    p2 = "biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago"
    p3 = "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci"
    p4 = "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s"
    p5 = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"
    print("----------Run Shift Test----------")
    print(compute_unique_shifts(p1, p2))
    print(compute_unique_shifts(p1, p3))
    print(compute_unique_shifts(p1, p4))
    print(compute_unique_shifts(p1, p5))
    print(compute_unique_shifts(p2, p3))
    print(compute_unique_shifts(p2, p4))
    print(compute_unique_shifts(p2, p5))
    print(compute_unique_shifts(p3, p4))
    print(compute_unique_shifts(p3, p5))
    print(compute_unique_shifts(p4, p5))

def run_encrypt_test():
    p1 = "cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch"
    p2 = "biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago"
    p3 = "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci"
    p4 = "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s"
    p5 = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"
    print("----------Run Encrypt Test----------")
    c1 = encrypt(p1)
    print(c1)
    print(compute_unique_shifts(c1, p1))
    print(compute_unique_shifts(c1, p2))
    print(compute_unique_shifts(c1, p3))
    print(compute_unique_shifts(c1, p4))
    print(compute_unique_shifts(c1, p5))

def run_random_encrypt_test():
    p1 = "cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch"
    p2 = "biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago"
    p3 = "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci"
    p4 = "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s"
    p5 = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"
    print("----------Run Random Encrypt Test----------")
    c1 = random_encrypt(p1)
    print(c1)
    print(compute_unique_shifts(c1, p1))
    print(compute_unique_shifts(c1, p2))
    print(compute_unique_shifts(c1, p3))
    print(compute_unique_shifts(c1, p4))
    print(compute_unique_shifts(c1, p5))

def run_insertion_random_encrypt_test():
    p1 = "cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch"
    p2 = "biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago"
    p3 = "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci"
    p4 = "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s"
    p5 = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"
    c = random_encrypt(p1)
    c = c[:10] + 'q' + c[10:]
    c = c[:50] + 'p' + c[50:]
    c = c[:100] + 'a' + c[100:]
    c = c[:150] + 'z' + c[150:]
    c = c[:200] + 't' + c[200:]
    c = c[:250] + 'l' + c[250:]
    c = c[:300] + 'h' + c[300:]
    c = c[:350] + 'a' + c[350:]
    c = c[:400] + 'z' + c[400:]
    c = c[:450] + 'c' + c[450:]
    print("----------Run Insertion Random Encrypt Test----------")
    print(compute_unique_shifts_with_insertion(c, p1))
    print(compute_unique_shifts_with_insertion(c, p2))
    print(compute_unique_shifts_with_insertion(c, p3))
    print(compute_unique_shifts_with_insertion(c, p4))
    print(compute_unique_shifts_with_insertion(c, p5))

def run_insertion_random_encrypt_test2():
    p1 = "cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch"
    p2 = "biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago"
    p3 = "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci"
    p4 = "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s"
    p5 = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"
    c = random_encrypt(p1)
    # for i in range(0, 40):
    #     t = reverse_translate(random.randint(1, 27))
    #     c = c[:9*i] + t + c[9*i:]
    # c = c[:255] + 'a' + c[255:]
    # c = c[:385] + 'q' + c[385:]
    # c = c[:500] + 'q' + c[500:]
    # c = c[:507] + 'q' + c[507:]
    # c = c[:510] + 'q' + c[510:]
    # c = c[:516] + 'q' + c[516:]
    # c = c[:523] + 'q' + c[523:]
    # c = c[:532] + 'q' + c[532:]
    # c = c[:540] + 'q' + c[540:]
    # c = c[:546] + 'q' + c[546:]

    for i in range(0, 50):
        t = reverse_translate(random.randint(1, 27))
        c = c[:10*i] + t + c[10*i:]

    # for i in range(0, 100, 4):
    #     t = reverse_translate(random.randint(1, 27))
    #     c = c[:5*(i + 1)] + t + c[5*(i+1):]
    # for i in range(0, 100, 4):
    #     t = reverse_translate(random.randint(1, 27))
    #     c = c[:5*i] + t + c[5*i:]

    # for i in range(0, 50):
    #     t = reverse_translate(random.randint(1, 27))
    #     c = c[:499 + i] + t + c[499 + i:]

    # for i in range(0, 50):
    #     t = reverse_translate(random.randint(1, 27))
    #     c = c[:i] + t + c[i:]

    print(len(c))

    print("----------Run Insertion Random Encrypt Test----------")
    print(compute_unique_shifts_with_insertion(c, p1))
    print(compute_unique_shifts_with_insertion(c, p2))
    print(compute_unique_shifts_with_insertion(c, p3))
    print(compute_unique_shifts_with_insertion(c, p4))
    print(compute_unique_shifts_with_insertion(c, p5))
    print("----------Run Insertion Random Encrypt Test 2----------")
    print(compute_unique_shifts_with_insertion2(c, p1))
    print(compute_unique_shifts_with_insertion2(c, p2))
    print(compute_unique_shifts_with_insertion2(c, p3))
    print(compute_unique_shifts_with_insertion2(c, p4))
    print(compute_unique_shifts_with_insertion2(c, p5))

def encrypt_every_t(p):
    t = random.randint(1, 24)
    keyword = [reverse_translate(random.randint(1, 27)) for i in range(0, t)]
    keyword = "".join(keyword)
    c = ""
    j =0
    for i in range(0, len(p)):
        k = translate(keyword[j])
        c = c + shift(k, p[i])
        j = (i + 1) % t
    return c

# run_shift_test()
# run_encrypt_test()
# run_random_encrypt_test()
#run_insertion_random_encrypt_test()
# run_insertion_random_encrypt_test2()