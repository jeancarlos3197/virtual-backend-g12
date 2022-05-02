import nodemailer from "nodemailer";

const transporter = nodemailer.createTransport({
  host: "smtp.gmail.com",
  port: 587,
  auth: {
    user: process.env.EMAIL_ACOUNT,
    pass: process.env.EMAIL_PASSWORD,
  },
});

export const enviarCorreoValidacion = async ({ destinatario, hash }) => {
  const html = `
  <p>
    Hola para comenzar a disfrutar de toas las ofertas en nuestro Minimarket, por favor haz click en el siguiente enlace 
    <a href="${process.env.FRONTEND_URL}?hash=${hash}">
      Valida mi cuenta
    </a>
  </p>`;
  try {
    await transporter.sendMail({
      from: "jeancarlosademir321@gmail.com",
      to: destinatario,
      subject: "Validación correo de minimarket App",
      html,
    });
  } catch (error) {
    console.log(error);
    return error;
  }
};
