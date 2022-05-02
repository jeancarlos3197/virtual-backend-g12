import { Prisma } from "../prisma.js";
import { hashSync, compareSync } from "bcrypt";
import jsonwebtoken from "jsonwebtoken";
import cryptojs from "crypto-js";

import { enviarCorreoValidacion } from "../utils/sendMail.js";

import { usuarioRequestDTO, loginRequestDTO } from "../dtos/usuarios.dto.js";

export const crearUsuario = async (req, res) => {
  try {
    const data = usuarioRequestDTO(req.body);
    const passwordEncriptada = hashSync(data.password, 10);

    const nuevoUsuario = await Prisma.usuario.create({
      data: { ...data, password: passwordEncriptada },
      select: {
        id: true,
        nombre: true,
        email: true,
        rol: true,
        validado: true,
      },
    });

    const hash = cryptojs.AES.encrypt(
      JSON.stringify({
        nombre: nuevoUsuario.nombre,
        email: nuevoUsuario.email,
      }),
      process.env.LLAVE_ENCRIPTACION
    ).toString();

    await enviarCorreoValidacion({
      destinatario: nuevoUsuario.email,
      hash,
    });

    return res.status(201).json({
      message: "Usuario creado exitosamente",
      usuario: nuevoUsuario,
    });
  } catch (error) {
    return res.status(400).json({
      message: "Error al crear el usuario",
      content: error.message,
    });
  }
};

export const login = async (req, res) => {
  try {
    const data = loginRequestDTO(req.body);
    const usuarioEncontrado = await Prisma.usuario.findUnique({
      where: { email: data.email },
      rejectOnNotFound: true,
    });

    if (compareSync(data.password, usuarioEncontrado.password)) {
      const token = jsonwebtoken.sign(
        {
          id: usuarioEncontrado.id,
          mensaje: "API de minimarket",
        },
        process.env.JWT_TOKEN,
        { expiresIn: "1h" }
      );
      // el expiresIn recibe un numero (sera expresado en segundo) y si le pasamos un string:
      // '10' > 10 milisegundos
      // '1 days' > 1 dia
      // '1y' > 1 año
      // '7d' > 7 dias
      return res.json({
        message: "Bienvenido",
        content: token,
      });
    } else {
      throw new Error("Credenciales incorrectas");
    }
  } catch (error) {
    if (error instanceof Error) {
      return res.status(400).json({
        message: "Error al loguearse",
        content: error.message,
      });
    }
  }
};

export const confirmarCuenta = async (req, res) => {
  try {
    const data = req.body;
    // aca decodificamos el hash que viene en el correo
    const informacion = JSON.parse(
      cryptojs.AES.decrypt(data.hash, process.env.LLAVE_ENCRIPTACION).toString(
        cryptojs.enc.Utf8
      )
    );
    console.log(informacion);

    const usuarioEncontrado = await Prisma.usuario.findFirst({
      where: {
        email: informacion.email,
        validado: false,
      },
      rejectOnNotFound: true,
      select: {
        id: true,
        validado: true,
      },
    });

    if (!usuarioEncontrado) {
      throw new Error("El usuario ya fue validado");
    }
    const usuarioValidado = await Prisma.usuario.update({
      where: {
        id: usuarioEncontrado.id,
      },
      data: {
        validado: true,
      },
    });

    return res.json({
      message: "Cuenta validada correctamente",
      content: usuarioValidado,
    });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(400).json({
        message: "Error al loguearse",
        content: error.message,
      });
    }
  }
};

export const perfil = async (req, res) => {
  console.log(req.user)
  return res.json({
    message: "Bienvenido",
    content: req.user,
  })
}