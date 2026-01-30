## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2025-02-14 - Dynamic JS Diagrams Accessibility
**Learning:** Interactive visualizations generated via JS (like the Smart Hub diagram) often lack keyboard accessibility because they use `div`s with click handlers or hover effects but no `tabindex`, `role`, or ARIA labels.
**Action:** When auditing dynamic components, check `tabindex="0"`, `role="img"` (or `button`), and `aria-label` are programmatically added during generation. Ensure CSS uses `:focus-visible` to mirror `:hover` effects.
