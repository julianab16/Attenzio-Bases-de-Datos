-- #######################################################
-- file:data.sql
-- Attenzio - DB Project
-- #######################################################

\c attenzio

-- Insert record into the Rol table
INSERT INTO Rol (rol_id, nombre) VALUES 
(1, 'Administrador'),
(2, 'Profesor'),
(3, 'Estudiante');

-- Insert record into the Usuario table
INSERT INTO Usuario (id, rol_id, nombre, correo, contraseña, numero, direccion, foto) VALUES
(1, 1, 'Admin User', 'admin@example.com', 'admin123', '1234567890', 'Calle Principal 123', NULL),
(2, 2, 'Profesor Uno', 'profesor1@example.com', 'prof123', '0987654321', 'Calle Secundaria 456', NULL),
(3, 3, 'Estudiante Uno', 'estudiante1@example.com', 'estu123', '5555555555', 'Calle Universitaria 789', NULL);

-- Insert record into the Curso table
INSERT INTO Curso (curso_id, nombre, codigo, descripcion) VALUES
(1, 'Matemáticas', 'MATH101', 'Curso introductorio de matemáticas'),
(2, 'Física', 'PHYS101', 'Curso introductorio de física');

-- Insert record into the Clase table
INSERT INTO Clase (clase_id, curso_id, nombre, fecha, hora) VALUES 
(1, 1, 'Álgebra Lineal', '2024-11-12', '08:00:00'),
(2, 2, 'Mecánica Clásica', '2024-11-13', '10:00:00');

-- Insert record into the EstudianteClase table
INSERT INTO EstudianteClase (id, clase_id, latitud, longitud, fecha, hora) VALUES
(3, 1, '20.659698', '-103.349609', '2024-11-22', '09:05:00'),
(3, 2, '20.659698', '-103.349609', '2024-11-22', '11:05:00');

-- Insert record into the Pregunta table
INSERT INTO Pregunta (QR, clase_id, enunciado) VALUES 
(1, 1, '¿Cuál es la solución del sistema de ecuaciones?'),
(2, 2, '¿Cuál es la segunda ley de Newton?');

-- Insert record into the Opcion table
INSERT INTO Opcion (OQR, QR, contenido) VALUES 
(1, 1, 'x=2, y=3'),
(2, 1, 'x=1, y=1'),
(3, 2, 'F=m*a'),
(4, 2, 'F=m/a');

-- Insert record into the OpcionEstudiante table
INSERT INTO OpcionEstudiante (OQR, id, puntaje, latitud, longitud) VALUES
(1, 3, 10.00, '20.659698', '-103.349609'),
(3, 3, 10.00, '20.659698', '-103.349609');
