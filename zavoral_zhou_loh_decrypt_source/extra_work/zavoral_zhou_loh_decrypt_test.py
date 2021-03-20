import time
import argparse
import random
from ic_attack import ic_attack_random_insert, build_plaintext, encrypt
from generic_unique_shift_attack import unique_shift_attack, random_encrypt, shift, reverse_translate

def encrypt2(p, L=500, key_length=24):
    t = 0
    c = ""
    # cyclic shift encryption (test for when cycle is length t)
    for i in range(0, L):
        t = (t % key_length) + 4
        c = c + shift(t, p[i])
    return c

def run_cyclic_encrypt_test(runs):
    test1_success_count = 0
    test2_success_count = 0
    test1_fail_count = 0
    test2_fail_count = 0
    print('---------- running cyclic encrypt test: {} runs ----------'.format(runs))
    end = time.time()
    while runs:
        message_p = build_plaintext(target_length=500)
        message_1 = "cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch"
        message_2 = "biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago"
        message_3 = "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci"
        message_4 = "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s"
        message_5 = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"
        messages = [message_1, message_2, message_3, message_4, message_5, message_p]
       
        runs = runs - 1

        index_c = random.randint(0, 5)
        message_c = messages[index_c]
        ciphertext = encrypt(message_c)
        message_pp = ic_attack_random_insert(ciphertext)
        message_cc = unique_shift_attack(ciphertext, message_pp)
        if message_cc == message_c:
            if index_c == 5:
                test2_success_count = test2_success_count + 1
            else:
                test1_success_count = test1_success_count + 1
        else:
            if index_c == 5:
                test2_fail_count = test2_fail_count + 1
            else:
                test1_fail_count = test1_fail_count + 1
    end2 = time.time()
    print('Time Elapsed: {}'.format(end2-end))
    print('-------------- results: cyclic encrypt test --------------')
    print('test 1 success: {}'.format(test1_success_count))
    print('test 2 success: {}'.format(test2_success_count))
    print('test 1 failed: {}'.format(test1_fail_count))
    print('test 2 failed: {}'.format(test2_fail_count))

def run_cyclic_encrypt_test2(runs):
    test1_success_count = 0
    test2_success_count = 0
    test1_fail_count = 0
    test2_fail_count = 0
    print('---------- running cyclic encrypt test 2: {} runs ----------'.format(runs))
    end = time.time()
    while runs:
        message_p = build_plaintext(target_length=500)
        message_1 = "cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch"
        message_2 = "biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago"
        message_3 = "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci"
        message_4 = "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s"
        message_5 = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"
        messages = [message_1, message_2, message_3, message_4, message_5, message_p]
        
        runs = runs - 1

        index_c = random.randint(0, 5)
        message_c = messages[index_c]
        ciphertext = encrypt2(message_c)
        message_pp = ic_attack_random_insert(ciphertext)
        message_cc = unique_shift_attack(ciphertext, message_pp)
        if message_cc == message_c:
            if index_c == 5:
                test2_success_count = test2_success_count + 1
            else:
                test1_success_count = test1_success_count + 1
        else:
            if index_c == 5:
                test2_fail_count = test2_fail_count + 1
            else:
                test1_fail_count = test1_fail_count + 1
    end2 = time.time()
    print('Time Elapsed: {}'.format(end2-end))
    print('-------------- results: cyclic encrypt test 2 --------------')
    print('test 1 success: {}'.format(test1_success_count))
    print('test 2 success: {}'.format(test2_success_count))
    print('test 1 failed: {}'.format(test1_fail_count))
    print('test 2 failed: {}'.format(test2_fail_count))

