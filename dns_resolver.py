import dns.resolver 
from colorama import Fore, Back, Style

print("Example: google.com")

ans = input("Enter Domain Name: ")
answers = dns.resolver.resolve(ans, "MX")
answers1 = dns.resolver.resolve(ans, "A")
answers2 = dns.resolver.resolve(ans, "AAAA")
answers3 = dns.resolver.resolve(ans, "NS")

for rdata in answers:
    if rdata.status == 200:
        print("")
        print(Fore.RED + "MX Record")
        print('Host', rdata.exchange, 'has prefence', rdata.preference)
    else:
        print("MX not found")
for rdata in answers1:
    if rdata == True:
        print("")
        print(Fore.CYAN + "A Record")
        print('Host', rdata.exchange, 'has prefence', rdata.preference)
    else:
        print("A not found")
for rdata in answers2:
    if rdata == True:
        print("")
        print(Fore.YELLOW + "AAAA Record")
        print('Host', rdata.exchange, 'has prefence', rdata.preference)
    else:
        print("AAAA not found")
for rdata in answers3:
    if rdata == True:
        print("")
        print(Fore.BLUE + "NS Record")
        print('Host', rdata.exchange, 'has prefence', rdata.preference)
    else:
        print("NS not found")