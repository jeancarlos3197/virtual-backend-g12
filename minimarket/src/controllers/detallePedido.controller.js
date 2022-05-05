import { crearDetallePedidoRequestDTO } from "../dtos/detallePedido.dto.js";
import { Prisma } from "../prisma.js";

export const crearDetallePedido = async (req, res) => {
  try {
    const data = crearDetallePedidoRequestDTO(req.body);

    await Prisma.$transaction(async () => {
      const { precio } = await Prisma.producto.findUnique({
        where: { id: data.productoId },
        rejectOnNotFound: true,
        select: { precio: true },
      });

      const { id, total } = await Prisma.pedido.findUnique({
        where: { id: data.pedidoId },
        select: { id: true, total: true },
        rejectOnNotFound: true,
      });

      const { subTotal } = await Prisma.detallePedido.create({
        data: { ...data, subTotal: precio * data.cantidad },
        select: { subTotal: true },
      });

      await Prisma.pedido.update({
        data: { total: total + subTotal },
        where: { id },
      });
    });

    return res.status(201).json({
      message: "Detalle de pedido agregado exitosamente",
    });
  } catch (error) {
    return res.status(400).json({
      message: "Error al crear el detalle pedido",
      content: error.message,
    });
  }
};
