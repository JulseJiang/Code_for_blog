# encoding: utf-8
"""
@author: julse@qq.com
@time: 2020/12/1 20:17
@desc:
"""
def readIDlist(filePath,by = '\n'):
    fo = open(filePath,'r')
    lines = fo.readlines()
    # 'P67999\n', 'P0ADV1\n', 'P0A6F5\n',
    list = []
    for line in lines:
        list.append(line.split(by)[0])
    fo.close()
    # 'P67999', 'P0ADV1', 'P0A6F5'
    return list
def extractPPIFromIntAct(finPair,foutPair):
    # finPair = r'E:\data\intact\intact.txt'
    # foutPair = r'E:\data\intact\pair.txt'
    with open(finPair, 'r', encoding='UTF-8') as fi, open(foutPair, 'w') as fo:
        line = fi.readline()
        while (line):
            line = fi.readline()
            pair = line.split('\t', maxsplit=2)
            try:
                a = pair[0]
                b = pair[1]
                if 'uniprotkb:' in a and 'uniprotkb:' in b:
                    a = a.replace('uniprotkb:', '')
                    b = b.replace('uniprotkb:', '')
                    if '-' in a: a = a.split('-')[0]
                    if '-' in b: b = b.split('-')[0]
                    fo.write('%s\t%s\n' % (a, b))
                    fo.flush()
                    print(a, b)
                else:
                    continue
            except:
                print(pair)
def findPartner(finPair,foutPair,finList):
    # finPair = r'E:\data\intact\pair.txt'
    # foutPair = r'E:\data\intact\pair_related.txt'
    # finList = r'E:\githubCode\BioDataCoding\Parsers\ttd\TMP_accession_list.csv'
    TMPlist = readIDlist(finList)
    count = 0
    with open(finPair, 'r', encoding='UTF-8') as fi, open(foutPair, 'w') as fo:
        line = fi.readline()
        while (line):
            pair = line[:-1].split('\t', maxsplit=2)
            try:
                a = pair[0]
                b = pair[1]
                if a in TMPlist and b in TMPlist:
                    fo.write('%s\t%s\n' % (a, b))
                else:
                    if a in TMPlist:
                        fo.write('%s\t%s\n' % (a, b))
                    if b in TMPlist:
                        fo.write('%s\t%s\n' % (b, a))
                fo.flush()
                count = count + 1
                print(count)
            except:
                print(pair)
            line = fi.readline()
if __name__ == '__main__':
    print()
    # finPair = r'E:\data\intact\intact.txt'
    # foutPair = r'E:\data\intact\pair.txt'
    # extractPPIFromIntAct(finPair, foutPair)

    # finPair = r'E:\data\intact\pair.txt'
    # foutPair = r'E:\data\intact\pair_related.txt'
    # finList = r'E:\githubCode\BioDataCoding\Parsers\ttd\TMP_accession_list.csv'
    # findPartner(finPair, foutPair, finList)