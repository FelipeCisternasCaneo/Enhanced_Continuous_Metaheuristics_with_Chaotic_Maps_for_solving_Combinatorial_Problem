from BD.sqlite import BD
import json

bd = BD()


fs  = False
scp = True
ben = False
empatia = False
mkp = False
kp = False
ml = False
mhs = ['GWO','WOA','SCA']
cantidad = 0

DS_actions = [
    'V1-STD', 'V1-COM', 'V1-PS', 'V1-ELIT',
    'V2-STD', 'V2-COM', 'V2-PS', 'V2-ELIT',
    'V3-STD', 'V3-COM', 'V3-PS', 'V3-ELIT',
    'V4-STD', 'V4-COM', 'V4-PS', 'V4-ELIT',
    'S1-STD', 'S1-COM', 'S1-PS', 'S1-ELIT',
    'S2-STD', 'S2-COM', 'S2-PS', 'S2-ELIT',
    'S3-STD', 'S3-COM', 'S3-PS', 'S3-ELIT',
    'S4-STD', 'S4-COM', 'S4-PS', 'S4-ELIT',
]

paramsML = json.dumps({
    'MinMax'        : 'min',
    'DS_actions'    : DS_actions,
    'gamma'         : 0.4,
    'policy'        : 'e-greedy',
    'qlAlphaType'   : 'static',
    'rewardType'    : 'withPenalty1',
    'stateQ'        : 2
})


if empatia:
    # poblar ejecuciones FS
    # instancias = bd.obtenerInstancias(f'''
    #                                   'EMPATIA-V01','EMPATIA-V02','EMPATIA-V03','EMPATIA-V04','EMPATIA-V05','EMPATIA-V06','EMPATIA-V07','EMPATIA-V08','EMPATIA-V09','EMPATIA-V10','EMPATIA-V11','EMPATIA-V12','EMPATIA-V13','EMPATIA-V14','EMPATIA-V15','EMPATIA-V16','EMPATIA-V17','EMPATIA-V18','EMPATIA-V19','EMPATIA-V20','EMPATIA-V21','EMPATIA-V22','EMPATIA-V23','EMPATIA-V24','EMPATIA-V25','EMPATIA-V26','EMPATIA-V27','EMPATIA-V28','EMPATIA-V29','EMPATIA-V30','EMPATIA-V31','EMPATIA-V32','EMPATIA-V33','EMPATIA-V34','EMPATIA-V35','EMPATIA-V36','EMPATIA-V37','EMPATIA-V38','EMPATIA-V39','EMPATIA-V40','EMPATIA-V41','EMPATIA-V42'
    #                                   ''')
    instancias = bd.obtenerInstancias(f'''
                                      'EMPATIA-9'
                                      ''')
    iteraciones = 500
    experimentos = 31
    poblacion = 50
    for instancia in instancias:

        for mh in mhs:
            binarizacion = 'V4-STD'
            if ml:
                data = {}
                data['MH']          = mh
                data['paramMH']     = f'iter:{str(iteraciones)},pop:{str(poblacion)},cros:0.6;mut:0.01'
                data['ML']          = 'Q-Learning'
                data['paramML']     = paramsML
                data['ML_FS']       = ''
                data['paramML_FS']  = ''
                data['estado']      = 'pendiente'

                cantidad +=experimentos
                bd.insertarExperimentos(data, experimentos, instancia[0])
            else:
                data = {}
                data['experimento'] = f'{mh} {binarizacion}'
                data['MH']          = mh
                data['paramMH']     = f'iter:{str(iteraciones)},pop:{str(poblacion)},DS:{binarizacion},cros:0.9;mut:0.20'
                # data['paramMH']     = f'iter:{str(iteraciones)},pop:{str(poblacion)},DS:V4-ELIT'
                # data['paramMH']     = f'iter:{str(iteraciones)},pop:{str(poblacion)},DS:X4-ELIT'
                # data['paramMH']     = f'iter:{str(iteraciones)},pop:{str(poblacion)},DS:Z4-ELIT'
                data['ML']          = ''
                data['paramML']     = ''
                data['ML_FS']       = ''
                data['paramML_FS']  = ''
                data['estado']      = 'pendiente'

                cantidad +=experimentos
                bd.insertarExperimentos(data, experimentos, instancia[0])

