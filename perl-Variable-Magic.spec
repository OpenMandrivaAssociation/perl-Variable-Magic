%define upstream_name    Variable-Magic
%define upstream_version 0.53

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Associate magic to variables from Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Variable/Variable-Magic-%{upstream_version}.tar.gz

BuildRequires:	perl(Carp)
BuildRequires:	perl(Config)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(XSLoader)
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

%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.460.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.460.0-1
+ Revision: 635558
- update to new version 0.46

* Sun Nov 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.450.0-1mdv2011.0
+ Revision: 602394
- update to new version 0.45

* Sat Nov 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.440.0-1mdv2011.0
+ Revision: 594312
- update to new version 0.44

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.430.0-2mdv2011.0
+ Revision: 555212
- rebuild

* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.430.0-1mdv2011.0
+ Revision: 551203
- update to 0.43

* Tue Mar 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.410.0-1mdv2010.1
+ Revision: 521648
- update to 0.41

  + Shlomi Fish <shlomif@mandriva.org>
    - Fixed some typos in the description.

* Thu Jan 07 2010 Jérôme Quelin <jquelin@mandriva.org> 0.400.0-1mdv2010.1
+ Revision: 487051
- update to 0.40

* Tue Dec 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.390.0-1mdv2010.1
+ Revision: 472249
- update to 0.39

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.380.0-1mdv2010.1
+ Revision: 460776
- update to 0.38

* Wed Aug 26 2009 Jérôme Quelin <jquelin@mandriva.org> 0.370.0-1mdv2010.0
+ Revision: 421390
- update to 0.37

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.360.0-1mdv2010.0
+ Revision: 401920
- rebuild using %%perl_convert_version

* Mon Jul 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdv2010.0
+ Revision: 393003
- update to new version 0.36

* Sun May 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.35-1mdv2010.0
+ Revision: 376726
- update to new version 0.35

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdv2010.0
+ Revision: 370245
- update to new version 0.34

* Mon Mar 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.32-1mdv2009.1
+ Revision: 346934
- update to new version 0.32

* Fri Feb 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-1mdv2009.1
+ Revision: 343198
- update to new version 0.31

* Fri Feb 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.30-1mdv2009.1
+ Revision: 340031
- update to new version 0.30

* Mon Feb 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.29-1mdv2009.1
+ Revision: 338672
- update to new version 0.29

* Sun Jan 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.28-1mdv2009.1
+ Revision: 333404
- update to new version 0.28

* Tue Jan 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.27-1mdv2009.1
+ Revision: 331595
- update to new version 0.27
- update to new version 0.27

* Mon Jan 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.26-1mdv2009.1
+ Revision: 324970
- import perl-Variable-Magic


* Mon Jan 05 2009 cpan2dist 0.26-1mdv
- initial mdv release, generated with cpan2dist


