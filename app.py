from flask import Flask, render_template, request,redirect, uri_for 
from flask_sqlalchemy import SQLAlchemy 
import os
import requests

app = Flask(__name__)
URL_WEBHOOK_DISCORD = "https://discord.com/api/webhooks/1523337443452129383/DQ8-4oSPzsjEeGAz8aee1_JtR8x0eXvMp26rB4l4fhxO4L8ERd0mzfGZn9NYUi12-Xt6"

basedir = os.path.abspath(os.paht.dirname(__file__))
app.config['SQLALCHEMY_DATARSE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tienda.db')
app.config['SQLALCHEMY_TRAK_MODIFICATIONS'] = False
db =SQLAlchemy(app)

TELEFONO_CONTACTO = "928315704"

class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telefono =db.Column(db.String(20), nullable=False)
    nombre =db.Column(db.String(50), nullable=False)
    cantidad = db.Colum(db.String(50), default="0")
    producto_ref = db.Column(db.String(100), default="-")
    estado_pago = db.Column(db.String(50, default="Deuda"))
    estado_entraga = db.Column(db.String(50), default="Pendiente")

with app.app_contex():
    db.create_all()

PRODUCTOS = [
    {
        "id": 1,
        "nombre": "Zeolita Clinoptilolita micronizada",
        "precio": 120.00,
        "peso": 500.00,
        "imagen": "Zeolita Clinoptilolita micronizada.jpg",
        "descripcion": "Producto Natural Absorbe y elimina metales pesados como mercurio, aluminio, plomo, entre otros y toxinas, corrige cuestiones hormonales afectos a la tiroides, infertilidad, ovario poliquístico, menopausia, mejora la digestión y la absorción intestinal de minerales y vitaminas, remineralizante y alcalinizante, regula los niveles de azúcar en la sangre, desinflama y regenera las articulaciones, efectivo para bajar de peso…"

    },
    {
        "id":2,
        "nombre": "Tierra de Diatomeas (Bentonita)",
        "precio": 45.00,
        "peso": 500.00,
        "imagen": "Tierra de DIatomeas.jpg",
        "descripcion": "Producto natural Remineralizante por excelencia, con altocontenido de silicio orgánico natural. Regenerador del sistema óseo, artrosis, osteoporosis, reduce la inflamación por varices, desintoxicante natural de toxinas por alimentos refinados y fármacos, desparasitante efectivo."
    },
    {
        "id":3,
        "nombre":"Citrato de Magnesio",
        "precio": 48.00,
        "peso": 500.00,
        "imagen": "Citrato de Magnesio.jpg",
        "descripcion": "Suplemento mineral de mayor absorción. Presente en más de 300 acciones bioquímicas del organismo, regenerador del sistema óseo y nervioso, regulador digestivo, relajante, efectivo para mejorar la calidad de sueño, eleva la energía, otros…"
    },
    {
        "id":4,
        "nombre": "Citrato de Potasio",
        "precio": 48.00,
        "peso": 500.00,
        "imagen": "Citrato de Potasio.jpg",
        "descripcion": "Suplemento mineral de mayor absorción. Elimina calambres, controla la presión alta, controla el deseo de comer en exceso o antojo de dulces, retención de líquido, previene y elimina piedras de los riñones, entre otros…"
    },
    {
        "id":5,
        "nombre": "DMSO",
        "precio": 90.00,
        "peso": 100.00,
        "imagen": "DMSO.jpg",
        "descripcion": "Producto natural grado alimentario. Efectivo analgésico y antiinflamatorio. Regenerador celular y conductor por excelencia, cicatrizante efectivo, antiviral, desintoxicante."
    },
    {
        "id":6,
        "nombre": "Oxígeno Líquido ",
        "precio": 20.00,
        "peso": 50.00,
        "imagen": "Oxígeno Líquido .jpg",
        "descripcion": "Producto grado alimentario. Elimina y controla el incremento de patógenos como virus, bacterias, hongos. Tratamiento de diferentes enfermedades como trombosis, infecciones respiratorias, autoinmunes, otros…"
    },
    {
        "id":7,
        "nombre": "Bicarbonato de Sodio",
        "precio": 20.00,
        "peso": 500.00,
        "imagen": "Bicarbonato de Sodio.jpg",
        "descripcion": "Alcalinizante por excelencia. Ayuda a reducir la acidez estomacal, exfoliante, relajante muscular para pies, blanqueador dental, actúa también como desinfectante."
    },
    {
        "id":8,
        "nombre": "Kombucha",
        "precio": 15.00,
        "peso": 1.00,
        "imagen": "Kombucha.jpg",
        "descripcion": "Producto natural Fuente primaria de probióticos Contribuye a la regeneración de la flora intestinal Contribuye a la desintoxicación hepática Reduce los niveles de colesterol malo Controla los niveles de azúcar en sangre Fortalece el sistema inmune."
    },
    {
        "id":9,
        "nombre": "CDS",
        "precio": 48.00,
        "peso": 500.00,
        "imagen": "CDS.jpg",
        "descripcion": "H2O enriquecido de oxígeno Purificador de agua natural Alcaliniza el PH del organismo, proporciona mayor oxígeno, elimina patógenos como hongos, virus, parásitos y bacterias. Eficaz para diferentes padecimientos como el cáncer, pie diabético, diabetes, miomas, quistes, tumores, entre otros."
    },
]

@app.route('/index_principal')
def index_principal():
    return render_template('index_principal.html')

@app.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():
    if request.method == 'POST': 
        nom = request.form.get('nombre')
        tel = request.form.get('telefono')
        nuevo = Registro(nombre = nom, telefono = tel)
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('registro.html')

@app.route('/administracion', methods=['GET', 'POST'])
def administracion():
    if request.method == 'POST':
        reg_id = request.form.get('id')
        registro = Registro.query.get(reg_id)
        registro.cantidad = request.form.get('cantidad')
        registro.producto_ref = request.form.get('producto_ref')
        registro.estado_pago = request.form.get('estado_pago')
        registro.estado_entrega = request.form.get('estado_entrega')
        db.session.commit()
        return redirect(url_for('administracion'))
    
    registros = Registro.query.all()
    return render_template('administracion.html', registros=registros, productos=PRODUCTOS)


@app.route('/')

def home():
    query = request.args.get('q', '').lower()
    if query:
        resultados = [p for p in PRODUCTOS if query in p['nombre'].lower()]
    else:
        resultados = PRODUCTOS 
    return render_template('home.html', productos=resultados)

@app.route('/producto/<int:id>')
def producto(id):
    p = next((item for item in PRODUCTOS if item["id"] == id), None)
    if p:
        return render_template('producto.html', producto = p, Whatsapp = TELEFONO_CONTACTO)
    return "Producto no encontrado", 404

@app.route('/click')
def registrar_clic():
    user_id = request.args.get('user_id')

    if user_id:
        try:
            data = {
                "content": f"SISTEMA_MONEDAS_RECOMPENSA:{user_id}"
            }
            requests.post(URL_WEBHOOK_DISCORD, json=data)
            
            return redirect("/?status=success")
        except Exception as e:
            print(f"Error enviando webhook: {e}")

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
