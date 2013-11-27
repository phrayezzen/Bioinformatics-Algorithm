def frequentWordsProblem(text, k):
    """
    Frequent Words Problem: Find the most frequent k-mers in a string.
     Input: A string Text and an integer k.
     Output: All most frequent k-mers in Text.
     """
    freq = {}
    for i in xrange(len(text)-k):
        if text[i:i+k] not in freq:
            freq[text[i:i+k]] = 0
        freq[text[i:i+k]] += 1
        
    maxx = max(freq.values())
    maxes = set()
    for k in freq.iterkeys():
        if freq[k] == maxx:
            maxes.add(k)

    s = ''
    for i in maxes:
        s += i + ' '

    return s[0:len(s)-1]
