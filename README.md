# 🌟 Image Processing App

A simple and friendly web app to resize images and convert their formats, built with Streamlit and Pillow (PIL). Perfect for quick edits and downloads! ⚡🖼️

---

## ✨ Features
- 🔄 **Resize images** with optional aspect ratio preservation
- 🎨 **Convert image format** between `JPEG` and `PNG`
- 👀 **Preview** before downloading
- ⬇️ **One-click download** of processed images

---

## 📦 Tech Stack
- 🐍 Python
- 🧱 Streamlit
- 🖼️ Pillow (PIL)

---

## 📁 Project Structure
```
Image Conversoin/
├─ src/
│  ├─ app.py          # Streamlit UI and app logic
│  └─ utils.py        # Image utilities (resize, convert)
└─ README.md
```

---

## 🚀 Getting Started

### 1) Clone the repository
```bash
git clone <your-repo-url>
cd "Farshad's exercises on Project-Based-Python/Image Conversoin"
```

### 2) Create and activate a virtual environment (recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
```

### 3) Install dependencies
```bash
pip install -U pip
pip install streamlit pillow
```

### 4) Run the app
```bash
streamlit run src/app.py
```

Then open the URL shown in the terminal (usually `http://localhost:8501`). 🌐

---

## 🧭 Usage Guide
1. 📤 Upload an image (`.jpg`, `.jpeg`, `.png`).
2. 🧩 Choose a process: **Resize** or **Type Conversion**.
3. ✂️ For Resize:
   - ✅ Enable "Keep aspect ratio" to maintain image proportions.
   - ✏️ Enter the desired width; height auto-fills if aspect ratio is kept.
   - ▶️ Click "Resize image" to preview and download.
4. 🎯 For Type Conversion:
   - 🗂️ Choose `JPEG` or `PNG`.
   - ▶️ Click "Convert Image Type" to preview and download.

---

## 🛠️ Implementation Details
- `resize_image(image, width, height, keep_aspect_ratio)` uses `thumbnail` to preserve aspect ratio, and `resize` for exact sizing.
- `convert_image_type(image, output_format)` normalizes the format and handles `RGBA → JPEG` by converting to `RGB` to avoid errors.

---

## 🔐 Supported Formats
- Input: `JPG`, `JPEG`, `PNG`
- Output: `JPEG`, `PNG`

> Note: Converting images with transparency to `JPEG` will remove transparency (converted to white background via `RGB`).

---

## 🧪 Example
- Upload `photo.png`
- Convert to `JPEG`
- Download `converted_image.jpeg` ✅

---

## 🤝 Contributing
PRs are welcome! If you have ideas (more formats, quality controls, etc.), feel free to open an issue or a pull request. 💡

---

## 📜 License
This project is for educational purposes. Add a license if you plan to distribute. 📝

---

## 🙌 Credits
Built by Farshad with ❤️ using Streamlit and Pillow.
