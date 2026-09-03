# Evals

The configuration in the plugin steers the agent, so it
deserves the regression testing that code gets. This suite runs whenever
that configuration changes, and on a nightly schedule.

## Building the suite

Collect 20 to 50 real tasks from recent work, each with its accepted
outcome. Write each as a JSON file: the prompt, plus the checks that
define acceptable — tests pass, lint clean, behaviour unchanged, policy
followed.

Every production incident earns an eval, written by the team that owned
the incident. It stays in the suite as a regression test.

## Keeping it live

Treat this as a living suite. As models improve, cases that once
discriminated stop doing so. Retire them and add new ones from what
monitoring surfaces.

Gate configuration changes on the results: a skill change that drops the
pass rate gets reviewed before it merges.
