[![CI](https://github.com/SamsonandDelilah/fastsvg/actions/workflows/ci.yml/badge.svg)](https://github.com/SamsonandDelilah/fastsvg/actions/workflows/ci.yml)

# ⚡ FastSVG - Blazing Fast Dynamic SVG Placeholder Toolset

A lightweight, multi-ecosystem developer utility to generate scalable, razor-sharp SVG placeholders on the fly. 

Whether you need a standalone **Python API Microservice** or a pure client-side **TypeScript function** for your React/Vue frontend, FastSVG prevents Cumulative Layout Shift (CLS) without the bloat of heavy image libraries.

---

## 🎨 Supported Ecosystems

Choose the tool that fits your current stack perfectly:

1. **`python-api/`** – A high-performance, zero-dependency FastAPI server. Perfect as a central microservice.
2. **`ts-snippet/`** – A pure frontend TypeScript function. Generates instant Data-URLs directly in the user's browser (Zero server overhead).

---

## 🚀 Features

* 📦 **Zero Dependencies:** No heavy image processing engines (like Pillow/PIL or Canvas). Pure string generation.
* ⚡ **Ultra Low Latency:** Generates SVGs in microseconds directly in memory.
* 📐 **Perfectly Scalable:** Pure vectors look razor-sharp on any Retina, Mobile, or 4K display.
* 🛠️ **CLS Optimization:** Allows browsers to lock down aspect ratios instantly to prevent jumping layouts.
* 🌈 **Highly Customizable:** Change dimensions, background colors, text colors, and labels dynamically.

---

## 🛠️ Quick Start

### Option A: Python API Microservice

Navigate to the `/python-api` folder, install the minimal requirements, and fire up the server:

```bash
cd python-api
pip install fastapi uvicorn
uvicorn main:app --reload
```
The API is now live at `http://127.0.0`

### Option B: TypeScript Frontend Snippet

Copy the function from `/ts-snippet/index.ts` directly into your web project. No installation required.

```typescript
import { getSvgPlaceholder } from './ts-snippet';

// Generates an instant, browser-native Data-URL
const placeholderUrl = getSvgPlaceholder("400x300", { 
  bg: "0055ff", 
  textColor: "ffffff",
  text: "Loading..." 
});

// Use it directly in your components (React, Vue, Next.js, etc.)
// <img src={placeholderUrl} width="400" height="300" alt="Preview" />
```

---

## 📖 API Endpoint Examples (Python Server)

Embed these endpoints directly into your dynamic HTML, CMS, or fallback logic:

* **Default Placeholder (Grey, 300x200):** `.../placeholder/300x200`
* **Square Placeholder (400x400):** `.../placeholder/400`
* **Custom Colors (Blue/White):** `.../placeholder/600x400?bg=0055ff&text_color=ffffff`
* **Custom Text Label:** `.../placeholder/300x200?text=Product+Preview`

---

## 🔮 Roadmap: The Rust & WASM Evolution (V2)

To push performance to the absolute physical limit and enable ultra-low-cost hosting, we are currently working on **FastSVG V2**, powered by **Rust**:

- [ ] **FastSVG Core in Rust:** Rewriting the string builder engine in safe, blazingly fast Rust.
- [ ] **WebAssembly (WASM) Build:** Compiling the Rust core into an npm package. Run native Rust speed directly inside the browser or on Edge Runtimes (Cloudflare Workers, Vercel Edge).
- [ ] **Pre-defined Design Templates:** Gradient backgrounds, skeleton screen wireframes, and subtle loading animations.

*Contributions and ideas for the Rust/WASM implementation are highly welcome! Open an issue or submit a PR.*

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
