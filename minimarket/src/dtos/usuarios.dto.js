import prisma from "@prisma/client";
import validator from "validator";

export function usuarioRequestDTO({ nombre, email, password, rol }) {
  const errores = [];

  if (!validator.isEmail(email)) {
    errores.push("El email no es un correo.");
  }

  if (validator.isEmpty(password)) {
    errores.push("El pass no puede estar vacío.");
  }

  if (validator.isEmpty(nombre)) {
    errores.push("El nombre no puede estar vacío.");
  }

  if (
    rol !== prisma.USUARIO_ROL.ADMINISTRADOR &&
    rol !== prisma.USUARIO_ROL.CLIENTE
  ) {
    errores.push("El rol no es válido.");
  }

  if (errores.length != 0) {
    throw Error(errores);
  } else {
    return {
      nombre,
      email,
      password,
      rol,
    };
  }
}

export function loginRequestDTO({ email, password }) {
  const errores = [];
  if (!validator.isEmail(email)) {
    errores.push("El email no es un correo.");
  }
  if (validator.isEmpty(password)) {
    errores.push("El pass no puede estar vacío.");
  }

  if (errores.length != 0) {
    throw Error(errores);
  } else {
    return {
      email,
      password,
    };
  }
}
