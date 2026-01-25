## 2025-02-14 - Keyboard Accessibility Foundations
**Learning:** Even visually polished marketing sites often miss basic keyboard accessibility. The absence of a skip link and focus indicators on key inputs like search creates a major barrier.
**Action:** Always check for `focus:outline-none` in Tailwind projects. If removed, ensure a replacement `focus:ring` or similar is added immediately. Always check for a skip link on pages with heavy navigation.

## 2025-02-14 - Dynamic Element Styles
**Learning:** Elements created via JS with inline `style.transform` properties block CSS hover/focus transforms unless `!important` is used. This is common in chart/diagram generators.
**Action:** When adding hover/focus effects to JS-generated elements that use inline positioning/transforms, ensure the CSS rules use `!important` or that the JS does not set properties that conflict with the desired interactive state.
