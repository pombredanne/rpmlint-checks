Name:		usr-bad
Version:	0
Release:	0
Group:		Foo
Summary:	Bar
License:	GPL
BuildRoot:	%_tmppath/%name-%version-build

%description
%_target
%_target_cpu

%install
install -D -m 644 /etc/motd %buildroot/usr/qvm/test

%clean
rm -rf %buildroot

%files
/usr/*
