import { Router } from "express";

import {
  confirmarCuenta,
  crearUsuario,
  login,
  perfil,
} from "../controllers/usuarios.controller.js";
import { verificarToken } from "../utils/validador.js";

export const usuarioRoutes = Router();

usuarioRoutes.post("/registro", crearUsuario);
usuarioRoutes.post("/login", login);
usuarioRoutes.post("/confirmar-cuenta", confirmarCuenta);
usuarioRoutes.get("/perfil", verificarToken, perfil);
