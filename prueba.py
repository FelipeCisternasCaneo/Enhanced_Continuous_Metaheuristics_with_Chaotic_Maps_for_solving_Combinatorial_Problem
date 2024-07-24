import os


data = os.listdir('./Problem/SCP/Instances/')        
for d in data:
    # print(d)
    nombre = d.split(".")[0]
    nombre = f'{nombre[3:]}'
    print(nombre)

# import pandas as pd
# from Problem.FS.Problem import FeatureSelection as fs

# instance = fs('CTG')

# print(instance.getClases())

# print(instance.getDatos())




# instance = KP('f1_l-d_kp_10_269')

# print(instance.getCapacity())
# print(instance.getItems())
# print(instance.getProfits())
# print(instance.getTradeOff())
# print(instance.getWeights())
# print(instance.getOptimum())

# print("----------------------------------------------------------------")

# # solution = np.array([1,1,1,1,1,1,1,1,1,1])
# solution = np.random.randint(low=0, high=2, size = (instance.getItems()))

# print(solution)

# print(instance.factibilityTest(solution))

# print("----------------------------------------------------------------")

# solution = instance.repair(solution)

# print(solution)

# print(instance.fitness(solution))
# print(instance.factibilityTest(solution))


# print("----------------------------------------------------------------")



# ds = 'COM'

# separacion = ds.split("_")

# print(len(separacion))





















# from Problem.EMPATIA.database.prepare_dataset import prepare_47vol_solap

# data_dir = './Problem/EMPATIA/'

# loader = prepare_47vol_solap(data_dir)

# ids = loader.dataset['vol_id'].unique()

# print(ids)

# eliminar = "["

# i = 0
# for id in ids:
#     if i == 12 or i == 13 or i == 23 or i == 25:
#         print(id)
#     else:
#         eliminar = eliminar + "," + str(id)
#     i+=1
    
# print(eliminar)

# loader.dataset = loader.exclude_volunteers([1,3,4,10,11,13,16,20,23,24,25,26,31,35,36,37,38,41,42,44,46,49,52,53,54,56,59,61,62,68,70,71,75,79,81,83,86,93,95,103,104,108,113])

# ids = loader.dataset['vol_id'].unique()

# print(ids)











# import pandas as pd
# from scipy.stats import mannwhitneyu
# from BD.sqlite import BD

# bd = BD()

# tecnicas = bd.obtenerTecnicas()


# for tecnica in tecnicas:
#     for t in tecnicas:
#         if t[0] != tecnica[0]:
#             archivo = open(f'./Resultados/Test_Estadisticos/{tecnica[0]}_contra_{t[0]}.csv', 'w')
#             archivo.close()

# datos = pd.read_csv('./Resultados/fscore_EMPATIA-V01.csv')


# # print(len(tecnicas))
# # i = 1
# # for tecnica in tecnicas:
# #     test_estadistico.write(f' {tecnica[0]} ')
# #     if i < len(tecnicas):
# #         test_estadistico.write(f' , ')
# #     else:
# #         test_estadistico.write(f' \n ')
# #     i += 1

# for tecnica in tecnicas:
#     data_x = datos[datos['MH'].isin([tecnica[0]])]
#     x = data_x['FSCORE']
#     for t in tecnicas:
#         if t[0] != tecnica[0]:
#             data_y = datos[datos['MH'].isin([t[0]])]
#             y = data_y['FSCORE']
#             p_value = mannwhitneyu(x,y, alternative='greater')
#             print(f'Comparando {tecnica[0]} contra {t[0]}: {p_value[1]}')
#             archivo = open(f'./Resultados/Test_Estadisticos/{tecnica[0]}_contra_{t[0]}.csv', 'a')
#             archivo.write(f'{p_value[1]}\n')

# print("------------------------------------------------------------------------------------")
# datos = pd.read_csv('./Resultados/fscore_EMPATIA-V02.csv')

