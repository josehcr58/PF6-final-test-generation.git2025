def mostrar_menu(menu):
    """Muestra el menú de manera organizada."""
    print("✨ ¡Bienvenido al Restaurante de Dio! ✨")
    print("--------------------------------------------------")

    # Iterar sobre las categorías y sus platos
    for categoria, platos in menu.items():
        # Usamos título y centramos la categoría para destacarla
        print(f"\n🌟 --- **{categoria.upper()}** --- 🌟")

        # Iterar sobre cada plato en la categoría
        for plato, descripcion in platos.items():
            # Formatear el plato y su descripción
            print(f"- **{plato}:** {descripcion}")
    
    print("\n--------------------------------------------------")
    print("¡Gracias por visitarnos! Vuelva pronto. 🙏")

# Definición del Menú con un diccionario anidado
menu_colombiano = {
    "Entradas y Pasabocas": {
        "Empanadas": "Fritura de maíz rellena de carne y/o papa.",
        "Aborrajado": "Plátano maduro frito, relleno de queso y bocadillo (dulce de guayaba).",
        "Patacones con Hogao": "Rodajas de plátano verde frito y aplanado, servido con salsa de tomate y cebolla.",
    },
    "Platos Fuertes Regionales": {
        "Bandeja Paisa (Antioquia)": "Frijoles, arroz, carne molida, chicharrón, huevo frito, plátano maduro, aguacate y arepa. ¡El plato insignia!",
        "Ajiaco Santafereño (Bogotá)": "Sopa de pollo con tres tipos de papa (pastusa, sabanera y criolla), mazorca y guascas, servida con crema de leche y alcaparras.",
        "Sancocho de Gallina (Costa y Valle)": "Sopa espesa a base de gallina, yuca, plátano, papa y mazorca, cocinada en leña en algunas regiones.",
        "Lechona (Tolima y Huila)": "Cerdo horneado relleno de arroz, carne de cerdo y especias.",
        "Mojarra Frita (Costa Atlántica)": "Pescado entero frito, servido con arroz con coco y patacones.",
    },
    "Postres": {
        "Obleas": "Galletas delgadas y grandes rellenas de arequipe (dulce de leche) y a veces queso y mermelada.",
        "Arroz con Leche": "Arroz cocido en leche con canela, azúcar y pasas.",
    },
    "Bebidas Típicas": {
        "Jugo de Lulo": "Bebida refrescante hecha con la fruta exótica Lulo.",
        "Aguardiente (Solo para Adultos)": "Licor anisado destilado de caña de azúcar.",
        "Chocolate Santafereño": "Chocolate caliente servido con queso y pan.",
    }
}

# Llamar a la función para mostrar el menú
mostrar_menu(menu_colombiano)

