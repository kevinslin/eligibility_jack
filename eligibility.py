#!/usr/bin/envy python2.7
import random
import time

mcm_crest_medium = """
$$O:Z$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Z$=ZZ$$
Z$$$~~$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Z:O=$Z$$$
$$$ZZ~$~Z$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Z$$~:OZ$$$$$
$$$$$$O~~O$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$:O:$$$$$$$$
$$$$$$$$=7~Z$$$$$$$$$$$$$MNO$$Z8M8Z$$$$$$$$$$$$Z~~7$$$$$$$$$
$$$$$$$$ZZ~~=$$$$$$ZOIDO8N88+?ZOO8OD7IMZ$$$$ZZ~I:$$$$$$$$$$$
$$$$$$$$$$Z~Z~$$ZDI8888O+O8O=8:OO=O:OOO8IZ$$~~~87$$$$$$$$$$$
$$$$$$$$$$$$O~I$DOO~O,OO8:DO8ODOOODOOOO8DOIM~:$$$$$$$$$$$$$$
$$$$$$$$$$$$$M$D8:8D7DOO887?77?I8DOOOO7NODODIZ$$$$$$$$$$$$$$
$$$$$$$$$$$$I8O:OO~OO$DZ$$8+~~=M$$ZM?DO8D8?NNZM7$$$$$$$$$$$$
$$$$$$$$$$ZIOO....,==~~~=~~==~~=~~~~~~==....MOD8$$$$$$$$$$$$
$$$$$$$$$D$88O......+~=~~~+D8DONNN=~~= .... M:O8$$$$$$$$$$$$
$$$$$$$$$I8:~8.    +$O88==Z88OOOOM~~M:......MOOODN$$$$$$$$$$
$$$$$$$$I8~NOO~=   .+8O.~MDMI8DOO8~OOO8...:=M~IOO7Z$$$$$$$$$
$$$$$$$$DOOOD8~~~,..I.8O8NDONOOOON.D.NN..=~=M88DO8I$$$$$$$$$
$$$$$$$MO:O8DO~~~~~ .,NO88OOOOOOON.8...:~~~=M8~:OD7$$$$$$$$$
$$$$$$$IOD~~D7~~~~~=~. ,8N8OOOO8M...M.~=~~~=MO8DOOD$$$$$$$$$
$$$$$$$IOOO7OI~~~~~~~=..DOO8NN8O+...ZN~~~~~=MZN+~88N$$$$$$$$
$$$$$$$IDNO8O$~~~~~~IZ88OO8O8OOOOM:~~N~~~~~~MMDN8?ON$$$$$$$$
$$$$$$$I8I=~D?=~~~~MD88NDNM..N8OOOD===M~~~~=M8O8OO8D$$$$$$$$
$$$$$$$7O?OO88M~~~~~+~=+.NOOOOO8OOON~MN~~~~~$O:888D$$$$$$$$$
$$$$$$7MO~D88OM~=~~~=~,..MOOONIOOOO?N+~~~~~NOO==:DI$$$$$$$$$
$$$$$$$$$OONNI777~~~:.,:.8OO8~ MOO8...~~~~~IOOOOO88$7$$$$$$$
$$$$$$$7$OII7III7~~ .NNMOOOO88=~.8OOD. ==~8OOOOOOI$7$$$$$$$$
$$$$$777ZI7ID8O87I....NN.D===D8~8OON.....NOOOOO8ON7777$$77$$
$$$77$777IINON8OOID ....=~~~~OOO8D,....,?OOOOOODN777777777$$
$777$77$$77IOOOOOO8ZM.~=~===~~M7=~~~.8+8OOOOOOOM7$7777777777
$777$8?$77Z8N8OOOOOODZ7ODDID88DDOZM?DOOOOOOOOI+~$77ZO$777777
$77777$:$~~::IOOOOOOOONIN$OOOOOO7DOOOOOOOOO8O?=7~ODN77777777
777$777$D8~$$7$M8OOI8OOOO$OOZI8O78OOOOOOO8D$77$~8DD$77777777
777$$78ONNO$77777$D8OOOOO$OOOOOO7D8OO8DID$7777$D8DOO$$777777
7$7$7OOO777N$$7777787ZOOOZOOOOOO7888D8O$77777$+$778ZO8$$7777
77$D8O8$777$777777777$ZN$M8OOOOOD7OO777777777Z7777$$8O877777
$O8DO7777777777777777777$MI8OO8IIZ777777777777777777$$D8O877
OOO877777777777777777777$7IDN787I?77777777777777777777$OOO7$
$Z$7777777777777777777777IZ?=~~?7O777777777777777777777$$$77
7777777777777777777777777IIO~=Z~7$77777777777777777777777777
77777777777777777777777777DI7III7777777777777777777777777777
777777777777777777777777777777777777777777777777777777777777
"""

# Number of people that will be assigned housing
LIMIT = 10
NAMES = "eligibility.txt"
DIVIDER = "-----------------------------------"

def main():
    """
    Run eligiblity jack
    """
    print ("starting eligibility jack...")
    out = []
    with open("eligibility.txt", "r") as fh: lines = fh.readlines()
    lines = map(lambda x: x.rstrip("\n"), lines)
    num = 1
    while (lines):
        name = random.choice(lines)
        out.append((num, name))
        lines.remove(name)
        print (num, name)
        num += 1
        #time.sleep(0.5)
        if (num == LIMIT+1): print (DIVIDER)
    return out


if __name__ == "__main__":
    print (mcm_crest_medium)
    print ("Welcome to the eligibility jack...")
    print ("People who are assigned numbers 1 to %d are guaranteeed housing" %
            LIMIT)
    print ("Hit any key to begin...")
    raw_input("")
    res = main()
    print (DIVIDER)
    with open ("eligibility_results.txt", "w+") as fh:
        fh.write(DIVIDER)
        fh.write("guaranteed:\n")
        for name in res[:LIMIT]: fh.write(str(name[0]) + ": " + name[1] + "\n")
        fh.write(DIVIDER)
        fh.write("waiting list:\n")
        for name in res[LIMIT:]:
            fh.write(str(name[0]) + ": " + name[1] + "\n")
