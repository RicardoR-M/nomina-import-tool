post_db = 'CLARO_IN_CALIDAD'
post_db_table = 'NOMINA_POST'
post_maxColNumber = 75
post_xl_colNameRow = 4
post_xl_firstDataRow = post_xl_colNameRow + 1
post_xl_colCheckFlag = 'A'  # verifica si existe data en esa columna, si no encuentra finaliza el loop de registro de evas
post_xl_hoja = 'NÓMINA POSTPAGO'  # Nombre de la hoja donde se encuentra la data
post_xl_firstDataCol = 'A'  # Columna donde empieza la data

post = [
    {'colName': 'DNI', 'sqlName': 'DNI', 'tipo': 'dni', 'estado': 'fijo'},
    {'colName': 'USUARIO', 'sqlName': 'CODIGO_E', 'tipo': 'trim_str', 'estado': 'fijo'},
    {'colName': 'TIPO DE GESTIÓN', 'sqlName': 'TIPO_GESTION', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'AGENTE', 'sqlName': 'AGENTE', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'PERFIL 1', 'sqlName': 'CARGO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'FECHA DE INGRESO', 'sqlName': 'FECHA_INGRESO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'ESTADO', 'sqlName': 'ESTADO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'SUB ESTADO ', 'sqlName': 'SUBESTADO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'CONDICION ', 'sqlName': 'CONDICIÓN', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'TURNO ', 'sqlName': 'TURNO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'SUPERVISOR NOV', 'sqlName': 'SUPERVISOR', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'RUS', 'sqlName': 'RUS', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'SEDE', 'sqlName': 'SEDE', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'FECHA BAJA', 'sqlName': 'FECHA_BAJA', 'tipo': 'default', 'estado': 'fijo'},
]
