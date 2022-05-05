import mercadopago from "mercadopago";

import { Prisma } from "../prisma.js";

export const crearPreferencia = async (req, res) => {
  try {
    const { pedidoId } = req.body;
    const pedidoEncontrado = await Prisma.pedido.findUnique({
      where: { id: pedidoId },
      rejectOnNotFound: true,
      include: {
        usuario: true,
        detallePedidos: { include: { producto: true } },
      },
    });
    console.log(pedidoEncontrado);

    const preferencia = await mercadopago.preferences.create({
      auto_return: "approved",
      back_urls: {
        failure: "http://localhost:3000/pago-fallido",
        pending: "http://localhost:3000/pago-pendiente",
        success: "http://localhost:3000/pago-exitoso",
      },
      metadata: {
        nombre: "Prueba",
      },
      payer: {
        name: pedidoEncontrado.usuario.nombre,
        // surname: "De Rivero",
        // address: {
        //   zip_code: "04002",
        //   street_name: "Calle Los Girasoles",
        //   street_number: 105,
        // },
        email: "test_user_46542185@testuser.com", // pedidoEncontrado.usuario.email,
      },
      items: pedidoEncontrado.detallePedidos.map((detallePedido) => ({
        id: detallePedido.productoId,
        currency_id: "PEN",
        title: detallePedido.producto.nombre,
        quantity: detallePedido.cantidad,
        unit_price: detallePedido.producto.precio,
      })),
      // [
      //   {
      //     id: "1234",
      //     category_id: "456",
      //     currency_id: "PEN",
      //     description: "Zapatillas de Outdoor",
      //     picture_url: "https://imagenes.com",
      //     quantity: 1,
      //     title: "Zapatillas edicion Otoño",
      //     unit_price: 75.2,
      //   },
      // ],
      notification_url:
        "https://0d58-2001-1388-5564-5490-49ae-572e-a87d-c947.ngrok.io/mp-webhooks",
    });

    await Prisma.pedido.update({
      where: { id: pedidoId },
      data: { processId: preferencia.body.id, estado: "CREADO" },
    });

    console.log(preferencia);

    return res.json({
      message: "Preferencia generado exitosamente",
      content: preferencia,
    });
  } catch (error) {
    return res.json({
      message: "Error al crear la preferencia",
      content: error.message,
    });
  }
};

export const MercadoPagoWebhooks = async (req, res) => {
  console.log("---body---");
  console.log(req.body);

  console.log("---params---");
  console.log(req.params);

  console.log("---headers---");
  console.log(req.headers);

  console.log("---queryparams---");
  console.log(req.query);

  if (req.query.topic == "merchant_order") {
    const { id } = req.query;
    const orden_comercial = await mercadopago.merchant_orders.get(id);
    console.log("la orden es: ");
    console.log(orden_comercial);

    const pedido = await Prisma.pedido.findFirst({
      where: { processId: orden_comercial.body.preference_id },
    });
    if (!pedido) {
      console.log("Pedido incorrecto");
    }
    if (orden_comercial.body.order_status === "paid") {
      await Prisma.pedido.updateMany({
        where: { processId: orden_comercial.body.preference_id },
        data: { estado: "PAGADO" },
      });
    }
  }

  return res.status(201).json({
    message: "Webhooks recibido exitosamente",
  });
};
