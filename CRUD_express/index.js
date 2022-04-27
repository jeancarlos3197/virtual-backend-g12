import express from "express";
import cors from "cors";
// usando type CommonJS
// const express = require('express')

const servidor = express();
// middleware intermediario que permite visulaizar información adicional
// ahora podremos recibir y transcribirlo en un formato json
servidor.use(express.json());
servidor.use(express.raw()); // para recibir datos en formato raw o puero texto
// servidor.use(express.urlencoded()) // para recibir datos en formato urlencoded
// el method Get siempre será accedido
servidor.use(
  cors({
    origin: ["http://127.0.0.1:5500"],
    methods: ["POST", "PUT", "DELETE"],
    allowedHeaders: ["Content-Type", "Authorization"],
  })
);

const productos = [
  {
    nombre: "platano",
    precio: 1.8,
    disponible: true,
  },
];

servidor.get("/", (req, res) => {
  return res.status(200).json({
    message: "bienvenido a mi api de productos",
  });
});

servidor.post("/productos", (req, res) => {
  console.log(req.body);
  const data = req.body;

  productos.push(data);

  return res.status(201).json({
    message: "Producto agregado exitosamente",
  });
});

servidor.get("/productos", (req, res) => {
  const data = productos;
  return res.json({
    data,
  });
});

servidor
  .route("/producto/:id")
  .get((req, res) => {
    const { id } = req.params;

    if (productos.length < id) {
      return res.status(400).json({
        message: "El producto no existe",
      });
    }

    const data = productos[id - 1];
    return res.json({
      data,
    });
  })
  .put((req, res) => {
    const { id } = req.params;

    if (productos.length < id) {
      return res.status(400).json({
        message: "El producto a actualizar no existe",
      });
    }

    productos[id - 1] = req.body;

    return res.json({
      message: "Producto actualizado exitosamente",
      content: productos[id - 1],
    });
  })
  .delete((req, res) => {
    const { id } = req.params;
    if (productos.length < id) {
      return res.status(400).json({
        message: "El producto a eliminar no existe",
      });
    }

    productos.splice(id - 1, 1);
    return res.json({
      message: "Producto eliminado exitosamente",
    });
  });

servidor.listen(3000, () => {
  console.log("servidor corriendo exitosamente en el puerto 3000");
});
