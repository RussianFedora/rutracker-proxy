%global gitcommit_full a15e53d8bd2cce479093844a79fdbaa155cd2d08
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})

Name:           rutracker-proxy
Version:        0.1
Release:        0.1.git%{gitcommit}%{?dist}
Summary:        Proxy for rutracker

License:        MIT
URL:            https://github.com/zhulik/rutracker-proxy
Source0:        https://github.com/zhulik/rutracker-proxy/tarball/%{gitcommit_full}
Source1:        %{name}.service
Source2:        https://github.com/elazarl/goproxy/tarball/master
Source3:        net.tar.gz

BuildRequires:  golang
BuildRequires:  go-compilers-golang-compiler
BuildRequires:  pkgconfig(systemd)

ExclusiveArch:  %{go_arches}

%description
Tool for proxying client's announces to blocked tracker servers.

%prep
%autosetup -n zhulik-%{name}-%{gitcommit}
mkdir -p src/github.com/zhulik/rutracker-proxy
mv selector src/github.com/zhulik/rutracker-proxy/

mkdir -p src/github.com/elazarl
tar -xvf %{SOURCE2}
mv elazarl-goproxy* src/github.com/elazarl/goproxy

mkdir -p src/golang.org/x/
tar -xvf %{SOURCE3} -C src/golang.org/x/

%build
export GOPATH=$(pwd):%{gopath}
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
