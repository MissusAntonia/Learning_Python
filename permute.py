def permute1(seq):
    if not seq:
        return [seq]
    else:
        res=[]
        for i in range(len(seq)):
            rest=seq[:i]+ seq[i+1:]
            for x in permute1(rest):
                res.append(seq[i:i+1]+ x)
        return res


def permute2(seq):
    if not seq: # Shuffle any sequence: generator
        yield seq # Empty sequence
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:] # Delete current node
            for x in permute2(rest): # Permute the others
                yield seq[i:i+1] + x # Add node at front
