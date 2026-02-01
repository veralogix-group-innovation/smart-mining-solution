## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2025-02-15 - Interactive Diagrams
**Learning:** Custom visual diagrams (like the Smart Hub) built with divs and CSS transforms are often invisible to keyboard users. Adding `tabindex="0"`, `role="img"`, and `aria-label` makes them perceivable, but they also need visual focus states that mirror hover effects.
**Action:** When implementing custom interactive elements, always pair `:hover` styles with `:focus-visible` and ensure proper ARIA roles are applied dynamically if the content is generated via JS.
