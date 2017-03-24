Name: example
Version:1.0
Release : 1%{?dist}
Summary: For demonstrating the rpm creation process.
Group: Application/Sysem
Source0: %{name}-%{unmangles_version}.tar.gz
Requires:python

%prep
rm -rf %{buildroot}/*
%setup -n %{name} -n %{name}

%build
python -m compileall .

%install
mkdir -p %{buildroot}/usr/share/example/static/
mv %{_builddir}/%{name}/example %{buildroot}/usr/bin/example/
mv %{_builddir}/%{name}/*.pyc   %{buildroot}/usr/share/example/
mv %{_builddir}/%{name}/static %{buildroot}/usr/share/example/static
mv %{_builddir}/%{name}/dependencies %{buildroot}/usr/share/example/

%files
%attr(700, -, -)/usr/share/example/*
%attr(644,-,-)/usr/bin/example

%clean
rm -rf %{buildroot}
