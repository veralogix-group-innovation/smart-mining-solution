## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2025-02-14 - Accessible Interactive Diagrams
**Learning:** Custom interactive diagrams often exclude keyboard users. Using `role="img"`, `tabindex="0"`, and `aria-label` on generated nodes makes them accessible without complex widget roles.
**Action:** When animating elements on hover, always duplicate the effect for `:focus` to delight keyboard users equally.
