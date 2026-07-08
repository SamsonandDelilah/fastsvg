import { describe, it, expect } from 'vitest';
import { getSvgPlaceholder } from './index'; // Pfad zu Ihrer TS-Datei

describe('getSvgPlaceholder', () => {
    it('sollte einen Data-URL-String zurückgeben', () => {
        const result = getSvgPlaceholder("400x300", { bg: "0055ff" });

        expect(result).toBeTypeOf('string');
        expect(result).toContain('data:image/svg+xml');
    });

    it('sollte benutzerdefinierten Text enthalten', () => {
        const result = getSvgPlaceholder("400x300", { text: "Test-Label" });

        // Prüft, ob der übergebene Text im SVG codiert ist
        expect(result).toContain('Test-Label');
    });
});
