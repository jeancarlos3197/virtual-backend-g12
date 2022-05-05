import { Router } from "express";
import {
  actualizarProducto,
  crearProducto,
  eliminarProducto,
  listarProductos,
} from "../controllers/productos.controller.js";
import { validarAdmin, verificarToken } from "../utils/validador.js";

export const productosRouter = Router();
productosRouter
  .route("/productos")
  .get(listarProductos)
  .post(verificarToken, validarAdmin, crearProducto);
productosRouter
  .route("/producto/:id")
  .all(verificarToken, validarAdmin)
  .put(actualizarProducto)
  .delete(eliminarProducto);
