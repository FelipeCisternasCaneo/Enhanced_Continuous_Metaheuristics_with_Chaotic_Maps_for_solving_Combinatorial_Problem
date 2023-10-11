import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import seaborn as sns
from util import util
from BD.sqlite import BD
bd = BD()
tablas = False
graficos = True
diversidad = False
dirResultado = './Resultados/'

instancias = bd.obtenerInstanciasEjecutadas('SCP')
mhs = bd.obtenerTecnicas()

if tablas:

    archivoResumenFitness = open(f'{dirResultado}resumen_fitness_SCP.csv', 'w')
    archivoResumenTimes = open(f'{dirResultado}resumen_times_SCP.csv', 'w')
    archivoResumenPercentage = open(f'{dirResultado}resumen_percentage_SCP.csv', 'w')

    archivoResumenFitness.write(',')
    archivoResumenTimes.write(',')
    archivoResumenPercentage.write(',')

    for instancia in instancias:
        if instancia[0] != 'scpc1' and instancia[0] != 'scpd1':
            archivoResumenFitness.write(f' ,{instancia[0]}, ,')
            archivoResumenTimes.write(f' ,{instancia[0]}, ,')
            archivoResumenPercentage.write(f' ,{instancia[0]},')

    archivoResumenFitness.write(' \n')
    archivoResumenTimes.write(' \n')
    archivoResumenPercentage.write(' \n')

    archivoResumenFitness.write('experiment ')
    archivoResumenTimes.write('experiment ')
    archivoResumenPercentage.write('experiment ')

    for instancia in instancias:
        if instancia[0] != 'scpc1' and instancia[0] != 'scpd1':
            archivoResumenFitness.write(f',best, avg. , RPD')
            archivoResumenTimes.write(f',min time (s), avg. time (s), std time (s)')
            archivoResumenPercentage.write(f',avg. XPL%, avg. XPT%')

    archivoResumenFitness.write(' \n')
    archivoResumenTimes.write(' \n')
    archivoResumenPercentage.write(' \n')

    for mh in mhs:
        
        experimentos = bd.obtenerExperimentos('SCP', mh[0])
        
        for experimento in experimentos:
            
            archivoResumenFitness.write(f'{experimento[0]}')
            archivoResumenTimes.write(f'{experimento[0]}')
            archivoResumenPercentage.write(f'{experimento[0]}')
            
            for instancia in instancias:
                if instancia[0] != 'scpc1' and instancia[0] != 'scpd1':
                    ejecuciones = bd.obtenerEjecuciones(instancia[0], mh[0], experimento[0])
                    
                    tiempos         = []
                    rendimiento     = []
                    exploracion     = []
                    explotacion     = []
                    optimo          = bd.obtenerOptimoInstancia(instancia[0])
                    optimo = float(optimo[0][0])
                    
                    print(f'Analizando experimento {experimento[0]} asociado a la instancia {instancia[0]} metaheuristica {mh[0]} -- optimo: {optimo}')
                    
                    for ejecucion in ejecuciones:
                        id                  = ejecucion[0]
                        nombre_archivo      = ejecucion[2]
                        archivo             = ejecucion[3]
                        tiempo_ejecucion    = ejecucion[5]
                        
                        direccionDestiono = './Resultados/Transitorio/'+nombre_archivo+'.csv'
                        # print("-------------------------------------------------------------------------------")
                        util.writeTofile(archivo,direccionDestiono)
                        
                        data = pd.read_csv(direccionDestiono, on_bad_lines='skip')
                        
                        iteraciones = data['iter']
                        fitness     = data['fitness']
                        time        = data['time']
                        xpl         = data['XPL']
                        xpt         = data['XPT']
                        
                        ultimo = len(iteraciones) - 1
                        
                        rendimiento.append(fitness[ultimo])
                        exploracion.append(np.round(np.mean(xpl), decimals=2))
                        explotacion.append(np.round(np.mean(xpt), decimals=2))
                        tiempos.append(tiempo_ejecucion)
                    
                        if diversidad:
                            
                            if not os.path.exists(f'{dirResultado}/Graficos/SCP/{experimento[0]}/{instancia[0]}'):
                                os.makedirs(f'{dirResultado}/Graficos/SCP/{experimento[0]}/{instancia[0]}')
                            
                            figPER, axPER = plt.subplots()
                            axPER.plot(iteraciones, xpl, color="r", label=r"$\overline{XPL}$"+": "+str(np.round(np.mean(xpl), decimals=2))+"%")
                            axPER.plot(iteraciones, xpt, color="b", label=r"$\overline{XPT}$"+": "+str(np.round(np.mean(xpt), decimals=2))+"%")
                            axPER.set_title(f'XPL% - XPT% {mh[0]} {experimento[0].split("-")[1]} {instancia[0]}')
                            axPER.set_ylabel("Percentage")
                            axPER.set_xlabel("Iteration")
                            axPER.legend(loc = 'upper right')
                            plt.savefig(f'{dirResultado}/Graficos/SCP/{experimento[0]}/{instancia[0]}/Percentage_{instancia[0]}_{experimento[0]}_{id}.pdf')
                            plt.close('all')
                            print(f'Grafico de exploracion y explotacion realizado para {experimento[0]}, id: {id}, instancia: {instancia[0]}')
                        
                        os.remove('./Resultados/Transitorio/'+nombre_archivo+'.csv')
                    
                    rpd = np.round( ( (100 * ( np.min(rendimiento) - optimo ) ) / optimo), 3 )
                    
                    archivoResumenFitness.write(f',{np.min(rendimiento)},{np.round(np.average(rendimiento),3)},{rpd}')
                    # archivoResumenTimes.write(f',{np.min(tiempos)},{np.round(np.average(tiempos),3)},{np.std(np.average(tiempos),3)}')
                    # archivoResumenPercentage.write(f',{np.round(np.average(exploracion),3)},{np.round(np.average(explotacion),3)}')

            archivoResumenFitness.write(' \n')
            archivoResumenTimes.write(' \n')
            archivoResumenPercentage.write(' \n')

    archivoResumenFitness.close()
    archivoResumenTimes.close()
    archivoResumenPercentage.close()
    
