%define name    misdn2
%define version 1.5
%define libname %mklibname %{name}
%define snap    20090602
%define release %mkrel %{snap}.1
%define	epoch	2
%define	name_old	misdn
%define	libname_old	%mklibname %{name_old}

Summary:	Modular ISDN (mISDN) version 2
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		System/Libraries
License:	GPL
URL:		http://www.misdn.org/index.php/Main_Page
Source0:	http://www.linux-call-router.de/download/lcr-%{version}/mISDNuser_%{snap}.tar.gz
Provides:	%{name_old} = %{epoch}:%{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Epoch:		%{epoch}

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
Provides:	%{libname_old} = %{epoch}:%{version}-%{release}

%description -n	%{libname}
Modular ISDN (mISDN) is the new ISDN stack of the linux kernel
version 2.6.

This package provides the shared mISDN libraries.

%package -n	%{libname}-devel
Summary:	Static library and header files for the mISDN libraries
Group:		Development/C
Provides:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	lib%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	%{libname_old}-devel = %{epoch}:%{version}-%{release}
Provides:	%{name_old}-devel = %{epoch}:%{version}-%{release}
Provides:	lib%{name_old}-devel = %{epoch}:%{version}-%{release}
Requires:	%{libname} = %{epoch}:%{version}-%{release}
Epoch:		%{epoch}

%description -n	%{libname}-devel
Modular ISDN (mISDN) is the new ISDN stack of the linux kernel
version 2.6.

This package provides shared and static libraries and header
files.

%prep

%setup -q -n mISDNuser

# fix strange perms
find . -type f -exec chmod 644 {} \;
find . -type d -exec chmod 755 {} \;

# cvs cleanup
for i in `find . -type d -name CVS` `find . -type d -name .svn` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
	if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

%build
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
LDFLAGS="${LDFLAGS}"  ; export LDFLAGS
%make INSTALL_PREFIX=%{buildroot} INSTALL_LIBDIR=%{_libdir}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall INSTALL_PREFIX=%{buildroot} INSTALL_LIBDIR=%{_libdir}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/mISDNuser/*.*
%{_libdir}/*.a

