import mongoose from "mongoose";
import bcryptjs from "bcryptjs";
// toda la configuracion que estamos haciendo es solamente a nivel de mongoose
// https://mongoosejs.com/docs/schematypes.html

const libroSchema = new mongoose.Schema(
  {
    nombre: {
      type: mongoose.Schema.Types.String,
      required: true,
    },
    avance: {
      type: mongoose.Schema.Types.String,
      enum: ["INCOMPLETO", "COMPLETO"],
      required: true,
    },
    numPagina: {
      type: mongoose.Schema.Types.Number,
      min: 1,
      name: "num_pagina",
    },
  },
  // https://mongoosejs.com/docs/guide.html#options
  {
    //_id: false,
    timestamps: { updatedAt: "fecha_actualizacion" },
  }
);

const usuarioSchema = new mongoose.Schema({
  correo: {
    type: mongoose.Schema.Types.String,
    required: true,
    unique: true,
    lowercase: true,
    maxlength: 100,
  },
  nombre: mongoose.Schema.Types.String,
  telefono: {
    type: mongoose.Schema.Types.Number,
    required: false,
  },
  password: {
    type: mongoose.Schema.Types.String,
    set: (valorActual) => bcryptjs.hashSync(valorActual, 10),
  },
  // libro: libroSchema, relacion 1:1
  libros: [libroSchema], // relacion 1:N
});

export const Usuario = mongoose.model("usuarios", usuarioSchema);
