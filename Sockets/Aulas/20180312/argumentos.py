import sys
print('foram digitados', len(sys.argv), 'argumentos')
i = 0
for argumento in sys.argv:
    print(i, " argumento ", argumento)
    i += 1
