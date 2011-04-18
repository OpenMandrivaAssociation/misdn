%define libname %mklibname misdn %{epoch}

Summary:	Modular ISDN (mISDN) version 2
Name:		misdn
Version:	2
Release:	20110416.2
Epoch:		2
Group:		System/Libraries
License:	GPL
URL:		http://www.misdn.org/index.php/Main_Page
Source0:	http://www.colognechip.com/download/mISDN/socket/mISDNuser.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Provides:	misdn2
Provides:	mISDNuser
Provides:	mISDN2user

%description
mISDN supports a complete BRI and PRI ETSI compliant DSS1 protocol stack for
the TE mode and for the NT mode. It is the successor of the "old" isdn4linux
subsystem, in particular its "HiSax" family of drivers. It has growing
support for the interface cards of hisax and additionally supports
the cool HFCmulti chip based cards

%package -n	%{libname}
Summary:	Modular ISDN (mISDN) libraries
Group:		System/Libraries
Epoch:		%{epoch}
Provides:	%{_lib}mISDN
Provides:	%{_lib}mISDN2user
Provides:	%{_lib}misdn
Provides:	%{_lib}misdn0
Provides:	%{_lib}misdn2

%description -n	%{libname}
Modular ISDN (mISDN) is the new ISDN stack of the linux kernel
version 2.6.

This package provides the shared mISDN libraries.

%package -n	%{libname}-devel
Summary:	Static library and header files for the mISDN libraries
Group:		Development/C
Provides:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	lib%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	%{libname} = %{epoch}:%{version}-%{release}
Epoch:		%{epoch}
Provides:	%{_lib}mISDN-devel
Provides:	%{_lib}mISDN2user-devel
Provides:	%{_lib}misdn-devel
Provides:	%{_lib}misdn0-devel
Provides:	%{_lib}misdn2-devel

%description -n	%{libname}-devel
Modular ISDN (mISDN) is the new ISDN stack of the linux kernel
version 2.6.

This package provides shared and static libraries and header
files.

%package gui
License:	GPLv2
Summary:	Qt application to watch the status of mISDN cards
Group:		Monitoring
BuildRequires:	libqt4-devel

%description gui
This subpackage contain a little Qt tool for watching the status of
ISDN cards.

%prep

%setup -q -n mISDNuser

# cvs cleanup
for i in `find . -type d -name CVS` `find . -type d -name .svn` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
	if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

%build

%configure2_5x --enable-gui
%make

%install

rm -rf %{buildroot}
%makeinstall INSTALL_PREFIX=%{buildroot} INSTALL_LIBDIR=%{_libdir}

%clean

rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/misdn*
%{_bindir}/l1oipctrl
%{_sbindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/mISDN/*.*
%{_libdir}/*.la
%{_libdir}/*.a

%files gui
%defattr(-,root,root)
%{_bindir}/qmisdnwatch

