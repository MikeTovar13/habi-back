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
    id_propietario integer,
    fecha_creacion datetime,
    fecha_modificacion datetime,
    FOREIGN KEY (id_localidad) REFERENCES localidad(id)
    FOREIGN KEY (id_propietario) REFERENCES propietario(id)
);

--Ciudades
INSERT INTO ciudad (nombre, fecha_creacion, fecha_modificacion) VALUES ("Bogota", date("now"), date("now"));
INSERT INTO ciudad (nombre, fecha_creacion, fecha_modificacion) VALUES ("Medellin", date("now"), date("now"));

--Localidades Bogota
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Chapinero", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Tunjuelito", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Teusaquillo", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Sumapaz", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Suba", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Santa Fe", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("San Cristobal", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Rafael Uribe Uribe", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Puente Aranda", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Los Martires", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("La Candelario", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Kennedy", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Fontibon", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Engativa", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Ciudad Bolivar", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Bosa", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Barrios Unidos", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Antonio Nariño", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Usme", 1, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Usaquen", 1, date("now"), date("now"));

-- Localidades Medellin
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Castilla", 2, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Belen", 2, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Guayabal", 2, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Poblado", 2, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("San Javier", 2, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("La America", 2, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Laureles-Estadio", 2, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("La Candelaria", 2, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Buenos Aires", 2, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Villa Hermosa", 2, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Doce de Octubre", 2, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Aranjuez", 2, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Manrique", 2, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Santa Cruz", 2, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Robledo", 2, date("now"), date("now"));
INSERT INTO localidad (nombre, id_ciudad, fecha_creacion, fecha_modificacion) VALUES ("Popular", 2, date("now"), date("now"));

-- Trigger para borrar inmuebles cuando se borra el propietario
CREATE TRIGGER delete_propietario_cascada
BEFORE DELETE ON propietario
BEGIN
    DELETE FROM inmueble WHERE id_propietario = old.id;
END;