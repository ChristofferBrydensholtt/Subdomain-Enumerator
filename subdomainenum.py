import dns.resolver
import sys

possibleSubs = []
fwriter = open("foundSubs.txt", "a")


def discoverSubs():
    createlistofsubs()
    for sub in possibleSubs:
        queryline = sub+"."+sys.argv[1]
        try:
            ip_value = dns.resolver.resolve(queryline, 'A')
            if ip_value:
                print(queryline, " was found!")
                fwriter.write(queryline + "\n")

        except dns.resolver.NXDOMAIN:
            print(queryline,"was not found!")

        except dns.resolver.LifetimeTimeout:
            print("Time over, continuing")
            continue
        except dns.resolver.NoAnswer:
            print(queryline + " No Answer")





def createlistofsubs():
    freader = open("subdomains.txt", "r")
    for line in freader:
        possibleSubs.append(line.strip())


discoverSubs()