if graficos:
    iteraciones     = []
    rendimientos    = dict()
    if not os.path.exists(f'{dirResultado}/Best/SCP'):
        os.makedirs(f'{dirResultado}/Best/SCP')    
    for mh in mhs:
        experimentos = bd.obtenerExperimentosEspecial('SCP', mh[0], 'STD')
        for instancia in instancias:
            figSTD, axSTD = plt.subplots()
            noGraficar = False
            for experimento in experimentos:
                if instancia[0] != 'scpc1' and instancia[0] != 'scpd1':
                    mejor = bd.obtenerMejoresEjecucionesSCP(instancia[0], mh[0], experimento[0])
                    print(f'Analizando experimento {experimento[0]} asociado a la instancia {instancia[0]} metaheuristica {mh[0]}')
                    for m in mejor:
                        id                  = m[0]
                        nombre_archivo      = m[2]
                        archivo             = m[3]
                        direccionDestiono = './Resultados/Transitorio/'+nombre_archivo+'.csv'
                        # print("-------------------------------------------------------------------------------")
                        util.writeTofile(archivo,direccionDestiono)                        
                        data = pd.read_csv(direccionDestiono, on_bad_lines='skip')
                        if len(data['iter']) == 501:
                            iteraciones = data['iter']
                        fitness     = data['fitness']
                        rendimientos[f'{experimento[0]} - {instancia[0]}'] = fitness
                        
                        os.remove('./Resultados/Transitorio/'+nombre_archivo+'.csv')
            if instancia[0] != 'scpc1' and instancia[0] != 'scpd1':            
                for clave in rendimientos:
                    etiqueta = f'{clave.split("-")[1]}'
                    if mh[0] in clave and instancia[0] in clave and 'STD' in clave:        
                        if len(rendimientos[clave]) == 501:
                            print("Entre al if",str(len(rendimientos[clave])),noGraficar, str(len(iteraciones)))
                            axSTD.plot(iteraciones, rendimientos[clave], label=etiqueta)
                        else: 
                            print("Entre al else",str(len(rendimientos[clave])),noGraficar)
                            noGraficar = True
                if not noGraficar:
                    axSTD.set_title(f'Coverage {instancia[0]} - {mh[0]} - STD')
                    axSTD.set_ylabel("Fitness")
                    axSTD.set_xlabel("Iteration")
                    axSTD.legend(loc = 'upper right')
                    plt.savefig(f'{dirResultado}/Best/SCP/fitness_{instancia[0]}_{mh[0]}_STD.pdf')
                    plt.close('all')
                    print(f'Grafico de fitness realizado {instancia[0]} - {mh[0]} - STD')     
                
                
    for mh in mhs:
        experimentos = bd.obtenerExperimentosEspecial('SCP', mh[0], 'COM')
        for instancia in instancias:
            figSTD, axSTD = plt.subplots()
            noGraficar = False
            for experimento in experimentos:
                if instancia[0] != 'scpc1' and instancia[0] != 'scpd1':
                    mejor = bd.obtenerMejoresEjecucionesSCP(instancia[0], mh[0], experimento[0])
                    print(f'Analizando experimento {experimento[0]} asociado a la instancia {instancia[0]} metaheuristica {mh[0]}')
                    for m in mejor:
                        id                  = m[0]
                        nombre_archivo      = m[2]
                        archivo             = m[3]
                        direccionDestiono = './Resultados/Transitorio/'+nombre_archivo+'.csv'
                        # print("-------------------------------------------------------------------------------")
                        util.writeTofile(archivo,direccionDestiono)                        
                        data = pd.read_csv(direccionDestiono, on_bad_lines='skip')
                        if len(data['iter']) == 501:
                            iteraciones = data['iter']
                        fitness     = data['fitness']
                        rendimientos[f'{experimento[0]} - {instancia[0]}'] = fitness
                        
                        os.remove('./Resultados/Transitorio/'+nombre_archivo+'.csv')
            if instancia[0] != 'scpc1' and instancia[0] != 'scpd1':            
                for clave in rendimientos:
                    etiqueta = f'{clave.split("-")[1]}'
                    if mh[0] in clave and instancia[0] in clave and 'COM' in clave:        
                        if len(rendimientos[clave]) == 501:
                            print("Entre al if",str(len(rendimientos[clave])),noGraficar, str(len(iteraciones)))
                            axSTD.plot(iteraciones, rendimientos[clave], label=etiqueta)
                        else: 
                            print("Entre al else",str(len(rendimientos[clave])),noGraficar)
                            noGraficar = True
                if not noGraficar:
                    axSTD.set_title(f'Coverage {instancia[0]} - {mh[0]} - COM')
                    axSTD.set_ylabel("Fitness")
                    axSTD.set_xlabel("Iteration")
                    axSTD.legend(loc = 'upper right')
                    plt.savefig(f'{dirResultado}/Best/SCP/fitness_{instancia[0]}_{mh[0]}_COM.pdf')
                    plt.close('all')
                    print(f'Grafico de fitness realizado {instancia[0]} - {mh[0]} - COM') 
                
    for mh in mhs:
        experimentos = bd.obtenerExperimentosEspecial('SCP', mh[0], 'ELIT')
        for instancia in instancias:
            figSTD, axSTD = plt.subplots()
            noGraficar = False
            for experimento in experimentos:
                if instancia[0] != 'scpc1' and instancia[0] != 'scpd1':
                    mejor = bd.obtenerMejoresEjecucionesSCP(instancia[0], mh[0], experimento[0])
                    print(f'Analizando experimento {experimento[0]} asociado a la instancia {instancia[0]} metaheuristica {mh[0]}')
                    for m in mejor:
                        id                  = m[0]
                        nombre_archivo      = m[2]
                        archivo             = m[3]
                        direccionDestiono = './Resultados/Transitorio/'+nombre_archivo+'.csv'
                        # print("-------------------------------------------------------------------------------")
                        util.writeTofile(archivo,direccionDestiono)                        
                        data = pd.read_csv(direccionDestiono, on_bad_lines='skip')
                        if len(data['iter']) == 501:
                            iteraciones = data['iter']
                        fitness     = data['fitness']
                        rendimientos[f'{experimento[0]} - {instancia[0]}'] = fitness
                        
                        os.remove('./Resultados/Transitorio/'+nombre_archivo+'.csv')
            if instancia[0] != 'scpc1' and instancia[0] != 'scpd1':            
                for clave in rendimientos:
                    etiqueta = f'{clave.split("-")[1]}'
                    if mh[0] in clave and instancia[0] in clave and 'ELIT' in clave:        
                        if len(rendimientos[clave]) == 501:
                            print("Entre al if",str(len(rendimientos[clave])),noGraficar, str(len(iteraciones)))
                            axSTD.plot(iteraciones, rendimientos[clave], label=etiqueta)
                        else: 
                            print("Entre al else",str(len(rendimientos[clave])),noGraficar)
                            noGraficar = True
                if not noGraficar:
                    axSTD.set_title(f'Coverage {instancia[0]} - {mh[0]} - ELIT')
                    axSTD.set_ylabel("Fitness")
                    axSTD.set_xlabel("Iteration")
                    axSTD.legend(loc = 'upper right')
                    plt.savefig(f'{dirResultado}/Best/SCP/fitness_{instancia[0]}_{mh[0]}_ELIT.pdf')
                    plt.close('all')
                    print(f'Grafico de fitness realizado {instancia[0]} - {mh[0]} - ELIT') 
    
    