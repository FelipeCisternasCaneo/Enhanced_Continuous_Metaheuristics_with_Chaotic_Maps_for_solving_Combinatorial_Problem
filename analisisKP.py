import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import seaborn as sns
from util import util
from BD.sqlite import BD
bd = BD()
tablas = True
graficos = True
diversidad = True
dirResultado = './Resultados/'

instancias = bd.obtenerInstanciasEjecutadas('KP')
mhs = bd.obtenerTecnicas()

if tablas:

    archivoResumenFitness = open(f'{dirResultado}resumen_fitness_KP.csv', 'w')
    archivoResumenTimes = open(f'{dirResultado}resumen_times_KP.csv', 'w')
    archivoResumenPercentage = open(f'{dirResultado}resumen_percentage_KP.csv', 'w')

    archivoResumenFitness.write(',')
    archivoResumenTimes.write(',')
    archivoResumenPercentage.write(',')

    instancias = bd.obtenerInstanciasEjecutadas('KP')
    mhs = bd.obtenerTecnicas()

    for instancia in instancias:
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
        archivoResumenFitness.write(f',best, avg. , RPD')
        archivoResumenTimes.write(f',min time (s), avg. time (s), std time (s)')
        archivoResumenPercentage.write(f',avg. XPL%, avg. XPT%')

    archivoResumenFitness.write(' \n')
    archivoResumenTimes.write(' \n')
    archivoResumenPercentage.write(' \n')

    for mh in mhs:
        
        experimentos = bd.obtenerExperimentos('KP', mh[0])
        
        for experimento in experimentos:
            
            archivoResumenFitness.write(f'{experimento[0]}')
            archivoResumenTimes.write(f'{experimento[0]}')
            archivoResumenPercentage.write(f'{experimento[0]}')
            
            for instancia in instancias:
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
                        
                        if not os.path.exists(f'{dirResultado}/Graficos/KP/{experimento[0]}/{instancia[0]}'):
                            os.makedirs(f'{dirResultado}/Graficos/KP/{experimento[0]}/{instancia[0]}')
                        
                        figPER, axPER = plt.subplots()
                        axPER.plot(iteraciones, xpl, color="r", label=r"$\overline{XPL}$"+": "+str(np.round(np.mean(xpl), decimals=2))+"%")
                        axPER.plot(iteraciones, xpt, color="b", label=r"$\overline{XPT}$"+": "+str(np.round(np.mean(xpt), decimals=2))+"%")
                        axPER.set_title(f'XPL% - XPT% {mh[0]} {experimento[0].split("-")[1]} {instancia[0]}')
                        axPER.set_ylabel("Percentage")
                        axPER.set_xlabel("Iteration")
                        axPER.legend(loc = 'upper right')
                        plt.savefig(f'{dirResultado}/Graficos/KP/{experimento[0]}/{instancia[0]}/Percentage_{instancia[0]}_{experimento[0]}_{id}.pdf')
                        plt.close('all')
                        print(f'Grafico de exploracion y explotacion realizado para {experimento[0]}, id: {id}, instancia: {instancia[0]}')
                    
                    os.remove('./Resultados/Transitorio/'+nombre_archivo+'.csv')
                
                rpd = np.round( ( (100 * ( optimo - np.max(rendimiento) ) ) / optimo), 3 )
                
                archivoResumenFitness.write(f',{np.max(rendimiento)},{np.round(np.average(rendimiento),3)},{rpd}')
                # archivoResumenTimes.write(f',{np.min(tiempos)},{np.round(np.average(tiempos),3)},{np.std(tiempos)}')
                # archivoResumenPercentage.write(f',{np.round(np.average(exploracion),3)},{np.round(np.average(explotacion),3)}')

            archivoResumenFitness.write(' \n')
            archivoResumenTimes.write(' \n')
            archivoResumenPercentage.write(' \n')

    archivoResumenFitness.close()
    archivoResumenTimes.close()
    archivoResumenPercentage.close()
    
