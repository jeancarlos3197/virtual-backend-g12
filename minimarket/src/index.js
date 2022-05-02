import express, { json } from "express";
import { productosRouter } from "./routes/productos.routes.js";
import { usuarioRoutes } from "./routes/usuarios.routes.js";

const app = express();

app.use(json());

const PORT = process.env.PORT ?? 3000;

app.get("/", (req, res) => {
  res.json({
    message: "Bienvenido a mi API del minimarket",
  });
});

app.use(productosRouter);
app.use(usuarioRoutes);

app.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puero ${PORT}`);
});
