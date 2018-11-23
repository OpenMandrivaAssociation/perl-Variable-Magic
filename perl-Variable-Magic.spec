%define upstream_name    Variable-Magic
%define upstream_version 0.62

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Associate magic to variables from Perl
Url:		http://metacpan.org/pod/Variable::Magic
Source0:	http://www.cpan.org/modules/by-module/Variable/Variable-Magic-%{upstream_version}.tar.gz

BuildRequires:	perl(Carp)
BuildRequires:	perl(Config)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(XSLoader)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
Magic is Perl's way of enhancing objects. This mechanism lets the user add
extra data to any variable and hook syntactical operations (such as access,
assignation or destruction) that can be applied to it. With this module,
you can add your own magic to any variable without the pain of the C API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorarch}/Variable
%{perl_vendorarch}/auto/Variable
