#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Argh: The Natural CLI
Summary(pl.UTF-8):	Argh - naturalna linia poleceń
Name:		python-argh
# keep 0.27.x here for python2 support
Version:	0.27.2
Release:	1
License:	LGPL v3
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/argh/
Source0:	https://files.pythonhosted.org/packages/source/a/argh/argh-%{version}.tar.gz
# Source0-md5:	8b14734d9813da553490acd3bf602ebb
URL:		https://pypi.org/project/argh/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-iocapture >= 0.1.2
BuildRequires:	python-mock
BuildRequires:	python-pytest >= 2.3.7
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-iocapture >= 0.1.2
BuildRequires:	python3-pytest >= 2.3.7
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Argh is a smart wrapper for argparse. Argparse is a very powerful
tool; Argh just makes it easy to use.

%description -l pl.UTF-8
Argh to inteligentne obudowanie argparse. Argparse to potężne
narzędzie - argh czyni je łatwym w użyciu.

%package -n python3-argh
Summary:	Argh: The Natural CLI
Summary(pl.UTF-8):	Argh - naturalna linia poleceń
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.7

%description -n python3-argh
Argh is a smart wrapper for argparse. Argparse is a very powerful
tool; Argh just makes it easy to use.

%description -n python3-argh -l pl.UTF-8
Argh to inteligentne obudowanie argparse. Argparse to potężne
narzędzie - argh czyni je łatwym w użyciu.

%prep
%setup -q -n argh-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
LC_ALL=C.UTF-8 \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest test
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest test
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS README.rst
%{py_sitescriptdir}/argh
%{py_sitescriptdir}/argh-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-argh
%defattr(644,root,root,755)
%doc AUTHORS README.rst
%{py3_sitescriptdir}/argh
%{py3_sitescriptdir}/argh-%{version}-py*.egg-info
%endif
