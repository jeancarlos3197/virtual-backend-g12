from flask_restful import Resource, request
from flask_jwt import jwt_required
# from sendgrid.helpers.mail import Email, To, Content, Mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from os import environ

from config import conexion, sendgrid

from dtos.registro_dto import LoginDTO, RegistroDTO, UsuarioResponseDTO
from dtos.usuario_dto import ResetPasswordRequestDTO
from models.usuarios import Usuario

class RegistroController(Resource):
  def post(self):
    # da todo el body convertido en diccionario
    body = request.get_json()
    try:
      data = RegistroDTO().load(body)
      nuevoUsuario = Usuario(**data)
      # Generar un hash de la contraseña
      nuevoUsuario.encriptar_pwd()
      conexion.session.add(nuevoUsuario)
      conexion.session.commit()
      respuesta = UsuarioResponseDTO().dump(nuevoUsuario)
      return {
        'message': 'Usuario registrado exitosamente',
        'content': respuesta
      }, 201
      
    except Exception as e:
      conexion.session.rollback()
      return{ 
        'message': 'Error al registrar al usuario',
        'content': e.args
      }, 400

class LoginController(Resource):
  def post(self):
    body = request.get_json()
    try:
      data= LoginDTO().load(body)
      return {
        'message': 'Bienvenido'
      }
    except Exception as e:
      return {
        'message': 'Credenciales incorrectas',
        'content': e.args
      }

class ResetPasswordController(Resource):
  def post(self):
    body = request.get_json()
    # -----------------------Utilizando la libreria de python de mensajeria
    mensaje = MIMEMultipart()
    email_emisor = environ.get('EMAIL_EMISOR')
    email_password = environ.get('EMAIL_PASSWORD')
    try:
      data = ResetPasswordRequestDTO().load(body)
      # validar si existe ese usuario
      usuarioEncontrado = conexion.session.query(Usuario).filter_by(correo = data.get('correo')).first()
      if usuarioEncontrado is not None:
        texto = "Hola este es un mensaje de prueba."
        mensaje['Subject'] = 'Reinciar contraseña  Monedero App'
        html = open('./email_templates/joshua_template.html').read().format(usuarioEncontrado.nombre, usuarioEncontrado.correo, environ.get('URL_FRONT'))
        # siempre que queramos agregar un HTML como texto del mensaje tiene que ir despues del texto ya que rimerotratara de enviar el ultimo y si no puede envuara el anterior
        # mensaje.attach(MIMEText(texto, 'plain'))
        mensaje.attach(MIMEText(html, 'html'))
        # inicio el envio del correo
        # SERVIDOR                        |  Puerto
        # outlook > outlook.office365.com | 587
        # gmail >   smtp.gmail.com        | 587
        # hotmail > smtp.live.com         | 587
        # icloud >  smtp.mail.me.com      | 587
        # yahoo >   smtp.mail.yahoo.com   | 587
        emisorSMTP = SMTP('smtp.gmail.com', 587)
        emisorSMTP.starttls()
        emisorSMTP.login(email_emisor,email_password)
        # envio el correo
        emisorSMTP.sendmail(
          from_addr=email_emisor,
          to_addrs=usuarioEncontrado.correo,
          msg = mensaje.as_string()
        )
        # finaliza la sesion de mi correo
        emisorSMTP.quit()
      return {
        'message': 'Correo enviado exitosamente'
      },201
    except Exception as e:
      return {
        'message': 'Error al enviar el correo',
        'content': e.args
      }, 400

    # -----------------------utilizando sendgrid
    # try:
    #   data = ResetPasswordRequestDTO().load(body)
    #   usuarioEncontrado = conexion.session.query(Usuario).filter_by(correo=data.get('correo')).first()
    #   if usuarioEncontrado is not None:
    #     from_email = Email('carlos.ademir_66@hotmail.com')
    #     to_email = To(usuarioEncontrado.correo)
    #     subject = 'Reinicia tu contraseña del Monedero App'
    #     content = Content('text/plain', 'Hola, has solicitado el reincio de tu contraseña, haz click en el siguiente enlace para cambiar, sino has sido tu ignorar este mensaje, ...')
    #     mail = Mail(from_email, to_email,subject, content)
    #     envia_correo = sendgrid.client.mail.send.post(request_body=mail.get())
    #     el estado de la respuesta de sendgrid
    #     print (envia_correo.status_code)
    #     el cuerpo de la respuesta de sendgrid
    #     print (envia_correo.body)
    #     los cabeceros de la respuesta de sendgrid
    #     print (envia_correo.headers)

    #   return {
    #     'message':'Correo enviado exitosamente'
    #   }
    # except Exception as e:
    #   return {
    #     'message':'Error al resetear la password',
    #     'content': e.args
    #   }