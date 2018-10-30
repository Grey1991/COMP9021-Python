money = [1,2,5,10,20,50,100]
amount = int(input('Input the desired amount: '))

L = []
while amount:
    current = money.pop()
    if current<= amount:
        num = amount//current
        amount = amount%current
        L.append((current,num))
total = sum(i[1] for i in L)
if total == 1:
    print('\n1 banknote is needed.')
else:
    print('\n{} banknotes are needed.'.format(total))
print('The detail is:')
for i in L:
    print('{:>4}: {}'.format('$'+str(i[0]),i[1]))
