import bcryptjs from "bcryptjs";
import jwt from "jsonwebtoken";

import { Usuario } from "../models/usuarios.models.js";

export const registrarUsuario = async (req, res) => {
  // creare mi DTO de registro
  const data = req.body;
  try {
    const nuevoUsuario = await Usuario.create(data);

    console.log(Object.keys(nuevoUsuario));

    delete nuevoUsuario["_doc"]["password"];

    return res.status(201).json({
      message: "Usuario creado correctamente",
      content: nuevoUsuario,
    });
  } catch (error) {
    return res.status(400).json({
      message: "Error al crear el usuario",
      content: error.message,
    });
  }
};

export const login = async (req, res) => {
  const data = req.body;

  const usuarioEncontrado = await Usuario.findOne({ correo: data.correo });
  if (!usuarioEncontrado) {
    return res.status(400).json({
      message: "Credenciales incorrectas",
    });
  }

  if (bcryptjs.compareSync(data.password, usuarioEncontrado.password)) {
    const token = jwt.sign(
      { _id: usuarioEncontrado._id },
      process.env.JWT_SECRET,
      {
        expiresIn: "1h",
      }
    );

    return res.status(200).json({
      message: "Bienvenido",
      content: token,
    });
  } else {
    return res.status(400).json({
      message: "Credenciales incorrectas",
    });
  }
};
