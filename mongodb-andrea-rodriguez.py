"""
Proyecto: Bases de datos NoSQL en MongoDB

Descripción:
Este archivo contiene la documentación completa del caso seleccionado, 
la estructura de la base de datos, las consultas realizadas en MongoDB, 
sus explicaciones y los resultados obtenidos. 
"""

# ============================================================
# 1. CASO SELECCIONADO
# ============================================================

"""
Para la actividad se trabajaron dos bases de datos:

1. BASE DE DATOS 1 – Tienda Local (creada manualmente en MongoDB)
   Colecciones:
   - productos
   - clientes
   - ventas

2. BASE DE DATOS 2 – Dataset Netflix (aprox. 8.807 documentos)
   Importado desde archivo CSV usando MongoDB Compass.

Ambos casos fueron utilizados para estudiar el funcionamiento de bases de datos NoSQL 
de tipo documental utilizando MongoDB.
"""


# ============================================================
# 2. ESTRUCTURA DE LA BASE DE DATOS – TIENDA LOCAL
# ============================================================

"""
A continuación se muestran ejemplos reales de los documentos insertados 
en cada colección. Estos datos fueron posteriormente usados en consultas 
y operaciones CRUD.
"""

# COLECCIÓN: PRODUCTOS
productos = [
    {
        "nombre": "Camiseta básica",
        "categoria": "Ropa",
        "precio": 35000,
        "stock": 42,
        "tallas": ["S", "M", "L"],
        "colores": ["Negro", "Blanco"],
        "descripcion": "Camiseta de algodón unisex",
        "fecha_registro": "2025-11-20"
    },
    {
        "nombre": "Gorra deportiva",
        "categoria": "Accesorios",
        "precio": 20000,
        "stock": 15,
        "colores": ["Azul", "Negro"],
        "descripcion": "Gorra ajustable para uso diario",
        "fecha_registro": "2025-11-20"
    }
]

# COLECCIÓN: CLIENTES
clientes = [
    {
        "nombre": "Andrea López",
        "telefono": "3145678901",
        "email": "andrea.lopez@example.com"
    },
    {
        "nombre": "Carlos Ramírez",
        "telefono": "3178852312",
        "email": "carlos.ramirez@example.com"
    }
]

# COLECCIÓN: VENTAS
ventas = [
    {
        "producto_id": "691bef8a39b59879b174afff",
        "cantidad": 1,
        "total": 35000,
        "fecha": "2025-11-21"
    },
    {
        "producto_id": "691bf02639b59879b174b003",
        "cantidad": 2,
        "total": 40000,
        "fecha": "2025-11-22"
    }
]


# ============================================================
# 3. IMPLEMENTACIÓN DEL DATASET NETFLIX
# ============================================================

codigo_creacion = """
use universidad;
db.createCollection("dataset-net");
"""

"""
Explicación:
- Se crea la base de datos 'universidad'.
- Se crea la colección 'dataset-net', donde se almacenarán los datos del catálogo de Netflix.
"""


# ============================================================
# 4. INSERCIÓN DE DATOS (CON EXPLICACIÓN)
# ============================================================

codigo_insert = """
db["dataset-net"].insertOne({
  show_id: "t10001",
  type: "Movie",
  title: "Ejemplo Película",
  director: "Andrea R.",
  country: "Colombia",
  date_added: "November 18, 2025",
  release_year: 2025,
  rating: "PG",
  duration: "120 min",
  listed_in: "Drama",
  description: "Película de ejemplo para la tarea."
});
"""

"""
Explicación:
- Se inserta un documento tipo 'Movie'.
- Se incluyen campos clave como país, rating, año, género y duración.
- MongoDB genera automáticamente el campo _id.
"""


# Inserción múltiple
codigo_insert_many = """
db["dataset-net"].insertMany([
  {
    show_id: "t10002",
    type: "TV Show",
    title: "Serie Ejemplo 1",
    country: "Mexico",
    release_year: 2024,
    duration: "1 Season"
  },
  {
    show_id: "t10003",
    type: "Movie",
    title: "Película Ejemplo 2",
    country: "Argentina",
    release_year: 2023,
    duration: "95 min"
  }
]);
"""

"""
Resultado:
{
  acknowledged: true,
  insertedIds: {
      '0': ObjectId(...),
      '1': ObjectId(...)
  }
}
"""


# ============================================================
# 5. CONSULTAS CRUD – EXPLICACIÓN + RESULTADOS
# ============================================================

# -------------------- READ (SELECT) --------------------------

codigo_find5 = """
db["dataset-net"].find().limit(5);
"""

resultado_find5 = """
Devuelve los primeros 5 documentos del catálogo de Netflix.
Estos incluyen campos como título, tipo, país, año y duración.
"""

codigo_buscar_titulo = """
db["dataset-net"].find({ title: "Dick Johnson Is Dead" });
"""

