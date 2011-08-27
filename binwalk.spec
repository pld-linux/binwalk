Summary:	Binary image analyze tool
Name:		binwalk
Version:	0.3.8
Release:	1
License:	MIT
Group:		Applications/Development
Source0:	http://binwalk.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	bc145f8b9abd5e79d5bc3aecdc0ab829
URL:		http://code.google.com/p/binwalk/
BuildRequires:	autoconf >= 2.65
BuildRequires:	curl-devel
BuildRequires:	libmagic-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Binwalk is a tool for searching a given binary image for embedded files
and executable code. Specifically, it is designed for identifying files
and code embedded inside of firmware images. Binwalk uses the libmagic
library, so it is compatible with magic signatures created for the Unix
file utility.

Binwalk also includes a custom magic signature file which contains
improved signatures for files that are commonly found in firmware
images such as compressed/archived files, firmware headers, Linux
kernels, bootloaders, filesystems, etc. 

%prep
%setup -q
perl -ne 's/-lz/-lmagic/; print unless /^tar -zxvf \$FILE\.tar\.gz/' -i src/configure.ac
perl -ne 'print unless /FILE/' -i src/Makefile.in

%build
cd src
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}
