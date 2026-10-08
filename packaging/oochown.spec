Name:           oochown
Version:        0.2.0
Release:        1%{?dist}
Summary:        Changes user and group ownership of filesystem objects within container bounds.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oochown
Source0:        oochown-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oochown is a sovereign, capability-bounded OWNERSHIP MANAGER written
in pure openOODA, featuring zero ambient authority, systemd-tmpfiles declarative
synthesis, and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oochown
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oochown-uninstall

%files
/usr/bin/oochown
/usr/bin/oochown-uninstall

%changelog
* Thu Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevate to pure openOODA implementation with dual CLI and MCP surface
