#!/usr/bin/python3
# If the sentence is empty, the first character should be equal to None
def multiple_returns(sentence):
    if len(sentence) == 0:
        return len(sentence), None,
    else:
        return len(sentence), sentence[0]
