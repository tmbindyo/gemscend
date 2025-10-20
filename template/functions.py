import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def download_images_from_url(url: str, save_dir="template/static"):
    """
    Downloads all images from <img> tags and inline background-image URLs
    from a given page. Saves into the specified folder, keeping folder structure.

    - Skips images that already exist
    - Creates folders automatically
    """

    os.makedirs(save_dir, exist_ok=True)

    # Fetch page HTML
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    # Collect image URLs
    img_urls = set()

    # From <img> tags
    for img in soup.find_all("img"):
        if img.get("src"):
            img_urls.add(img.get("src"))

    # From inline styles (background-image, etc.)
    style_pattern = re.compile(r'url\([\'"]?(.*?)[\'"]?\)')
    for tag in soup.find_all(style=True):
        style_content = tag["style"]
        matches = style_pattern.findall(style_content)
        for match in matches:
            img_urls.add(match)

    # Download images
    for img_url in img_urls:
        full_url = urljoin(url, img_url)

        parsed_url = urlparse(img_url)
        file_path = parsed_url.path.lstrip("/")  # remove leading /
        local_path = os.path.join(save_dir, file_path)

        if os.path.exists(local_path):
            print(f"⏩ Skipping (already exists): {local_path}")
            continue

        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        try:
            print(f"⬇️ Downloading {full_url} → {local_path}")
            img_data = requests.get(full_url, timeout=10)
            img_data.raise_for_status()
            with open(local_path, "wb") as f:
                f.write(img_data.content)
        except Exception as e:
            print(f"❌ Failed to download {full_url}: {e}")


# Example usage:
# download_images_from_url("https://html.kodesolution.com/2025/finclix-html/index-3.html")




def update_html_with_static(file_path: str, static_prefix="images/"):
    """
    Reads an HTML file, replaces image paths with Django static template tags.
    
    - Converts <img src="images/..."> to <img src="{% static 'images/...' %}">
    - Converts inline background-image URLs to {% static 'images/...' %}
    """

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    # Update <img src="...">
    for img in soup.find_all("img", src=True):
        src = img["src"]
        if src.startswith(static_prefix):  
            img["src"] = f"{{% static '{src}' %}}"

    # Update inline background-image in style attributes
    for tag in soup.find_all(style=True):
        style = tag["style"]
        # Match background-image: url('images/...')
        match = re.search(r"url\(['\"]?(%s[^'\"]+)['\"]?\)" % re.escape(static_prefix), style)
        if match:
            path = match.group(1)
            new_style = re.sub(
                r"url\(['\"]?(%s[^'\"]+)['\"]?\)" % re.escape(static_prefix),
                f"url('{{% static \"{path}\" %}}')",
                style
            )
            tag["style"] = new_style

    # Save updated file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(f"✅ Updated: {file_path}")


import re

def update_static_paths(file_path: str):
    """
    Updates <img src="..."> and inline style background-image URLs
    to use Django {% static %}.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Fix <img src="...">
    content = re.sub(
        r'src="(images/[^"]+)"',
        "src=\"{% static '\\1' %}\"",
        content
    )

    # Fix background-image: url(...)
    content = re.sub(
        r'url\([\'\"]?(images/[^)\'\"]+)[\'\"]?\)',
        "url('{% static \"\\1\" %}')",
        content
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Updated: {file_path}")



