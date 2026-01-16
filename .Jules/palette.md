## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2025-02-14 - Accessible Interactive Diagrams
**Learning:** Custom Javascript-generated diagrams (like the Smart Hub) are often invisible to assistive technology. Making them keyboard-accessible with `tabindex="0"`, `role="img"`, and `aria-label` transforms them from "pictures" into navigable content.
**Action:** When building custom interactive visualizations, always pair `div`-based nodes with `tabindex="0"` and meaningful ARIA labels. Ensure `:focus-visible` styles mimic hover effects for a consistent experience.
