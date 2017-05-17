%global gitcommit_full a15e53d8bd2cce479093844a79fdbaa155cd2d08
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})

Name:           rutracker-proxy
Version:        0.1
Release:        0.1.git%{gitcommit}%{?dist}
Summary:        Proxy for rutracker

License:        GPLv3+
URL:            https://github.com/zhulik/rutracker-proxy
Source0:        https://github.com/zhulik/rutracker-proxy/tarball/%{gitcommit_full}
Source1:        %{name}.service

BuildRequires:  golang
BuildRequires:  go-compilers-golang-compiler
BuildRequires:  pkgconfig(systemd)

ExclusiveArch:  %{go_arches}

%description
Tool for proxying client's announces to blocked tracker servers.

%prep
%autosetup -n zhulik-%{name}-%{gitcommit}


%build
go get github.com/elazarl/goproxy
go get github.com/zhulik/rutracker-proxy/selector
%gobuild


%install
install -p -D -m 755 zhulik-%{name}-%{gitcommit} %{buildroot}%{_bindir}/%{name}
install -p -D -m 644 %{SOURCE1}  %{buildroot}%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%{_bindir}/%{name}
%{_unitdir}/%{name}.service


%changelog
* Tue May 16 2017 vascom <vascom2@gmail.com> - 0.1-0.1.gita15e53d
- Initial packaging