def run_random_encrypt_test(runs):
    test1_success_count = 0
    test2_success_count = 0
    test1_fail_count = 0
    test2_fail_count = 0
    print('---------- running random encrypt test: {} runs ----------'.format(runs))
    end = time.time()
    while runs:
        message_p = build_plaintext(target_length=500)
        message_1 = "cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch"
        message_2 = "biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago"
        message_3 = "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci"
        message_4 = "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s"
        message_5 = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"
        messages = [message_1, message_2, message_3, message_4, message_5, message_p]
        
        runs = runs - 1

        index_c = random.randint(0, 5)
        message_c = messages[index_c]
        ciphertext = random_encrypt(message_c)
        message_pp = ic_attack_random_insert(ciphertext)
        message_cc = unique_shift_attack(ciphertext, message_pp)
        if message_cc == message_c:
            if index_c == 5:
                test2_success_count = test2_success_count + 1
            else:
                test1_success_count = test1_success_count + 1
        else:
            if index_c == 5:
                test2_fail_count = test2_fail_count + 1
            else:
                test1_fail_count = test1_fail_count + 1
    end2 = time.time()
    print('Time Elapsed: {}'.format(end2-end))
    print('-------------- results: random encrypt test --------------')
    print('test 1 success: {}'.format(test1_success_count))
    print('test 2 success: {}'.format(test2_success_count))
    print('test 1 failed: {}'.format(test1_fail_count))
    print('test 2 failed: {}'.format(test2_fail_count))

def run_cyclic_encrypt_insertion_test(runs):
    test1_success_count = 0
    test2_success_count = 0
    test1_fail_count = 0
    test2_fail_count = 0
    print('---------- running cyclic encrypt insertion test: {} runs ----------'.format(runs))
    end = time.time()
    while runs:
        message_p = build_plaintext(target_length=500)
        message_1 = "cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch"
        message_2 = "biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago"
        message_3 = "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci"
        message_4 = "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s"
        message_5 = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"
        messages = [message_1, message_2, message_3, message_4, message_5, message_p]
        
        runs = runs - 1

        index_c = random.randint(0, 5)
        message_c = messages[index_c]
        ciphertext = encrypt(message_c)

        # insertions
        ciphertext = ciphertext[:350] + 'z' + ciphertext[350:]

        message_pp = ic_attack_random_insert(ciphertext)
        message_cc = unique_shift_attack(ciphertext, message_pp)
        if message_cc == message_c:
            if index_c == 5:
                test2_success_count = test2_success_count + 1
            else:
                test1_success_count = test1_success_count + 1
        else:
            if index_c == 5:
                test2_fail_count = test2_fail_count + 1
            else:
                test1_fail_count = test1_fail_count + 1
    end2 = time.time()
    print('Time Elapsed: {}'.format(end2-end))
    print('-------------- results: cyclic encrypt insertion test --------------')
    print('test 1 success: {}'.format(test1_success_count))
    print('test 2 success: {}'.format(test2_success_count))
    print('test 1 failed: {}'.format(test1_fail_count))
    print('test 2 failed: {}'.format(test2_fail_count))

def run_cyclic_encrypt_insertion_test2(runs):
    test1_success_count = 0
    test2_success_count = 0
    test1_fail_count = 0
    test2_fail_count = 0
    print('---------- running cyclic encrypt insertion test 2: {} runs ----------'.format(runs))
    end = time.time()
    while runs:
        message_p = build_plaintext(target_length=500)
        message_1 = "cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch"
        message_2 = "biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago"
        message_3 = "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci"
        message_4 = "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s"
        message_5 = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"
        messages = [message_1, message_2, message_3, message_4, message_5, message_p]

        runs = runs - 1

        index_c = random.randint(0, 5)
        message_c = messages[index_c]
        ciphertext = encrypt(message_c)

        # insertions
        ciphertext = ciphertext[:100] + 'z' + ciphertext[100:]
        ciphertext = ciphertext[:150] + 'z' + ciphertext[150:]
        ciphertext = ciphertext[:250] + 'z' + ciphertext[250:]
        ciphertext = ciphertext[:350] + 'z' + ciphertext[350:]
        ciphertext = ciphertext[:450] + 'z' + ciphertext[450:]
        ciphertext = ciphertext[:470] + 'z' + ciphertext[470:]

        message_pp = ic_attack_random_insert(ciphertext)
        message_cc = unique_shift_attack(ciphertext, message_pp)
        if message_cc == message_c:
            if index_c == 5:
                test2_success_count = test2_success_count + 1
            else:
                test1_success_count = test1_success_count + 1
        else:
            if index_c == 5:
                test2_fail_count = test2_fail_count + 1
            else:
                test1_fail_count = test1_fail_count + 1
    end2 = time.time()
    print('Time Elapsed: {}'.format(end2-end))
    print('-------------- results: cyclic encrypt insertion test 2 --------------')
    print('test 1 success: {}'.format(test1_success_count))
    print('test 2 success: {}'.format(test2_success_count))
    print('test 1 failed: {}'.format(test1_fail_count))
    print('test 2 failed: {}'.format(test2_fail_count))

