mval_db = 'CLARO_MESA_VALIDACIONES'
mval_db_table = 'nomina_mesaval'
mval_maxColNumber = 60
mval_xl_colNameRow = 3
mval_xl_firstDataRow = mval_xl_colNameRow + 1
mval_xl_colCheckFlag = 'A'  # verifica si existe data en esa columna, si no encuentra finaliza el loop de registro de evas
mval_xl_hoja = 'NOMINA'  # Nombre de la hoja donde se encuentra la data
mval_xl_firstDataCol = 'A'  # Columna donde empieza la data

mval = [
    {'colName': 'DNI', 'sqlName': 'DNI', 'tipo': 'str', 'estado': 'fijo'},
    {'colName': 'CODIGO E', 'sqlName': 'CODIGO_E', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'TIPO DE GESTION', 'sqlName': 'TIPO_GESTION', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'APELLIDOS NOMBRES', 'sqlName': 'AGENTE', 'tipo': 'trim_str', 'estado': 'fijo'},
    {'colName': 'FECHA DE INGRESO', 'sqlName': 'FECHA_INGRESO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'CARGO', 'sqlName': 'CARGO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'CONDICIÓN', 'sqlName': 'CONDICION', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'ESTADO', 'sqlName': 'ESTADO', 'tipo': 'default', 'estado': 'var'},
    {'colName': 'SUB ESTADO', 'sqlName': 'SUBESTADO', 'tipo': 'default', 'estado': 'var'},
    {'colName': 'DETALLE DE SERVICIO', 'sqlName': 'TIPO_ATENCION', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'TURNO', 'sqlName': 'TURNO', 'tipo': 'default', 'estado': 'var'},
    {'colName': 'SUPERVISOR', 'sqlName': 'SUPERVISOR', 'tipo': 'trim_str', 'estado': 'var'},
    {'colName': 'OBSERVACION', 'sqlName': 'OBSERVACION', 'tipo': 'default', 'estado': 'fijo'},
]
