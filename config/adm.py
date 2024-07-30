adm_db = 'CLARO_IN_HFC'
adm_db_table = 'NOMINA_ADM'
adm_maxColNumber = 75
adm_xl_colNameRow = 2
adm_xl_firstDataRow = adm_xl_colNameRow + 1
adm_xl_colCheckFlag = 'A'  # verifica si existe data en esa columna, si no encuentra finaliza el loop de registro de evas
adm_xl_hoja = 'NOMINA'  # Nombre de la hoja donde se encuentra la data
adm_xl_firstDataCol = 'A'  # Columna donde empieza la data

adm = [
    {'colName': 'DNI', 'sqlName': 'DNI', 'tipo': 'dni', 'estado': 'fijo'},
    {'colName': 'USUARIO', 'sqlName': 'CODIGO_E', 'tipo': 'trim_str', 'estado': 'fijo'},
    {'colName': 'TIPO DE GESTION', 'sqlName': 'TIPO_GESTION', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'APELLIDOS Y NOMBRES', 'sqlName': 'AGENTE', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'CARGO', 'sqlName': 'CARGO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'FECHA INCORP.', 'sqlName': 'FECHA_INGRESO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'ESTADO', 'sqlName': 'ESTADO', 'tipo': 'default', 'estado': 'var'},
    {'colName': 'SUB ESTADO', 'sqlName': 'SUBESTADO', 'tipo': 'default', 'estado': 'var'},
    {'colName': 'CONDICIÓN', 'sqlName': 'CONDICIÓN', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'TURNO', 'sqlName': 'TURNO', 'tipo': 'default', 'estado': 'var'},
    {'colName': 'SUPERVISOR', 'sqlName': 'SUPERVISOR', 'tipo': 'default', 'estado': 'var'},
    {'colName': 'FECHA DE CESE', 'sqlName': 'FECHA_BAJA', 'tipo': 'default', 'estado': 'fijo'},
]
