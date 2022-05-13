import morgan from "morgan";
import express from "express";
import mongoose from "mongoose";
import { usuariosRouter } from "./routes/usuarios.routes.js";
import { librosRouter } from "./routes/libros.routes.js";

const app = express();
const logger = morgan("dev");
app.use(logger);
app.use(express.json());

app.use(usuariosRouter);
app.use(librosRouter);
// morgan es un middleweate que me ayuda hacer seguimientos a las peticiones de mi api
const PORT = process.env.PORT ?? 3000;

mongoose
  .connect(process.env.MONGO_URL, { dbName: process.env.DBNAME })
  .then((valor) => {
    console.log("Conectado a la base de datos");
  })
  .catch((err) => {
    console.error("Error al conectar a la base de datos", err);
  });

app.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
