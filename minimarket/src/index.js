import express, { json } from "express";
import mercadopago from "mercadopago";
import { detallePedidoRoutes } from "./routes/detallePedido.routes.js";
import { pagosRouter } from "./routes/pagos.routes.js";
import { pedidosRouter } from "./routes/pedidos.routes.js";
import { productosRouter } from "./routes/productos.routes.js";
import { usuarioRoutes } from "./routes/usuarios.routes.js";

const app = express();

mercadopago.configure({
  access_token: process.env.MP_ACCESS_TOKEN,
  integrator_id: process.env.MP_INTEGRATOR_ID,
});

app.use(json());

const PORT = process.env.PORT ?? 3000;

app.get("/", (req, res) => {
  res.json({
    message: "Bienvenido a mi API del minimarket",
  });
});

app.use(productosRouter);
app.use(usuarioRoutes);
app.use(pedidosRouter);
app.use(detallePedidoRoutes);
app.use(pagosRouter);

app.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puero ${PORT}`);
});
