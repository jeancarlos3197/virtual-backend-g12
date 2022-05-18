import validator from "validator";
import prisma from "@prisma/client";

export const crearDetallePedidoRequestDTO = ({
  cantidad,
  unidadMedida,
  productoId,
  pedidoId,
}) => {
  const errores = [];
  if (
    validator.isEmpty(cantidad.toString()) ||
    !validator.isNumeric(cantidad.toString())
  ) {
    errores.map("Cantidad debe ser un numero y es requerida");
  }
  if (
    validator.isEmpty(unidadMedida) ||
    (unidadMedida !== prisma.UM_PRODUCTO.KG &&
      unidadMedida !== prisma.UM_PRODUCTO.UNIDAD)
  ) {
    errores.map(
      `unidadMedida debe ser ${prisma.UM_PRODUCTO.KG} o ${prisma.UM_PRODUCTO.UNIDAD}`
    );
  }
  if (
    validator.isEmpty(productoId.toString()) ||
    !validator.isNumeric(productoId.toString())
  ) {
    errores.map("El producto debe ser un numero y es requerido");
  }
  if (
    validator.isEmpty(pedidoId.toString()) ||
    !validator.isNumeric(pedidoId.toString())
  ) {
    errores.map("El pedido deve ser numerp y es requerido");
  }

  if (errores.length != 0) {
    throw new Error(errores);
  } else {
    return {
      cantidad,
      unidadMedida,
      productoId,
      pedidoId,
    };
  }
};