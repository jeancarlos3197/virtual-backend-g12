import jsonwebtoken from "jsonwebtoken";
import { Prisma } from "../prisma.js";

export async function verificarToken(req, res, next) {
  // middleware
  // es un intermediario que sirve para hacer una validación previa antes del controlador final
  if (!req.headers.authorization) {
    return res.status(401).json({
      message: "No hay token",
    });
  }
  try {
    const token = req.headers.authorization.split(" ")[1];

    const payload = jsonwebtoken.verify(token, process.env.JWT_TOKEN);

    const usuarioEncontrado = await Prisma.usuario.findUnique({
      where: { id: payload.id },
      rejectOnNotFound: true,
    })

    req.user = usuarioEncontrado;

    next();
  } catch (error) {
    return res.status(401).json({
      message: "Token invalida",
      content: error.message,
    });
  }
}
