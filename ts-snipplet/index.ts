export interface PlaceholderOptions {
    bg?: string;        // Hex-Farbe ohne # (z.B. "0055ff")
    textColor?: string; // Hex-Farbe ohne # (z.B. "ffffff")
    text?: string;      // Eigener Text
}

/**
 * Generiert eine skalierbare SVG-Platzhalter-Data-URL direkt im Browser.
 */
export function getSvgPlaceholder(size: string, options: PlaceholderOptions = {}): string {
    // 1. Dimensionen parsen
    let width = 300;
    let height = 200;

    if (size.toLowerCase().includes('x')) {
        const [w, h] = size.toLowerCase().split('x');
        width = parseInt(w, 10) || 300;
        height = parseInt(h, 10) || 200;
    } else {
        const s = parseInt(size, 10) || 300;
        width = s;
        height = s;
    }

    // 2. Farben & Text validieren
    const hexRegex = /^([A-Fa-f0-9]{3}|[A-Fa-f0-9]{6})$/;
    const bg = options.bg && hexRegex.test(options.bg) ? `#${options.bg}` : '#eeeeee';
    const textColor = options.textColor && hexRegex.test(options.textColor) ? `#${options.textColor}` : '#aaaaaa';
    const displayText = options.text || `${width} x ${height}`;

    // 3. Dynamische Schriftgröße berechnen
    const fontSize = Math.max(12, Math.min(width, height) * 0.08);

    // 4. SVG-String erstellen
    const svg = `<svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" xmlns="http://w3.org">
    <rect width="100%" height="100%" fill="${bg}"/>
    <text x="50%" y="50%" font-family="Helvetica, Arial, sans-serif" font-size="${fontSize}px" fill="${textColor}" dominant-baseline="middle" text-anchor="middle">
      ${displayText}
    </text>
  </svg>`;

    // 5. Als direkt nutzbare Data-URL zurückgeben
    return `data:image/svg+xml;utf8,${encodeURIComponent(svg)}`;
}
