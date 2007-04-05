Name:		pciutils
Version:	2.2.4
Release: 	3%{?dist}
Source:		ftp://atrey.karlin.mff.cuni.cz/pub/linux/pci/%{name}-%{version}.tar.gz
Patch0:		pciutils-strip.patch
Patch1: 	pciutils-2.2.4-buf.patch
Patch2:		pciutils-2.1.10-scan.patch
Patch3: 	pciutils-havepread.patch
Patch6: 	pciutils-2.2.1-idpath.patch
Patch7:		pciutils-2.1.99-gcc4.patch
Patch8: 	pciutils-2.2.4-multilib.patch
License:	GPL
URL:		http://atrey.karlin.mff.cuni.cz/~mj/pciutils.shtml
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExclusiveOS: 	Linux
Requires:	hwdata
BuildRequires:	zlib-devel
Summary: PCI bus related utilities
Group: Applications/System

%description
The pciutils package contains various utilities for inspecting and
setting devices connected to the PCI bus. The utilities provided
require kernel version 2.1.82 or newer (which support the
/proc/bus/pci interface).

%package devel
Summary: Linux PCI development library
Group: Development/Libraries
Requires: zlib-devel

%description devel
This package contains a library for inspecting and setting
devices connected to the PCI bus.

%prep
%setup -q -n pciutils-%{version}
%patch0 -p1 -b .strip
%patch1 -p1 -b .buf
%patch2 -p1 -b .scan
%patch3 -p1 -b .pread
%patch6 -p1 -b .idpath
%patch7 -p1 -b .glibcmacros
%patch8 -p1 -b .multilib

%build
make OPT="$RPM_OPT_FLAGS -D_GNU_SOURCE=1" PREFIX="/usr" IDSDIR="/usr/share/hwdata"  %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{sbin,%{_mandir}/man8,%{_libdir},%{_includedir}/pci}

install lspci setpci update-pciids $RPM_BUILD_ROOT/sbin
install lspci.8 setpci.8 update-pciids.8 $RPM_BUILD_ROOT%{_mandir}/man8
install lib/libpci.a $RPM_BUILD_ROOT%{_libdir}
install lib/pci.h $RPM_BUILD_ROOT%{_includedir}/pci
install lib/header.h $RPM_BUILD_ROOT%{_includedir}/pci
install lib/config.h $RPM_BUILD_ROOT%{_includedir}/pci
install lib/types.h $RPM_BUILD_ROOT%{_includedir}/pci

