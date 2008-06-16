%define	snap 20061023

%define	major 0
%define libname	%mklibname misdn %{major}

Summary:	Modular ISDN (mISDN) libraries
Name:		misdn
Version:	3.4
Release:	%mkrel 0.%{snap}.3
Group:		System/Libraries
License:	GPL
URL:		http://isdn.jolly.de/
Source0:	mISDNuser-%{snap}.tar.bz2
Source1:	mISDN.tar.bz2
# Build shared libraries, use optflags:
Patch0:		mISDNuser-shared.diff
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Modular ISDN (mISDN) is the new ISDN stack of the linux kernel
version 2.6.

This package provides shared and static libraries as well as 
various header files.

%package -n	%{libname}
Summary:	Modular ISDN (mISDN) libraries
Group:          System/Libraries
Epoch:		%{epoch}

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

%description -n	%{libname}-devel
Modular ISDN (mISDN) is the new ISDN stack of the linux kernel
version 2.6.

This package provides shared and static libraries and header
files.

%prep

%setup -q -n mISDNuser -a1

# fix strange perms
find . -type f -exec chmod 644 {} \;
find . -type d -exec chmod 755 {} \;

# cvs cleanup
for i in `find . -type d -name CVS` `find . -type d -name .svn` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

%patch0 -p1
    
%build

%make LDFLAGS="%ldflags"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}/mISDNuser

# install static libs
install -m0644 i4lnet/libisdnnet.a %{buildroot}%{_libdir}/
install -m0644 lib/libmISDN.a %{buildroot}%{_libdir}/
install -m0644 suppserv/libsuppserv.a %{buildroot}%{_libdir}/
install -m0644 tenovis/lib/libtenovis.a %{buildroot}%{_libdir}/

install -m0644 i4lnet/libisdnnet_pic.a %{buildroot}%{_libdir}/
install -m0644 lib/libmISDN_pic.a %{buildroot}%{_libdir}/
install -m0644 suppserv/libsuppserv_pic.a %{buildroot}%{_libdir}/

# install shared libs
install -m0755 i4lnet/libisdnnet.so.%{major} %{buildroot}%{_libdir}/
install -m0755 lib/libmISDN.so.%{major} %{buildroot}%{_libdir}/
install -m0755 suppserv/libsuppserv.so.%{major} %{buildroot}%{_libdir}/
install -m0755 tenovis/lib/libtenovis.so.%{major} %{buildroot}%{_libdir}/

# make some softlinks
ln -s libisdnnet.so.%{major} %{buildroot}%{_libdir}/libisdnnet.so
ln -s libmISDN.so.%{major} %{buildroot}%{_libdir}/libmISDN.so
ln -s libsuppserv.so.%{major} %{buildroot}%{_libdir}/libsuppserv.so
ln -s libtenovis.so.%{major} %{buildroot}%{_libdir}/libtenovis.so

# install headers
install -m0644 i4lnet/*.h %{buildroot}%{_includedir}/mISDNuser/
install -m0644 include/*.h %{buildroot}%{_includedir}/mISDNuser/
install -m0644 tenovis/lib/*.h %{buildroot}%{_includedir}/mISDNuser/
install -m0644 suppserv/*.h %{buildroot}%{_includedir}/mISDNuser/

# hack the headers...
pushd %{buildroot}%{_includedir}/mISDNuser
    for h in *.h; do
	perl -pi -e "s|\"${h}\"|\<mISDNuser/${h}\>|g" *.h
    done
    perl -pi -e "s|\<mISDNif.h\>|\<mISDNuser/mISDNif.h\>|g" mISDNlib.h
popd

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING.LIB LICENSE
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%dir %{_includedir}/mISDNuser
%{_includedir}/mISDNuser/*.h
%{_libdir}/*.so
%{_libdir}/*.a


