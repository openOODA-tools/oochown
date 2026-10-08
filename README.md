# oochown: Sovereign OWNERSHIP MANAGER

<div align="center">

```
================================================================================
                                oochown
               Sovereign openOODA OWNERSHIP MANAGER
================================================================================
```

**Sovereign OWNERSHIP MANAGER**  
*Changes user and group ownership of filesystem objects with systemd-tmpfiles synthesis.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oochown/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oochown-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oochown/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oochown/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oochown-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oochown/uninstall.sh | bash
```

---

## 2. CLI Usage

```
oochown 0.2.0 (openOODA sovereign files & navigation)
usage: oochown [OPTION]... [OWNER][:[GROUP]] FILE...
  or:  oochown [OPTION]... --reference=RFILE FILE...

Change the owner and/or group of each FILE to OWNER and/or GROUP.

Options:
  -c, --changes          like verbose but report only when a change is made
  -f, --silent, --quiet  suppress most error messages
  -v, --verbose          output a diagnostic for every file processed
  -R, --recursive        operate on files and directories recursively
      --reference=RFILE  use RFILE's owner and group rather than specifying values
      --dry-run          simulate ownership changes without modifying disk
      --tmpfiles         synthesize declarative systemd-tmpfiles rules
      --demo             run demonstration scenarios with synthetic fixtures
      --json             output formatted as JSON Lines
  -h, --help             display this help and exit
  -V, --version          output version information and exit
      --mcp              run as Model Context Protocol stdio server
```

---

## 3. Declarative systemd-tmpfiles Synthesis

Following pure systemd-native server architecture, `oochown` emits declarative rules for `/etc/tmpfiles.d/*.conf`:

```bash
# Generate declarative non-recursive (z) and recursive (Z) rules:
oochown --tmpfiles www-data:www-data /var/www/html
oochown --tmpfiles -R staff:staff /srv/shared
```

Output:
```ini
# /etc/tmpfiles.d/oochown.conf - declarative ownership rules
# Type Path Mode UID GID Age Argument
z /var/www/html - www-data www-data - -
Z /srv/shared - staff staff - -
```

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oochown` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

```bash
oochown --mcp
```

### Registered Tools
* **`chown_resolve`**: Resolve user and group specification against `/etc/passwd` and `/etc/group`.
* **`chown_inspect`**: Inspect filesystem path owner, group, UID, and GID.
* **`chown_plan`**: Plan ownership change for path without disk modification.
* **`chown_tmpfiles`**: Synthesize declarative systemd-tmpfiles rule for path.
* **`chown_audit`**: Audit path ownership against expected user and group requirements.

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
