"""
Created  on Fri Jul 30 2021

@author: rgomes
"""

# lançamento vertical
# h = v0 - 0.5gt²
# g = 10 m/s^2
# t = 0.6 s


'''
# uma maneira de calcular h e exibir o resultado
v0=5
g=10
t=0.6
h=v0*t - 0.5*g*t**2
print(h)
'''

# outra maneira de calcular o h [definindo uma função]
# def nome_da_funcao(par1,par2, ..., parn)
# par de parametro
#       comandos1
#       comandos2
#       return alguma coisa

#definição da minha função altura vertical
#=========================================
def h(v0,t,g=9.8):
        return v0*t - 0.5*g*t**2
#=========================================

# aqui a função h está sendo definida em função 
# desses parametros v0, t e g
# veja que não precisamos informar o valor de g, pois já
# está sendo definido dentro dos parametros

#================================================
# outra maneira de calcular a altura é
# deixar em função dos parâmetros e determiná-los depois

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# def h(v0,t,g):
#         return v0*t - 0.5*g*t**2

# print(h(5,0.6,10))
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#=====================================================

# v0=5
# g=10
# t=0.6
# h=v0*t - 0.5*g*t**2
# print(h)
