%define name	dspam-scripts
%define version	0.0.6
%define release	1mdk

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