if fs:
    # poblar ejecuciones FS
    # instancias = bd.obtenerInstancias(f'''
    #                                   "sonar","ionosphere","Immunotherapy","Divorce","wdbc","breast-cancer-wisconsin"
    #                                   ''')
    instancias = bd.obtenerInstancias(f'''
                                      "CTG"
                                      ''')
    iteraciones = 100
    experimentos = 1
    poblacion = 50
    # clasificadores = ["KNN","RandomForest","Xgboost"]
    clasificadores = ["Gradient Boosting"]
    # DS_actions = [
    #     'S4-STD', 'S4-COM', 'S4-ELIT',
    #     'V4-STD', 'V4-COM', 'V4-ELIT',
    #     'X4-STD', 'X4-COM', 'X4-ELIT',
    #     'Z4-STD', 'Z4-COM', 'Z4-ELIT']
    DS_actions = ['S4-STD']
    # clasificadores = ["KNN"]
    for instancia in instancias:

        for mh in mhs:
            for clasificador in clasificadores:
                if ml:
                    data = {}
                    data['experimento'] = f'{mh} Q-Learning'
                    data['MH']          = mh
                    data['paramMH']     = f'iter:{str(iteraciones)},pop:{str(poblacion)}'
                    data['ML']          = 'Q-Learning'
                    data['paramML']     = paramsML
                    data['ML_FS']       = clasificador
                    data['paramML_FS']  = f'k:5'
                    data['estado']      = 'pendiente'

                    cantidad +=experimentos
                    bd.insertarExperimentos(data, experimentos, instancia[0])
                else:
                    for ds in DS_actions:
                        data = {}
                        data['experimento'] = f'{mh} {ds} {clasificador}'
                        data['MH']          = mh
                        data['paramMH']     = f'iter:{str(iteraciones)},pop:{str(poblacion)},DS:{ds},cros:0.9;mut:0.20'
                        # data['paramMH']     = f'iter:{str(iteraciones)},pop:{str(poblacion)},DS:S4-COM'
                        data['ML']          = ''
                        data['paramML']     = ''
                        data['ML_FS']       = clasificador
                        data['paramML_FS']  = f'k:5'
                        data['estado']      = 'pendiente'

                        cantidad +=experimentos
                        bd.insertarExperimentos(data, experimentos, instancia[0])

if scp:
    # poblar ejecuciones SCP
    instancias = bd.obtenerInstancias(f'''
                                      "scpd1","scpc1","scpb1","scpa1"
                                      ''')
    iteraciones = 500
    experimentos = 31
    poblacion = 20
    for instancia in instancias:

        for mh in mhs:
            binarizaciones = ['S2-STD','S2-STD_LOG','S2-STD_PIECE','S2-STD_SINE','S2-STD_SINGER','S2-STD_SINU','S2-STD_TENT','S2-STD_CIRCLE',
                              'S2-COM','S2-COM_LOG','S2-COM_PIECE','S2-COM_SINE','S2-COM_SINGER','S2-COM_SINU','S2-COM_TENT','S2-COM_CIRCLE',
                              'S2-ELIT','S2-ELIT_LOG','S2-ELIT_PIECE','S2-ELIT_SINE','S2-ELIT_SINGER','S2-ELIT_SINU','S2-ELIT_TENT','S2-ELIT_CIRCLE']
            for binarizacion in binarizaciones:
                
                data = {}
                data['experimento'] = f'{mh} {binarizacion}'
                data['MH']          = mh
                data['paramMH']     = f'iter:{str(iteraciones)},pop:{str(poblacion)},DS:{binarizacion},repair:complex,cros:0.9;mut:0.20'
                data['ML']          = ''
                data['paramML']     = ''
                data['ML_FS']       = ''
                data['paramML_FS']  = ''
                data['estado']      = 'pendiente'

                cantidad +=experimentos
                bd.insertarExperimentos(data, experimentos, instancia[0])
            
