# Web Performance Examples

Use these browser-specific metrics and prompts only when they match the measured
user experience. They are examples, not universal performance goals. Verify current
thresholds and project requirements before applying them.

Common Core Web Vitals thresholds:

| Metric                         | Good    | Needs improvement | Poor    |
| ------------------------------ | ------- | ----------------- | ------- |
| LCP, Largest Contentful Paint  | ≤ 2.5s  | ≤ 4.0s            | > 4.0s  |
| INP, Interaction to Next Paint | ≤ 200ms | ≤ 500ms           | > 500ms |
| CLS, Cumulative Layout Shift   | ≤ 0.1   | ≤ 0.25            | > 0.25  |

Web-specific investigation examples:

- first load: network waterfall, server response time, render-blocking resources,
  asset size, font loading, and image dimensions
- interaction delay: main-thread work, expensive rendering, long tasks, event
  handlers, and unnecessary UI updates
- navigation or data loading: request waterfalls, cache behavior, streaming, and
  user-visible loading states