%files
%defattr(0644, root, root, 0755)
%{_mandir}/man8/*
%attr(0755, root, root) /sbin/*
%doc README ChangeLog pciutils.lsm

%files devel
%defattr(0644, root, root, 0755)
%{_libdir}/libpci.a
%{_includedir}/pci

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Apr  5 2007 Peter Jones <pjones@redhat.com> - 2.2.4-3
- buildreq zlib-devel, so we know configure will find it consistently.

* Mon Apr  2 2007 Harald Hoyer <harald@redhat.com> - 2.2.4-2
- added alpha to multilib patch (#231790)
- specfile cleanup
- Resolves: rhbz#231790

* Fri Jan 26 2007 Harald Hoyer <harald@redhat.com> - 2.2.4-1
- version 2.2.4
- truncate long device names (#205948)
- Resolves: rhbz#205948

* Wed Aug  9 2006 Peter Jones <pjones@redhat.com> - 2.2.3-4
- Add definitions for more pci storage classes

* Mon Jul 17 2006 Jesse Keating <jkeating@redhat.com> - 2.2.3-3
- rebuild

* Fri Jun 02 2006 Harald Hoyer <harald@redhat.com> 2.2.3-2
- corrected multilib patch

* Tue May 23 2006 Harald Hoyer <harald@redhat.com> 2.2.3-1
- version 2.2.3
- multilib patch (bug #192743)

* Thu Feb 23 2006 Harald Hoyer <harald@redhat.com> 2.2.1-2
- added update-pciids shell script and manpage (bz #178582)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.2.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.2.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Dec 13 2005 Bill Nottingham <notting@redhat.com> - 2.2.1-1
- update to 2.2.1, adjust patches

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu May 19 2005 Bill Nottingham <notting@redhat.com> - 2.1.99.test8-10
- allow 64-bit addresses on x86_64 (#158217, <Matt_Domsch@dell.com>)

* Tue May 10 2005 Bill Nottingham <notting@redhat.com> - 2.1.99.test8-9
- fix debuginfo generation

* Mon Mar 14 2005 Bill Nottingham <notting@redhat.com> - 2.1.99.test8-8
- add patch for glibc macros (#151032, <redhat-bugzilla@linuxnetz.de>)

* Wed Mar  2 2005 Bill Nottingham <notting@redhat.com> - 2.1.99.test8-7
- FC4. GCC 4. fore!

* Tue Jan 25 2005 Bill Nottingham <notting@redhat.com> - 2.1.99.test8-6
- remove explicit kernel dep (#146153)

* Fri Jan 21 2005 Bill Nottingham <notting@redhat.com> - 2.1.99.test8-5
- fix domain bug (#138722, #144383)

* Mon Nov 22 2004 Jeremy Katz <katzj@redhat.com> - 2.1.99.test8-4
- don't use dietlibc on x86 anymore

* Thu Sep  2 2004 Bill Nottingham <notting@redhat.com> 2.1.99.test8-3
- change sysfs access for detecting devices who get fixed up in the
  kernel (#115522, #123802)

* Tue Aug 31 2004 Bill Nottingham <notting@redhat.com> 2.1.99.test8-2
- update to test8
- fix headers

* Fri Jul  9 2004 Bill Nottingham <notting@redhat.com> 2.1.99.test7-1
- update to test7
- fix segfault on some x86-64 boxen

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Dec  8 2003 Bill Nottingham <notting@redhat.com> 2.1.11-4
- fix paths for pci.ids, etc. (#111665)

* Tue Nov 25 2003 Bill Nottingham <notting@redhat.com> 2.1.11-3
- remove a few calls to ->error() in the sysfs code

* Fri Nov 21 2003 Jeremy Katz <katzj@redhat.com> 2.1.11-2
- build a diet libpci_loader.a on i386
- always assume pread exists, it does with diet and all vaguely recent glibc

* Fri Nov 21 2003 Bill Nottingham <notting@redhat.com> 2.1.11-1
- update to 2.1.11
- add patch for sysfs & pci domains support (<willy@debian.org>)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 12 2003 Bill Nottingham <notting@redhat.com>
- don't segfault when there's no pci bus (#84146)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 05 2002 Elliot Lee <sopwith@redhat.com> 2.1.10-5
- Add patch4 for ppc64. The basic rule seems to be that on any platform
where it is possible to be running a 64-bit kernel, we need to always 
print out 64-bit addresses.

* Mon Nov  4 2002 Bill Nottingham <notting@redhat.com> 2.1.10-4
- fix dir perms on /usr/include/pci

* Tue Oct 15 2002 Bill Nottingham <notting@redhat.com> 2.1.10-3
- use %%{_libdir}
- own /usr/include/pci
- build library with -fPIC

* Thu Jul  8 2002 Bill Nottingham <notting@redhat.com> 2.1.10-2
- don't build with -fomit-frame-pointer

* Mon Jun 24 2002 Bill Nottingham <notting@redhat.com> 2.1.10-1
- update to 2.1.10

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jun 17 2002 Bill Nottingham <notting@redhat.com> 2.1.9-4
- don't forcibly strip binaries

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Feb 22 2002 Bill Nottingham <notting@redhat.com>
- rebuild

* Wed Jan 30 2002 Bill Nottingham <notting@redhat.com>
- require hwdata now that pci.ids is there

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Dec 30 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- man page is now owned by root

* Wed Oct 17 2001 Bill Nottingham <notting@redhat.com>
- dump all the patches, ship pci.ids direct out of sourceforge CVS

* Wed Sep 26 2001 Bill Nottingham <notting@redhat.com>
- broadcom bcm5820 id (#53592)

* Fri Aug 10 2001 Bill Nottingham <notting@redhat.com>
- more ids

* Tue Jul 17 2001 Bill Nottingham <notting@redhat.com>
- add newline in printf in PCI-X patch (#49277)

* Mon Jul  9 2001 Bill Nottingham <notting@redhat.com>
- update broadcom patch
- add new ids from 2.4.6

* Mon May 28 2001 Bill Nottingham <notting@redhat.com>
- add a couple of e1000 ids

* Thu Mar 22 2001 Bill Nottingham <notting@redhat.com>
- another megaraid id

* Wed Mar 21 2001 Bill Nottingham <notting@redhat.com>
- another megaraid id

* Wed Mar 14 2001 Preston Brown <pbrown@redhat.com>
- LSI SCSI PCI id

* Wed Feb 21 2001 Nalin Dahyabhai <nalin@redhat.com>
- fix formatting problems

* Wed Feb 21 2001 Preston Brown <pbrown@redhat.com>
- add IBM ServeRAID entries

* Tue Feb 20 2001 Preston Brown <pbrown@redhat.com>
- i860 entries.

* Mon Feb 19 2001 Helge Deller <hdeller@redhat.de>
- added various pci ids 

* Fri Feb  2 2001 Bill Nottingham <notting@redhat.com>
- fix mishap in fixing mishap

* Thu Feb  1 2001 Bill Nottingham <notting@redhat.com>
- fix apparent mishap in pci.ids update from kernel (#25520)

* Tue Jan 23 2001 Bill Nottingham <notting@redhat.com>
- pci.ids updates

* Tue Dec 12 2000 Bill Nottingham <notting@redhat.com>
- big pile of pci.ids updates

* Tue Jul 25 2000 Nalin Dahyabhai <nalin@redhat.com>
- clean up patches to not generate badly-formatted files

* Tue Jul 25 2000 Preston Brown <pbrown@redhat.com>
- Vortex fixes laroche originally applied on kudzu moved here.

* Fri Jul 14 2000 Preston Brown <pbrown@redhat.com>
- pci ids for i815, new ati hardware

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jul 11 2000 Bill Nottingham <notting@redhat.com>
- yet more IDs
- PCI-X support from Matt Domsch

* Fri Jul  7 2000 Bill Nottingham <notting@redhat.com>
- some more QLogic ids

* Mon Jun 26 2000 Bill Nottingham <notting@redhat.com>
- more IDs from Dell

* Sat Jun 10 2000 Bill Nottingham <notting@redhat.com>
- update to 2.1.8

* Fri Apr 21 2000 Bill Nottingham <notting@redhat.com>
- update to 2.1.7

* Mon Apr 17 2000 Bill Nottingham <notting@redhat.com>
- update to 2.1.6

* Fri Mar  3 2000 Bill Nottingham <notting@redhat.com>
- add a couple of ids

* Mon Feb 14 2000 Bill Nottingham <notting@redhat.com>
- update to 2.1.5

* Thu Feb  3 2000 Bill Nottingham <notting@redhat.com>
- handle compressed man pages

* Mon Jan 24 2000 Bill Nottingham <notting@redhat.com>
- update to 2.1.4

* Thu Jan 20 2000 Bill Nottingham <notting@redhat.com>
- update to 2.1.3

* Fri Dec 24 1999 Bill Nottingham <notting@redhat.com>
- update to 2.1.2

* Tue Jun 29 1999 Bill Nottingham <notting@redhat.com>
- add -devel package

* Thu May 20 1999 Bill Nottingham <notting@redhat.com>
- update to 2.0

* Mon Apr 19 1999 Jakub Jelinek  <jj@ultra.linux.cz>
- update to 1.99.5
- fix sparc64 operation

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Thu Feb  4 1999 Bill Nottingham <notting@redhat.com>
- initial build
