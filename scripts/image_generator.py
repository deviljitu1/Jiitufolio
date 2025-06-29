#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import requests
import time

def generate_image(title, keywords, output_path="blog-img"):
    """
    Generate an image for a blog post using a placeholder service
    """
    try:
        os.makedirs(output_path, exist_ok=True)
        filename = title.lower().replace(" ", "-").replace(":", "").replace(",", "")
        filename = "".join(c for c in filename if c.isalnum() or c == "-")
        filename = filename[:50]
        image_url = f"https://picsum.photos/800/400?random={int(time.time())}"
        response = requests.get(image_url, timeout=30)
        response.raise_for_status()
        image_path = os.path.join(output_path, f"{filename}.png")
        with open(image_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Generated image: {image_path}")
        return image_path
    except Exception as e:
        print(f"❌ Error generating image: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python image_generator.py 'Title' 'Keywords'")
        sys.exit(1)
    title = sys.argv[1]
    keywords = sys.argv[2] if len(sys.argv) > 2 else ""
    print(f"🎨 Generating image for: {title}")
    print(f"🔑 Keywords: {keywords}")
    image_path = generate_image(title, keywords)
    if image_path:
        print(f"✅ Image generated successfully: {image_path}")
    else:
        print("❌ Failed to generate image")

if __name__ == "__main__":
    main() 