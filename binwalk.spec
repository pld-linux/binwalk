# TODO:
# - split library into subpackage?
#
%define	module	binwalk
Summary:	Binary image analyze tool
Name:		binwalk
Version:	2.3.3
Release:	5
License:	MIT
Group:		Development
Source0:	https://github.com/devttys0/binwalk/archive/v%{version}.tar.gz
# Source0-md5:	6a7e53667b24f1cb92c29ec477cb4953
URL:		https://github.com/devttys0/binwalk
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%setup -q

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc API.md README.md
%attr(755,root,root) %{_bindir}/binwalk
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info

