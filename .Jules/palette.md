## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.
## 2025-02-14 - Interactive Visualization Accessibility
**Learning:** Dynamically generated visualizations (like the Smart Hub) often rely on mouse-only interactions (hover). Adding `tabindex="0"` and `role="img"` makes them explorable by keyboard users, transforming a static graphic into an accessible feature.
**Action:** Whenever creating interactive diagrams or charts, ensure each node is keyboard focusable and announces its label.
