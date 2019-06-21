a = 'abcbseda'
sub = ['']
for x in a:
    sub += [x + i for i in sub]

