# Testing and maintenance

Select evidence for the changed behavior. This is a risk-based engineering
checklist derived from Apple's guidance, not a requirement to exercise every
integration for every change.

## Automated and interactive verification

Discover the repository's supported build and test commands, actual schemes,
test plans, and destinations. Follow [Xcode testing](https://developer.apple.com/documentation/xcode/testing).
Keep simulator and device configurations explicit and retain test results such
as `.xcresult` bundles. Ensure the intended targets and tests actually ran;
compilation or an empty test selection is not a passing behavioral test.

Use [Swift Testing](https://developer.apple.com/documentation/testing) for new
Swift unit tests when the toolchain supports it, while preserving valid XCTest
coverage. Use XCTest with
[XCUIAutomation](https://developer.apple.com/documentation/xcuiautomation) for UI
tests and XCTest performance measurement where appropriate. Migrate tests
incrementally, checking the toolchain's
[interoperability rules](https://developer.apple.com/documentation/testing/migratingfromxctest)
before sharing assertions between frameworks. Isolate test data and dependencies
so parallel execution does not couple tests through mutable global state.

| Area | Representative checks |
| --- | --- |
| Business and data behavior | Validation, state transitions, decoding, persistence, schema upgrades, time/calendar boundaries where relevant |
| UI and accessibility | Primary task, back/cancel, keyboard and focus, small/large layouts, accessibility text sizes, VoiceOver, contrast, long translations and right-to-left layouts |
| Lifecycle | Cold launch, interruption, inactive/background/resume, termination and relaunch, saved edits, restored destination and protected snapshot |
| Networking | Offline launch, slow or failed request, HTTP/decoding failure, stale cache, cancellation, uncertain write and safe retry |
| Privacy and accounts | Fresh-install prompt, refusal, limited/revoked access, locked device, sign-out/recovery, deletion where supported |
| System entry points | Notification action, deep link, widget/Live Activity, or intent opens or performs the intended task from cold and warm states |
| Background work | Completion, expiration, user cancellation, unavailable execution, recovery on next foreground launch |
| Purchases if present | Verified entitlement, pending/canceled purchase, restoration, refund/revocation using StoreKit testing and the appropriate sandbox |

Use previews for fast layout iteration, simulator/UI tests for repeatable flows,
and physical iPhones for affected hardware, biometrics, camera/sensors, real push
delivery, energy, thermal behavior, and system scheduling. Developer-triggered
background launches prove handler behavior, not normal scheduling or delivery.

## Performance and reliability

Follow [Improving your app's performance](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance):
measure a representative flow, locate the bottleneck, change one relevant cause,
and repeat the measurement. Use Instruments and Xcode diagnostics for launch,
responsiveness, memory/leaks, disk, networking, and energy as needed. Compare
equivalent builds, devices, datasets, and conditions; simulator timing does not
establish physical-device performance.

For shipping apps, inspect Xcode Organizer crashes and performance trends and
use [MetricKit](https://developer.apple.com/documentation/metrickit) when appropriate.
Select APIs for the supported OS; newer asynchronous reporting APIs and older
subscriber APIs have different availability. Preserve matching archives and
symbols for actionable crash reports, and avoid collecting sensitive payloads.

## Releases and ongoing maintenance

- Test fresh installation and upgrades, the oldest supported OS and the current
  shipping OS. Exercise betas separately to find upcoming changes. Recheck OS/SDK
  release notes and deprecations after toolchain or dependency updates.
- Inspect a release archive's signing, provisioning, entitlements, embedded
  extensions, resources, icons, versions, and privacy declarations. A successful
  unsigned build does not establish installability or valid distribution signing.
- Recheck [submission guidance](https://developer.apple.com/app-store/submitting/)
  and [upcoming requirements](https://developer.apple.com/news/upcoming-requirements/).
  SDK upload requirements and the deployment minimum are different constraints;
  do not encode a moving submission deadline as a permanent rule.
- Use [TestFlight](https://developer.apple.com/testflight/) for authorized beta
  feedback. Prepare accurate metadata, privacy and accessibility disclosures, and
  review access as applicable. Uploading, inviting testers, submitting, and
  releasing remain separate actions within the user's authorization.
- After release, use crash reports, feedback, and measured regressions to choose
  maintenance work. Report reproducible platform issues through
  [Feedback Assistant](https://developer.apple.com/feedback-assistant/) with OS/build
  versions, reproduction steps, and sanitized diagnostics.

At handoff, distinguish source-backed expectations from observed build, test,
simulator, and device results. Name unavailable checks and remaining risks without
claiming broader runtime or release conformance.
