## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2025-02-14 - Dynamic Interactive Elements
**Learning:** The "Smart Hub" diagram generates interactive nodes via JS with inline styles for positioning. This blocked standard CSS hover/focus transforms from working without `!important`, and the nodes were completely invisible to keyboard users.
**Action:** When creating custom interactive visualizations (non-standard controls), always explicity add `tabindex="0"`, `role`, and `aria-label` in the generation function. Ensure focus states mirror hover states, using `!important` if inline styles conflict.
