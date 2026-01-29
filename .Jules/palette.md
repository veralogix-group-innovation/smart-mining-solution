## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2025-02-14 - Dynamic Element Accessibility
**Learning:** Interactive-looking elements generated via JavaScript (like data visualization nodes) are frequently inaccessible `div`s. They require explicit `tabindex`, `role`, and `aria-label` attributes to be perceivable and operable by keyboard and screen reader users.
**Action:** When auditing dynamic visualizations, ensure every interactive or information-bearing node has `tabindex="0"`, a semantic role (e.g., `img`), and a descriptive `aria-label`. Match `:focus-visible` styles to `:hover` styles for consistency.
