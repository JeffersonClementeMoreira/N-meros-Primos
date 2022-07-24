from array import array

def inicial_primo(primo):


    if (primo == 2 or primo == 3 or primo == 5):
        e_primo.append(primo)
    else: 
         
        if ( primo % 2 == 0 ):
            nao_primo.append(primo)
        else:   
            soma = 0
            primo_analise = primo
            while (primo_analise > 0):
                resto = primo_analise % 10
                primo_analise = (primo_analise - resto)/10
                soma = soma + resto

            if (soma % 3 == 0 ):
                nao_primo.append(primo)
            else: 
                if(primo % 10 == 5 or primo % 10 == 0 ):
                    nao_primo.append(primo)
                else:
                    for i in range(len(e_primo)):
                        resto_primo =  primo % e_primo[i]
                        if (resto_primo == 0):
                            nao_primo.append(primo)
                            break

                        if i == (len(e_primo)-1):                   
                            e_primo.append(primo)              


    return e_primo





def numerosprimos(arrayprimos):

    arrayprimos = list(range(arrayprimos+1))
    global nao_primo
    global e_primo
    global primo


    nao_primo = []
    e_primo = []
    

    for i in range(1 , len(arrayprimos)):
        primo = arrayprimos[i]
        inicial_primo(primo)

    arrayprimos = e_primo


    return arrayprimos


numerosprimos(150)
