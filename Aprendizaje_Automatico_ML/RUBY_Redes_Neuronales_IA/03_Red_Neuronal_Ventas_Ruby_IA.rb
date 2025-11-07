
# En el siguiente codigo se muestra la creacion de una red neuronal con lenguaje ruby
# Con perceptrones que indican las iteraciones de la red neuronal }
# bundle init
# gem install ruby-fann
require 'ruby-fann'
require 'net/http'
require 'json'
require 'uri'

# --- Paso 1: Obtener datos desde una API pública segura ---
API_URL = 'https://fakestoreapi.com/products'

puts "Descargando datos desde API: #{API_URL}"
uri = URI(API_URL)
response = Net::HTTP.get(uri)
productos = JSON.parse(response)

# --- Paso 2: Convertir productos en datos de ventas simulados ---
# Supongamos que cada producto tuvo entre 10 y 100 ventas (unidades vendidas)
entradas = []
salidas = []

productos.each do |producto|
  precio = producto['price'].to_f
  unidades = rand(10..100)
  ingresos = (precio * unidades).round(2)

  entradas << [unidades.to_f, precio]
  salidas  << [ingresos]
end

puts "Datos cargados: #{entradas.size} productos simulados como ventas."

# --- Paso 3: Crear y entrenar la red neuronal ---
fann = RubyFann::Standard.new(
  num_inputs: 2,
  hidden_neurons: [6, 4],
  num_outputs: 1
)

training_data = RubyFann::TrainData.new(
  inputs: entradas,
  desired_outputs: salidas
)


puts "Entrenando la red neuronal..."
fann.train_on_data(training_data, 1000, 10, 0.01)
puts "Entrenamiento completado."
# --- Paso 4: Guardar y probar la red ---
fann.save("modelo_ventas_fakestore.net")
# Prueba de predicción:
puts "\nPredicción de ingresos para un producto nuevo:"
unidades = 50.0
precio = 20.0
prediccion = fann.run([unidades, precio])
puts "Unidades: #{unidades}, Precio: $#{precio}"
puts "Ingresos estimados: $#{prediccion.first.round(2)}"

 