if graficos:
    if not os.path.exists(f'{dirResultado}/Best/KP'):
        os.makedirs(f'{dirResultado}/Best/KP')
    iteraciones     = []
    rendimientos    = dict()
    for mh in mhs:
        experimentos = bd.obtenerExperimentosEspecial('KP', mh[0], 'STD')
        for instancia in instancias:
            figSTD, axSTD = plt.subplots()
            noGraficar = False
            for experimento in experimentos:
                mejor = bd.obtenerMejoresEjecucionesKP(instancia[0], mh[0], experimento[0])
                print(f'Analizando experimento {experimento[0]} asociado a la instancia {instancia[0]} metaheuristica {mh[0]}')
                for m in mejor:
                    id                  = m[0]
                    nombre_archivo      = m[2]
                    archivo             = m[3]
                    direccionDestiono = './Resultados/Transitorio/'+nombre_archivo+'.csv'
                    # print("-------------------------------------------------------------------------------")
                    util.writeTofile(archivo,direccionDestiono)                        
                    data = pd.read_csv(direccionDestiono, on_bad_lines='skip')
                    iteraciones = data['iter']
                    fitness     = data['fitness']
                    rendimientos[f'{experimento[0]} - {instancia[0]}'] = fitness
                    
                    os.remove('./Resultados/Transitorio/'+nombre_archivo+'.csv')         
            for clave in rendimientos:
                etiqueta = f'{clave.split("-")[1]}'
                if mh[0] in clave and instancia[0] in clave and 'STD' in clave:        
                    if len(rendimientos[clave]) == 501:
                        axSTD.plot(iteraciones, rendimientos[clave], label=etiqueta)
                    else: 
                        noGraficar = True
                    
            if not noGraficar:
                axSTD.set_title(f'Coverage {instancia[0]} - {mh[0]} - STD')
                axSTD.set_ylabel("Fitness")
                axSTD.set_xlabel("Iteration")
                axSTD.legend(loc = 'lower right')
                plt.savefig(f'{dirResultado}/Best/KP/fitness_{instancia[0]}_{mh[0]}_STD.pdf')
                plt.close('all')
                print(f'Grafico de fitness realizado {instancia[0]} - {mh[0]} - STD')     
                
                
    for mh in mhs:
        experimentos = bd.obtenerExperimentosEspecial('KP', mh[0], 'COM')
        for instancia in instancias:
            figSTD, axSTD = plt.subplots()
            noGraficar = False
            for experimento in experimentos:
                mejor = bd.obtenerMejoresEjecucionesKP(instancia[0], mh[0], experimento[0])
                print(f'Analizando experimento {experimento[0]} asociado a la instancia {instancia[0]} metaheuristica {mh[0]}')
                for m in mejor:
                    id                  = m[0]
                    nombre_archivo      = m[2]
                    archivo             = m[3]
                    direccionDestiono = './Resultados/Transitorio/'+nombre_archivo+'.csv'
                    # print("-------------------------------------------------------------------------------")
                    util.writeTofile(archivo,direccionDestiono)                        
                    data = pd.read_csv(direccionDestiono, on_bad_lines='skip')
                    iteraciones = data['iter']
                    fitness     = data['fitness']
                    rendimientos[f'{experimento[0]} - {instancia[0]}'] = fitness
                    
                    os.remove('./Resultados/Transitorio/'+nombre_archivo+'.csv')           
            for clave in rendimientos:
                etiqueta = f'{clave.split("-")[1]}'
                if mh[0] in clave and instancia[0] in clave and 'COM' in clave:        
                    if len(rendimientos[clave]) == 501:
                        axSTD.plot(iteraciones, rendimientos[clave], label=etiqueta)
                    else: 
                        noGraficar = True
            if not noGraficar:
                axSTD.set_title(f'Coverage {instancia[0]} - {mh[0]} - COM')
                axSTD.set_ylabel("Fitness")
                axSTD.set_xlabel("Iteration")
                axSTD.legend(loc = 'lower right')
                plt.savefig(f'{dirResultado}/Best/KP/fitness_{instancia[0]}_{mh[0]}_COM.pdf')
                plt.close('all')
                print(f'Grafico de fitness realizado {instancia[0]} - {mh[0]} - COM') 
                
    for mh in mhs:
        experimentos = bd.obtenerExperimentosEspecial('KP', mh[0], 'ELIT')
        for instancia in instancias:
            figSTD, axSTD = plt.subplots()
            noGraficar = False
            for experimento in experimentos:
                mejor = bd.obtenerMejoresEjecucionesKP(instancia[0], mh[0], experimento[0])
                print(f'Analizando experimento {experimento[0]} asociado a la instancia {instancia[0]} metaheuristica {mh[0]}')
                for m in mejor:
                    id                  = m[0]
                    nombre_archivo      = m[2]
                    archivo             = m[3]
                    direccionDestiono = './Resultados/Transitorio/'+nombre_archivo+'.csv'
                    # print("-------------------------------------------------------------------------------")
                    util.writeTofile(archivo,direccionDestiono)                        
                    data = pd.read_csv(direccionDestiono, on_bad_lines='skip')
                    iteraciones = data['iter']
                    fitness     = data['fitness']
                    rendimientos[f'{experimento[0]} - {instancia[0]}'] = fitness
                    
                    os.remove('./Resultados/Transitorio/'+nombre_archivo+'.csv')         
            for clave in rendimientos:
                etiqueta = f'{clave.split("-")[1]}'
                if mh[0] in clave and instancia[0] in clave and 'ELIT' in clave:        
                    if len(rendimientos[clave]) == 501:
                        axSTD.plot(iteraciones, rendimientos[clave], label=etiqueta)
                    else: 
                        noGraficar = True
            if not noGraficar:
                axSTD.set_title(f'Coverage {instancia[0]} - {mh[0]} - ELIT')
                axSTD.set_ylabel("Fitness")
                axSTD.set_xlabel("Iteration")
                axSTD.legend(loc = 'lower right')
                plt.savefig(f'{dirResultado}/Best/KP/fitness_{instancia[0]}_{mh[0]}_ELIT.pdf')
                plt.close('all')
                print(f'Grafico de fitness realizado {instancia[0]} - {mh[0]} - ELIT') 

