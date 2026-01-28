## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2026-01-28 - Accessible JS Diagrams
**Learning:** Custom interactive diagrams (like the Smart Hub) often rely solely on mouse hover events, excluding keyboard users.
**Action:** Use `tabindex="0"`, `role="img"`, and `aria-label` to make them focusable and informative. Share styles using `.class:hover, .class:focus-visible` to ensure consistent visual feedback.
