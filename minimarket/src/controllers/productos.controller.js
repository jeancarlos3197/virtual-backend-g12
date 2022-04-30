import { Prisma } from "../prisma.js";

export const crearProducto = async (req, res) => {
  console.log("primero");
  try {
    const nuevoProducto = await Prisma.producto.create({ data: req.body });
    console.log(nuevoProducto);
    console.log("ultimo");

    return res.status(201).json({
      message: "Producto agregado exitosamente",
      content: nuevoProducto,
    });
  } catch (error) {
    console.log(error);

    return res.json({
      message: "Erroral crear el producto",
    });
  }
};

export const listarProductos = async (req, res) => {
  const productos = await Prisma.producto.findMany();
  if (productos.length) {
    return res.json({
      message: "Lista de productos",
      content: productos,
    });
  } else {
    return res.json({
      message: "No hay productos",
    });
  }
};

export const actualizarProducto = async (req, res) => {
  const { id } = req.params;
  //findunique solo se utilizara las columnas unique en la tabla
  //findFirst por todas las clumnas
  try {
    const productoEncontrado = await Prisma.producto.findUnique({
      where: { id: +id },
      rejectOnNotFound: true,
    });

    const productoActualizado = await Prisma.producto.update({
      where: { id: productoEncontrado.id },
      data: req.body,
    });

    return res.status(201).json({
      message: "producto actualizado exitosamente",
      content: productoActualizado,
    });
  } catch (error) {
    return res.json({
      message: "Error al actualizar el producto",
      error: error.message,
    });
  }
};

export const eliminarProducto = async (req, res) => {
  const { id } = req.params;
  try {
    const productoEncontrado = await Prisma.producto.findUnique({
      where: { id: +id },
      select: { id: true },
      rejectOnNotFound: true,
    });

    await Prisma.producto.delete({
      where: { id: productoEncontrado.id },
    });

    return res.status(200).json({
      message: "Producto eliminado exitosamente",
    });
  } catch (error) {
    return res.json({
      message: "Error al eliminar el producto",
      error: error.message,
    });
  }
};
