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
mhs = ['PSO','GWO']
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



if scp:
    # poblar ejecuciones SCP
    instancias = bd.obtenerInstancias(f'''
                                      "scpcyc06","scpcyc07","scpclr10","scpclr11","scp41","scp61","scpb1","scpnrf1"
                                      ''')
    iteraciones = 500
    experimentos = 5
    poblacion = 20
    for instancia in instancias:

        for mh in mhs:
            binarizaciones = ['V3-STD','V3-STD_LOG','V3-STD_PIECE','V3-STD_SINE','V3-STD_SINGER','V3-STD_SINU','V3-STD_TENT','V3-STD_CIRCLE',
                              'V3-ELIT','V3-ELIT_LOG','V3-ELIT_PIECE','V3-ELIT_SINE','V3-ELIT_SINGER','V3-ELIT_SINU','V3-ELIT_TENT','V3-ELIT_CIRCLE']
            # binarizaciones = ['V3-ELIT']
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