def run_cyclic_encrypt_insertion_test3(runs):
    test1_success_count = 0
    test2_success_count = 0
    test1_fail_count = 0
    test2_fail_count = 0
    print('---------- running cyclic encrypt insertion test 3: {} runs ----------'.format(runs))
    end = time.time()
    while runs:
        message_p = build_plaintext(target_length=500)
        message_1 = "cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch"
        message_2 = "biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago"
        message_3 = "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci"
        message_4 = "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s"
        message_5 = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"
        messages = [message_1, message_2, message_3, message_4, message_5, message_p]
        
        runs = runs - 1

        index_c = random.randint(0, 5)
        message_c = messages[index_c]
        ciphertext = encrypt(message_c)

        # insertions
        for i in range(0, 100, 4):
            t = reverse_translate(random.randint(1, 27))
            ciphertext = ciphertext[:5*(i + 1)] + t + ciphertext[5*(i+1):]

        message_pp = ic_attack_random_insert(ciphertext)
        message_cc = unique_shift_attack(ciphertext, message_pp)
        if message_cc == message_c:
            if index_c == 5:
                test2_success_count = test2_success_count + 1
            else:
                test1_success_count = test1_success_count + 1
        else:
            if index_c == 5:
                test2_fail_count = test2_fail_count + 1
            else:
                test1_fail_count = test1_fail_count + 1
    end2 = time.time()
    print('Time Elapsed: {}'.format(end2-end))
    print('-------------- results: cyclic encrypt insertion test 3 --------------')
    print('test 1 success: {}'.format(test1_success_count))
    print('test 2 success: {}'.format(test2_success_count))
    print('test 1 failed: {}'.format(test1_fail_count))
    print('test 2 failed: {}'.format(test2_fail_count))

def run_cyclic_encrypt_insertion_test4(runs):
    test1_success_count = 0
    test2_success_count = 0
    test1_fail_count = 0
    test2_fail_count = 0
    print('---------- running cyclic encrypt insertion test 4: {} runs ----------'.format(runs))
    end = time.time()
    while runs:
        message_p = build_plaintext(target_length=500)
        message_1 = "cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch"
        message_2 = "biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago"
        message_3 = "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci"
        message_4 = "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s"
        message_5 = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"
        messages = [message_1, message_2, message_3, message_4, message_5, message_p]
        
        runs = runs - 1

        index_c = random.randint(0, 5)
        message_c = messages[index_c]
        ciphertext = encrypt(message_c)

        # insertions
        for i in range(0, 100, 4):
            t = reverse_translate(random.randint(1, 27))
            ciphertext = ciphertext[:5*(i + 1)] + t + ciphertext[5*(i+1):]

        for i in range(0, 100, 4):
            t = reverse_translate(random.randint(1, 27))
            ciphertext = ciphertext[:5*i] + t + ciphertext[5*i:]

        message_pp = ic_attack_random_insert(ciphertext)
        message_cc = unique_shift_attack(ciphertext, message_pp)
        if message_cc == message_c:
            if index_c == 5:
                test2_success_count = test2_success_count + 1
            else:
                test1_success_count = test1_success_count + 1
        else:
            if index_c == 5:
                test2_fail_count = test2_fail_count + 1
            else:
                test1_fail_count = test1_fail_count + 1
    end2 = time.time()
    print('Time Elapsed: {}'.format(end2-end))
    print('-------------- results: cyclic encrypt insertion test 4 --------------')
    print('test 1 success: {}'.format(test1_success_count))
    print('test 2 success: {}'.format(test2_success_count))
    print('test 1 failed: {}'.format(test1_fail_count))
    print('test 2 failed: {}'.format(test2_fail_count))

