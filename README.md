# LuxeClean Theme (Shopify + GitHub)

Tema mínimo de Shopify preparado para una landing de productos de belleza tipo Luxe Clean.

## Estructura

- `layout/theme.liquid`  
  Layout base del tema. Pinta `{{ content_for_layout }}` y aplica un fondo gris claro al body.

- `config/settings_schema.json`  
  Esquema mínimo de ajustes de tema para que Shopify lo considere un tema válido.

- `templates/index.json`  
  Plantilla de la home usando la sección `luxe-clean-landing`.

- `templates/page.luxe-clean-pack.json`  
  Plantilla de página Online Store 2.0 con dos secciones:
  - `luxe-clean-landing` (limpiador de brochas)
  - `luxe-skin-landing` (cepillo facial)

- `sections/luxe-clean-landing.liquid`  
  Hero + beneficios para el limpiador de brochas LuxeClean™.

- `sections/luxe-skin-landing.liquid`  
  Hero + beneficios para el cepillo facial Luxe Skin™.

## Cómo usarlo con Shopify + GitHub

1. Crea un repositorio en GitHub y sube TODO el contenido de esta carpeta respetando la estructura.
2. En Shopify Admin, ve a **Online store → Themes → Connect from GitHub** y selecciona este repositorio.
3. Shopify creará un nuevo tema con este código.
4. Publica el tema (o pruébalo primero como tema de vista previa).
5. Crea una página:
   - **Online store → Pages → Add page**, por ejemplo: “LuxeClean Ritual Pack”.
   - En “Theme template” selecciona: `page.luxe-clean-pack`.
6. Abre el editor de temas (**Customize**), selecciona la página que acabas de crear y:
   - Asigna el producto del pack o el bundle en la sección correspondiente.
   - Ajusta textos, imágenes y precios desde los paneles de cada sección.

Con esto tendrás una landing minimalista lista para enviar tráfico desde tus campañas y redes sociales.
