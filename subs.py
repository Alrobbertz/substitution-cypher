# Andrew Robbertz alrobbertz@wpi.edu
# Last Modified 11/01/2018
import string
import csv

cipher_text = '''CKCLBAELDK DGJ LFNSMBCA CGQEGCCAI JCUCKFS DGJ LACDBC SAFJMLBI BHDB LHDGQC BHC OFAKJ DGJ NDVC FMA KEUCI CDIECA BHC LCKK SHFGCI OC JCSCGJ FG BHC LFNSMBCAI MICJ EG GDBEFGDK ICLMAEBR DGJ BHC CKCLBAELDK IRIBCNI BHDB NDVC FMA LDAI FSCADBC OCAC DKK LACDBCJ TR CKCLBAELDK DGJ LFNSMBCA CGQEGCCAI DB OSE OC VCCS BHDB SAFQACII NFUEGQ PFAODAJ OEBH FMA EGGFUDBEUC ACICDALH DGJ FMB-FP-BHC TFY DSSAFDLHCI BHC JCSDABNCGB FP CKCLBAELDK DGJ LFNSMBCA CGQEGCCAEGQDB OSE LHDKKCGQCI IBMJCGBI BF SMIH BHCNICKUCI BF MGJCAIBDGJ IFLECBRI DGJ BCLHGFKFQRI LFNSKCY EIIMCI EG D TAFDJCA LFGBCYB BHDG OHDBI EG PAFGB FP BHCN OC ODGB FMA IBMJCGBI OHCBHCA BHCR DAC CDAGEGQ DG MGJCAQADJMDBC NEGFA FA D JFLBFADBC BF BDLVKC IFLECBRI NFIB SACIIEGQ SAFTKCNI DGJ MGLFUCA GCO ODRI FP IFKUEGQ BHCN OHCBHCA EBI JCUCKFSEGQ IRIBCNI BHDB LDG KFLDBC PEACPEQHBCAI EG BHC NEJJKC FP D TMAGEGQ TMEKJEGQ FA LACDBEGQ GCMAFSAFIBHCBELI BHDB KFFV DGJ PMGLBEFG KEVC GDBMADK KENTI FMA PDLMKBR DGJ IBMJCGBI DAC DB BHC PAFGB CJQC FP ACNDAVDTKC EGGFUDBEFG OHEKC DJUDGLEGQ BCLHGFKFQECI EI DB FMA LFAC OC DKIF BDVC HMNDG LFGGCLBEFGI UCAR ICAEFMIKR EG CLC OC SAEJC FMAICKUCI FG BHC PDNEKR-KEVC DBNFISHCAC OC LMKBEUDBC; PDLMKBR IBMJCGBI DGJ IBDPP CGLFMADQC CDLH FBHCAI CUCAR IMLLCII DGJ DAC BHCAC PFA BHC LHDKKCGQCI TFBH EG BHC LKDIIAFFN DGJ EG KEPC'''
englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
                     'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

# Create a Hash to store letter frequencies
alphabet = string.ascii_uppercase
cipherFreq = {letter: 0.00 for letter in alphabet}

# Count letter Frequency in the Cyphertext
for letter in cipher_text:
    if(letter.isalpha()):
        cipherFreq[letter] += 1


# Sort the cyphertext frequencies
cipherFreq = [(l, f/len(cipher_text)) for l, f in cipherFreq.iteritems()]
cipherFreq.sort(key=lambda x: x[1], reverse=True)
# Sort Actual English Language Frequencies
engFreq = [(l, f) for l, f in englishLetterFreq.iteritems()]
engFreq.sort(key=lambda x: x[1], reverse=True)
# Match the cypher text letters to English Language letters
mapping = {cipherFreq[i][0]: engFreq[i][0] for i in range(len(engFreq))}

'''
Within the dictionary, the first char is the cipher text value,
and the second char is the message text value.
For example, an 'A' in the cipher text maps to a 'R' in the message text.
'''
mapping = {
    'A': 'R',
    'C': 'E',
    'B': 'T',
    'E': 'I',
    'D': 'A',
    'G': 'N',
    'F': 'O',
    'I': 'S',
    'H': 'H',
    'K': 'L',
    'J': 'D',
    'M': 'U',
    'L': 'C',
    'O': 'W',
    'N': 'M',
    'Q': 'G',
    'P': 'F',
    'S': 'P',
    'R': 'Y',
    'U': 'V',
    'T': 'B',
    'W': 'J',
    'V': 'K',
    'Y': 'X',
    'X': 'Q',
    'Z': 'Z'}

# Try to convert cypher text into plain
plain_text = ''''''
for char in cipher_text:
    if(char.isalpha()):
        plain_text += mapping[char]
    else:
        plain_text += char

print(plain_text)