resultado_buscar_titulo = """
{
  "title": "Dick Johnson Is Dead",
  "type": "Movie",
  "release_year": 2020,
  "country": "United States",
  "listed_in": "Documentaries"
}
Explicación:
- La consulta busca un título exacto.
- La coincidencia pertenece al género documental y fue lanzada en 2020.
"""


# -------------------- UPDATE --------------------------

codigo_update1 = """
db["dataset-net"].updateOne(
  { show_id: "s1" },
  { $set: { rating: "PG-13 (Updated)" } }
);
"""

resultado_update1 = """
matchedCount: 1
modifiedCount: 1
Explicación:
- La consulta modifica el rating del documento con show_id = 's1'.
- matchedCount indica cuántos documentos coinciden con el filtro.
"""


codigo_update_many = """
db["dataset-net"].updateMany(
  { country: "United States" },
  { $set: { region: "North America" } }
);
"""

resultado_update_many = """
matchedCount: 2000+ (aprox.)
modifiedCount: mismo número
Explicación:
- Se actualizan todos los títulos producidos en EE.UU.
- Se agrega el campo 'region' con valor 'North America'.
"""


# -------------------- DELETE --------------------------

codigo_delete = """
db["dataset-net"].deleteOne({ show_id: "t10003" });
"""

resultado_delete = """
deletedCount: 1
Explicación:
- Se elimina el documento insertado manualmente para fines de prueba.
"""


# ============================================================
# 6. CONSULTAS CON FILTROS Y OPERADORES – EXPLICACIÓN + RESULTADOS
# ============================================================

codigo_filtros = """
db["dataset-net"].find({ type: "Movie" });
"""

resultado_filtros = """
Resultado:
- Total de películas encontradas: 6131
Explicación:
- Filtra únicamente los documentos donde type = 'Movie'.
"""


codigo_filtro_regex = """
db["dataset-net"].find({ title: { $regex: "Love", $options: "i" } });
"""

resultado_filtro_regex = """
Ejemplos de coincidencias:
- Love Alarm
- The Lovebirds
- Love & Anarchy
Explicación:
- $regex permite búsquedas parciales.
- $options 'i' ignora mayúsculas/minúsculas.
"""


codigo_filtro_anio = """
db["dataset-net"].find({ release_year: { $gt: 2018 }, type: "Movie" });
"""

resultado_filtro_anio = """
Ejemplos:
- The Irishman (2019)
- Marriage Story (2019)
- Enola Holmes (2020)
Explicación:
- Se filtran películas con fecha posterior al 2018.
"""


# ============================================================
# 7. CONSULTAS DE AGREGACIÓN – EXPLICACIÓN Y RESULTADOS
# ============================================================

codigo_agregacion_tipos = """
db["dataset-net"].aggregate([
  { $group: { _id: "$type", total: { $sum: 1 } } }
]);
"""

resultado_agregacion_tipos = """
{
  Movie: 6131,
  TV Show: 2676
}
Explicación:
- $group permite agrupar por categorías.
- $sum contabiliza cuántos elementos corresponden a cada tipo.
"""


codigo_agregacion_paises = """
db["dataset-net"].aggregate([
  { $group: { _id: "$country", cantidad: { $sum: 1 } } },
  { $sort: { cantidad: -1 } }
]);
"""

resultado_agregacion_paises = """
Primeros 3 países con más producciones:
1. United States – ~2600 títulos
2. India – ~1000 títulos
3. United Kingdom – ~450 títulos
"""


codigo_promedio_anio = """
db["dataset-net"].aggregate([
  { $group: { _id: null, promedio_anio: { $avg: "$release_year" } } }
]);
"""

resultado_promedio_anio = """
promedio_anio: 2014.7
Explicación:
- Promedia el campo release_year de todos los documentos.
"""


codigo_facet = """
[
  {
    "$facet": {
      "totalTitulos": [
        { "$count": "total" }
      ],
      "topPaises": [
        { "$group": { "_id": "$country", "total": { "$sum": 1 } } },
        { "$sort": { "total": -1 } },
        { "$limit": 5 }
      ],
      "tipoContenido": [
        { "$group": { "_id": "$type", "cantidad": { "$sum": 1 } } },
        { "$sort": { "cantidad": -1 } }
      ],
      "lanzamientosPorAno": [
        { "$group": { "_id": "$release_year", "total": { "$sum": 1 } } },
        { "$sort": { "_id": 1 } }
      ]
    }
  }
]
"""

resultado_facet = """
Resultados:
- Total de títulos: 8807
- Películas: 6131
- Series: 2676
- Países principales: USA, India, UK
- Tendencia por años: crecimiento notable entre 2013–2020

Explicación:
- $facet ejecuta múltiples pipelines en paralelo.
- Permite obtener diferentes análisis en una sola consulta.
"""


# ============================================================
# GRACIAS
# ============================================================
