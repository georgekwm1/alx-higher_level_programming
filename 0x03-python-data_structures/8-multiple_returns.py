#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence[0] = None
        tup_len = 0, sentence[0]
        return tup_len
    tup_len = len(sentence), sentence[0]
    return tup_len
