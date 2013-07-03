#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define	pdir	FCGI
%define	pnam	ProcManager
%include	/usr/lib/rpm/macros.perl
Summary:	FCGI::ProcManager - functions for managing FastCGI applications
Summary(pl.UTF-8):	FCGI::ProcManager - funkcje do zarządzania aplikacjami FastCGI
Name:		perl-FCGI-ProcManager
Version:	0.24
Release:	2
License:	LGPL v2.1
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/FCGI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0aa184b1e5339e0ad92f4c1439406304
URL:		http://search.cpan.org/dist/FCGI-ProcManager/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FCGI::ProcManager is used to serve as a FastCGI process manager. By
re-implementing it in Perl, developers can more finely tune
performance in their web applications, and can take advantage of
copy-on-write semantics prevalent in UNIX kernel process management.
The process manager should be invoked before the caller's request
loop.

%description -l pl.UTF-8
FCGI::ProcManager służy jako zarządca procesów FastCGI. Poprzez
reimplementację tego w Perlu programiści mogą poprawić wydajność ich
aplikacji WWW i wykorzystać zalety semantyki copy-on-write
przeważającej w zarządzaniu procesami w jądrach systemów UNIX.
Zarządca procesów powinien być wywoływany przed pętlą żądań
wywołującego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/%{pdir}/%{pnam}/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/FCGI/ProcManager.pm
%dir %{perl_vendorlib}/FCGI/ProcManager
%{perl_vendorlib}/FCGI/ProcManager/Constrained.pm
%{_mandir}/man3/*
