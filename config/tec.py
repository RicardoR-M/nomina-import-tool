tec_db = 'CLARO_IN_HFC'
tec_db_table = 'NOMINA_TEC'
tec_maxColNumber = 80
tec_xl_colNameRow = 3
tec_xl_firstDataRow = tec_xl_colNameRow + 1
tec_xl_colCheckFlag = 'A'  # verifica si existe data en esa columna, si no encuentra finaliza el loop de registro de evas
tec_xl_hoja = 'NOMINA'  # Nombre de la hoja donde se encuentra la data
tec_xl_firstDataCol = 'A'  # Columna donde empieza la data

tec = [
    {'colName': 'DNI', 'sqlName': 'DNI', 'tipo': 'dni', 'estado': 'fijo'},
    {'colName': 'CODIGO E', 'sqlName': 'CODIGO_E', 'tipo': 'trim_str', 'estado': 'fijo'},
    {'colName': 'TIPO DE GESTION', 'sqlName': 'TIPO_GESTION', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'APELLIDOS NOMBRES', 'sqlName': 'AGENTE', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'CARGO', 'sqlName': 'CARGO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'FECHA INGRESO', 'sqlName': 'FECHA_INGRESO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'ESTADO', 'sqlName': 'ESTADO', 'tipo': 'default', 'estado': 'var'},
    {'colName': 'SUB ESTADO', 'sqlName': 'SUBESTADO', 'tipo': 'default', 'estado': 'var'},
    {'colName': 'CONDICIÓN', 'sqlName': 'CONDICIÓN', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'TURNO', 'sqlName': 'TURNO', 'tipo': 'default', 'estado': 'var'},
    {'colName': 'SUPERVISOR', 'sqlName': 'SUPERVISOR', 'tipo': 'default', 'estado': 'var'},
    {'colName': 'FECHA DE CESE', 'sqlName': 'FECHA_BAJA', 'tipo': 'default', 'estado': 'fijo'},
]
