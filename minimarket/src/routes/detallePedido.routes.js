import { Router } from "express";

import { crearDetallePedido } from "../controllers/detallePedido.controller.js";
import { validarCliente, verificarToken } from "../utils/validador.js";

export const detallePedidoRoutes = Router();

detallePedidoRoutes.post(
  "/detalle-pedido",
  verificarToken,
  validarCliente,
  crearDetallePedido
);
