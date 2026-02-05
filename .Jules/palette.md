## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2025-02-14 - Dynamic Diagram Accessibility
**Learning:** Custom interactive diagrams built with JS and CSS hover effects often neglect keyboard users. Adding `tabindex="0"`, `role="img"`, and `aria-label` makes them navigable, and mirroring `:hover` styles with `:focus-visible` ensures consistent feedback.
**Action:** When auditing interactive graphics, check if they are keyboard-focusable. If not, add appropriate ARIA roles and ensure visual focus states match mouse hover interactions.
