import argparse
import time
from ic_attack import ic_attack, ic_attack_random_insert, build_plaintext
from generic_unique_shift_attack import unique_shift_attack
from test_suite import encrypt_every_t


def main():
    # parser = argparse.ArgumentParser(description='Given a ciphertext, attempts to decrypt it into the correct plaintext.')
    # parser.add_argument('--ciphertext', help='The ciphertext to be analyzed.')
    # cmdline = parser.parse_args()
    # ciphertext = ""
    # if cmdline.ciphertext:
    # 	ciphertext = cmdline.ciphertext
    # else:
    # 	ciphertext = input("Enter ciphertext: ")

    # test2_dict = []
    # with open("english_dict_process.txt") as file:
    #     test2_dict = [line.strip('\n') for line in file]
    # u = 84095
# replace candidate plaintexts with new plaintext when testing for Extra credit

    # p1 = "cabooses meltdowns bigmouth makework flippest neutralizers " + \
    #                "gipped mule antithetical imperials carom masochism stair retsina " + \
    #                "dullness adeste corsage saraband promenaders gestational mansuetude fig redress " +\
    #                "pregame borshts pardoner reforges refutations calendal moaning doggerel dendrology governs " + \
    #                "ribonucleic circumscriptions reassimilating machinize rebuilding mezcal fluoresced antepenults blacksmith " + \
    #                "constance furores chroniclers overlie hoers jabbing resigner quartics polishers mallow hovelling ch"

    # p2 = "biorhythmic personalizing abjure greets " +\
    #               "rewashed thruput kashmir chores fiendishly combatting alliums " +\
    #               "lolly milder postpaid larry annuli codgers apostatizing scrim carillon "+\
    #               "rust grimly lignifying lycanthrope samisen founds millimeters pentagon "+\
    #               "humidification checkup hilts agonise crumbs rejected kangaroo forenoons grazable "+\
    #               "acidy duellist potent recyclability capture memorized psalmed meters decline deduced "+\
    #               "after oversolicitousness demoralizers ologist conscript cronyisms melodized girdles nonago"

    # p3 = "hermitage rejoices oxgall bloodstone fisticuff huguenot janitress assailed eggcup jerseyites fetas leipzig copiers pushiness fesse precociously modules navigates gaiters caldrons lisp humbly datum recite haphazardly dispassion calculability circularization intangibles impressionist jaggy ascribable overseen copses devolvement permutationists potations linesmen hematic fowler pridefully inversive malthus remainders multiplex petty hymnaries cubby donne ohioans avenues reverts glide photos antiaci"
    # p4 = "leonardo oxygenate cascade fashion fortifiers annelids co intimates cads expanse rusting quashing julienne hydrothermal defunctive permeation sabines hurries precalculates discourteously fooling pestles pellucid circlers hampshirites punchiest extremist cottonwood dadoes identifiers retail gyrations dusked opportunities ictus misjudge neighborly aulder larges predestinate bandstand angling billet drawbridge pantomimes propelled leaned gerontologists candying ingestive museum chlorites maryland s"
    # p5 = "undercurrents laryngeal elevate betokened chronologist ghostwrites ombres dollying airship probates music debouching countermanded rivalling linky wheedled heydey sours nitrates bewares rideable woven rerecorded currie vasectomize mousings rootstocks langley propaganda numismatics foetor subduers babcock jauntily ascots nested notifying mountainside dirk chancellors disassociating eleganter radiant convexity appositeness axonic trainful nestlers applicably correctional stovers organdy bdrm insis"

    # Remember to add new plaintext to list
    # test1_list = [p1, p2, p3, p4, p5]

    test2_dict = [
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

    L = 64000
    test1_list = []
    for i in range(0, 5):
        test1_list.append(build_plaintext(L, test2_dict))

    # 84032
    # print("Length: ", len(test2_dict))
    # test2_dict = test2_dict
    # test2_dict = test2_dict[0:50]
    # test2_dict = test2_dict[0:40000]
    # print("Length: ", len(test2_dict))

    plaintext = build_plaintext(L, test2_dict)
    print("Plaintext: ")
    print(plaintext)
    ciphertext = encrypt_every_t(plaintext)



    # Replace test2_dict with another dict when testing for extra credit 2
    # this is default
    # test2_dict = [
    #     "awesomeness",
    #     "hearkened",
    #     "aloneness",
    #     "beheld",
    #     "courtship",
    #     "swoops",
    #     "memphis",
    #     "attentional",
    #     "pintsized",
    #     "rustics",
    #     "hermeneutics",
    #     "dismissive",
    #     "delimiting",
    #     "proposes",
    #     "between",
    #     "postilion",
    #     "repress",
    #     "racecourse",
    #     "matures",
    #     "directions",
    #     "pressed",
    #     "miserabilia",
    #     "indelicacy",
    #     "faultlessly",
    #     "chuted",
    #     "shorelines",
    #     "irony",
    #     "intuitiveness",
    #     "cadgy",
    #     "ferries",
    #     "catcher",
    #     "wobbly",
    #     "protruded",
    #     "combusting",
    #     "unconvertible",
    #     "successors",
    #     "footfalls",
    #     "bursary",
    #     "myrtle",
    #     "photocompose"
    # ]

# test2_dict = [
#     "awesomeness",
#     "hearkened",
#     "aloneness",
#     "beheld",
#     "courtship",
#     "swoops",
#     "memphis",
#     "attentional",
#     "pintsized",
#     "rustics",
#     "hermeneutics",
#     "dismissive",
#     "delimiting",
#     "proposes",
#     "between",
#     "postilion",
#     "repress",
#     "racecourse",
#     "matures",
#     "directions",
#     "pressed",
#     "miserabilia",
#     "indelicacy",
#     "faultlessly",
#     "chuted",
#     "shorelines",
#     "irony",
#     "intuitiveness",
#     "cadgy",
#     "ferries",
#     "catcher",
#     "wobbly",
#     "protruded",
#     "combusting",
#     "unconvertible",
#     "successors",
#     "footfalls",
#     "bursary",
#     "myrtle",
#     "photocompose", # extra
#     "photosynthesis",
#     "hungry",
#     "jeopardy",
#     "foolishness",
#     "ought",
#     "doubtful",
#     "pessimistic"
# ]
    # change this to correct L when testing extra credit.
    # L = 500

    # # Change
    start = time.time()
    message_pp = ic_attack_random_insert(ciphertext, L, test2_dict, test1_list)
    print("M' = ")
    print(unique_shift_attack(ciphertext, message_pp, L, test1_list))
    end = time.time()
    print("Time taken: ", end-start)

if __name__ == "__main__":
    main()