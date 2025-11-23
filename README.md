# LuxeClean Landing para Shopify

Este repositorio contiene los archivos mínimos para añadir la landing de Luxe Clean a tu tema de Shopify conectado con GitHub.

## Estructura

- `sections/luxe-clean-landing.liquid`  
  Sección de hero + beneficios para el limpiador de brochas LuxeClean™.

- `sections/luxe-skin-landing.liquid`  
  Sección de hero + beneficios para el cepillo facial Luxe Skin™.

- `templates/page.luxe-clean-pack.json`  
  Plantilla de página Online Store 2.0 que incluye las dos secciones una debajo de la otra.

## Cómo usarlo con Shopify + GitHub

1. Crea un repositorio en GitHub y sube estos archivos respetando la misma estructura de carpetas.
2. En Shopify Admin, ve a **Online store → Themes → Connect from GitHub** y conecta este repositorio.
3. Espera a que Shopify sincronice el tema.
4. En Shopify Admin, ve a **Online store → Pages → Add page** y crea una nueva página (por ejemplo, `Luxe Clean Pack`).
5. En la configuración de la página, selecciona la plantilla **`page.luxe-clean-pack`**.
6. Abre el editor de temas (**Customize**), elige esa página y:
   - Asigna el producto correcto en la sección **Luxe Clean Landing**.
   - Asigna el producto correcto en la sección **Luxe Skin Landing**.
   - Ajusta textos, imágenes y precios desde los paneles de configuración de cada sección.

Con eso tendrás una landing minimalista, tipo Apple, lista para enviar tráfico y vender tu `LuxeClean™ Ritual Pack`.
