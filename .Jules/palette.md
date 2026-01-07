## 2024-05-23 - Tab Interface Accessibility
**Learning:** Static site "tabs" implemented as buttons toggling divs are a common pattern that fails accessibility without proper ARIA roles. Adding `role="tablist"`, `role="tab"`, and `role="tabpanel"` transforms a collection of buttons into a navigable composite widget.
**Action:** When auditing static sites, check that "tabs" aren't just buttons with click handlers, but semantic components with proper keyboard support and screen reader announcements.
