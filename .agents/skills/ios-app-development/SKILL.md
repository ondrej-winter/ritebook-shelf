---
name: ios-app-development
description: Design, develop, review, test, and maintain native iOS applications using current Apple APIs and Human Interface Guidelines. Use for iPhone SwiftUI or UIKit interfaces, app lifecycle, concurrency, persistence, networking, privacy, system integrations, and iOS release readiness. Not for a watchOS-only change or a browser-only interface.
metadata:
  version: "1.0.0"
  last-verified: "2026-11-15T08:00:14Z"
---

# iOS App Development

Deliver an iPhone experience with documented platform choices and observable
verification evidence. Apply the guidance needed by the request; a design or code
review does not authorize implementation or distribution.

## Establish the platform context

Inspect project instructions, targets and schemes, deployment minimum, Swift
language mode, Xcode/SDK version, dependencies, entitlements, and existing UI and
data architecture. Identify supported iPhone configurations and whether iPad,
extensions, or a companion app are already in scope. Preserve those commitments;
do not raise the minimum OS or replace a working architecture merely to adopt a
new API.

Start research from [Apple's iOS resources](https://developer.apple.com/ios/resources/)
and the [iOS Pathway](https://developer.apple.com/ios/get-started/), then open the
specific article or symbol for each source-sensitive choice. Check availability,
deprecations, hardware and entitlement requirements against the project's SDK and
deployment target. Use availability guards and useful fallbacks where needed.

The Apple sources linked here were reviewed on 2026-11-15, including the
[iOS release notes](https://developer.apple.com/documentation/ios-ipados-release-notes),
[Xcode release notes](https://developer.apple.com/documentation/xcode-release-notes),
and [WWDC26 iOS guide](https://developer.apple.com/wwdc26/guides/ios/). Recheck these
when using the skill; separate shipping features from betas and developer previews.
Older samples demonstrate concepts, but current symbol documentation and the
installed SDK determine usable signatures. For JavaScript-only documentation,
follow Apple's offered Markdown link. If online sources are unavailable, use
local Xcode documentation and identify unresolved choices.

## Design the experience

Identify the primary task, navigation and entry points, and the loading, empty,
offline, error, and permission states that affect it. Follow
[Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios):
keep essential content prominent, support familiar touch interactions, and account
for interrupted use and changes in appearance or text size.

For UI creation or review, read
[design and accessibility](references/design-and-accessibility.md). It covers
navigation, adaptive layouts, system appearance, assistive technologies, and
localization. Prefer system components for familiar behavior and platform updates.

## Develop the requested behavior

Use Swift and [SwiftUI](https://developer.apple.com/documentation/swiftui) as a
starting point for new native interfaces. Preserve appropriate UIKit code and
integrate the two frameworks where it solves a concrete need. Apple's frameworks
do not require a particular application architecture.

- For state ownership, concurrency, lifecycle, storage, networking, background
  work, or system surfaces, read
  [development and integrations](references/development-and-integrations.md).
- For protected resources, accounts, sensitive storage, SDK data use, or privacy
  declarations, read [privacy and security](references/privacy-and-security.md)
  before adding access or collection.
- For watch-specific work, route that portion to `watchos-app-development` when
  available and its trigger matches; otherwise use Apple's watchOS documentation
  and report the missing specialized guidance. Do not assume iOS execution rules
  apply to the watch.

Implement a coherent user flow with recovery, rather than treating successful API
calls as the full behavior. Keep data ownership and external side effects explicit
so that cancellation, relaunch, and retries can be verified.

## Verify and maintain

Read [testing and maintenance](references/testing-and-maintenance.md) when choosing
acceptance checks, validating changes, measuring performance, or preparing an
upgrade or release. Run the project's relevant checks and exercise the affected
flow on appropriate destinations. If a device and OS are explicitly requested,
use that destination or report its unavailability instead of silently substituting.

Without macOS/Xcode or the required hardware, complete useful design, code, and
configuration review with execution explicitly unverified. Do not invent passing
builds or device observations.

Report changed behavior or prioritized findings, deployment assumptions, relevant
Apple sources, and checks actually run. Separate static/build, unit, simulator/UI,
and physical-device evidence. Identify remaining gaps and the next concrete check;
a successful build does not establish runtime behavior or release readiness.
