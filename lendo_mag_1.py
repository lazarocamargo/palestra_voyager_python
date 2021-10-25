# lendo os dados do magnetometro da Voyager 2 (Parametro F1)

import cdflib

mag_cdf = cdflib.CDF("voyager2_48s_mag-vim_20090131_v02.cdf")

F1 = mag_cdf.varget("F1", startrec = 10, endrec = 100, expand = True)

dados_mag_F1 = F1['Data']

import matplotlib.pyplot as plt

plt.plot(dados_mag_F1)

plt.ylabel("Campo Magnetico (nT)")

plt.show()
