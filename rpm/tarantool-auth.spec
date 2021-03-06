Name: tarantool-auth
Version: 0.1.0
Release: 1
Summary: Tarantool auth module
Group: Applications/Databases
License: BSD

URL: https://github.com/LinnikD/tarantool-auth
Source0: https://github.com/LinnikD/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch
Requires: tarantool >= 1.7.0
Requires: tarantool-curl >= 2.2.7

%description
auth lib for tarantool


%prep
%setup -q -n %{name}-%{version}

%define luapkgdir %{_datadir}/tarantool/auth

%install
rm -rf %{buildroot}/%{name}-%{version}

%{__mkdir_p} %{buildroot}/%{luapkgdir}/
cp -pR %{_builddir}/%{name}-%{version}/auth/* %{buildroot}/%{luapkgdir}/
cp -pR %{_builddir}/%{name}-%{version}/README.md %{buildroot}/%{luapkgdir}/README.md


%clean
rm -rf %{buildroot}


%files
%dir %{luapkgdir}
%dir %{luapkgdir}/model
%dir %{luapkgdir}/utils
%{luapkgdir}/*.lua
%{luapkgdir}/model/*.lua
%{luapkgdir}/utils/*.lua
%doc %{luapkgdir}/README.md
