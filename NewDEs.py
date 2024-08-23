from PIL import Image, ImageDraw, ImageFont

# Create an image with white background
image = Image.new('RGBA', (600, 600), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Define colors
primary_color = "#2E86AB"
accent_color = "#F39C12"

# Draw a more trendy map pin
circle_radius = 70
circle_center = (300, 220)
draw.ellipse((circle_center[0] - circle_radius, circle_center[1] - circle_radius,
              circle_center[0] + circle_radius, circle_center[1] + circle_radius), fill=primary_color, outline=None)

# Draw a triangle under the circle to form a map pin
triangle = [(circle_center[0], circle_center[1] + circle_radius),
            (circle_center[0] - circle_radius, circle_center[1]),
            (circle_center[0] + circle_radius, circle_center[1])]
draw.polygon(triangle, fill=primary_color)

# Load a trendy font
try:
    font_amigos = ImageFont.truetype("DejaVuSans-Bold.ttf", 50)
    font_tagline = ImageFont.truetype("DejaVuSans-Bold.ttf", 20)
except IOError:
    font_amigos = ImageFont.load_default()
    font_tagline = ImageFont.load_default()

# Add the text "Amigos" below the pin
text_amigos = "Amigos"
text_size_amigos = draw.textsize(text_amigos, font=font_amigos)
text_position_amigos = (300 - text_size_amigos[0] // 2, 400)
draw.text(text_position_amigos, text_amigos, fill=primary_color, font=font_amigos)

# Add the tagline "
