def allparams(a, b, /, c=42, *arg, d=256, **kwargs):
    print('a,b', a, b)
    print('c,d', c, d)
    print("args", arg)
    print("kwargs", kwargs)


allparams(1, 2)
allparams(1, 2, 3)
# c,d 3 256
allparams(1, 2, c=7)
allparams(1, 2, c=7)
# / - oddziela pozycyjne od arg po nazwie, te z lewej strony tylko jako pozycyjne
allparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, d=89)
allparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, d=89, e=78, k=67, radek='radek')
allparams(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, e=78, k=67, radek='radek')
# a,b 1 2
# c,d 3 256
# args (4, 5, 6, 7, 8, 9, 0, 10)
# kwargs {'e': 78, 'k': 67, 'radek': 'radek'}