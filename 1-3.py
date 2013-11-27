def reverseComplementProblem(pattern):
    l = len(pattern)
    s = ''
    vals = {'A':'T','G':'C','C':'G','T':'A'}
    for i in xrange(pattern):
        s += vals[pattern[l-i]]
    return s
