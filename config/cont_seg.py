segcont_db = 'CLARO_SEGUIMIENTO_CONTROL'
segcont_db_table = 'nomina_segcont'
segcont_maxColNumber = 70
segcont_xl_colNameRow = 3
segcont_xl_firstDataRow = segcont_xl_colNameRow + 1
segcont_xl_colCheckFlag = 'A'  # verifica si existe data en esa columna, si no encuentra finaliza el loop de registro de evas
segcont_xl_hoja = 'NOMINA'  # Nombre de la hoja donde se encuentra la data
segcont_xl_firstDataCol = 'A'  # Columna donde empieza la data

segcont = [
    {'colName': 'DNI', 'sqlName': 'DNI', 'tipo': 'str', 'estado': 'fijo'},
    {'colName': 'CODIGO E', 'sqlName': 'CODIGO_E', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'TIPO DE GESTION', 'sqlName': 'TIPO_GESTION', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'APELLIDOS NOMBRES', 'sqlName': 'AGENTE', 'tipo': 'trim_str', 'estado': 'fijo'},
    {'colName': 'FECHA ING EMPRESA', 'sqlName': 'FECHA_INGRESO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'CARGO', 'sqlName': 'CARGO', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'CONDICIÓN', 'sqlName': 'CONDICION', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'ESTADO', 'sqlName': 'ESTADO', 'tipo': 'default', 'estado': 'var'},
    {'colName': 'SUB ESTADO', 'sqlName': 'SUBESTADO', 'tipo': 'default', 'estado': 'var'},
    {'colName': 'ESPECIALIDAD', 'sqlName': 'TIPO_ATENCION', 'tipo': 'default', 'estado': 'fijo'},
    {'colName': 'TURNO', 'sqlName': 'TURNO', 'tipo': 'default', 'estado': 'var'},
    {'colName': 'SUPERVISOR', 'sqlName': 'SUPERVISOR', 'tipo': 'trim_str', 'estado': 'var'},
    {'colName': 'OBSERVACIONES', 'sqlName': 'OBSERVACION', 'tipo': 'default', 'estado': 'fijo'},
]
