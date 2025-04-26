import os

# Dossier contenant les images
folder = 'images/slideshow'
output_file = 'slideshow.html'

# Début du HTML
html_head = """<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <title>Slideshow Auto</title>
  <link rel='stylesheet' href='slideshow.css'>
</head>
<body>
<div class='slideshow-container'>
"""

# Corps du HTML généré
html_body = ""
indicators = "<div class='dots-container'>\n"

for index, filename in enumerate(sorted(os.listdir(folder))):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
        html_body += f"  <div class='slide'><img src='{folder}/{filename}' alt=''></div>\n"
        indicators += f"  <span class='dot' onclick='currentSlide({index + 1})'></span>\n"

indicators += "</div>\n"

# Ajout des boutons de navigation
controls = """
  <a class='prev' onclick='plusSlides(-1)'>&#10094;</a>
  <a class='next' onclick='plusSlides(1)'>&#10095;</a>
"""

# Fin du HTML
html_foot = f"""
</div>
{controls}
{indicators}
<script src='slideshow.js'></script>
</body>
</html>
"""

# Génération du fichier HTML
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_head + html_body + html_foot)

print(f'{output_file} généré avec succès !')