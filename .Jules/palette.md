## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2025-02-14 - Interactive Diagram Accessibility
**Learning:** Purely visual, JS-generated diagrams (like the Smart Hub) often exclude keyboard users. Using `tabindex="0"`, `role="img"`, and `aria-label` allows exploration. Crucially, mapping `:focus-visible` to existing `:hover` styles provides "delight" (animations) to keyboard users for free.
**Action:** When auditing "interactive" diagrams, ensure they are reachable and reacting to keyboard focus, not just mouse hover.
