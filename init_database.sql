CREATE TABLE propietario (
    id integer PRIMARY KEY AUTOINCREMENT,
    nombre text,
    telefono text,
    correo text,
    fecha_creacion datetime,
    fecha_modificacion datetime
);

CREATE TABLE ciudad (
    id integer PRIMARY KEY AUTOINCREMENT,
    nombre text,
    fecha_creacion datetime,
    fecha_modificacion datetime
);

CREATE TABLE localidad (
    id integer PRIMARY KEY AUTOINCREMENT,
    nombre text,
    id_ciudad integer,
    fecha_creacion datetime,
    fecha_modificacion datetime,
    FOREIGN KEY (id_ciudad) REFERENCES ciudad(id)
);

CREATE TABLE inmueble (
    id integer PRIMARY KEY AUTOINCREMENT,
    area real,
    habitaciones integer,
    precio integer,
    direccion text,
    id_localidad integer,
    fecha_creacion datetime,
    fecha_modificacion datetime,
    FOREIGN KEY (id_localidad) REFERENCES localidad(id)
);

CREATE TABLE propietario_inmueble (
    id integer PRIMARY KEY AUTOINCREMENT,
    id_propietario integer,
    id_inmueble integer,
    FOREIGN KEY (id_propietario) REFERENCES propietario(id),
    FOREIGN KEY (id_inmueble) REFERENCES inmueble(id)
);