#exercicío retirado de: https://www.urionlinejudge.com.br/judge/en/problems/view/1608

t = int(input(''))

respostas=[]
for i in range(0, t):
    d, l, b = str(input('')).split()
    b=int(b)
    
    p_i=str(input('')).split()

    niobizinhos=[]
    for j in range(0, b):
        bd=str(input('')).split()
       
        for k in range(1, len(bd)-1, 2):
            niobizinhos.append(
                int(p_i[int(bd[int(k)])])*
                int(bd[int(k+1)])
                )

    menor = niobizinhos[0]
    im = 0
    for j in range(1, len(niobizinhos)):
        if(niobizinhos[j] < menor):
            menor=niobizinhos[j]
            im=j

    respostas.append(im+1)

for i in respostas:
    print(i)
