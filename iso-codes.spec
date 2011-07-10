Name:	iso-codes
Summary:	ISO code lists and translations

Version:	3.16
Release:	2%{?dist}
License:	LGPLv2+
Group:	System Environment/Base
URL:	http://alioth.debian.org/projects/pkg-isocodes/
Source:	ftp://pkg-isocodes.alioth.debian.org/pub/pkg-isocodes/iso-codes-%{version}.tar.bz2
Patch0: iso-codes-3.16-translations.patch
BuildRequires:	gettext >= 0.16
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
# for /usr/share/xml
Requires: xml-common

%description
This package provides the ISO 639 Language code list, the ISO 4217
Currency code list, the ISO 3166 Territory code list, and ISO 3166-2
sub-territory lists, and all their translations in gettext format.

%package devel
Summary:	Files for development using %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
# for /usr/share/pkgconfig
Requires:	pkgconfig

%description devel
This package contains the pkg-config files for development
when building programs that use %{name}.


%prep
%setup -q
%patch0 -p2 -b .translations

%build
%configure
make %{_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT 

%find_lang iso-codes --all-name

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f iso-codes.lang
%defattr(-,root,root,-)
%doc ChangeLog README LICENSE
%dir %{_datadir}/xml/iso-codes
%{_datadir}/xml/iso-codes/*.xml

%files devel
%defattr(-,root,root,-)
%{_datadir}/pkgconfig/iso-codes.pc

%changelog
* Mon Aug 09 2010 Parag Nemade <pnemade AT redhat.com> - 3.16-2
- Resolves:rh#575765-[iso-codes] translations are not updated

* Fri May 07 2010 Parag Nemade <pnemade AT redhat.com> - 3.16-1
- Resolves:rh#575765-[iso-codes] translations are not updated
- Update to 3.16

* Wed Apr 14 2010 Parag Nemade <pnemade AT redhat.com> - 3.15-1
- Resolves:rh#575765-[iso-codes] translations are not updated
- Update to 3.15

* Tue Mar 02 2010 Parag Nemade <pnemade AT redhat.com> - 3.14-1
- Update to 3.14

* Tue Feb 02 2010 Parag Nemade <pnemade AT redhat.com> - 3.13-1
- Update to 3.13

* Tue Jan 12 2010 Parag Nemade <pnemade AT redhat.com> - 3.12.1-1
- Update to 3.12.1

* Wed Dec 02 2009 Parag Nemade <pnemade AT redhat.com> - 3.12-1
- Update to 3.12

* Mon Nov 02 2009 Parag Nemade <pnemade@redhat.com> - 3.11.1-1
- Update to 3.11.1

* Fri Oct 23 2009 Parag Nemade <pnemade@redhat.com> - 3.11-1
- Update to 3.11

* Thu Sep 17 2009 Parag Nemade <pnemade@redhat.com> - 3.10.3-1
- Update to 3.10.3

* Wed Aug 05 2009 Parag Nemade <pnemade@redhat.com> - 3.10.2-1
- Update to 3.10.2

* Tue Aug 04 2009 Parag Nemade <pnemade@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 02 2009 Parag Nemade <pnemade@redhat.com> - 3.10-2
- Upstream stopped providing iso_639.tab file since 3.9 release,
  so remove it from %%files.

* Tue Jun 02 2009 Parag Nemade <pnemade@redhat.com> - 3.10-1
- Update to 3.10

* Mon Apr 27 2009 Christopher Aillon <caillon@redhat.com> - 3.8-1
- Update to 3.8

* Sun Mar 22 2009 Christopher Aillon <caillon@redhat.com> - 3.7-1
- Update to 3.7

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb  2 2009 Christopher Aillon <caillon@redhat.com> - 3.6-1
- Update to 3.6

* Mon Jan  5 2009 Christopher Aillon <caillon@redhat.com> - 3.5.1-1
- Update to 3.5.1

* Tue Dec  9 2008 Christopher Aillon <caillon@redhat.com> - 3.5-1
- Update to 3.5

* Sat Sep 20 2008 Ville Skyttä <ville.skytta at iki.fi> - 3.3-1
- Update to 3.3.
- Address minor issues in merge review (#225918): update %%description,
  don't use %%makeinstall, drop unneeded %%debug_package override, use
  parallel build.

* Wed Jul  2 2008 Christopher Aillon <caillon@redhat.com> - 3.1-1
- Update to 3.1

* Wed May  7 2008 Christopher Aillon <caillon@redhat.com> 2.1-1
- Update to 2.1

* Sun Mar  9 2008 Christopher Aillon <caillon@redhat.com> 2.0-1
- Update to 2.0

* Wed Feb 27 2008 Christopher Aillon <caillon@redhat.com> 1.9-1
- Update to 1.9

* Tue Feb  5 2008 Matthias Clasen <mclasen@redhat.com> 1.8-2
- Bump gettext BR
- Use the smaller .bz2 tarball

* Sat Feb  2 2008 Matthias Clasen <mclasen@redhat.com> 1.8-1
- Update to 1.8

* Sat Dec 29 2007 Christopher Aillon <caillon@redhat.com> 1.7-1
- Update to 1.7

* Tue Dec  4 2007 Christopher Aillon <caillon@redhat.com> 1.6-1
- Update to 1.6

* Fri Oct 26 2007 Christopher Aillon <caillon@redhat.com> 1.5-1
- Update to 1.5

* Wed Sep  5 2007 Christopher Aillon <caillon@redhat.com> 1.4-1
- Update to 1.4

* Wed Aug  8 2007 Matthias Clasen <mclasen@redhat.com> 1.3-1
- Update to 1.3
- Update the license field
- Use %%find_lang for translations
- Don't create debuginfo

* Tue Jul 24 2007 Parag Nemade  <pnemade@redhat.com> 
- Update to 1.2

* Wed Mar  7 2007 Christopher Aillon <caillon@redhat.com> 1.0-1
- Update to 1.0

* Fri Oct 20 2006 Christopher Aillon <caillon@redhat.com> 0.56-1
- Update to 0.56

* Mon Aug 28 2006 Christopher Aillon <caillon@redhat.com> 0.53-1
- Update to 0.53

* Sat Jun 24 2006 Jesse Keating <jkeating@redhat.com> 0.49-2
- Missing BR gettext

* Sun Jan  1 2006 Christopher Aillon <caillon@redhat.com> 0.49-1
- Update to 0.49

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Aug 26 2005 Christopher Aillon <caillon@redhat.com> 0.47-1
- Update to 0.47

* Mon Jun 10 2005 Christopher Aillon <caillon@redhat.com> 0.46-2
- The .pc file should be installed in %%{_datadir} instead of %%{_libdir}
  since this is a noarch package.  64bit platforms will otherwise look in
  the 64bit version of the %%{_libdir} and not find the .pc file and 
  cause them to not find iso-codes

* Fri Jun 10 2005 Christopher Aillon <caillon@redhat.com> 0.46-1
- Initial RPM
