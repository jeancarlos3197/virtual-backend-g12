import validador from "validator";

export const libroRequestDTO = ({ nombre, avance, numPagina }) => {
  const errores = [];

  if (validador.isEmpty(nombre)) {
    errores.push("Nombre no puede estar vacio");
  }

  if (avance !== "INCOMPLETO" && avance !== "COMPLETO") {
    errores.push("Avance debe ser INCOMPLETO o COMPLETO");
  }

  if (avance === "INCOMPLETO") {
    if (validador.isEmpty(numPagina.toString()) || !numPagina) {
      errores.push("numPagina no puede estar vacio si avance es INCOMPLETO");
    }
  }

  if (errores.length !== 0) {
    throw Error(errores);
  } else {
    return { nombre, avance, numPagina };
  }
};
