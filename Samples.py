__author__ = 'laptevsasha'


def isStringPolynom(s):
    if s == s[-1::-1]:
        return "yes, it is"
    else:
        return "no, it isn't"

if __name__ == '__main__':
    testStingMas = ["111111", "abrakadabra", "tyt","","\n"]
    for testString in testStingMas:
        print(isStringPolynom(testString))