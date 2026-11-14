# Testing and maintenance

Use this reference to choose evidence for the changed behavior. The matrix is a
risk-based engineering checklist derived from Apple's platform guidance; select
applicable rows rather than treating every capability as mandatory.

## Automated and interactive verification

Run existing repository checks, then test watch-specific integration. Unit-test
state transitions, persistence, clock-dependent logic, retry behavior, and conflict
resolution where relevant. Add watch unit/UI targets and ensure the test scheme
actually runs them. Apple's
[watchOS test setup](https://developer.apple.com/documentation/watchos-apps/setting-up-tests-for-your-watchos-app)
describes unit and UI testing, but its extension-target screenshots are legacy:
select the actual app or shared module in a modern project.

| Area                  | Representative checks                                                                                                                                             |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Interface             | Small/large supported displays; large text; long translations; right-to-left layout; VoiceOver order and actions; Crown and touch navigation                      |
| Lifecycle             | Cold launch, wrist down/up, inactive/background, termination and relaunch, state restoration, Always On enabled/disabled and privacy redaction                    |
| Data                  | Offline launch, stale cache, empty content, permission refusal/revocation, delayed response, uncertain write and retry, persistence after restart                 |
| Independent use       | Fresh install, setup, authorization, account recovery if applicable, and useful operation without the iPhone app installed                                        |
| Networking            | Paired iPhone proxy, direct Wi-Fi, cellular where available, no connectivity, and transitions between routes                                                      |
| Phone sync            | Unreachable counterpart, absent companion, asynchronous activation/error, delayed updates, watch switching, conflicting edits                                     |
| Widgets               | Each supported family/configuration, placeholder, privacy, timeline rollover, stale data, cold launch/deep link, migration from installed ClockKit configurations |
| Notifications/intents | Authorization changes, foreground/background receipt, forwarding or direct delivery, short/long looks, actions and correct destination                            |
| Sessions/sensors      | Start, interruption, expiration, end, save/discard, relaunch recovery, and release of resources                                                                   |

Use previews and simulators for fast layout and flow checks; use a physical watch
for haptic feel, sensors, real network routes, wrist ergonomics, energy, and
system scheduling. Apple's
[content update guidance](https://developer.apple.com/documentation/watchos-apps/keeping-your-watchos-app-s-content-up-to-date)
specifically calls for testing different networking configurations. Validate
hardware-dependent behavior on supported devices. Record destination identifiers,
OS/build versions, commands, and results; do not quietly replace a requested model
or OS with another.

Smart Stack developer settings can accelerate relevance testing, but do not prove
normal production scheduling. See
[Smart Stack testing](https://developer.apple.com/documentation/widgetkit/widget-suggestions-in-smart-stacks#Test-widgets-in-Smart-Stacks).

## Performance and reliability

Measure launch/resume, input responsiveness, memory, CPU, transfers, and energy
for the actual flow before making performance claims. Use Xcode diagnostics and
Instruments supported by the target device/toolchain. Compare like-for-like
scenarios, including inactive display and background sessions; reduce unnecessary
work and repeat the affected measurement.

Follow [Improving performance](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance)
for the measurement cycle. Check platform availability of individual instruments,
metrics, and diagnostic APIs rather than assuming every iOS facility supports
watchOS. Preserve test results and sanitized diagnostics without recording health
data or credentials.

## Release preparation and ongoing maintenance

- Check current [watchOS release notes](https://developer.apple.com/documentation/watchos-release-notes)
  and [Apple's watchOS guide](https://developer.apple.com/wwdc26/guides/watchos/)
  for changes affecting the app. Verify symbol availability, hardware, locale,
  and runtime capability before using newer APIs. New platform features, including
  intelligence or additional HealthKit types, are optional product decisions.
- Recheck deployment settings, supported architectures, entitlements, signing,
  embedded widget resources, icons, and version alignment in a release archive.
  Test upgrades and stored-data migration as well as fresh installation. Validate
  the oldest supported OS and the current release; test betas separately without
  treating beta compatibility as a shipping requirement.
- Inspect the app and SDKs for applicable
  [privacy manifest declarations](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files),
  including required-reason API use. Ensure declarations and usage descriptions
  reflect actual behavior; a manifest does not replace authorization or App Store
  privacy disclosures.
- Before distribution, review the current
  [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
  for the app's features, privacy, health data, accounts, and purchases. Use
  [TestFlight](https://developer.apple.com/testflight/) for authorized beta
  distribution and collect feedback on real watch usage, crashes, and battery
  impact. Creating code or a review does not itself authorize uploading a build.
- After OS/SDK or dependency changes, rerun affected flows and revisit custom
  appearance, deprecated APIs, background behavior, and widget migrations.
  Report reproducible platform issues through
  [Feedback Assistant](https://developer.apple.com/bug-reporting/), with relevant
  diagnostics and reproduction steps.

Handoff should separate documented behavior, automated evidence, simulator
observations, and physical-device evidence, with explicit gaps and follow-up
checks. Static checks alone do not certify device behavior or release readiness.
