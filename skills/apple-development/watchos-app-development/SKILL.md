---
name: watchos-app-development
description: Design, develop, review, test, and maintain watchOS applications using current Apple APIs and Human Interface Guidelines. Use for Apple Watch SwiftUI interfaces, complications and Smart Stack widgets, background execution, independent operation, phone connectivity, and watch-specific integrations. Not for an iOS-only change with no Apple Watch behavior.
metadata:
  version: "1.0.0"
  last-verified: "2026-11-14T19:50:55Z"
---

# watchOS App Development

Deliver a focused Apple Watch experience with documented API choices and explicit
verification evidence. Apply only the parts needed by the requested work; a UI
review does not authorize implementation or distribution.

## Establish the platform context

Inspect the project's instructions, targets, deployment minimum, Xcode/SDK version,
capabilities, and existing watch surfaces. Identify whether the app is watch-only,
independent with an optional iPhone companion, or deliberately dependent. Preserve
the deployment minimum and product scope unless a change is authorized.

Before choosing an unfamiliar API, check its watchOS availability, deprecations,
hardware requirements, and current signature. Start from Apple's
[watchOS resources](https://developer.apple.com/watchos/resources/) and
[watchOS app documentation](https://developer.apple.com/documentation/watchos-apps),
then open the specific article or symbol. Check
[release notes](https://developer.apple.com/documentation/watchos-release-notes)
for the target OS and SDK; distinguish shipping APIs from beta-only features.

This skill's source review was performed on 2026-11-14, including watchOS 27 release
notes and the [WWDC26 watchOS guide](https://developer.apple.com/wwdc26/guides/watchos/).
Recheck changing requirements during use. Treat older sample project structure and
availability annotations as examples; prefer current symbol availability and the
installed SDK when they differ. If documentation cannot be fetched, use Xcode's
local documentation and mark unresolved choices. Without a macOS/Xcode runtime,
provide design or code review with execution explicitly unverified.

## Shape the wrist experience

Identify the essential information and action someone needs in a brief wrist
raise. Make that action obvious, keep navigation shallow, and select useful entry
points: app, complication, Smart Stack, notification, or Siri. Do not shrink an
entire phone interface onto the watch or add every system surface by default.
Follow [Designing for watchOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos).

For interface work, read [design and accessibility](references/design-and-accessibility.md).
It covers navigation, Digital Crown, adaptive layouts, Always On, gestures,
notifications, and the current system appearance.

## Develop with current platform patterns

- Prefer SwiftUI's app lifecycle and system controls for new interfaces. Use a
  single watch app target for logic, assets, and entitlements; separate widget and
  test targets remain appropriate. For legacy dual-target apps, use Apple's
  [single-target migration](https://developer.apple.com/documentation/watchos-apps/migrating-to-a-single-target-watchos-app)
  and review replacement of `WKExtension` APIs with `WKApplication` counterparts.
- Aim for independent installation, setup, authorization, and useful operation.
  An optional iPhone can help, but should not be the only data or authentication
  path for an independent app. Follow
  [Creating independent watchOS apps](https://developer.apple.com/documentation/watchos-apps/creating-independent-watchos-apps).
- Build new complications and watch widgets with WidgetKit and SwiftUI. Preserve
  existing configurations when migrating ClockKit; use the migration guidance in
  the runtime reference rather than simply deleting the old provider.
- Design for suspension and deferred delivery. Persist meaningful state, display
  cached or unavailable content honestly, and reconcile updates when execution
  resumes. A requested background refresh or widget reload is not a deadline.

For data freshness, background work, WatchConnectivity, widgets, App Intents,
authentication, or HealthKit, read
[runtime and integrations](references/runtime-and-integrations.md). Select only
the needed capability and its documented execution model.

## Verify and maintain

Read [testing and maintenance](references/testing-and-maintenance.md) when defining
acceptance checks, validating changes, investigating performance, or preparing a
release. Run the repository's relevant checks and exercise the affected watch
flows. Match an explicitly requested device and OS; report an unavailable
destination rather than silently substituting another.

Report the implemented behavior or review findings, relevant Apple sources,
deployment assumptions, and evidence by level: static/build, unit tests,
simulator/UI tests, and physical watch. Name skipped or unavailable checks and the
remaining device-dependent risks. A successful build or simulator run does not
establish real battery use, haptics, sensors, network routing, or system scheduling.
