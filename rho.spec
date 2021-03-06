%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name: rho
Version: 0.0.20
Release: 1%{?dist}
Summary: An SSH system profiler

Group: Applications/Internet
License: GPLv2
URL: http://github.com/jmrodri/rho
Source0: http://alikins.fedorapeople.org/files/rho/rho-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-setuptools
Requires: python-paramiko
Requires: python-netaddr
Requires: python-simplejson
Requires: python-crypto

%description
Rho is a tool for scanning your network, logging into systems via SSH, and
retrieving information about them.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT
install -D -p -m 644 doc/rho.1 $RPM_BUILD_ROOT%{_mandir}/man1/rho.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README AUTHORS COPYING
%{_bindir}/rho
%{python_sitelib}/*
%{_mandir}/man1/rho.1.gz

%changelog
* Wed Nov 18 2009 Adrian Likins <alikins@redhat.com> 0.0.20-1
- RHEL5 is using an even older version of python-netaddr that requires most API
  transmogrifying. Namely, lack of netaddr.IP class. (alikins@redhat.com)

* Fri Nov 13 2009 Adrian Likins <alikins@redhat.com> 0.0.19-1
- Merge Fedora Package review spec changes from Mark McLoughlin
  <markmc@redhat.com> (markmc@redhat.com)
- Add the config file version to the begining of the encrypted config file as
  well (alikins@redhat.com)
- Change the AES ciper mode of CFB and store/retrive a 16bit initialization
  vector for use with CFB. (alikins@redhat.com)
- Use a different salt each time we say the file. (alikins@redhat.com)

* Fri Nov 13 2009 Mark McLoughlin <markmc@redhat.com> - 0.0.16-2
- Include egg info
- Drop the -O1 arg from 'setup.py install'
- Don't chdir for manpage install
- Kill some whitespace

* Wed Nov 11 2009 Adrian Likins <alikins@redhat.com> 0.0.16-1
- Add a RhoCmd class for detecting if we are a virt guest or host
  (alikins@redhat.com)

* Wed Nov 04 2009 Adrian Likins <alikins@redhat.com> 0.0.15-1
- add bits generated to .gitignore (shut up git) (alikins@redhat.com)
- Don't use weird style of classes on 2.4, use Class(object)
  (alikins@redhat.com)
- A few more tweaks to make Queue24 work the same way as the Queue.Queue in
  2.6. (alikins@redhat.com)
- On python2.4 (aka, rhel5) Queue.Queue doesn't have the .join or .task_done
  methods, which we use and like. So check for them and if they aren't there,
  use our own implementation (pretty much c&p from the 2.6 version of
  Queue.Queue). A little ugly, but alas. (alikins@redhat.com)
- use new style classes, python2.4 doesn't like class FOO()
  (alikins@redhat.com)

* Tue Nov 03 2009 Adrian Likins <alikins@redhat.com> 0.0.13-1
- Fix a bug where we weren't actually consuming the Queue if there weren't as
  many or more threads than hosts. (alikins@redhat.com)
- remove --debug option, it doesn't do anything (alikins@redhat.com)

* Sat Oct 31 2009 Devan Goodwin <dgoodwin@rm-rf.ca> 0.0.11-1
- Support Netaddr > 0.7 (jbowes@repl.ca)
- add a DmiRhoCmd. Grab some basic DMI info. (alikins@redhat.com)
- fix wrong help in "rho profile show" (profile, not auth)
  (alikins@redhat.com)

* Thu Oct 29 2009 Adrian Likins <alikins@redhat.com> 0.0.10-1
- add SourceURL
- remove ssh_queue.py
- fix man page install

* Wed Oct 28 2009 Devan Goodwin <dgoodwin@redhat.com> 0.0.6-1
- Fix "rho scan nosuchprofile". (dgoodwin@redhat.com)
- Update README. (dlackey@redhat.com)

* Tue Oct 27 2009 Devan Goodwin <dgoodwin@redhat.com> 0.0.5-1
- Too many features/bugfixes to list. Approaching first release.
* Wed Oct 21 2009 Devan Goodwin <dgoodwin@redhat.com> 0.0.2-1
- Beginning to get usable.
* Thu Oct 15 2009 Devan Goodwin <dgoodwin@redhat.com> 0.0.1-1
- Initial packaging.
