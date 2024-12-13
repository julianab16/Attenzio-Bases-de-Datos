-- #######################################################
-- file:schema.sql
-- Attenzio - DB Project
-- #######################################################

\c attenzio

-- Rol table
CREATE TABLE Rol( 
rol_id INTEGER PRIMARY KEY NOT NULL, 
nombre VARCHAR(50) NOT NULL
);

-- Usuario table
CREATE TABLE Usuario( 
id INTEGER PRIMARY KEY NOT NULL,
rol_id INTEGER NOT NULL, 
nombre VARCHAR(50) NOT NULL,
correo VARCHAR(50) NOT NULL,
contraseña VARCHAR(50) NOT NULL,
numeroCelular VARCHAR(50),
direccion VARCHAR(50),
foto BYTEA,
FOREIGN KEY (rol_id) REFERENCES Rol (rol_id) 
);

-- Curso table
CREATE TABLE Curso( 
curso_id INTEGER PRIMARY KEY NOT NULL, 
nombre VARCHAR(50) NOT NULL,
codigo VARCHAR(50) NOT NULL,
descripcion VARCHAR(100) NOT NULL
);

-- Clase table
CREATE TABLE Clase( 
clase_id INTEGER PRIMARY KEY NOT NULL, 
curso_id INTEGER NOT NULL, 
nombre VARCHAR(50) NOT NULL, 
fecha DATE NOT NULL,
hora TIME NOT NULL,
FOREIGN KEY (curso_id) REFERENCES Curso (curso_id) 
);

-- EstudianteClase table
CREATE TABLE EstudianteClase( 
id INTEGER NOT NULL, 
clase_id INTEGER NOT NULL,
latitud  VARCHAR(50) NOT NULL,
longitud  VARCHAR(50) NOT NULL,
fecha DATE NOT NULL,
hora TIME NOT NULL,
PRIMARY KEY (id, clase_id),
FOREIGN KEY (clase_id) REFERENCES Clase (clase_id),
FOREIGN KEY (id) REFERENCES Usuario (id) 
);

-- Pregunta table
CREATE TABLE Pregunta ( 
QR INTEGER PRIMARY KEY NOT NULL, 
clase_id INTEGER NOT NULL,
enunciado VARCHAR(100) NOT NULL,
FOREIGN KEY (clase_id) REFERENCES Clase (clase_id)
);

-- Opcion table
CREATE TABLE Opcion ( 
OQR INTEGER PRIMARY KEY NOT NULL, 
QR INTEGER NOT NULL,
contenido VARCHAR(100) NOT NULL,
FOREIGN KEY (QR) REFERENCES Pregunta (QR)
);

-- OpcionEstudiante table
CREATE TABLE OpcionEstudiante ( 
OQR INTEGER NOT NULL,
id INTEGER NOT NULL,
puntaje DECIMAL(5,2) NOT NULL,
latitud  VARCHAR(50) NOT NULL,
longitud VARCHAR(50) NOT NULL,
PRIMARY KEY (OQR, id),
FOREIGN KEY (id) REFERENCES Usuario (id) 
);

