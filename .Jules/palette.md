## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2025-02-14 - Accessible Visual Delight
**Learning:** Purely visual interactive elements (like the Hub diagram nodes) often rely solely on :hover for delight. Keyboard users miss out entirely.
**Action:** When using CSS transforms for hover effects, always pair :hover with :focus-visible and ensure the element has tabindex="0" and a role.