if kp:
    # poblar ejecuciones SCP
    instancias = bd.obtenerInstancias(f'''
                                      "knapPI_1_100_1000_1","knapPI_2_100_1000_1","knapPI_3_100_1000_1","knapPI_1_200_1000_1","knapPI_2_200_1000_1","knapPI_3_200_1000_1","knapPI_1_500_1000_1","knapPI_2_500_1000_1","knapPI_3_500_1000_1","knapPI_1_1000_1000_1","knapPI_2_1000_1000_1","knapPI_3_1000_1000_1","knapPI_1_2000_1000_1","knapPI_2_2000_1000_1","knapPI_3_2000_1000_1"
                                      ''')
    iteraciones = 500
    experimentos = 28
    poblacion = 20
    for instancia in instancias:

        for mh in mhs:
            binarizaciones = ['S2-STD','S2-STD_LOG','S2-STD_PIECE','S2-STD_SINE','S2-STD_SINGER','S2-STD_SINU','S2-STD_TENT','S2-STD_CIRCLE',
                              'S2-COM','S2-COM_LOG','S2-COM_PIECE','S2-COM_SINE','S2-COM_SINGER','S2-COM_SINU','S2-COM_TENT','S2-COM_CIRCLE',
                              'S2-ELIT','S2-ELIT_LOG','S2-ELIT_PIECE','S2-ELIT_SINE','S2-ELIT_SINGER','S2-ELIT_SINU','S2-ELIT_TENT','S2-ELIT_CIRCLE']
            for binarizacion in binarizaciones:
                
                data = {}
                data['experimento'] = f'{mh} {binarizacion}'
                data['MH']          = mh
                data['paramMH']     = f'iter:{str(iteraciones)},pop:{str(poblacion)},DS:{binarizacion},cros:0.9;mut:0.20'
                data['ML']          = ''
                data['paramML']     = ''
                data['ML_FS']       = ''
                data['paramML_FS']  = ''
                data['estado']      = 'pendiente'

                cantidad +=experimentos
                bd.insertarExperimentos(data, experimentos, instancia[0])

if mkp:
    # poblar ejecuciones MKP
    instancias = bd.obtenerInstancias(f'''
                                      "mknap1_2","mknap2_2"
                                      ''')
    iteraciones = 500
    experimentos = 1
    poblacion = 10
    for instancia in instancias:

        for mh in mhs:
            binarizacion = 'V4-STD'
            data = {}
            data['experimento'] = f'{mh} {binarizacion}'
            data['MH']          = mh
            data['paramMH']     = f'iter:{str(iteraciones)},pop:{str(poblacion)},DS:{binarizacion}'
            data['ML']          = ''
            data['paramML']     = ''
            data['ML_FS']       = ''
            data['paramML_FS']  = ''
            data['estado']      = 'pendiente'

            cantidad +=experimentos
            bd.insertarExperimentos(data, experimentos, instancia[0])
            
if ben:
    # poblar ejecuciones Benchmark
    instancias = bd.obtenerInstancias(f'''
                                      "F7","F8","F9","F10"
                                      ''')
    iteraciones = 500
    experimentos = 31
    poblacion = 30
    for instancia in instancias:
        for mh in mhs:
            data = {}
            data['experimento'] = f'{mh} {instancia[1]}'
            data['MH']          = mh
            data['paramMH']     = f'iter:{str(iteraciones)},pop:{str(poblacion)}'
            data['ML']          = ''
            data['paramML']     = ''
            data['ML_FS']       = ''
            data['paramML_FS']  = ''
            data['estado']      = 'pendiente'

            cantidad +=experimentos
            bd.insertarExperimentos(data, experimentos, instancia[0])

print("------------------------------------------------------------------")
print(f'Se ingresaron {cantidad} experimentos a la base de datos')
print("------------------------------------------------------------------")

