#!/usr/bin/env python3
"""
Generate PWA icon assets for MindVault
Creates 192x192, 512x512, and maskable icons with the MindVault branding
"""

from PIL import Image, ImageDraw
import os

# Create directory if it doesn't exist
os.makedirs('static/images', exist_ok=True)

def create_icon(size, maskable=False):
    """Create a PWA icon with MindVault branding"""
    # Create image with gradient background
    img = Image.new('RGBA', (size, size), (5, 6, 8, 255))  # Dark background
    draw = ImageDraw.Draw(img)
    
    # Draw gradient-like background (cyan to purple)
    for i in range(size):
        # Linear gradient from cyan (0, 242, 255) to purple (112, 0, 255)
        r = int(0 + (112 - 0) * (i / size))
        g = int(242 + (0 - 242) * (i / size))
        b = int(255 + (255 - 255) * (i / size))
        draw.line([(0, i), (size, i)], fill=(r, g, b, 200))
    
    # Draw shield icon (simplified)
    margin = size // 4
    # Shield outline
    draw.rectangle(
        [margin, margin, size - margin, size - 2*margin],
        outline=(0, 242, 255, 255),
        width=size // 16
    )
    
    # Center circle (lock)
    center = size // 2
    radius = size // 6
    draw.ellipse(
        [center - radius, center - radius, center + radius, center + radius],
        outline=(0, 242, 255, 255),
        width=size // 16
    )
    
    return img

# Generate icons
print("Generating PWA icons...")

# 192x192 screenshot
img_192 = create_icon(192)
img_192.save('static/images/screenshot-192w.png')
print("✓ Created screenshot-192w.png")

# 512x512 screenshot
img_512 = create_icon(512)
img_512.save('static/images/screenshot-512w.png')
print("✓ Created screenshot-512w.png")

# 192x192 regular icon
img_192.save('static/images/icon-192x192.png')
print("✓ Created icon-192x192.png")

# 512x512 regular icon
img_512.save('static/images/icon-512x512.png')
print("✓ Created icon-512x512.png")

# Maskable icon (same as regular but can be masked)
img_512.save('static/images/icon-maskable.png')
print("✓ Created icon-maskable.png")

print("\n✓ All PWA icons generated successfully!")
print("  Location: static/images/")
print("  Files: icon-192x192.png, icon-512x512.png, icon-maskable.png, screenshot-192w.png, screenshot-512w.png")
