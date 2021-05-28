#有一口水缸,总容量50升,现在已装15升,每次挑水4升,问几次挑满
counts=0

for i in range(0,51,4):
    if i<=50-15:
        counts=counts+1

print(f'挑满需要:{counts}')