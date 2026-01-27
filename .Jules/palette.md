## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2025-05-18 - Interactive Diagrams & Accessibility
**Learning:** Custom interactive diagrams built with absolute positioning and JS often get skipped by keyboard users. Adding `tabindex="0"` and mirroring hover effects to `:focus-visible` turns a "dead" visual into an accessible feature.
**Action:** When auditing custom visuals, check if they convey information. If so, make them focusable with `role="img"` and `aria-label`, and ensure visual feedback matches mouse interactions.