# for tecnica in tecnicas:
#     data_x = datos[datos['MH'].isin([tecnica[0]])]
#     x = data_x['FSCORE']
#     for t in tecnicas:
#         if t[0] != tecnica[0]:
#             data_y = datos[datos['MH'].isin([t[0]])]
#             y = data_y['FSCORE']
#             p_value = mannwhitneyu(x,y, alternative='greater')
#             print(f'Comparando {tecnica[0]} contra {t[0]}: {p_value[1]}')
#             archivo = open(f'./Resultados/Test_Estadisticos/{tecnica[0]}_contra_{t[0]}.csv', 'a')
            # archivo.write(f'{p_value[1]}\n')









        

# x = [1,2,3,4,5,6,7,8,9,10]
# y = [11,22,33,44,55,66,77,88,99,100]

# 

# print(p_value)


# from Problem.FS.Problem import FeatureSelection as fs
# import numpy as np
# from sklearn.model_selection import train_test_split, cross_val_score, KFold
# from sklearn.ensemble import RandomForestClassifier
# # instance = fs('ionosphere')
# instance = fs('LSVT')


# print(instance.getClases())

# print(instance.getDatos().values)


# SEED = 12
# classifier = RandomForestClassifier(random_state = SEED)
        
# # scoring=['accuracy','f1','precision','recall']
# print("------------------------------------------------------------------------------------------------------")
# for i in range(20):
#     accuracy_cross    = cross_val_score(estimator=classifier, X=instance.getDatos().values, y=instance.getClases(), cv=5, n_jobs=5, scoring='accuracy')
#     f1Score_cross     = cross_val_score(estimator=classifier, X=instance.getDatos().values, y=instance.getClases(), cv=5, n_jobs=5, scoring='f1')
#     presicion_cross   = cross_val_score(estimator=classifier, X=instance.getDatos().values, y=instance.getClases(), cv=5, n_jobs=5, scoring='precision')
#     recall_cross      = cross_val_score(estimator=classifier, X=instance.getDatos().values, y=instance.getClases(), cv=5, n_jobs=5, scoring='recall')
#     print(accuracy_cross, np.round(accuracy_cross.mean(), decimals=3))
#     print(f1Score_cross, np.round(f1Score_cross.mean(), decimals=3))
#     print(presicion_cross, np.round(presicion_cross.mean(), decimals=3))
#     print(recall_cross, np.round(recall_cross.mean(), decimals=3))
#     print("------------------------------------------------------------------------------------------------------")


















# from Problem.FS.Problem import FeatureSelection as fs
# from Classical_Techniques.mutual_information_classification import MIR
# from Classical_Techniques.minimal_redundancy_mazimum_relevance import MRMR
# from Classical_Techniques.sequential_feature_selection import SFS
# from Classical_Techniques.recursive_feature_elimination import rfe
# from Classical_Techniques.boruta import boruta
# import numpy as np
# import time

# instancia = 'breast-cancer-wisconsin'

# instance = fs(instancia)

# print(instance.getDatos())
# print(instance.getClases())

# for i in np.arange(0.001, 0.25, 0.001):
#     tiempoInicializacion1 = time.time()
#     lista = MIR(instance.getDatos(), instance.getClases(), threshold = i)
    
#     seleccion = np.where(np.array(lista) == 1)[0]
#     clasificador = 'KNN'
#     parametrosC = 'k:5'
#     fitness, accuracy, f1Score, presicion, recall, mcc, errorRate, totalFeatureSelected = instance.fitness(seleccion, clasificador, parametrosC)
#     tiempoInicializacion2 = time.time()
#     print(
#         f'{lista}'+
#         f', b: {str(fitness)}'+
#         f', t: {str(round(tiempoInicializacion2-tiempoInicializacion1,3))}'+
#         f', a: {str(accuracy)}'+
#         f', fs: {str(f1Score)}'+
#         f', p: {str(presicion)}'+
#         f', rc: {str(recall)}'+
#         f', mcc: {str(mcc)}'+
#         f', eR: {str(errorRate)}'+
#         f', TFS: {str(totalFeatureSelected)}'
#     )

# for i in range(5, instance.getTotalFeature()):
#     tiempoInicializacion1 = time.time()
#     lista = MRMR(instance.getDatos(), instance.getClases(), n_variables=i)
    
