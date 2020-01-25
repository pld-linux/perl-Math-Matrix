#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Math
%define		pnam	Matrix
Summary:	Math::Matrix Perl module - multiply and invert matrices
Summary(pl.UTF-8):	Moduł Perla Math::Matrix - mnożenie i odwracanie macierzy
Name:		perl-Math-Matrix
Version:	0.5
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	840a9ef812ad12bd1798752f1e90cf41
URL:		http://search.cpan.org/dist/Math-Matrix/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Matrix - Multiply and invert Matrices.

%description -l pl.UTF-8
Moduł Math::Matrix - mnożący i odwracający macierze.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Math/Matrix.pm
%{_mandir}/man3/*
