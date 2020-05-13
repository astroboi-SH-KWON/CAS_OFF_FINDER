#!/home/hkim/anaconda3/bin/python3.6

import os, sys
from collections import OrderedDict


def CountSeq():

    with open('SampleList.txt') as Input:
        for strFile in Input:
            strFile = strFile.replace('\n','').replace('\r','').strip() + '_result.txt'

            with open('./Output/FirstResult/' + strFile) as Input,\
                open('./Output/CountResult/' + strFile.split('.')[:-1][0] + '_count.txt' , 'w') as Output:

                dictSeq   = OrderedDict()
                listInput = [strRow.replace('\n','').split('\t') for strRow in Input.readlines()]
                setMut    = set()

                for listCol in listInput:
                    strSeq  = listCol[0]
                    strMut  = listCol[5]
                    setMut.add(strMut)
                    dictSeq[strSeq] = OrderedDict()
                #print(setMut) {'2', '0', '1'}
                listMut = sorted(list(setMut))

                Output.write('\t'.join(['Sequence'] + listMut) + '\n')

                for strSeq in dictSeq:
                    for strMut in listMut:
                        dictSeq[strSeq][strMut] = 0

                for listCol in listInput:
                    strSeq  = listCol[0]
                    strMut  = listCol[5]

                    dictSeq[strSeq][strMut] += 1

                for strSeq, dictValue in dictSeq.items():

                    strCount = '\t'.join([str(v) for k, v in dictValue.items()])
                    Output.write('\t'.join([strSeq, strCount])+'\n')

CountSeq()
