# TODO:
# - split library into subpackage?
# (but 3.x versions are rewritten in rust, so python module is gone)
#
Summary:	Binary image analyze tool
Summary(pl.UTF-8):	Narzędzie do analizy modułów binarnych
Name:		binwalk
Version:	2.3.4
Release:	1
License:	MIT
Group:		Development
#Source0Download: https://github.com/ReFirmLabs/binwalk/releases
Source0:	https://github.com/ReFirmLabs/binwalk/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	182a4e0d99600e30f06007910bcd037d
Patch0:		%{name}-python.patch
URL:		https://github.com/ReFirmLabs/binwalk
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# rpm tries to strip as ELF, but it's not ELF
%define		_noautostrip	.*/binwalk/magic/executables

%description
Binwalk is a tool for searching a given binary image for embedded
files and executable code. Specifically, it is designed for
identifying files and code embedded inside of firmware images. Binwalk
uses the libmagic library, so it is compatible with magic signatures
created for the Unix file utility.

Binwalk also includes a custom magic signature file which contains
improved signatures for files that are commonly found in firmware
images such as compressed/archived files, firmware headers, Linux
kernels, bootloaders, filesystems, etc.

%description -l pl.UTF-8
Binwalk to narzędzie do przeszukiwania danego obrazu binarnego pod
kątem osadzonych plików i kodu wykonywalnego. Jest zaprojektowane w
szczególności do identyfikowania plików i kodu osadzonego wewnątrz
obrazów firmware'u. Binwalk wykorzystuje bibliotekę libmagic, więc
jest zgodny z sygnaturami magicznymi tworzonymi dla narzędzia
uniksowego file.

Binwalk zawiera także własny plik z sygnaturami magicznymi,
zawierający ulepszone sygnatury dla plików często występujących w
obrazach firmware'u, takimi jak pliki skompresowane albo archiwa,
nagłówki firmware'u, jądra Linuksa, bootloadery, systemy plików itp.

%prep
%setup -q
%patch -P0 -p1

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc API.md README.md
%attr(755,root,root) %{_bindir}/binwalk
%{py3_sitescriptdir}/binwalk
%{py3_sitescriptdir}/binwalk-2.3.3-py*.egg-info
