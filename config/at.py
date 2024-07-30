at_db = 'CLARO_IN_CALIDAD_AT'
at_db_table = 'NOMINA_AT'
at_maxColNumber = 50
at_xl_colNameRow = 4
at_xl_firstDataRow = at_xl_colNameRow + 1
at_xl_firstDataCol = 'B'  # Columna donde empieza la data
at_xl_colCheckFlag = 'B'  # verifica si existe data en esa columna, si no encuentra finaliza el loop de registro de evas
at_xl_hoja = 'ACTIVOS'  # Nombre de la hoja donde se encuentra la data

at = [
    {'colName': 'DNI', 'sqlName': 'DNI', 'tipo': 'dni', 'estado': 'fijo'},
    {'colName': 'USUARIO', 'sqlName': 'CODIGO_E', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'TIPO DE GESTIÓN', 'sqlName': 'TIPO_GESTION', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'AGENTES ', 'sqlName': 'AGENTE', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'CARGO', 'sqlName': 'CARGO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': '''FECHA DE 
INGESO''', 'sqlName': 'FECHA_INGRESO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'ESTADO', 'sqlName': 'ESTADO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'SUB ESTADO', 'sqlName': 'SUBESTADO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'TURNO', 'sqlName': 'TURNO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'CONDICION', 'sqlName': 'CONDICIÓN', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'SUPERVISOR', 'sqlName': 'SUPERVISOR', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'INICIO', 'sqlName': 'SUBESTADO_INICIO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'FIN', 'sqlName': 'SUBESTADO_FIN', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'FECHA DE BAJA', 'sqlName': 'FECHA_BAJA', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'SITE', 'sqlName': 'SEDE', 'tipo': 'default', 'estado': 'fijo'},
]
