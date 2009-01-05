%define module   Variable-Magic
%define version    0.26
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Associate magic to variables from Perl
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Variable/%{module}-%{version}.tar.gz
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(XSLoader)
BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Magic is Perl way of enhancing objects. This mechanism let the user add
extra data to any variable and hook syntaxical operations (such as access,
assignation or destruction) that can be applied to it. With this module,
you can add your own magic to any variable without the pain of the C API.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorarch/Variable
%perl_vendorarch/auto/Variable

