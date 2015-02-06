%define name	dspam-scripts
%define version	0.0.6
%define release	7

Summary:	A script for let dspam learning maildirs of spam/ham
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Mail
URL:		http://www.kalysto.org/utilities/dspam-scripts/index.en.html
Source0:	http://www.kalysto.org/pkg/%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-root
BuildArch:	noarch

%description
This package holds the 'dspam-learn' bash script that will help greatly using
dspam learning by looking at mailbox directories rather than a forwarding
method. This is much as you could have set it with Spamassassin and the
sa-learn.

%prep
%setup

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/mail/
%makeinstall
install -m 644 src/sample/dspam-learn.rc $RPM_BUILD_ROOT%{_sysconfdir}/mail/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README README.en.desc
%doc README.fr.desc THANKS
%{_bindir}/dspam-learn
%config(noreplace) %{_sysconfdir}/mail/dspam-learn.rc



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.6-6mdv2011.0
+ Revision: 617902
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.0.6-5mdv2010.0
+ Revision: 428384
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.0.6-4mdv2009.0
+ Revision: 244551
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.0.6-2mdv2008.1
+ Revision: 140722
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 0.0.6-2mdv2008.0
+ Revision: 70206
- use %%mkrel


* Thu Jan 27 2005 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.0.6-1mdk
- Initial release.