#     seleccion = np.where(np.array(lista) == 1)[0]
#     clasificador = 'KNN'
#     parametrosC = 'k:5'
#     fitness, accuracy, f1Score, presicion, recall, mcc, errorRate, totalFeatureSelected = instance.fitness(seleccion, clasificador, parametrosC)
#     tiempoInicializacion2 = time.time()
#     print(
#         f'{lista}'+
#         f', b: {str(fitness)}'+
#         f', t: {str(round(tiempoInicializacion2-tiempoInicializacion1,3))}'+
#         f', a: {str(accuracy)}'+
#         f', fs: {str(f1Score)}'+
#         f', p: {str(presicion)}'+
#         f', rc: {str(recall)}'+
#         f', mcc: {str(mcc)}'+
#         f', eR: {str(errorRate)}'+
#         f', TFS: {str(totalFeatureSelected)}'
#     )

# for i in range(5, instance.getTotalFeature()):
#     tiempoInicializacion1 = time.time()
#     lista = SFS(instance.getDatos(), instance.getClases(), n_variables=i)
    
#     seleccion = np.where(np.array(lista) == 1)[0]
#     clasificador = 'KNN'
#     parametrosC = 'k:5'
#     fitness, accuracy, f1Score, presicion, recall, mcc, errorRate, totalFeatureSelected = instance.fitness(seleccion, clasificador, parametrosC)
#     tiempoInicializacion2 = time.time()
#     print(
#         f'{lista}'+
#         f', b: {str(fitness)}'+
#         f', t: {str(round(tiempoInicializacion2-tiempoInicializacion1,3))}'+
#         f', a: {str(accuracy)}'+
#         f', fs: {str(f1Score)}'+
#         f', p: {str(presicion)}'+
#         f', rc: {str(recall)}'+
#         f', mcc: {str(mcc)}'+
#         f', eR: {str(errorRate)}'+
#         f', TFS: {str(totalFeatureSelected)}'
#     )

# for i in range(5, instance.getTotalFeature()):
#     tiempoInicializacion1 = time.time()
#     lista = rfe(instance.getDatos(), instance.getClases(), n_variables=i)
    
#     seleccion = np.where(np.array(lista) == 1)[0]
#     clasificador = 'KNN'
#     parametrosC = 'k:5'
#     fitness, accuracy, f1Score, presicion, recall, mcc, errorRate, totalFeatureSelected = instance.fitness(seleccion, clasificador, parametrosC)
#     tiempoInicializacion2 = time.time()
#     print(
#         f'{lista}'+
#         f', b: {str(fitness)}'+
#         f', t: {str(round(tiempoInicializacion2-tiempoInicializacion1,3))}'+
#         f', a: {str(accuracy)}'+
#         f', fs: {str(f1Score)}'+
#         f', p: {str(presicion)}'+
#         f', rc: {str(recall)}'+
#         f', mcc: {str(mcc)}'+
#         f', eR: {str(errorRate)}'+
#         f', TFS: {str(totalFeatureSelected)}'
#     )

# for i in np.arange(10, 100, 10):
#     tiempoInicializacion1 = time.time()
#     lista = boruta(instance.getDatos(), instance.getClases(), i)
    
#     seleccion = np.where(np.array(lista) == 1)[0]
#     clasificador = 'KNN'
#     parametrosC = 'k:5'
#     fitness, accuracy, f1Score, presicion, recall, mcc, errorRate, totalFeatureSelected = instance.fitness(seleccion, clasificador, parametrosC)
#     tiempoInicializacion2 = time.time()
#     print(
#         f'{lista}'+
#         f', b: {str(fitness)}'+
#         f', t: {str(round(tiempoInicializacion2-tiempoInicializacion1,3))}'+
#         f', a: {str(accuracy)}'+
#         f', fs: {str(f1Score)}'+
#         f', p: {str(presicion)}'+
#         f', rc: {str(recall)}'+
#         f', mcc: {str(mcc)}'+
#         f', eR: {str(errorRate)}'+
#         f', TFS: {str(totalFeatureSelected)}'
#     )