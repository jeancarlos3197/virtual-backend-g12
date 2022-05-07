import { libroRequestDTO } from "../dtos/libro.request.dto.js";
import { Usuario } from "../models/usuarios.models.js";

export const agregarLibro = async (req, res) => {
  try {
    const data = req.body;
    const usuarioActual = req.user;

    usuarioActual.libros.push(data);
    // https://mongoosejs.com/docs/documents.html#updating-using-save
    await usuarioActual.save();

    return res.json({
      message: "ok",
      content: usuarioActual.libros,
    });
  } catch (error) {
    return res.status(400).json({
      message: "Error al crear el libro",
      content: error.message,
    });
  }
};

export const listarLibros = async (req, res) => {
  const usuarioActual = req.user;
  const libros = usuarioActual.libros;
  return res.json({
    message: "ok",
    content: libros,
  });
};

export const devolverLibro = async (req, res) => {
  const { _id } = req.params;
  //https://www.mongodb.com/docs/manual/reference/operator/projection/positional/#proj._S_
  // usando las propiedades de la base de datos
  const libroEncontrado = await Usuario.find(
    {
      _id: req.user._id, //id del usuario
      "libros._id": _id, //id del libro
    },
    {
      "libros.$": 1, // solo el libro que se quiere devolver
    }
  );
  //forma tradicional
  const libro = req.user.libros.filter((libro) => libro._id == _id);

  return res.json({
    message: "ok",
    content: libro,
    content2: libroEncontrado,
  });
};
