# Change Log
All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).


## v2.0.3 - 2026-09-18
### What's Changed
#### 🐛 Bug Fixes
* `.github/workflows`: move the reusable workflows to `obervinov/_templates@v4.0.0`. Node 20 is removed from the Actions runner on 2026-09-23, and the pinned templates still called `actions/create-release` (`runs.using: node12`, archived) along with a set of `node20` actions — releases and checks in this repository would stop running.
#### 📚 Documentation
* `README.md`: fix the unbalanced quote that made the pasted `pyproject.toml` invalid, and unpin the last icon still on `_templates@v1.0.5`.
* `README.md`: replace the hand-maintained GitHub Actions Templates table with a badge that reads the pinned version out of `.github/workflows/pr.yaml` — the table went stale on every template bump because nothing kept it in sync.


## v2.0.2 - 2025-12-23
### What's Changed
**full changelog**: https://github.com/obervinov/messages-package/compare/v2.0.1..v2.0.2 by @obervinov https://github.com/obervinov/messages-package/pull/32
#### 🚀 Features
* upgrade dependencies to latest versions
* fix codeql warnings


## v2.0.1 - 2025-07-10
### What's Changed
**full changelog**: https://github.com/obervinov/messages-package/compare/v2.0.0..v2.0.1 by @obervinov https://github.com/obervinov/messages-package/pull/28
#### 🚀 Features
* Bump workflows to `v2.1.1`
* Bump dependencies to latest versions


## v2.0.0 - 2024-10-11
### What's Changed
**full changelog**: https://github.com/obervinov/messages-package/compare/v1.0.4..v2.0.0 by @obervinov https://github.com/obervinov/messages-package/pull/27
#### 💥 Breaking Changes
* Bump python version to `3.12`
#### 📚 Bug Fixes
* [Fix invalid default path to messages.json ](https://github.com/obervinov/messages-package/issues/25)
#### 🚀 Features
* Bump workflows to `v2.0.0`
* [Add additional exceptions for more informative errors](https://github.com/obervinov/messages-package/issues/26)


## v1.0.4 - 2024-02-04
### What's Changed
**full changelog**: https://github.com/obervinov/messages-package/compare/v1.0.3...v1.0.4 by @obervinov https://github.com/obervinov/messages-package/pull/24
#### 📚 Bug Fixes
* [List all supported versions of python](https://github.com/obervinov/messages-package/issues/23)
* [Soft handling of situations where a configuration file or alias does not exist](https://github.com/obervinov/messages-package/issues/22)


## v1.0.3 - 2024-01-29
### What's Changed
**full changelog**: https://github.com/obervinov/messages-package/compare/v1.0.2...v1.0.3 by @obervinov https://github.com/obervinov/messages-package/pull/21
#### 📚 Documentation
* [Fix typos in README.md](https://github.com/obervinov/messages-package/issues/20)


## v1.0.2 - 2024-01-24
### What's Changed
**full changelog**: https://github.com/obervinov/messages-package/compare/v1.0.1...v1.0.2 by @obervinov https://github.com/obervinov/messages-package/pull/19
#### 🐛 Bug Fixes
* fixed import of main code via `__init__.py`


## v1.0.1 - 2024-01-20
### What's Changed
**full changelog**: https://github.com/obervinov/messages-package/compare/v1.0.0...v1.0.1 by @obervinov https://github.com/obervinov/messages-package/pull/17
#### 🐛 Bug Fixes
* [Update Test](https://github.com/obervinov/messages-package/issues/6)
* [Update GitHub Actions workflow](https://github.com/obervinov/messages-package/issues/7)
#### 📚 Documentation
* [Update PR template](https://github.com/obervinov/messages-package/issues/10)
* [Update README.md](https://github.com/obervinov/messages-package/issues/4)
#### 💥 Breaking Changes
* [Migration from pip to poetry](https://github.com/obervinov/messages-package/issues/3)
#### 🚀 Features
* [Update GitHub Actions workflow](https://github.com/obervinov/messages-package/issues/7)
* [Add support for the environment variable `MESSAGES_CONFIG`](https://github.com/obervinov/messages-package/issues/15)


## v1.0.0 - 2023-03-15
### What's Changed
**Full Changelog**: https://github.com/obervinov/messages-package/commits/v1.0.0
#### 💥 Breaking Changes
* **Module release**