def run_random_encrypt_insertion_test(runs):
    test1_success_count = 0
    test2_success_count = 0
    test1_fail_count = 0
    test2_fail_count = 0
    print('---------- running random encrypt insertion test: {} runs ----------'.format(runs))
    end = time.time()
    while runs:
        message_p = build_plaintext(target_length=500)
        message_1 = "cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch"
        message_2 = "biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago"
        message_3 = "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci"
        message_4 = "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s"
        message_5 = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"
        messages = [message_1, message_2, message_3, message_4, message_5, message_p]
    
        runs = runs - 1

        index_c = random.randint(0, 5)
        message_c = messages[index_c]
        ciphertext = random_encrypt(message_c)

        # insertions
        for i in range(0, 100, 4):
            t = reverse_translate(random.randint(1, 27))
            ciphertext = ciphertext[:5*(i + 1)] + t + ciphertext[5*(i+1):]

        message_pp = ic_attack_random_insert(ciphertext)
        message_cc = unique_shift_attack(ciphertext, message_pp)
        if message_cc == message_c:
            if index_c == 5:
                test2_success_count = test2_success_count + 1
            else:
                test1_success_count = test1_success_count + 1
        else:
            if index_c == 5:
                test2_fail_count = test2_fail_count + 1
            else:
                test1_fail_count = test1_fail_count + 1
    end2 = time.time()
    print('Time Elapsed: {}'.format(end2-end))
    print('-------------- results: random encrypt insertion test --------------')
    print('test 1 success: {}'.format(test1_success_count))
    print('test 2 success: {}'.format(test2_success_count))
    print('test 1 failed: {}'.format(test1_fail_count))
    print('test 2 failed: {}'.format(test2_fail_count))

def run_random_encrypt_insertion_test2(runs):
    test1_success_count = 0
    test2_success_count = 0
    test1_fail_count = 0
    test2_fail_count = 0
    print('---------- running random encrypt insertion test 2: {} runs ----------'.format(runs))
    end = time.time()
    while runs:
        message_p = build_plaintext(target_length=500)
        message_1 = "cabooses meltdowns bigmouth makework flippest neutralizers gipped mule antithetical imperials carom masochism stair retsina dullness adeste corsage saraband promenaders gestational mansuetude fig redress pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch"
        message_2 = "biorhythmic personalizing abjure greets rewashed thruput kashmir chores fiendishly combatting alliums lolly milder postpaid larry annuli codgers apostatizing scrim carillon rust grimly lignifying lycanthrope samisen founds millimeters pentagon humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable acidy duellist potent recyclability capture memorized psalmed meters decline deduced after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago"
        message_3 = "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci"
        message_4 = "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s"
        message_5 = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"
        messages = [message_1, message_2, message_3, message_4, message_5, message_p]
        
        runs = runs - 1

        index_c = random.randint(0, 5)
        message_c = messages[index_c]
        ciphertext = random_encrypt(message_c)

        # insertions
        for i in range(0, 100, 4):
            t = reverse_translate(random.randint(1, 27))
            ciphertext = ciphertext[:5*(i + 1)] + t + ciphertext[5*(i+1):]

        for i in range(0, 100, 4):
            t = reverse_translate(random.randint(1, 27))
            ciphertext = ciphertext[:5*i] + t + ciphertext[5*i:]

        message_pp = ic_attack_random_insert(ciphertext)
        message_cc = unique_shift_attack(ciphertext, message_pp)
        if message_cc == message_c:
            if index_c == 5:
                test2_success_count = test2_success_count + 1
            else:
                test1_success_count = test1_success_count + 1
        else:
            if index_c == 5:
                test2_fail_count = test2_fail_count + 1
            else:
                test1_fail_count = test1_fail_count + 1
    end2 = time.time()
    print('Time Elapsed: {}'.format(end2-end))
    print('-------------- results: random encrypt insertion test 2 --------------')
    print('test 1 success: {}'.format(test1_success_count))
    print('test 2 success: {}'.format(test2_success_count))
    print('test 1 failed: {}'.format(test1_fail_count))
    print('test 2 failed: {}'.format(test2_fail_count))

def main():
    runs = 100
    run_cyclic_encrypt_test(runs)
    run_cyclic_encrypt_test2(runs)
    run_random_encrypt_test(runs)
    run_cyclic_encrypt_insertion_test(runs)
    run_cyclic_encrypt_insertion_test2(runs)
    run_cyclic_encrypt_insertion_test3(runs)
    run_cyclic_encrypt_insertion_test4(runs)
    run_random_encrypt_insertion_test(runs)
    run_random_encrypt_insertion_test2(runs)


if __name__ == "__main__":
    main()