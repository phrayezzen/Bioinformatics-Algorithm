from itertools import product

def check_strings(a, b, tol):
    t = 0
    for i in xrange(len(a)):
        if a[i] != b[i]:
            t += 1
            if t > tol:
                return False
    return True

def most_kmers(text, k, d):
    kmers = []
    strs = len(text)-k
    maxx = 0
    for i in xrange(strs):
        #curr = "".join(i)
        curr = text[i:i+k]
        count = 0
        for j in xrange(strs):
            check = text[j:j+k]
            if check_strings(curr, check, d):
                count += 1
        if count > maxx:
            kmers = [curr]
            maxx = count
        elif count == maxx:
            kmers.append(curr)


    while True:
        first_max = maxx
        for x in kmers:
            for y in xrange(len(x)):
                for z in 'AGCT':
                    curr = x[0:y]+z+x[y+1:]
                    count = 0
                    for a in xrange(strs):
                        check = text[a:a+k]
                        if check_strings(curr, check, d):
                            count += 1
                    if count > maxx:
                        kmers = [curr]
                        maxx = count
                    elif count == maxx:
                        kmers.append(curr)
        if first_max == maxx:
            break

    return kmers

#kmer = most_kmers('ACGTTGCATGTCGCATGATGCATGAGAGCT',4, 1)
kmer = most_kmers('TAAGAAGAGAACTCTTGTAGTCGATTATCAGTGTAGTCGATTAAGAAGATAAGAAGATATCAGTGAACTCTTTATCAGTTATCAGTTAAGAAGATATCAGTGTAGTCGATACCTCTAGAACTCTTTATCAGTACCTCTAACCTCTATAAGAAGAGAACTCTTTATCAGTTATCAGTGTAGTCGATTAAGAAGAACCTCTAACCTCTAGAACTCTTGAACTCTTACCTCTAGTAGTCGATGAACTCTTGTAGTCGATGTAGTCGATACCTCTAGAACTCTTTAAGAAGAGTAGTCGATTAAGAAGAGTAGTCGATGAACTCTTACCTCTAACCTCTAGTAGTCGATGTAGTCGATGTAGTCGATTAAGAAGAACCTCTATATCAGTGTAGTCGATTAAGAAGATAAGAAGATATCAGTTATCAGTTAAGAAGAGAACTCTTGAACTCTTTAAGAAGAGAACTCTTACCTCTAACCTCTATATCAGTGAACTCTTGTAGTCGATTAAGAAGAACCTCTAGTAGTCGATTATCAGTGTAGTCGATGAACTCTTTATCAGTACCTCTAGAACTCTTGAACTCTTTATCAGTTAAGAAGATATCAGTGAACTCTTTAAGAAGATAAGAAGATATCAGTACCTCTAGAACTCTTTATCAGTTATCAGTTAAGAAGAGTAGTCGATGTAGTCGATTATCAGTTATCAGTGTAGTCGATACCTCTATATCAGTGTAGTCGATTATCAGTTAAGAAGAGAACTCTTGTAGTCGATGAACTCTTACCTCTAACCTCTAACCTCTATATCAGTGTAGTCGATGTAGTCGATACCTCTA',10, 3)

print " ".join(kmer)
