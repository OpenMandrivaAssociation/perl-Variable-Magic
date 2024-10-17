%define upstream_name    Variable-Magic
%define upstream_version 0.62
%ifarch %{x86_64}
# FIXME bug
%global _debugsource_template %{nil}
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	10

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Associate magic to variables from Perl
Url:		https://metacpan.org/pod/Variable::Magic
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
%make_build

%install
%make_install

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorarch}/Variable
%{perl_vendorarch}/auto/Variable
