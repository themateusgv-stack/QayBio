from flask import Flask, render_template, request

app = Flask(__name__)

TELEFONO_CONTACTO = "51900000000"

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

if __name__ == '__main__':
    app.run(debug=True)