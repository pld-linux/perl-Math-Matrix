%include	/usr/lib/rpm/macros.perl
Summary:	Math-Matrix perl module
Summary(pl):	Modu³ perla Math-Matrix
Name:		perl-Math-Matrix
Version:	0.2
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/Math-Matrix-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math-Matrix perl module.

%description -l pl
Modu³ perla Math-Matrix.

%prep
%setup -q -n Math-Matrix-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT


gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Math/Matrix.pm
%{perl_sitearch}/auto/Math/Matrix

%{_mandir}/man3/*
