%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Matrix
Summary:	Math::Matrix Perl module - Multiply and invert Matrices
Summary(pl):	Modu³ Perla Math::Matrix - mno¿±cy i odwracaj±cy macierze
Name:		perl-Math-Matrix
Version:	0.4
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Matrix - Multiply and invert Matrices.

%description -l pl
Modu³ Math::Matrix - mno¿±cy i odwracaj±cy macierze.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/Matrix.pm
%{_mandir}/man3/*
